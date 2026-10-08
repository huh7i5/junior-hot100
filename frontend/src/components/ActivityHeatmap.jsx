import React, { useState, useMemo } from 'react';
import { 
  Flame, 
  Trophy, 
  Calendar, 
  Sparkles, 
  ChevronDown, 
  ChevronUp,
  Target,
  Zap
} from 'lucide-react';

const MONTH_NAMES = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];

function formatDayStr(d) {
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

export default function ActivityHeatmap({ activityHistory = {} }) {
  const [isExpanded, setIsExpanded] = useState(true);
  const [hoveredDay, setHoveredDay] = useState(null);

  // 计算连续打卡天数与历史纪录
  const { currentStreak, longestStreak, totalActiveDays, totalPoints } = useMemo(() => {
    const today = new Date();
    const todayStr = formatDayStr(today);
    
    const yesterday = new Date(today);
    yesterday.setDate(today.getDate() - 1);
    const yesterdayStr = formatDayStr(yesterday);

    let streak = 0;
    let checkDate = new Date(today);

    // 今日有打卡从今日开始倒推；今日尚无从昨日倒推
    if ((activityHistory[todayStr] || 0) > 0) {
      streak++;
      checkDate.setDate(checkDate.getDate() - 1);
    } else if ((activityHistory[yesterdayStr] || 0) > 0) {
      checkDate = yesterday;
    }

    if (streak > 0 || (activityHistory[yesterdayStr] || 0) > 0) {
      while (true) {
        const dStr = formatDayStr(checkDate);
        if ((activityHistory[dStr] || 0) > 0) {
          streak++;
          checkDate.setDate(checkDate.getDate() - 1);
        } else {
          break;
        }
      }
    }

    // 计算最长连续与总活跃天数
    const sortedDates = Object.keys(activityHistory).filter(d => activityHistory[d] > 0).sort();
    let maxStreak = 0;
    let temp = 0;
    let prev = null;
    let points = 0;

    sortedDates.forEach(dateStr => {
      points += activityHistory[dateStr];
      const cur = new Date(dateStr);
      if (prev) {
        const diff = Math.round((cur - prev) / (1000 * 60 * 60 * 24));
        if (diff === 1) temp++;
        else temp = 1;
      } else {
        temp = 1;
      }
      prev = cur;
      if (temp > maxStreak) maxStreak = temp;
    });

    maxStreak = Math.max(maxStreak, streak);

    return {
      currentStreak: streak,
      longestStreak: maxStreak,
      totalActiveDays: sortedDates.length,
      totalPoints: points
    };
  }, [activityHistory]);

  // 生成最近 26 周 (约半年) 的热力格子数据，按列排列
  const { weeks, monthLabels } = useMemo(() => {
    const today = new Date();
    const weeksCount = 26; // 26周
    const totalDays = weeksCount * 7;

    // 结束日期对齐到本周周六 (0:周日, 6:周六)
    const dayOfWeek = today.getDay();
    const endDate = new Date(today);
    endDate.setDate(today.getDate() + (6 - dayOfWeek));

    const startDate = new Date(endDate);
    startDate.setDate(endDate.getDate() - totalDays + 1);

    const columns = [];
    const months = [];
    let lastMonth = -1;

    const cur = new Date(startDate);
    for (let w = 0; w < weeksCount; w++) {
      const colDays = [];
      for (let d = 0; d < 7; d++) {
        const dateStr = formatDayStr(cur);
        const count = activityHistory[dateStr] || 0;
        const isToday = cur.toDateString() === today.toDateString();
        const isFuture = cur > today;

        colDays.push({
          dateStr,
          month: cur.getMonth(),
          dayOfMonth: cur.getDate(),
          count,
          isToday,
          isFuture
        });

        // 记录月份标题显示位置
        if (d === 0) {
          const m = cur.getMonth();
          if (m !== lastMonth) {
            months.push({ colIndex: w, name: MONTH_NAMES[m] });
            lastMonth = m;
          }
        }

        cur.setDate(cur.getDate() + 1);
      }
      columns.push(colDays);
    }

    return { weeks: columns, monthLabels: months };
  }, [activityHistory]);

  const getCellColor = (count, isFuture, isToday) => {
    if (isFuture) return 'bg-transparent border border-dashed border-slate-200/50 dark:border-slate-800/50 opacity-20';
    if (count <= 0) return 'bg-slate-100 dark:bg-slate-800/40 border border-slate-200/60 dark:border-slate-800/70 hover:border-slate-400';
    if (count <= 2) return 'bg-emerald-300 dark:bg-emerald-950 border border-emerald-400 dark:border-emerald-800/80 hover:brightness-110';
    if (count <= 5) return 'bg-emerald-400 dark:bg-emerald-700 border border-emerald-500 dark:border-emerald-600 hover:brightness-110';
    if (count <= 8) return 'bg-emerald-500 dark:bg-emerald-500 border border-emerald-600 dark:border-emerald-400 hover:brightness-110';
    return 'bg-emerald-600 dark:bg-emerald-400 border border-emerald-700 dark:border-emerald-300 shadow-sm shadow-emerald-500/40 hover:brightness-110';
  };

  return (
    <div className="bg-white/90 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 mb-6 shadow-sm transition-colors duration-150">
      
      {/* 顶部标题与打卡连胜统计 */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 pb-3 border-b border-slate-100 dark:border-slate-800/60">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 flex items-center justify-center border border-emerald-500/20">
            <Calendar className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
              <span>刷题修行热力图</span>
              <span className="text-[11px] font-normal text-slate-400"> (Activity Heatmap)</span>
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              记录你在本地每一次打卡与知识点突破 · 浏览器永久保留
            </p>
          </div>
        </div>

        {/* 核心打卡数据微徽章 */}
        <div className="flex items-center gap-2 flex-wrap">
          {/* 连续打卡 */}
          <div 
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-400 border border-amber-200 dark:border-amber-800/40"
            title="连续活跃打卡天数（今天或昨天有打卡即计入）"
          >
            <Flame className="w-4 h-4 text-amber-500 fill-amber-500/30" />
            <span>连续:</span>
            <span className="font-bold text-sm">{currentStreak}</span>
            <span className="text-[10px]">天</span>
          </div>

          {/* 历史最长 */}
          <div 
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800/40"
            title="历史最长连续打卡纪录"
          >
            <Trophy className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
            <span>纪录:</span>
            <span className="font-bold text-sm">{longestStreak}</span>
            <span className="text-[10px]">天</span>
          </div>

          {/* 累计活跃 */}
          <div 
            className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800/60 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700/60"
            title="总计打卡天数"
          >
            <Target className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
            <span>活跃:</span>
            <span className="font-bold text-sm">{totalActiveDays}</span>
            <span className="text-[10px]">天</span>
          </div>

          {/* 折叠切换按钮 */}
          <button
            onClick={() => setIsExpanded(prev => !prev)}
            className="p-1.5 rounded-lg text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
            title={isExpanded ? '收起热力图' : '展开热力图'}
          >
            {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* 热力图主体网格 */}
      {isExpanded && (
        <div className="pt-3 animate-in fade-in duration-150">
          <div className="overflow-x-auto pb-2 scrollbar-none">
            <div className="inline-block min-w-full">
              
              {/* 月份标题栏 */}
              <div className="flex text-[11px] text-slate-400 font-medium pl-6 mb-1 h-4">
                {monthLabels.map((m, idx) => (
                  <div 
                    key={idx}
                    style={{ marginLeft: idx === 0 ? `${m.colIndex * 15}px` : `${(m.colIndex - monthLabels[idx - 1].colIndex - 1) * 15}px` }}
                  >
                    {m.name}
                  </div>
                ))}
              </div>

              {/* 星期标签 + 热力格子阵列 */}
              <div className="flex items-start gap-1.5">
                {/* 星期指引 (周一、周三、周五) */}
                <div className="flex flex-col justify-between text-[10px] text-slate-400 font-medium pr-1 h-[98px]">
                  <span className="leading-none pt-0.5">日</span>
                  <span className="leading-none">二</span>
                  <span className="leading-none">四</span>
                  <span className="leading-none pb-0.5">六</span>
                </div>

                {/* 26 列 x 7 行 */}
                <div className="flex gap-[3.5px]">
                  {weeks.map((col, wIdx) => (
                    <div key={wIdx} className="flex flex-col gap-[3.5px]">
                      {col.map((cell) => {
                        const colorClass = getCellColor(cell.count, cell.isFuture, cell.isToday);
                        return (
                          <div
                            key={cell.dateStr}
                            onMouseEnter={() => setHoveredDay(cell)}
                            onMouseLeave={() => setHoveredDay(null)}
                            title={`${cell.dateStr}: ${cell.count > 0 ? `完成 ${cell.count} 个检查点突破` : '未打卡'}`}
                            className={`w-[11.5px] h-[11.5px] rounded-[3px] transition-all duration-150 cursor-pointer ${colorClass} ${
                              cell.isToday ? 'ring-1.5 ring-emerald-500 ring-offset-1 dark:ring-offset-slate-900' : ''
                            }`}
                          />
                        );
                      })}
                    </div>
                  ))}
                </div>
              </div>

            </div>
          </div>

          {/* 底部信息栏：悬停动态提示 + 颜色刻度指示 */}
          <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 pt-2 border-t border-slate-100 dark:border-slate-800/40">
            <div className="flex items-center gap-1.5 min-h-[20px]">
              {hoveredDay ? (
                <span className="animate-in fade-in flex items-center gap-1 text-slate-800 dark:text-slate-200">
                  <span className="font-mono font-semibold">{hoveredDay.dateStr}</span>
                  <span>:</span>
                  <strong className={hoveredDay.count > 0 ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-400'}>
                    {hoveredDay.count > 0 ? `攻克 ${hoveredDay.count} 个检查点` : '无打卡记录'}
                  </strong>
                </span>
              ) : (
                <span className="text-[11px] text-slate-400">悬停格子查看单日突破明细</span>
              )}
            </div>

            {/* 颜色图例 */}
            <div className="flex items-center gap-1.5 text-[11px]">
              <span>少</span>
              <div className="w-2.5 h-2.5 rounded-[2px] bg-slate-100 dark:bg-slate-800/40 border border-slate-200/60 dark:border-slate-800/70" />
              <div className="w-2.5 h-2.5 rounded-[2px] bg-emerald-300 dark:bg-emerald-950 border border-emerald-400 dark:border-emerald-800/80" />
              <div className="w-2.5 h-2.5 rounded-[2px] bg-emerald-400 dark:bg-emerald-700 border border-emerald-500 dark:border-emerald-600" />
              <div className="w-2.5 h-2.5 rounded-[2px] bg-emerald-500 dark:bg-emerald-500 border border-emerald-600 dark:border-emerald-400" />
              <div className="w-2.5 h-2.5 rounded-[2px] bg-emerald-600 dark:bg-emerald-400 border border-emerald-700 dark:border-emerald-300" />
              <span>多</span>
            </div>
          </div>

        </div>
      )}

    </div>
  );
}
