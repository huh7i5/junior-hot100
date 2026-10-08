import React from 'react';
import { CheckCircle2, ChevronRight, Sparkles, BookOpen } from 'lucide-react';

const DIFFICULTY_STYLE = {
  Easy: 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border-emerald-500/30',
  Medium: 'bg-amber-500/10 text-amber-700 dark:text-amber-400 border-amber-500/30',
  Hard: 'bg-rose-500/10 text-rose-700 dark:text-rose-400 border-rose-500/30'
};

const DIFFICULTY_LABEL = {
  Easy: '简单',
  Medium: '中等',
  Hard: '困难'
};

export default function ProblemCard({ problem, onOpenDetail }) {
  const isMastered = problem.status === 'mastered';
  const isInProgress = problem.status === 'in_progress';
  const score = problem.mastery_score || 0;
  const completedCount = problem.completed_checkpoints || 0;
  const totalCount = problem.total_checkpoints || 5;

  return (
    <div
      onClick={() => onOpenDetail(problem)}
      className={`group relative rounded-2xl border p-4 sm:p-5 cursor-pointer transition-all duration-200 active:scale-[0.99] ${
        isMastered
          ? 'bg-white dark:bg-slate-900/40 border-emerald-400/60 dark:border-emerald-500/40 hover:border-emerald-500 hover:shadow-md dark:hover:bg-slate-900/70'
          : isInProgress
          ? 'bg-white dark:bg-slate-900/40 border-amber-400/60 dark:border-amber-500/30 hover:border-amber-500 hover:shadow-md dark:hover:bg-slate-900/70'
          : 'bg-white dark:bg-slate-900/30 border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 hover:shadow-md dark:hover:bg-slate-900/60'
      }`}
    >
      {/* 顶部标签行 */}
      <div className="flex items-center justify-between gap-2 mb-2.5">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="text-xs font-mono font-bold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-800/80 px-2 py-0.5 rounded-md border border-slate-200 dark:border-slate-700">
            #{problem.frontend_id}
          </span>
          <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-md border ${DIFFICULTY_STYLE[problem.difficulty] || ''}`}>
            {DIFFICULTY_LABEL[problem.difficulty] || problem.difficulty}
          </span>
          <span className="text-[11px] text-slate-600 dark:text-slate-400 bg-slate-100/70 dark:bg-slate-800/40 px-2 py-0.5 rounded-md border border-slate-200 dark:border-slate-800">
            {problem.category}
          </span>
        </div>

        <span className="text-[11px] font-medium text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800/50 px-2 py-0.5 rounded-full">
          Day {problem.day}
        </span>
      </div>

      {/* 题目名称 */}
      <div className="mb-3">
        <h3 className="text-base font-bold text-slate-900 dark:text-slate-100 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center gap-1.5">
          {problem.title_cn}
          {isMastered && (
            <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 inline" />
          )}
        </h3>
        <p className="text-xs text-slate-400 dark:text-slate-500 truncate mt-0.5">
          {problem.title_en}
        </p>
      </div>

      {/* 底部微检查点与进度 */}
      <div className="pt-3 border-t border-slate-100 dark:border-slate-800/60 flex items-center justify-between text-xs">
        {/* 动态微检查点指示 */}
        <div className="flex items-center gap-1.5 text-slate-400">
          <div className="flex items-center gap-1">
            {Array.from({ length: totalCount }).map((_, idx) => {
              const isDone = idx < completedCount;
              return (
                <div
                  key={idx}
                  title={`检查点 ${idx + 1}/${totalCount}`}
                  className={`w-2 h-2 rounded-full transition-colors ${
                    isDone 
                      ? 'bg-emerald-500 dark:bg-emerald-400 shadow-sm shadow-emerald-500/50' 
                      : 'bg-slate-200 dark:bg-slate-700'
                  }`}
                />
              );
            })}
          </div>
          <span className="text-[11px] text-slate-400 dark:text-slate-500 ml-1 font-mono">
            {completedCount}/{totalCount} 点
          </span>
        </div>

        {/* 掌握度百分比 */}
        <div className="flex items-center gap-2">
          <span className={`font-mono font-bold text-xs ${
            isMastered 
              ? 'text-emerald-600 dark:text-emerald-400' 
              : isInProgress 
              ? 'text-amber-600 dark:text-amber-400' 
              : 'text-slate-400 dark:text-slate-500'
          }`}>
            {score}%
          </span>
          <ChevronRight className="w-4 h-4 text-slate-400 dark:text-slate-600 group-hover:text-slate-700 dark:group-hover:text-slate-300 group-hover:translate-x-0.5 transition-all" />
        </div>
      </div>

      {/* 底部细线条进度条 */}
      <div className="absolute bottom-0 left-4 right-4 h-0.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
        <div
          className={`h-full transition-all duration-300 ${
            isMastered
              ? 'bg-emerald-500'
              : isInProgress
              ? 'bg-amber-400'
              : 'bg-transparent'
          }`}
          style={{ width: `${score}%` }}
        />
      </div>
    </div>
  );
}
