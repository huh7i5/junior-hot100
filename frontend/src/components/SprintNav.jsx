import React from 'react';
import { Calendar, Check } from 'lucide-react';

const DAY_LABELS = {
  1: { title: "Day 1", topic: "哈希/双指针/滑窗", count: 17 },
  2: { title: "Day 2", topic: "矩阵与链表全解", count: 18 },
  3: { title: "Day 3", topic: "二叉树与图论遍历", count: 19 },
  4: { title: "Day 4", topic: "回溯搜索与二分查找", count: 14 },
  5: { title: "Day 5", topic: "栈/堆与贪心矩阵", count: 12 },
  6: { title: "Day 6", topic: "动态规划一维经典", count: 10 },
  7: { title: "Day 7", topic: "多维DP与技巧收官", count: 10 },
};

export default function SprintNav({ selectedDay, onSelectDay, dayStats = [] }) {
  // 建立 day -> stat 快速索引
  const statsMap = {};
  dayStats.forEach(s => {
    statsMap[s.day] = s;
  });

  return (
    <div className="bg-white/80 dark:bg-slate-900/40 border border-slate-200 dark:border-slate-800/80 rounded-2xl p-2.5 sm:p-3 mb-6 shadow-sm backdrop-blur-md transition-colors duration-150">
      <div className="flex items-center gap-2 mb-2 px-2 text-xs font-semibold text-slate-500 dark:text-slate-400">
        <Calendar className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
        <span>7 天冲刺时间线 (Sprint Roadmap)</span>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-2">
        {/* 全部按钮 */}
        <button
          onClick={() => onSelectDay(null)}
          className={`flex flex-col items-center justify-center p-2.5 rounded-xl border text-left transition-all active:scale-[0.98] ${
            selectedDay === null
              ? 'bg-emerald-50 dark:bg-emerald-500/10 border-emerald-400 dark:border-emerald-500/50 text-emerald-700 dark:text-emerald-300 ring-1 ring-emerald-400/30 dark:ring-emerald-500/30 shadow-sm'
              : 'bg-slate-50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-slate-200'
          }`}
        >
          <span className="text-xs font-bold">全部题库</span>
          <span className="text-[11px] text-slate-400 dark:text-slate-500 mt-0.5">100 题全景</span>
        </button>

        {/* Day 1 - Day 7 */}
        {[1, 2, 3, 4, 5, 6, 7].map(day => {
          const info = DAY_LABELS[day];
          const stat = statsMap[day] || { total: info.count, mastered: 0, avg_score: 0 };
          const isSelected = selectedDay === day;
          const isAllMastered = stat.mastered === stat.total && stat.total > 0;

          return (
            <button
              key={day}
              onClick={() => onSelectDay(day)}
              className={`relative flex flex-col p-2.5 rounded-xl border transition-all active:scale-[0.98] ${
                isSelected
                  ? 'bg-emerald-50 dark:bg-emerald-500/15 border-emerald-400 dark:border-emerald-500/60 text-emerald-800 dark:text-emerald-200 ring-1 ring-emerald-400/40 dark:ring-emerald-500/40 shadow-sm'
                  : 'bg-slate-50 dark:bg-slate-800/30 border-slate-200 dark:border-slate-800/80 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/70 hover:text-slate-900 dark:hover:text-slate-200'
              }`}
            >
              <div className="flex items-center justify-between w-full">
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">{info.title}</span>
                {isAllMastered ? (
                  <span className="w-4 h-4 rounded-full bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center">
                    <Check className="w-2.5 h-2.5 stroke-[3]" />
                  </span>
                ) : (
                  <span className="text-[10px] text-slate-400 dark:text-slate-500 font-medium">
                    {stat.mastered}/{stat.total}
                  </span>
                )}
              </div>
              <span className="text-[11px] truncate w-full text-slate-500 dark:text-slate-400 mt-1" title={info.topic}>
                {info.topic}
              </span>
              
              {/* 微型进度细线 */}
              <div className="w-full bg-slate-200 dark:bg-slate-800 h-1 rounded-full overflow-hidden mt-2">
                <div 
                  className="bg-emerald-500 h-full rounded-full transition-all duration-300"
                  style={{ width: `${stat.avg_score || 0}%` }}
                />
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}
