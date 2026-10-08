import React, { useState, useEffect } from 'react';
import ProblemDescription from './ProblemDescription';
import { 
  X, 
  ExternalLink, 
  CheckSquare, 
  Square, 
  Copy, 
  Check, 
  Sparkles, 
  AlertTriangle, 
  Code2, 
  FileText,
  RotateCcw,
  Zap,
  BookOpen,
  HelpCircle,
  Layers,
  Bookmark,
  ChevronLeft,
  ChevronRight
} from 'lucide-react';

const DIFFICULTY_STYLE = {
  Easy: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border-emerald-500/30',
  Medium: 'bg-amber-500/10 text-amber-700 dark:text-amber-400 border-amber-500/30',
  Hard: 'bg-rose-500/10 text-rose-700 dark:text-rose-400 border-rose-500/30'
};

export default function ProblemDetailModal({
  problemDetail,
  onClose,
  onToggleCheckpoint,
  onBatchToggle,
  onSaveNotes,
  onNavigatePrev,
  onNavigateNext,
  currentIndex,
  totalProblems
}) {
  const [activeCodeLang, setActiveCodeLang] = useState('javascript');
  const [copied, setCopied] = useState(false);
  const [notes, setNotes] = useState('');
  const [isSavingNotes, setIsSavingNotes] = useState(false);
  const [notesSavedNotice, setNotesSavedNotice] = useState(false);

  useEffect(() => {
    if (problemDetail?.problem?.notes !== undefined) {
      setNotes(problemDetail.problem.notes || '');
    }
  }, [problemDetail]);

  // ESC 键关闭弹窗 & 左右方向键切题 (仅在未聚焦文本输入时)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        onClose();
        return;
      }
      
      const isInputActive = ['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName);
      if (!isInputActive) {
        if ((e.key === 'ArrowLeft' || e.key === 'PageUp') && onNavigatePrev) {
          e.preventDefault();
          onNavigatePrev();
        } else if ((e.key === 'ArrowRight' || e.key === 'PageDown') && onNavigateNext) {
          e.preventDefault();
          onNavigateNext();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose, onNavigatePrev, onNavigateNext]);

  if (!problemDetail) return null;

  const { problem, checkpoints = [], solution } = problemDetail;

  // 解析 JS 函数科普
  let jsHelpers = [];
  try {
    if (solution?.js_helpers) {
      jsHelpers = typeof solution.js_helpers === 'string' 
        ? JSON.parse(solution.js_helpers) 
        : solution.js_helpers;
    }
  } catch (e) {
    jsHelpers = [];
  }

  // 当前展示的代码
  const currentCode = activeCodeLang === 'javascript' 
    ? (solution?.code_js || solution?.code_python) 
    : solution?.code_python;

  const handleCopyCode = () => {
    if (currentCode) {
      navigator.clipboard.writeText(currentCode);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

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
  const completedCount = checkpoints.filter(c => c.completed === 1).length;

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-slate-950/60 dark:bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-6 transition-all animate-in fade-in duration-150">
      {/* 遮罩点击关闭 */}
      <div className="fixed inset-0" onClick={onClose} />

      {/* 居中大弹窗卡片 */}
      <div 
        onClick={(e) => e.stopPropagation()} 
        className="relative w-full max-w-4xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700/80 rounded-2xl sm:rounded-3xl shadow-2xl max-h-[92vh] flex flex-col overflow-hidden z-10 transition-colors duration-150"
      >
        {/* 顶部标题栏 */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 bg-white/95 dark:bg-slate-900/95 sticky top-0 z-20 flex items-center justify-between gap-4">
          <div className="flex items-center gap-3 flex-wrap">
            {/* 上一题 / 下一题 顶栏快捷导航 */}
            <div className="flex items-center bg-slate-100 dark:bg-slate-800/80 p-0.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs">
              <button
                onClick={onNavigatePrev}
                disabled={!onNavigatePrev}
                className="p-1 text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white disabled:opacity-30 disabled:hover:text-slate-400 rounded transition"
                title="上一题 (快捷键: ← 或 PageUp)"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
              {currentIndex !== undefined && totalProblems && (
                <span className="px-1.5 font-mono text-[11px] font-semibold text-slate-500 dark:text-slate-400">
                  {currentIndex + 1}/{totalProblems}
                </span>
              )}
              <button
                onClick={onNavigateNext}
                disabled={!onNavigateNext}
                className="p-1 text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white disabled:opacity-30 disabled:hover:text-slate-400 rounded transition"
                title="下一题 (快捷键: → 或 PageDown)"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>

            <span className="text-xs font-mono font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700">
              #{problem.frontend_id}
            </span>
            <span className={`text-xs font-semibold px-2.5 py-1 rounded-lg border ${DIFFICULTY_STYLE[problem.difficulty] || ''}`}>
              {problem.difficulty === 'Easy' ? '简单' : problem.difficulty === 'Medium' ? '中等' : '困难'}
            </span>
            <span className="text-xs text-slate-600 dark:text-slate-400 bg-slate-100 dark:bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-800">
              {problem.category}
            </span>
            <span className="text-xs text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-300 dark:border-emerald-500/20 font-medium">
              Day {problem.day} 冲刺
            </span>
            <h2 className="text-lg sm:text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
              {problem.title_cn}
              <span className="text-xs sm:text-sm font-normal text-slate-500 dark:text-slate-400">({problem.title_en})</span>
            </h2>
          </div>

          <div className="flex items-center gap-2 shrink-0">
            <a
              href={`https://leetcode.cn/problems/${problem.slug}/`}
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 text-slate-500 hover:text-emerald-600 dark:text-slate-400 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl transition"
              title="在力扣 (LeetCode) 打开原题"
            >
              <ExternalLink className="w-5 h-5" />
            </a>
            <button
              onClick={onClose}
              className="p-2 text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl transition"
              title="关闭 (ESC)"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* 弹窗主体滚动区域 */}
        <div className="flex-1 overflow-y-auto px-6 py-5 space-y-6">
          {/* 进度与一键操作栏 */}
          <div className="bg-slate-50 dark:bg-slate-950/70 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="relative w-12 h-12 flex items-center justify-center">
                <svg className="w-12 h-12 transform -rotate-90" viewBox="0 0 36 36">
                  <path
                    className="text-slate-200 dark:text-slate-800"
                    strokeWidth="3.5"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                  <path
                    className="text-emerald-500 dark:text-emerald-400 transition-all duration-500 ease-out"
                    strokeDasharray={`${problem.mastery_score || 0}, 100`}
                    strokeWidth="3.5"
                    strokeLinecap="round"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                </svg>
                <span className="absolute text-xs font-bold text-slate-800 dark:text-slate-200 font-mono">
                  {problem.mastery_score}%
                </span>
              </div>
              <div>
                <div className="text-sm font-bold text-slate-800 dark:text-slate-200">
                  {problem.mastery_score === 100
                    ? '🎉 已全面攻克 (Mastered)'
                    : problem.mastery_score > 0
                    ? '⚡ 正在按照步骤细扣中'
                    : '⏳ 待开始啃题'}
                </div>
                <div className="text-xs text-slate-500 mt-0.5">
                  已完成 {completedCount} / {checkpoints.length} 个解法打卡点
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => onBatchToggle(problem.id, !isAllComplete)}
                className={`px-3.5 py-1.5 text-xs font-semibold rounded-xl border transition flex items-center gap-1.5 active:scale-95 ${
                  isAllComplete
                    ? 'bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'
                    : 'bg-emerald-600 hover:bg-emerald-500 text-white border-emerald-500 shadow-sm shadow-emerald-600/30'
                }`}
              >
                {isAllComplete ? (
                  <>
                    <RotateCcw className="w-3.5 h-3.5" />
                    <span>重置打卡</span>
                  </>
                ) : (
                  <>
                    <Zap className="w-3.5 h-3.5" />
                    <span>一键全通关 (100%)</span>
                  </>
                )}
              </button>
            </div>
          </div>

          {/* 1️⃣ 第一步：原题描述与测试用例 (Problem Statement & Examples) */}
          <ProblemDescription 
            description={problem.description} 
            slug={problem.slug} 
          />

          {/* 2️⃣ 第二步：初学者大白话破题思路 (Junior Level Guide) */}
          <div className="bg-gradient-to-r from-emerald-50 via-teal-50 to-slate-50 dark:from-emerald-950/40 dark:via-teal-950/30 dark:to-slate-900 border border-emerald-300 dark:border-emerald-500/30 rounded-2xl p-4 sm:p-5 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-emerald-800 dark:text-emerald-400 font-bold text-sm">
                <BookOpen className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                <span>核心思路剖析与初学者大白话 (破题第二步)</span>
              </div>
              <div className="flex items-center gap-2 text-[11px] font-mono text-slate-600 dark:text-slate-400">
                <span className="bg-white/80 dark:bg-slate-800/80 px-2 py-0.5 rounded border border-emerald-200 dark:border-slate-700">
                  时空: <span className="text-emerald-700 dark:text-emerald-400 font-semibold">{solution?.time_complexity}</span> / <span className="text-teal-700 dark:text-teal-400 font-semibold">{solution?.space_complexity}</span>
                </span>
              </div>
            </div>
            <p className="text-sm sm:text-base text-emerald-950 dark:text-emerald-100/90 leading-relaxed font-normal">
              {solution?.plain_explanation || solution?.core_insight}
            </p>
          </div>

          {/* 3️⃣ 第三步：优雅规范的最优解源码 (Solution Code) */}
          <div className="space-y-2">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <Code2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                <span className="text-sm font-bold text-slate-800 dark:text-slate-200">解答源码 (观码第三步)</span>

                {/* 语言切换器 */}
                <div className="flex items-center bg-slate-100 dark:bg-slate-950 p-0.5 rounded-lg border border-slate-200 dark:border-slate-800 text-xs ml-2">
                  <button
                    onClick={() => setActiveCodeLang('javascript')}
                    className={`px-2.5 py-1 rounded-md font-medium transition ${
                      activeCodeLang === 'javascript'
                        ? 'bg-amber-100 dark:bg-amber-500/20 text-amber-800 dark:text-amber-300 border border-amber-300 dark:border-amber-500/30'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                    }`}
                  >
                    JavaScript (首选)
                  </button>
                  <button
                    onClick={() => setActiveCodeLang('python')}
                    className={`px-2.5 py-1 rounded-md font-medium transition ${
                      activeCodeLang === 'python'
                        ? 'bg-emerald-100 dark:bg-emerald-500/20 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/30'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                    }`}
                  >
                    Python 3
                  </button>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <button
                  onClick={handleCopyCode}
                  className="flex items-center gap-1 text-xs text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 px-3 py-1 rounded-lg border border-slate-300 dark:border-slate-700 transition active:scale-95"
                >
                  {copied ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                      <span className="text-emerald-600 dark:text-emerald-400">已复制代码</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5" />
                      <span>一键复制</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            <div className="relative rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-inner">
              <pre className="p-4 text-xs sm:text-sm text-emerald-300/90 overflow-x-auto font-mono leading-relaxed max-h-96">
                <code>{currentCode || '// 暂无代码'}</code>
              </pre>
            </div>
          </div>

          {/* 4️⃣ 第四步：按照解法细扣代码与知识点打卡 (Tailored Checkpoints & Points) */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <h3 className="text-sm font-bold text-slate-800 dark:text-slate-200 flex items-center gap-2">
                <Layers className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                <span>对照上方代码细扣知识点打卡 (细扣第四步，共 {checkpoints.length} 个要点)</span>
              </h3>
              <span className="text-xs text-slate-400 dark:text-slate-500">点击卡片即可切换完成状态</span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {checkpoints.map((cp) => {
                const isChecked = cp.completed === 1;
                return (
                  <div
                    key={cp.id}
                    onClick={() => onToggleCheckpoint(cp.id)}
                    className={`group p-3.5 rounded-xl border cursor-pointer transition-all duration-150 flex items-start gap-3 active:scale-[0.99] ${
                      isChecked
                        ? 'bg-emerald-50 dark:bg-emerald-950/20 border-emerald-400 dark:border-emerald-500/50 hover:border-emerald-500 ring-1 ring-emerald-400/20'
                        : 'bg-slate-50 dark:bg-slate-950/50 border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-950/80'
                    }`}
                  >
                    <div className="mt-0.5 text-emerald-600 dark:text-emerald-400 shrink-0">
                      {isChecked ? (
                        <CheckSquare className="w-5 h-5 fill-emerald-500/20 text-emerald-600 dark:text-emerald-400" />
                      ) : (
                        <Square className="w-5 h-5 text-slate-400 dark:text-slate-600 group-hover:text-slate-600 dark:group-hover:text-slate-400" />
                      )}
                    </div>

                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between gap-1 mb-1">
                        <span className={`text-xs sm:text-sm font-bold ${
                          isChecked ? 'text-emerald-800 dark:text-emerald-300 line-through decoration-emerald-500/40' : 'text-slate-800 dark:text-slate-200'
                        }`}>
                          {cp.title}
                        </span>
                        <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400 bg-slate-200/80 dark:bg-slate-900 px-1.5 py-0.5 rounded border border-slate-300 dark:border-slate-800 shrink-0">
                          {cp.weight}%
                        </span>
                      </div>
                      <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                        {cp.detail}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 5️⃣ 第五步：JS 核心函数与语法保姆级小贴士 (JS Cheat Sheet) */}
          {jsHelpers.length > 0 && (
            <div className="bg-amber-50/50 dark:bg-slate-950/60 border border-amber-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 space-y-3">
              <div className="flex items-center gap-2 text-amber-700 dark:text-amber-400 font-bold text-sm">
                <HelpCircle className="w-4 h-4 text-amber-600 dark:text-amber-400" />
                <span>代码注解：本题用到的 JavaScript 核心函数与 API 通俗小贴士</span>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {jsHelpers.map((helper, idx) => (
                  <div key={idx} className="bg-white dark:bg-slate-900/80 border border-amber-200/60 dark:border-slate-800 rounded-xl p-3 text-xs space-y-1 shadow-sm">
                    <div className="font-mono font-bold text-amber-700 dark:text-amber-300 flex items-center gap-1.5">
                      <span className="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                      {helper.name}
                    </div>
                    <p className="text-slate-700 dark:text-slate-300 leading-relaxed">{helper.what_it_does}</p>
                    {helper.junior_tip && (
                      <div className="text-slate-600 dark:text-slate-400 bg-amber-50/50 dark:bg-slate-950/60 p-2 rounded-lg border border-amber-100 dark:border-slate-800/80 text-[11px] leading-relaxed">
                        <strong className="text-amber-700 dark:text-amber-400">💡 初学者提醒：</strong>
                        {helper.junior_tip}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* 6️⃣ 第六步：面试高危红线与避坑警示 (Traps) */}
          {solution?.traps && (
            <div className="bg-rose-50 dark:bg-rose-950/20 border border-rose-200 dark:border-rose-500/30 rounded-2xl p-4 sm:p-5 flex items-start gap-3">
              <AlertTriangle className="w-5 h-5 text-rose-500 dark:text-rose-400 shrink-0 mt-0.5" />
              <div>
                <h4 className="text-sm font-bold text-rose-700 dark:text-rose-300 mb-1">面试高危红线与边界避坑指南</h4>
                <p className="text-xs sm:text-sm text-rose-800 dark:text-rose-200/80 leading-relaxed">
                  {solution.traps}
                </p>
              </div>
            </div>
          )}

          {/* 7️⃣ 第七步：个人学习手记与白板草稿 (Notes) */}
          <div className="space-y-2">
            <div className="flex items-center justify-between">
              <label htmlFor="notes" className="text-sm font-bold text-slate-800 dark:text-slate-200 flex items-center gap-2">
                <Bookmark className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                <span>个人学习手记 / 易错点备忘 (沉淀第七步)</span>
              </label>
              {notesSavedNotice && (
                <span className="text-xs text-emerald-600 dark:text-emerald-400 flex items-center gap-1 animate-in fade-in">
                  <Check className="w-3.5 h-3.5" /> 已自动保存
                </span>
              )}
            </div>

            <textarea
              id="notes"
              rows={3}
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              placeholder="在此记录你刷此题时的心得、容易手滑的Bug、或者面试时想到的追问拓展... (支持自动持久化)"
              className="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl p-3 text-xs sm:text-sm text-slate-800 dark:text-slate-200 placeholder:text-slate-400 dark:placeholder:text-slate-600 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500/30 transition resize-none"
            />

            <div className="flex justify-end">
              <button
                onClick={handleSaveNotes}
                disabled={isSavingNotes}
                className="px-4 py-1.5 text-xs font-semibold text-slate-100 bg-slate-800 hover:bg-slate-700 active:scale-95 border border-slate-700 rounded-xl transition disabled:opacity-50"
              >
                {isSavingNotes ? '正在保存...' : '保存笔记'}
              </button>
            </div>
          </div>
        </div>

        {/* 底部吸底导航条 (上一题 / 下一题) */}
        <div className="px-6 py-3 border-t border-slate-200 dark:border-slate-800 bg-slate-50/90 dark:bg-slate-900/90 flex items-center justify-between">
          <button
            onClick={onNavigatePrev}
            disabled={!onNavigatePrev}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 disabled:opacity-35 transition active:scale-95"
          >
            <ChevronLeft className="w-4 h-4" />
            <span>上一题</span>
          </button>

          <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
            {currentIndex !== undefined && totalProblems && (
              <span>第 <strong className="text-emerald-600 dark:text-emerald-400">{currentIndex + 1}</strong> 关 / 共 {totalProblems} 关</span>
            )}
          </div>

          <button
            onClick={onNavigateNext}
            disabled={!onNavigateNext}
            className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white disabled:opacity-35 disabled:hover:bg-emerald-600 transition active:scale-95 shadow-sm shadow-emerald-600/20"
          >
            <span>下一题</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
