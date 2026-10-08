import React, { useRef } from 'react';
import { 
  Trophy, 
  CheckCircle2, 
  Clock, 
  CircleDashed, 
  Download, 
  Upload,
  Sparkles,
  Target,
  Sun,
  Moon,
  LayoutGrid,
  Compass
} from 'lucide-react';

export default function Header({ 
  overview, 
  onExport,
  onImport,
  theme = 'dark',
  onToggleTheme,
  viewMode = 'grid',
  onViewModeChange
}) {
  const fileInputRef = useRef(null);
  const summary = overview?.summary || {
    total_problems: 100,
    mastered_problems: 0,
    in_progress_problems: 0,
    todo_problems: 100,
    total_checkpoints: 520,
    completed_checkpoints: 0,
    overall_progress: 0.0
  };

  const progress = summary.overall_progress || 0;

  return (
    <header className="border-b border-slate-200 dark:border-slate-800 bg-white/90 dark:bg-slate-900/75 backdrop-blur-xl sticky top-0 z-30 shadow-sm dark:shadow-lg transition-colors duration-150">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          
          {/* Logo & Main Title */}
          <div className="flex items-center space-x-3.5">
            <div className="w-11 h-11 rounded-xl bg-gradient-to-tr from-emerald-600 via-teal-500 to-cyan-400 flex items-center justify-center shadow-md shadow-emerald-500/20 ring-1 ring-black/5 dark:ring-white/20 shrink-0">
              <Trophy className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h1 className="text-xl sm:text-2xl font-black tracking-tight text-slate-900 dark:text-white flex items-center">
                  Hot 100 原子化突破体系
                </h1>
                <span className="px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border border-emerald-500/30 rounded-full">
                  7-Day Sprint
                </span>
              </div>
              <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 flex items-center gap-1.5 mt-0.5">
                <Sparkles className="w-3.5 h-3.5 text-amber-500 dark:text-amber-400 shrink-0" />
                <span><strong className="text-emerald-600 dark:text-emerald-400 font-semibold">{summary.total_checkpoints || 520}</strong> 个深度检查点 · 深度量化掌控每一题破题逻辑与边界死穴</span>
              </p>
            </div>
          </div>

          {/* Right Toolbar: View Mode + Theme Switcher + Metrics + Export */}
          <div className="flex flex-wrap items-center gap-3 sm:gap-4">
            
            {/* 渐进模式 / 全览看板 切换器 */}
            <div className="flex items-center bg-slate-100 dark:bg-slate-800/80 p-1 rounded-xl border border-slate-200 dark:border-slate-700/70 text-xs shadow-inner">
              <button
                onClick={() => onViewModeChange && onViewModeChange('grid')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-medium transition-all active:scale-[0.98] ${
                  viewMode === 'grid'
                    ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200/80 dark:border-slate-700'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
                title="网格全览模式：平铺 100 道题目与多维分类筛选"
              >
                <LayoutGrid className="w-3.5 h-3.5" />
                <span>全览看板</span>
              </button>

              <button
                onClick={() => onViewModeChange && onViewModeChange('progressive')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-medium transition-all active:scale-[0.98] ${
                  viewMode === 'progressive'
                    ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-sm border border-slate-200/80 dark:border-slate-700'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                }`}
                title="渐进模式：关卡主线递进、焦点攻坚推荐、里程碑冲刺"
              >
                <Compass className="w-3.5 h-3.5" />
                <span>渐进闯关</span>
              </button>
            </div>

            {/* 总体掌握度指示器 */}
            <div className="hidden sm:flex items-center bg-slate-100/90 dark:bg-slate-800/80 px-3.5 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700/60 shadow-inner">
              <div className="mr-2.5">
                <div className="text-[11px] text-slate-500 dark:text-slate-400 font-medium flex items-center gap-1">
                  <Target className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
                  全局掌控
                </div>
                <div className="text-base font-bold text-emerald-600 dark:text-emerald-400 tracking-tight leading-none">
                  {progress}%
                </div>
              </div>
              <div className="w-16 bg-slate-200 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                <div 
                  className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500 ease-out"
                  style={{ width: `${Math.min(100, Math.max(0, progress))}%` }}
                />
              </div>
            </div>

            {/* 统计指标徽章 */}
            <div className="flex items-center gap-1.5 text-xs">
              <div 
                className="flex items-center gap-1 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-400 px-2.5 py-1.5 rounded-lg border border-emerald-200 dark:border-emerald-800/40"
                title={`已完全攻克的题目数量: ${summary.mastered_problems}/100`}
              >
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                <span className="text-[11px]">已过:</span>
                <span className="font-bold text-xs">{summary.mastered_problems}</span>
              </div>
              <div 
                className="flex items-center gap-1 bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-400 px-2.5 py-1.5 rounded-lg border border-amber-200 dark:border-amber-800/40"
                title={`正在按照检查点逐项啃题的数量: ${summary.in_progress_problems}`}
              >
                <Clock className="w-3.5 h-3.5 text-amber-600 dark:text-amber-400" />
                <span className="text-[11px]">攻坚:</span>
                <span className="font-bold text-xs">{summary.in_progress_problems}</span>
              </div>
              <div 
                className="flex items-center gap-1 bg-slate-100 dark:bg-slate-800/60 text-slate-600 dark:text-slate-400 px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700/40"
                title={`尚未开始的题目数量: ${summary.todo_problems}`}
              >
                <CircleDashed className="w-3.5 h-3.5 text-slate-400" />
                <span className="text-[11px]">待刷:</span>
                <span className="font-bold text-xs">{summary.todo_problems}</span>
              </div>
            </div>

            {/* 白天/夜间 模式切换按钮 */}
            <button
              onClick={onToggleTheme}
              title={theme === 'dark' ? '切换为清爽白天模式 (Light Mode)' : '切换为护眼暗黑模式 (Dark Mode)'}
              className="p-2 rounded-xl text-slate-600 dark:text-slate-300 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700 transition active:scale-95 shadow-sm"
              aria-label="Toggle Theme"
            >
              {theme === 'dark' ? (
                <Sun className="w-4 h-4 text-amber-400" />
              ) : (
                <Moon className="w-4 h-4 text-indigo-600" />
              )}
            </button>

            {/* 导入备份按钮与隐藏输入框 */}
            <input
              type="file"
              ref={fileInputRef}
              accept=".json"
              className="hidden"
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (file && onImport) {
                  const reader = new FileReader();
                  reader.onload = (event) => {
                    try {
                      const data = JSON.parse(event.target.result);
                      onImport(data);
                    } catch (err) {
                      alert('解析备份文件失败，请确认文件格式正确');
                    }
                  };
                  reader.readAsText(file);
                }
                e.target.value = '';
              }}
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              title="导入此前的备份 JSON 文件 (跨设备/重装无缝恢复)"
              className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition shadow-sm active:scale-95"
            >
              <Upload className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
              <span className="hidden sm:inline">导入恢复</span>
            </button>

            {/* 导出备份按钮 */}
            <button
              onClick={onExport}
              title="导出当前做题进度与心得为 JSON 文件 (本地无云端依赖)"
              className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition shadow-sm active:scale-95"
            >
              <Download className="w-3.5 h-3.5 text-slate-500 dark:text-slate-400" />
              <span className="hidden sm:inline">导出备份</span>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
