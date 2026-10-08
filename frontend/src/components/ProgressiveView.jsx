import React, { useState } from 'react';
import { 
  Flame, 
  CheckCircle2, 
  CircleDashed, 
  Clock, 
  ChevronRight, 
  Trophy, 
  Target, 
  Sparkles,
  ArrowRight,
  BookOpen,
  Calendar,
  Layers,
  Compass
} from 'lucide-react';

const DAY_INFO = {
  1: { title: "Day 1", topic: "哈希/双指针/滑窗", count: 17 },
  2: { title: "Day 2", topic: "矩阵与链表全解", count: 18 },
  3: { title: "Day 3", topic: "二叉树与图论遍历", count: 19 },
  4: { title: "Day 4", topic: "回溯搜索与二分查找", count: 14 },
  5: { title: "Day 5", topic: "栈/堆与贪心矩阵", count: 12 },
  6: { title: "Day 6", topic: "动态规划一维经典", count: 10 },
  7: { title: "Day 7", topic: "多维DP与技巧收官", count: 10 },
};

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

export default function ProgressiveView({ 
  problems = [], 
  overview, 
  onOpenDetail 
}) {
  // 查找当前应该攻坚的关卡焦点 (第一个未通关题目，优先正在攻坚中)
  const inProgressQuest = problems.find(p => p.status === 'in_progress');
  const firstTodoQuest = problems.find(p => p.status === 'todo');
  const activeQuest = inProgressQuest || firstTodoQuest || problems[0];

  const activeQuestIndex = activeQuest 
    ? problems.findIndex(p => p.id === activeQuest.id)
    : 0;

  // 默认选中的 Day（若 activeQuest 存在，默认选中 activeQuest.day，否则为 1）
  const [selectedDay, setSelectedDay] = useState(activeQuest?.day || 1);

  // 过滤出所选 Day 的题目列表
  const dayProblems = problems.filter(p => p.day === selectedDay);

  const isAllMastered = problems.length > 0 && problems.every(p => p.status === 'mastered');

  return (
    <div className="space-y-6 animate-in fade-in duration-200">
      
      {/* 1. 当前攻坚焦点关卡 (Active Quest Spotlight) */}
      {isAllMastered ? (
        <div className="bg-gradient-to-r from-emerald-500/20 via-teal-500/15 to-emerald-600/20 border border-emerald-500/40 rounded-3xl p-6 sm:p-8 text-center shadow-lg backdrop-blur-md">
          <div className="w-16 h-16 bg-emerald-500/20 border border-emerald-500/40 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-inner">
            <Trophy className="w-8 h-8 text-emerald-400" />
          </div>
          <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-2">
            🎉 恭喜！你已全量攻克 LeetCode Hot 100 全套题目！
          </h2>
          <p className="text-sm text-slate-600 dark:text-slate-300 max-w-lg mx-auto">
            所有 100 道核心题目及其深度微检查点均已点亮。你现在可以随时复盘任意关卡或重置单项打卡保持手感！
          </p>
        </div>
      ) : activeQuest && (
        <div className="relative overflow-hidden rounded-3xl border border-emerald-400/50 dark:border-emerald-500/40 bg-gradient-to-br from-white via-emerald-50/20 to-teal-50/30 dark:from-slate-900 dark:via-emerald-950/20 dark:to-slate-900 p-6 sm:p-7 shadow-lg shadow-emerald-500/5">
          {/* 背景装饰光晕 */}
          <div className="absolute -top-12 -right-12 w-48 h-48 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6 relative z-10">
            <div className="space-y-3 max-w-2xl">
              {/* 标签栏 */}
              <div className="flex items-center gap-2 flex-wrap">
                <span className="inline-flex items-center gap-1 px-3 py-1 text-xs font-black bg-emerald-600 text-white rounded-full shadow-sm shadow-emerald-600/30 uppercase tracking-wide">
                  <Flame className="w-3.5 h-3.5" />
                  当前主线关卡 #{activeQuestIndex + 1} / 100
                </span>
                <span className="px-2.5 py-0.5 text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded-lg border border-slate-200 dark:border-slate-700">
                  Day {activeQuest.day} · {DAY_INFO[activeQuest.day]?.topic}
                </span>
                <span className={`text-xs font-semibold px-2.5 py-0.5 rounded-lg border ${DIFFICULTY_STYLE[activeQuest.difficulty] || ''}`}>
                  {DIFFICULTY_LABEL[activeQuest.difficulty] || activeQuest.difficulty}
                </span>
                <span className="text-xs text-slate-600 dark:text-slate-400 bg-white/80 dark:bg-slate-800/80 px-2.5 py-0.5 rounded-lg border border-slate-200 dark:border-slate-700">
                  {activeQuest.category}
                </span>
              </div>

              {/* 题目标题 */}
              <div>
                <h2 className="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white flex items-center gap-2">
                  <span>#{activeQuest.frontend_id}</span>
                  <span>{activeQuest.title_cn}</span>
                  <span className="text-sm sm:text-base font-normal text-slate-500 dark:text-slate-400">
                    ({activeQuest.title_en})
                  </span>
                </h2>
                <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
                  当前关卡进度: {activeQuest.completed_checkpoints || 0} / {activeQuest.total_checkpoints || 5} 个要点打卡 
                  ({activeQuest.mastery_score || 0}%)
                </p>
              </div>

              {/* 关卡微检查点小圆点 */}
              <div className="flex items-center gap-1.5 pt-1">
                {Array.from({ length: activeQuest.total_checkpoints || 5 }).map((_, idx) => {
                  const isDone = idx < (activeQuest.completed_checkpoints || 0);
                  return (
                    <div 
                      key={idx}
                      className={`h-2.5 rounded-full transition-all duration-300 ${
                        isDone 
                          ? 'w-6 bg-emerald-500 shadow-sm shadow-emerald-500/50' 
                          : 'w-2.5 bg-slate-200 dark:bg-slate-700'
                      }`}
                      title={`要点 ${idx + 1}`}
                    />
                  );
                })}
              </div>
            </div>

            {/* 立即进入攻坚按钮 */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 shrink-0">
              <button
                onClick={() => onOpenDetail(activeQuest)}
                className="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-2xl text-sm font-black bg-emerald-600 hover:bg-emerald-500 text-white shadow-lg shadow-emerald-600/30 transition-all active:scale-95"
              >
                <span>🔥 立即攻坚此题 (查看大白话与代码)</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 2. 7-Day 闯关路线图指示器 (Stage Stepper) */}
      <div className="bg-white/90 dark:bg-slate-900/50 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm backdrop-blur-md">
        <div className="flex items-center justify-between mb-3 px-1">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-700 dark:text-slate-300">
            <Compass className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            <span>7-Day 阶段关卡路径 (Stage Milestones)</span>
          </div>
          <span className="text-[11px] text-slate-500 dark:text-slate-400">
            点击切换阶段，查看关卡链条
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2.5">
          {[1, 2, 3, 4, 5, 6, 7].map(day => {
            const info = DAY_INFO[day];
            const stageProblems = problems.filter(p => p.day === day);
            const masteredCount = stageProblems.filter(p => p.status === 'mastered').length;
            const totalStage = stageProblems.length || info.count;
            const isStageDone = masteredCount === totalStage && totalStage > 0;
            const isStageCurrent = activeQuest?.day === day;
            const isSelected = selectedDay === day;

            return (
              <button
                key={day}
                onClick={() => setSelectedDay(day)}
                className={`relative flex flex-col p-3 rounded-2xl border text-left transition-all active:scale-[0.98] ${
                  isSelected
                    ? 'bg-emerald-50 dark:bg-emerald-500/15 border-emerald-400 dark:border-emerald-500/60 ring-2 ring-emerald-400/40 shadow-sm'
                    : 'bg-slate-50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                }`}
              >
                {/* 阶段标题与图标 */}
                <div className="flex items-center justify-between w-full mb-1">
                  <span className={`text-xs font-black ${
                    isSelected ? 'text-emerald-700 dark:text-emerald-300' : 'text-slate-800 dark:text-slate-200'
                  }`}>
                    {info.title}
                  </span>
                  {isStageDone ? (
                    <span className="w-4 h-4 rounded-full bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 flex items-center justify-center">
                      <CheckCircle2 className="w-3.5 h-3.5" />
                    </span>
                  ) : isStageCurrent ? (
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                  ) : null}
                </div>

                <div className="text-[11px] text-slate-500 dark:text-slate-400 truncate mb-2" title={info.topic}>
                  {info.topic}
                </div>

                {/* 进度百分比 */}
                <div className="flex items-center justify-between text-[10px] text-slate-400 dark:text-slate-500 mb-1 font-mono">
                  <span>{masteredCount}/{totalStage} 关</span>
                  <span>{Math.round((masteredCount / (totalStage || 1)) * 100)}%</span>
                </div>

                {/* 进度细线 */}
                <div className="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
                  <div 
                    className="bg-emerald-500 h-full rounded-full transition-all duration-300"
                    style={{ width: `${(masteredCount / (totalStage || 1)) * 100}%` }}
                  />
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* 3. 当前选中 Day 关卡链条 (Sequential Quest Trail) */}
      <div className="bg-white/80 dark:bg-slate-900/40 border border-slate-200 dark:border-slate-800 rounded-3xl p-5 sm:p-6 shadow-sm">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between pb-4 border-b border-slate-200 dark:border-slate-800 mb-5 gap-2">
          <div>
            <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <span className="px-2 py-0.5 text-xs font-bold bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 rounded-lg border border-emerald-500/20">
                Day {selectedDay} 关卡序列
              </span>
              <span>{DAY_INFO[selectedDay]?.topic}</span>
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
              本阶段共 {dayProblems.length} 道题目，按题号与认知曲线层层递进，点击任意卡片即可进入深度拆解
            </p>
          </div>
        </div>

        {/* 顺序关卡列表 */}
        <div className="space-y-3">
          {dayProblems.map((problem, idx) => {
            const isMastered = problem.status === 'mastered';
            const isInProgress = problem.status === 'in_progress';
            const isCurrentActive = activeQuest?.id === problem.id;
            const completedCount = problem.completed_checkpoints || 0;
            const totalCount = problem.total_checkpoints || 5;

            return (
              <div
                key={problem.id}
                onClick={() => onOpenDetail(problem)}
                className={`group relative flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-2xl border transition-all duration-150 cursor-pointer active:scale-[0.99] gap-4 ${
                  isCurrentActive
                    ? 'bg-emerald-50/80 dark:bg-emerald-950/30 border-emerald-400 dark:border-emerald-500/60 ring-2 ring-emerald-400/30 shadow-md'
                    : isMastered
                    ? 'bg-white dark:bg-slate-900/60 border-slate-200 dark:border-slate-800/80 hover:border-emerald-300 dark:hover:border-emerald-500/40'
                    : isInProgress
                    ? 'bg-amber-50/40 dark:bg-amber-950/20 border-amber-300 dark:border-amber-500/40 hover:border-amber-400'
                    : 'bg-slate-50/70 dark:bg-slate-900/30 border-slate-200 dark:border-slate-800/60 hover:border-slate-300 dark:hover:border-slate-700'
                }`}
              >
                {/* 左侧：关卡序列序号 + 状态图标 + 题目信息 */}
                <div className="flex items-center gap-3.5 min-w-0">
                  {/* 状态徽章 */}
                  <div className="shrink-0 flex items-center justify-center">
                    {isMastered ? (
                      <div className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center border border-emerald-500/30">
                        <CheckCircle2 className="w-5 h-5" />
                      </div>
                    ) : isCurrentActive ? (
                      <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center shadow-md shadow-emerald-600/30 animate-pulse">
                        <Target className="w-5 h-5" />
                      </div>
                    ) : isInProgress ? (
                      <div className="w-8 h-8 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400 flex items-center justify-center border border-amber-500/30">
                        <Clock className="w-5 h-5" />
                      </div>
                    ) : (
                      <div className="w-8 h-8 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-400 flex items-center justify-center border border-slate-200 dark:border-slate-700">
                        <CircleDashed className="w-5 h-5" />
                      </div>
                    )}
                  </div>

                  <div className="min-w-0">
                    <div className="flex items-center gap-2 flex-wrap mb-1">
                      <span className="text-xs font-mono font-bold text-slate-500 dark:text-slate-400">
                        #{problem.frontend_id}
                      </span>
                      <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-md border ${DIFFICULTY_STYLE[problem.difficulty] || ''}`}>
                        {DIFFICULTY_LABEL[problem.difficulty] || problem.difficulty}
                      </span>
                      <span className="text-[10px] text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800/60 px-2 py-0.5 rounded-md border border-slate-200 dark:border-slate-700">
                        {problem.category}
                      </span>
                      {isCurrentActive && (
                        <span className="text-[10px] font-bold text-emerald-700 dark:text-emerald-300 bg-emerald-100 dark:bg-emerald-500/20 px-2 py-0.5 rounded-md border border-emerald-300 dark:border-emerald-500/40">
                          🎯 当前攻坚
                        </span>
                      )}
                    </div>

                    <h4 className="text-sm sm:text-base font-bold text-slate-900 dark:text-slate-100 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center gap-2 truncate">
                      <span>{problem.title_cn}</span>
                      <span className="text-xs font-normal text-slate-400 dark:text-slate-500 truncate">
                        ({problem.title_en})
                      </span>
                    </h4>
                  </div>
                </div>

                {/* 右侧：检查点进度 + 操作按钮 */}
                <div className="flex items-center justify-between sm:justify-end gap-4 shrink-0 pt-2 sm:pt-0 border-t sm:border-t-0 border-slate-100 dark:border-slate-800">
                  {/* 检查点点位 */}
                  <div className="flex items-center gap-2">
                    <div className="flex items-center gap-1">
                      {Array.from({ length: totalCount }).map((_, cIdx) => {
                        const isDone = cIdx < completedCount;
                        return (
                          <div
                            key={cIdx}
                            className={`w-2 h-2 rounded-full transition-colors ${
                              isDone 
                                ? 'bg-emerald-500 dark:bg-emerald-400 shadow-sm shadow-emerald-500/50' 
                                : 'bg-slate-200 dark:bg-slate-700'
                            }`}
                          />
                        );
                      })}
                    </div>
                    <span className="text-xs text-slate-500 dark:text-slate-400 font-mono">
                      {completedCount}/{totalCount} 点
                    </span>
                  </div>

                  {/* 状态文字或按钮 */}
                  <div className="flex items-center gap-2">
                    <span className={`text-xs font-bold font-mono ${
                      isMastered 
                        ? 'text-emerald-600 dark:text-emerald-400' 
                        : isInProgress 
                        ? 'text-amber-600 dark:text-amber-400' 
                        : 'text-slate-400 dark:text-slate-500'
                    }`}>
                      {problem.mastery_score || 0}%
                    </span>

                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onOpenDetail(problem);
                      }}
                      className="px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 group-hover:border-emerald-400 group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition"
                    >
                      {isMastered ? '复盘' : isCurrentActive ? '开始攻坚' : '查看'}
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

    </div>
  );
}
