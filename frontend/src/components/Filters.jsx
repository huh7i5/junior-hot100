import React from 'react';
import { Search, Filter, X, Tag } from 'lucide-react';

export default function Filters({
  search,
  onSearchChange,
  difficulty,
  onDifficultyChange,
  status,
  onStatusChange,
  selectedCategory,
  onCategoryChange,
  categories = [],
  onResetFilters
}) {
  const hasActiveFilters = search || difficulty || status !== 'all' || selectedCategory;

  return (
    <div className="bg-white/90 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 mb-6 shadow-sm transition-colors duration-150">
      <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-4">
        {/* 搜索框 */}
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={search}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="搜索题号、中文题名或英文 (如: 1, 两数之和, Two Sum)..."
            className="w-full bg-slate-50 dark:bg-slate-950/80 border border-slate-200 dark:border-slate-800 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20 text-slate-900 dark:text-slate-100 text-sm rounded-xl pl-10 pr-4 py-2.5 outline-none transition placeholder:text-slate-400 dark:placeholder:text-slate-500"
          />
          {search && (
            <button
              onClick={() => onSearchChange('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 p-1"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        {/* 状态与难度筛选组合 */}
        <div className="flex flex-wrap items-center gap-3">
          {/* 难度 */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-950/70 p-1 rounded-xl border border-slate-200 dark:border-slate-800 text-xs shadow-inner">
            {['', 'Easy', 'Medium', 'Hard'].map((diff) => (
              <button
                key={diff}
                onClick={() => onDifficultyChange(diff)}
                className={`px-2.5 py-1.5 rounded-lg font-medium transition active:scale-[0.98] ${
                  difficulty === diff
                    ? 'bg-white dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200/60 dark:border-transparent'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
              >
                {diff === '' ? '全部难度' : diff === 'Easy' ? '简单' : diff === 'Medium' ? '中等' : '困难'}
              </button>
            ))}
          </div>

          {/* 状态 */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-950/70 p-1 rounded-xl border border-slate-200 dark:border-slate-800 text-xs shadow-inner">
            {[
              { id: 'all', label: '全部状态' },
              { id: 'mastered', label: '已通关' },
              { id: 'in_progress', label: '攻坚中' },
              { id: 'todo', label: '待开始' }
            ].map((st) => (
              <button
                key={st.id}
                onClick={() => onStatusChange(st.id)}
                className={`px-2.5 py-1.5 rounded-lg font-medium transition active:scale-[0.98] ${
                  status === st.id
                    ? 'bg-white dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200/60 dark:border-transparent'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
              >
                {st.label}
              </button>
            ))}
          </div>

          {hasActiveFilters && (
            <button
              onClick={onResetFilters}
              className="text-xs text-rose-600 dark:text-rose-400 hover:text-rose-700 dark:hover:text-rose-300 flex items-center gap-1 px-2.5 py-1.5 rounded-lg hover:bg-rose-50 dark:hover:bg-rose-500/10 transition active:scale-95"
              title="重置所有搜索和筛选条件"
            >
              <X className="w-3.5 h-3.5" />
              <span>清空筛选</span>
            </button>
          )}
        </div>
      </div>

      {/* 分类专题标签横滑区 */}
      {categories.length > 0 && (
        <div className="flex items-center gap-1.5 mt-3 pt-3 border-t border-slate-200 dark:border-slate-800/80 overflow-x-auto pb-1 scrollbar-none text-xs">
          <span className="text-slate-500 dark:text-slate-400 flex items-center gap-1 shrink-0 mr-1 text-[11px] font-medium">
            <Tag className="w-3 h-3 text-slate-400" />
            专题:
          </span>
          <button
            onClick={() => onCategoryChange('')}
            className={`px-2.5 py-1 rounded-lg shrink-0 font-medium transition active:scale-[0.98] ${
              !selectedCategory
                ? 'bg-emerald-50 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/40 shadow-sm'
                : 'bg-slate-50 dark:bg-slate-800/40 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'
            }`}
          >
            全部专题
          </button>
          {categories.map((c) => (
            <button
              key={c.category}
              onClick={() => onCategoryChange(selectedCategory === c.category ? '' : c.category)}
              className={`px-2.5 py-1 rounded-lg shrink-0 font-medium transition flex items-center gap-1.5 active:scale-[0.98] ${
                selectedCategory === c.category
                  ? 'bg-emerald-50 dark:bg-emerald-500/20 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-500/40 shadow-sm'
                  : 'bg-slate-50 dark:bg-slate-800/40 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-slate-200 border border-slate-200 dark:border-slate-800'
              }`}
            >
              <span>{c.category}</span>
              <span className="text-[10px] text-slate-500 dark:text-slate-400 bg-slate-200/80 dark:bg-slate-900 px-1.5 py-0.2 rounded-full font-mono">
                {c.mastered}/{c.total}
              </span>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
