import React, { useState, useEffect } from 'react';
import { 
  X, 
  ExternalLink, 
  CheckCircle2, 
  Circle, 
  CheckSquare, 
  Square, 
  Copy, 
  Check, 
  Sparkles, 
  AlertTriangle, 
  Code2, 
  FileText,
  RotateCcw,
  Zap
} from 'lucide-react';

const DIFFICULTY_STYLE = {
  Easy: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
  Medium: 'bg-amber-500/10 text-amber-400 border-amber-500/30',
  Hard: 'bg-rose-500/10 text-rose-400 border-rose-500/30'
};

const DIMENSION_ICONS = {
  pattern: '🎯',
  corner_case: '🛡️',
  solution: '✍️',
  complexity: '⏱️'
};

const DIMENSION_NAMES = {
  pattern: '破题眼 / 模式识别',
  corner_case: '边界防守 / 死穴防范',
  solution: '手写最优解 / 无Bug实现',
  complexity: '时空分析 / 口述演练'
};

export default function ProblemDetailDrawer({
  problemDetail,
  onClose,
  onToggleCheckpoint,
  onBatchToggle,
  onSaveNotes
}) {
  if (!problemDetail) return null;

  const { problem, checkpoints = [], solution } = problemDetail;

  const [copied, setCopied] = useState(false);
  const [notes, setNotes] = useState(problem.notes || '');
  const [isSavingNotes, setIsSavingNotes] = useState(false);
  const [notesSavedNotice, setNotesSavedNotice] = useState(false);

  useEffect(() => {
    setNotes(problem.notes || '');
  }, [problem.id, problem.notes]);

  // 复制代码到剪贴板
  const handleCopyCode = () => {
    if (solution?.code_python) {
      navigator.clipboard.writeText(solution.code_python);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  // 保存笔记
  const handleSaveNotes = async () => {
    setIsSavingNotes(true);
    try {
      await onSaveNotes(problem.id, notes);
      setNotesSavedNotice(true);
      setTimeout(() => setNotesSavedNotice(false), 2500);
    } finally {
      setIsSavingNotes(false);
    }
  };

  const isAllComplete = checkpoints.length > 0 && checkpoints.every(c => c.completed === 1);

  return (
    <div className="fixed inset-0 z-50 overflow-hidden bg-slate-950/70 backdrop-blur-sm flex justify-end transition-opacity">
      {/* 遮罩点击关闭 */}
      <div className="absolute inset-0" onClick={onClose} />

      {/* 抽屉主体 */}
      <div className="relative w-full max-w-2xl bg-slate-900 border-l border-slate-800 shadow-2xl h-full flex flex-col z-10 overflow-hidden">
        {/* 头部导航与标题 */}
        <div className="p-5 border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-20 flex items-start justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-1.5 flex-wrap">
              <span className="text-xs font-mono font-bold text-slate-400 bg-slate-800 px-2 py-0.5 rounded border border-slate-700">
                #{problem.frontend_id}
              </span>
              <span className={`text-xs font-semibold px-2 py-0.5 rounded border ${DIFFICULTY_STYLE[problem.difficulty] || ''}`}>
                {problem.difficulty === 'Easy' ? '简单' : problem.difficulty === 'Medium' ? '中等' : '困难'}
              </span>
              <span className="text-xs text-slate-400 bg-slate-800/60 px-2 py-0.5 rounded border border-slate-800">
                {problem.category}
              </span>
              <span className="text-xs text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20 font-medium">
                Day {problem.day} 专题
              </span>
            </div>

            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              {problem.title_cn}
              <span className="text-sm font-normal text-slate-400">({problem.title_en})</span>
            </h2>
          </div>

          <div className="flex items-center gap-2">
            <a
              href={`https://leetcode.cn/problems/${problem.slug}/`}
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 text-slate-400 hover:text-emerald-400 hover:bg-slate-800 rounded-xl transition"
              title="在力扣 (LeetCode) 打开原题"
            >
              <ExternalLink className="w-5 h-5" />
            </a>
            <button
              onClick={onClose}
              className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition"
              title="关闭详情"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* 滚动内容区 */}
        <div className="flex-1 overflow-y-auto p-5 sm:p-6 space-y-6">
          {/* 掌握度概览与批量操作栏 */}
          <div className="bg-slate-950/60 border border-slate-800/80 rounded-2xl p-4 flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="relative w-12 h-12 flex items-center justify-center">
                <svg className="w-12 h-12 transform -rotate-90" viewBox="0 0 36 36">
                  <path
                    className="text-slate-800"
                    strokeWidth="3.5"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                  <path
                    className="text-emerald-400 transition-all duration-500 ease-out"
                    strokeDasharray={`${problem.mastery_score || 0}, 100`}
                    strokeWidth="3.5"
                    strokeLinecap="round"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                </svg>
                <span className="absolute text-xs font-bold text-slate-200">
                  {problem.mastery_score}%
                </span>
              </div>
              <div>
                <div className="text-sm font-bold text-slate-200">
                  {problem.mastery_score === 100
                    ? '🎉 已全面掌握'
                    : problem.mastery_score > 0
                    ? '⚡ 正在攻坚突破'
                    : '⏳ 尚未开始攻关'}
                </div>
                <div className="text-xs text-slate-500 mt-0.5">
                  已攻破 {checkpoints.filter(c => c.completed === 1).length} / {checkpoints.length} 个原子点
                </div>
              </div>
            </div>

            {/* 批量操作按钮 */}
            <div className="flex items-center gap-2">
              <button
                onClick={() => onBatchToggle(problem.id, !isAllComplete)}
                className={`px-3 py-1.5 text-xs font-semibold rounded-xl border transition flex items-center gap-1.5 active:scale-95 ${
                  isAllComplete
                    ? 'bg-slate-800 text-slate-300 border-slate-700 hover:bg-slate-700'
                    : 'bg-emerald-600 text-white border-emerald-500 hover:bg-emerald-500 shadow-sm shadow-emerald-600/30'
                }`}
              >
                {isAllComplete ? (
                  <>
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>重置进度</span>
                  </>
                ) : (
                  <>
                    <Zap className="w-3.5 h-3.5" />
                    <span>一键全通关</span>
                  </>
                )}
              </button>
            </div>
          </div>

          {/* 模块一：4 维原子微检查点 (Checkpoints) */}
          <div className="space-y-3">
            <h3 className="text-sm font-bold text-slate-300 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-emerald-400" />
              <span>4 维原子化微检查点 (Micro-Checkpoints)</span>
            </h3>

            <div className="space-y-2.5">
              {checkpoints.map((cp) => {
                const isChecked = cp.completed === 1;
                return (
                  <div
                    key={cp.id}
                    onClick={() => onToggleCheckpoint(cp.id)}
                    className={`group p-3.5 rounded-xl border cursor-pointer transition-all duration-150 flex items-start gap-3.5 ${
                      isChecked
                        ? 'bg-emerald-950/20 border-emerald-500/40 hover:border-emerald-500/60'
                        : 'bg-slate-950/50 border-slate-800 hover:border-slate-700 hover:bg-slate-950/80'
                    }`}
                  >
                    <div className="mt-0.5 text-emerald-400 shrink-0">
                      {isChecked ? (
                        <CheckSquare className="w-5 h-5 fill-emerald-500/20 text-emerald-400" />
                      ) : (
                        <Square className="w-5 h-5 text-slate-600 group-hover:text-slate-400" />
                      )}
                    </div>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-2">
                        <div className="flex items-center gap-2">
                          <span className="text-sm">
                            {DIMENSION_ICONS[cp.dimension] || '📌'}
                          </span>
                          <span className={`text-sm font-bold ${
                            isChecked ? 'text-emerald-300 line-through decoration-emerald-500/40' : 'text-slate-200'
                          }`}>
                            {cp.title}
                          </span>
                        </div>
                        <span className="text-[11px] font-mono text-slate-500 bg-slate-900 px-2 py-0.5 rounded border border-slate-800 shrink-0">
                          {cp.weight}% 权重
                        </span>
                      </div>
                      <p className="text-xs text-slate-400 mt-1 leading-relaxed">
                        {cp.detail}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 模块二：核心破题口诀 (Core Insight) */}
          {solution?.core_insight && (
            <div className="bg-emerald-950/20 border border-emerald-500/30 rounded-2xl p-4">
              <h4 className="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5 mb-1.5">
                <Zap className="w-3.5 h-3.5" />
                核心破题眼与解题口诀
              </h4>
              <p className="text-sm text-emerald-100/90 leading-relaxed font-medium">
                {solution.core_insight}
              </p>
            </div>
          )}

          {/* 模块三：易错陷阱与边界防守 (Traps) */}
          {solution?.traps && (
            <div className="bg-amber-950/20 border border-amber-500/30 rounded-2xl p-4">
              <h4 className="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5 mb-1.5">
                <AlertTriangle className="w-3.5 h-3.5" />
                易错死穴与面试避坑指南
              </h4>
              <p className="text-sm text-amber-200/90 leading-relaxed">
                {solution.traps}
              </p>
            </div>
          )}

          {/* 模块四：最优解法源码 (Optimal Solution Code) */}
          {solution?.code_python && (
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold text-slate-300 flex items-center gap-2">
                  <Code2 className="w-4 h-4 text-emerald-400" />
                  <span>最优规范代码 (Python 3 最优解)</span>
                </h3>

                <div className="flex items-center gap-2">
                  <div className="text-[11px] font-mono text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
                    时间: <span className="text-emerald-400">{solution.time_complexity}</span>
                  </div>
                  <div className="text-[11px] font-mono text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
                    空间: <span className="text-emerald-400">{solution.space_complexity}</span>
                  </div>
                  <button
                    onClick={handleCopyCode}
                    className="flex items-center gap-1 text-xs text-slate-400 hover:text-white bg-slate-800 hover:bg-slate-700 px-2.5 py-1 rounded-lg border border-slate-700 transition"
                  >
                    {copied ? (
                      <>
                        <Check className="w-3.5 h-3.5 text-emerald-400" />
                        <span className="text-emerald-400">已复制</span>
                      </>
                    ) : (
                      <>
                        <Copy className="w-3.5 h-3.5" />
                        <span>复制代码</span>
                      </>
                    )}
                  </button>
                </div>
              </div>

              <div className="relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-inner">
                <pre className="p-4 text-xs sm:text-sm text-emerald-200/90 overflow-x-auto font-mono leading-relaxed">
                  <code>{solution.code_python}</code>
                </pre>
              </div>
            </div>
          )}

          {/* 模块五：个人攻坚笔记 (Personal Notes) */}
          <div className="space-y-2 pt-2">
            <div className="flex items-center justify-between">
              <h3 className="text-sm font-bold text-slate-300 flex items-center gap-2">
                <FileText className="w-4 h-4 text-emerald-400" />
                <span>个人白板手记与反思记录</span>
              </h3>
              {notesSavedNotice && (
                <span className="text-xs text-emerald-400 font-medium animate-pulse">
                  ✓ 手记已保存入库
                </span>
              )}
            </div>

            <textarea
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              placeholder="记录你在本题的思考、卡壳的地方、变种题型衍生或者面试口述技巧 (自动保存到本地 SQLite)..."
              rows={4}
              className="w-full bg-slate-950/80 border border-slate-800 focus:border-emerald-500/60 focus:ring-2 focus:ring-emerald-500/20 text-slate-200 text-xs sm:text-sm rounded-xl p-3.5 outline-none transition resize-y placeholder:text-slate-600"
            />

            <div className="flex justify-end">
              <button
                onClick={handleSaveNotes}
                disabled={isSavingNotes}
                className="px-4 py-2 text-xs font-semibold bg-slate-800 hover:bg-slate-700 active:scale-95 text-slate-200 border border-slate-700 rounded-xl transition"
              >
                {isSavingNotes ? '正在保存...' : '保存手记'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
