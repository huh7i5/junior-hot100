import React, { useState, useMemo } from 'react';
import { 
  FileText, 
  ExternalLink, 
  Copy, 
  Check, 
  Sparkles, 
  AlertCircle, 
  Terminal,
  Code2,
  SlidersHorizontal,
  Layers
} from 'lucide-react';
import { marked } from 'marked';

// 配置 marked 解析选项
marked.setOptions({
  breaks: true,
  gfm: true
});

/**
 * 将原始 Markdown 题目文本智能拆解为结构化数据
 */
function parseProblemDescription(rawText) {
  if (!rawText) return null;

  const lines = rawText.replace(/\r\n/g, '\n').split('\n');

  let currentMode = 'statement'; // 'statement' | 'example' | 'constraints'
  let statementLines = [];
  let examples = [];
  let currentExample = null;
  let constraints = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    // 识别约束/提示标题
    if (/^(?:###\s*)?(?:提示|约束条件|提示与约束条件)[:：]?$/.test(line)) {
      if (currentExample) {
        examples.push(currentExample);
        currentExample = null;
      }
      currentMode = 'constraints';
      continue;
    }

    // 识别示例标题: "### 示例 1", "示例 1:", "示例 1：", "示例1"
    const exampleMatch = line.match(/^(?:###\s*)?(示例\s*\d+)[:：]?$/);
    if (exampleMatch) {
      if (currentExample) {
        examples.push(currentExample);
      }
      currentExample = {
        title: exampleMatch[1].replace(/\s+/, ' '),
        input: '',
        output: '',
        explanation: '',
        rawLines: []
      };
      currentMode = 'example';
      continue;
    }

    // 识别题意描述标题: "### 题目描述"
    if (/^###\s*题目描述[:：]?$/.test(line)) {
      currentMode = 'statement';
      continue;
    }

    if (currentMode === 'statement') {
      statementLines.push(lines[i]);
    } else if (currentMode === 'example' && currentExample) {
      const inputMatch = line.match(/^(?:[-*]\s*)?(?:\*\*)?输入(?:\*\*)?[:：]\s*(.*)$/);
      const outputMatch = line.match(/^(?:[-*]\s*)?(?:\*\*)?输出(?:\*\*)?[:：]\s*(.*)$/);
      const expMatch = line.match(/^(?:[-*]\s*)?(?:\*\*)?解释(?:\*\*)?[:：]\s*(.*)$/);

      if (inputMatch) {
        currentExample.input = inputMatch[1].trim();
      } else if (outputMatch) {
        currentExample.output = outputMatch[1].trim();
      } else if (expMatch) {
        currentExample.explanation = expMatch[1].trim();
      } else if (line) {
        currentExample.rawLines.push(line);
      }
    } else if (currentMode === 'constraints') {
      const cleanConstraint = line.replace(/^[-*]\s*/, '').trim();
      if (cleanConstraint) {
        constraints.push(cleanConstraint);
      }
    }
  }

  if (currentExample) {
    examples.push(currentExample);
  }

  // 整理输出
  return {
    statement: statementLines.join('\n').trim(),
    examples,
    constraints
  };
}

/**
 * 辅助清洗输入输出中的冗余外层反引号
 */
function cleanCodeValue(val) {
  if (!val) return '';
  let str = val.trim();
  if (str.startsWith('`') && str.endsWith('`') && str.length >= 2) {
    str = str.slice(1, -1).trim();
  }
  return str;
}

export default function ProblemDescription({ description, slug }) {
  const [viewFormat, setViewFormat] = useState('structured'); // 'structured' | 'markdown'
  const [copiedIdx, setCopiedIdx] = useState(null);

  // 解析结构化数据
  const structuredData = useMemo(() => {
    return parseProblemDescription(description);
  }, [description]);

  // 全量 Markdown HTML (用于原文视图)
  const fullMarkdownHtml = useMemo(() => {
    if (!description) return '';
    return marked.parse(description);
  }, [description]);

  const handleCopy = (text, idx) => {
    if (!text) return;
    navigator.clipboard.writeText(cleanCodeValue(text));
    setCopiedIdx(idx);
    setTimeout(() => setCopiedIdx(null), 1800);
  };

  if (!description) {
    return (
      <div className="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 text-xs text-slate-500 dark:text-slate-400 flex items-center justify-between">
        <span>暂无原题详细题面，详情请参考力扣原题。</span>
        {slug && (
          <a
            href={`https://leetcode.cn/problems/${slug}/`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-emerald-600 dark:text-emerald-400 hover:underline flex items-center gap-1 font-medium"
          >
            打开力扣题面 <ExternalLink className="w-3 h-3" />
          </a>
        )}
      </div>
    );
  }

  return (
    <div className="bg-slate-50/70 dark:bg-slate-950/80 border border-slate-200 dark:border-slate-800/90 rounded-2xl sm:rounded-3xl p-4 sm:p-5 space-y-4 transition-colors">
      
      {/* 顶栏控制：标签 + 格式切换 + 力扣链接 */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800/80">
        <div className="flex items-center gap-2">
          <div className="w-6 h-6 rounded-lg bg-sky-500/10 text-sky-600 dark:text-sky-400 flex items-center justify-center">
            <FileText className="w-3.5 h-3.5" />
          </div>
          <span className="font-bold text-sm text-slate-900 dark:text-white">
            原题描述与测试用例 (审题第一步)
          </span>
        </div>

        <div className="flex items-center gap-2.5">
          {/* 排版模式切换器 */}
          <div className="flex items-center bg-slate-200/80 dark:bg-slate-900 p-0.5 rounded-lg border border-slate-300/80 dark:border-slate-800 text-xs shadow-inner">
            <button
              onClick={() => setViewFormat('structured')}
              className={`flex items-center gap-1 px-2.5 py-1 rounded-md font-medium transition active:scale-[0.98] ${
                viewFormat === 'structured'
                  ? 'bg-white dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
              title="结构化精读：将用例与约束条件拆分为直观卡片"
            >
              <Sparkles className="w-3 h-3" />
              <span>结构化排版</span>
            </button>
            <button
              onClick={() => setViewFormat('markdown')}
              className={`flex items-center gap-1 px-2.5 py-1 rounded-md font-medium transition active:scale-[0.98] ${
                viewFormat === 'markdown'
                  ? 'bg-white dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
              title="Markdown 渲染：经典格式呈现"
            >
              <Code2 className="w-3 h-3" />
              <span>Markdown</span>
            </button>
          </div>

          {/* 外链按钮 */}
          {slug && (
            <a
              href={`https://leetcode.cn/problems/${slug}/`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-xs text-slate-500 hover:text-emerald-600 dark:hover:text-emerald-400 flex items-center gap-1 transition px-2 py-1 rounded-lg hover:bg-slate-200/60 dark:hover:bg-slate-900 shrink-0"
              title="在力扣 (LeetCode) 查看官方原题面"
            >
              <span>力扣链接</span>
              <ExternalLink className="w-3 h-3" />
            </a>
          )}
        </div>
      </div>

      {/* 视图分支 */}
      {viewFormat === 'structured' && structuredData ? (
        <div className="space-y-4">
          
          {/* 1. 题意描述说明 (Statement) */}
          {structuredData.statement && (
            <div className="bg-white dark:bg-slate-900/70 border border-slate-200 dark:border-slate-800/80 rounded-2xl p-4 sm:p-5 shadow-sm">
              <div className="text-xs font-bold text-slate-500 dark:text-slate-400 mb-2 flex items-center gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span>题目要求</span>
              </div>
              <div 
                className="text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-sans space-y-2
                  [&_p]:mb-2.5 [&_p:last-child]:mb-0
                  [&_strong]:font-bold [&_strong]:text-slate-900 [&_strong]:dark:text-white
                  [&_code]:font-mono [&_code]:text-xs [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:rounded 
                  [&_code]:bg-emerald-50 [&_code]:dark:bg-emerald-950/60 
                  [&_code]:text-emerald-700 [&_code]:dark:text-emerald-300 
                  [&_code]:border [&_code]:border-emerald-200 [&_code]:dark:border-emerald-800/50"
                dangerouslySetInnerHTML={{ 
                  __html: marked.parse(structuredData.statement) 
                }}
              />
            </div>
          )}

          {/* 2. 官方示例示范卡片组 (Examples) */}
          {structuredData.examples.length > 0 && (
            <div className="space-y-2.5">
              <div className="flex items-center justify-between px-1">
                <div className="text-xs font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                  <SlidersHorizontal className="w-3.5 h-3.5 text-sky-500" />
                  <span>示例测试用例 ({structuredData.examples.length} 个)</span>
                </div>
                <span className="text-[11px] text-slate-400 dark:text-slate-500">
                  可一键复制用例输入
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {structuredData.examples.map((ex, idx) => {
                  const cleanInput = cleanCodeValue(ex.input);
                  const cleanOutput = cleanCodeValue(ex.output);
                  const isCopied = copiedIdx === idx;

                  return (
                    <div 
                      key={idx}
                      className="bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800 rounded-2xl p-3.5 sm:p-4 shadow-sm flex flex-col justify-between"
                    >
                      <div>
                        {/* 示例卡片顶部标头 */}
                        <div className="flex items-center justify-between mb-2.5 pb-2 border-b border-slate-100 dark:border-slate-800/60">
                          <span className="px-2 py-0.5 text-xs font-bold bg-sky-50 dark:bg-sky-950/50 text-sky-700 dark:text-sky-300 border border-sky-200 dark:border-sky-800/50 rounded-md">
                            {ex.title}
                          </span>

                          {cleanInput && (
                            <button
                              onClick={() => handleCopy(cleanInput, idx)}
                              className="text-[11px] text-slate-500 hover:text-slate-800 dark:hover:text-slate-200 flex items-center gap-1 px-1.5 py-0.5 rounded hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                              title="复制输入测试用例"
                            >
                              {isCopied ? (
                                <>
                                  <Check className="w-3 h-3 text-emerald-500" />
                                  <span className="text-emerald-600 dark:text-emerald-400 font-semibold">已复制</span>
                                </>
                              ) : (
                                <>
                                  <Copy className="w-3 h-3" />
                                  <span>复制输入</span>
                                </>
                              )}
                            </button>
                          )}
                        </div>

                        {/* 输入框 */}
                        {cleanInput && (
                          <div className="mb-2">
                            <span className="text-[11px] font-semibold text-slate-400 dark:text-slate-500 block mb-1">
                              输入:
                            </span>
                            <div className="bg-slate-50 dark:bg-slate-950 p-2 rounded-xl border border-slate-200 dark:border-slate-800/90 font-mono text-xs text-slate-800 dark:text-slate-200 break-all select-all">
                              {cleanInput}
                            </div>
                          </div>
                        )}

                        {/* 输出框 */}
                        {cleanOutput && (
                          <div className="mb-2">
                            <span className="text-[11px] font-semibold text-slate-400 dark:text-slate-500 block mb-1">
                              输出:
                            </span>
                            <div className="bg-emerald-50/70 dark:bg-emerald-950/30 p-2 rounded-xl border border-emerald-200 dark:border-emerald-800/40 font-mono text-xs text-emerald-700 dark:text-emerald-300 font-bold break-all select-all">
                              {cleanOutput}
                            </div>
                          </div>
                        )}

                        {/* 解释 (若有) */}
                        {ex.explanation && (
                          <div className="mt-2.5 p-2 bg-amber-50/60 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-800/40 rounded-xl text-xs text-amber-800 dark:text-amber-300/90 leading-relaxed">
                            <span className="font-bold mr-1">💡 解释:</span>
                            <span 
                              dangerouslySetInnerHTML={{ 
                                __html: marked.parseInline(ex.explanation) 
                              }} 
                            />
                          </div>
                        )}

                        {/* 原生附加说明行 */}
                        {ex.rawLines && ex.rawLines.length > 0 && (
                          <div className="mt-2 text-xs text-slate-500 dark:text-slate-400 font-sans space-y-1">
                            {ex.rawLines.map((rLine, rIdx) => (
                              <div key={rIdx} dangerouslySetInnerHTML={{ __html: marked.parseInline(rLine) }} />
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* 3. 边界与提示条件 (Constraints) */}
          {structuredData.constraints.length > 0 && (
            <div className="bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm">
              <div className="text-xs font-bold text-slate-700 dark:text-slate-300 mb-2.5 flex items-center gap-1.5">
                <AlertCircle className="w-3.5 h-3.5 text-amber-500" />
                <span>边界与约束条件 (数据规模)</span>
              </div>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                {structuredData.constraints.map((cText, idx) => (
                  <li 
                    key={idx}
                    className="flex items-start gap-2 bg-slate-50 dark:bg-slate-950/60 p-2.5 rounded-xl border border-slate-200/80 dark:border-slate-800 text-slate-700 dark:text-slate-300"
                  >
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-400 mt-1.5 shrink-0" />
                    <span 
                      className="font-mono [&_code]:font-mono [&_code]:text-emerald-600 [&_code]:dark:text-emerald-400 [&_strong]:text-slate-900 [&_strong]:dark:text-white"
                      dangerouslySetInnerHTML={{ 
                        __html: marked.parseInline(cText) 
                      }} 
                    />
                  </li>
                ))}
              </ul>
            </div>
          )}

        </div>
      ) : (
        /* Markdown 原文排版呈现 (已优化排版与样式渲染) */
        <div 
          className="bg-white dark:bg-slate-900/70 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 text-sm text-slate-800 dark:text-slate-200 leading-relaxed overflow-x-auto shadow-sm
            [&_h3]:text-base [&_h3]:font-bold [&_h3]:text-slate-900 [&_h3]:dark:text-white [&_h3]:mt-4 [&_h3]:mb-2 [&_h3]:pb-1 [&_h3]:border-b [&_h3]:border-slate-200 [&_h3]:dark:border-slate-800
            [&_p]:mb-2.5
            [&_ul]:list-disc [&_ul]:pl-5 [&_ul]:space-y-1.5 [&_ul]:my-2
            [&_li]:text-xs [&_li]:sm:text-sm [&_li]:text-slate-700 [&_li]:dark:text-slate-300
            [&_strong]:font-bold [&_strong]:text-slate-900 [&_strong]:dark:text-white
            [&_code]:font-mono [&_code]:text-xs [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:rounded 
            [&_code]:bg-emerald-50 [&_code]:dark:bg-emerald-950/60 
            [&_code]:text-emerald-700 [&_code]:dark:text-emerald-300 
            [&_code]:border [&_code]:border-emerald-200 [&_code]:dark:border-emerald-800/50"
          dangerouslySetInnerHTML={{ __html: fullMarkdownHtml }}
        />
      )}

    </div>
  );
}
