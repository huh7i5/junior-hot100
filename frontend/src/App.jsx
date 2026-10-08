import React, { useState, useEffect, useCallback } from 'react';
import Header from './components/Header';
import SprintNav from './components/SprintNav';
import Filters from './components/Filters';
import ProblemCard from './components/ProblemCard';
import ProblemDetailModal from './components/ProblemDetailModal';
import ProgressiveView from './components/ProgressiveView';
import ActivityHeatmap from './components/ActivityHeatmap';
import { 
  fetchOverview, 
  fetchProblems, 
  fetchProblemDetail, 
  toggleCheckpoint, 
  batchToggleCheckpoints, 
  updateProblemNotes,
  exportProgressData,
  fetchActivityHistory,
  importProgressData
} from './services/api';
import { Loader2, AlertCircle, Sparkles } from 'lucide-react';

export default function App() {
  const [overview, setOverview] = useState(null);
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Theme State: 'dark' | 'light'
  const [theme, setTheme] = useState(() => {
    try {
      return localStorage.getItem('hot100_theme') || 'dark';
    } catch (e) {
      return 'dark';
    }
  });

  // Sync theme with document class and localStorage
  useEffect(() => {
    try {
      localStorage.setItem('hot100_theme', theme);
      if (theme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } catch (e) {}
  }, [theme]);

  const handleToggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  // View Mode State: 'grid' (看板全览) | 'progressive' (渐进闯关)
  const [viewMode, setViewMode] = useState(() => {
    try {
      return localStorage.getItem('hot100_view_mode') || 'grid';
    } catch (e) {
      return 'grid';
    }
  });

  const handleViewModeChange = (mode) => {
    setViewMode(mode);
    try {
      localStorage.setItem('hot100_view_mode', mode);
    } catch (e) {}
  };

  // Filters State
  const [selectedDay, setSelectedDay] = useState(null);
  const [search, setSearch] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [status, setStatus] = useState('all');
  const [selectedCategory, setSelectedCategory] = useState('');

  // Active Problem Detail Drawer State
  const [activeProblemDetail, setActiveProblemDetail] = useState(null);
  const [drawerLoading, setDrawerLoading] = useState(false);

  // 加载总体统计
  const loadOverview = useCallback(async () => {
    try {
      const data = await fetchOverview();
      setOverview(data);
    } catch (err) {
      console.error('Failed to load overview:', err);
    }
  }, []);

  // 加载题目列表
  const loadProblems = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchProblems({
        day: selectedDay,
        category: selectedCategory,
        difficulty: difficulty,
        status: status,
        search: search
      });
      setProblems(data);
    } catch (err) {
      setError(err.message || '加载题目失败');
    } finally {
      setLoading(false);
    }
  }, [selectedDay, selectedCategory, difficulty, status, search]);

  // Activity Heatmap State
  const [activityHistory, setActivityHistory] = useState({});

  const loadActivity = useCallback(async () => {
    try {
      const data = await fetchActivityHistory();
      setActivityHistory(data || {});
    } catch (e) {
      console.error('Failed to load activity:', e);
    }
  }, []);

  useEffect(() => {
    loadOverview();
  }, [loadOverview]);

  useEffect(() => {
    loadProblems();
  }, [loadProblems]);

  useEffect(() => {
    loadActivity();
  }, [loadActivity]);

  // 打开题目详情抽屉
  const handleOpenDetail = async (problem) => {
    setDrawerLoading(true);
    try {
      const detail = await fetchProblemDetail(problem.id);
      setActiveProblemDetail(detail);
    } catch (err) {
      alert(`获取题目详情失败: ${err.message}`);
    } finally {
      setDrawerLoading(false);
    }
  };

  // 切换单项微检查点
  const handleToggleCheckpoint = async (checkpointId) => {
    try {
      const res = await toggleCheckpoint(checkpointId);
      // 更新抽屉中对应的 checkpoint 状态
      if (activeProblemDetail) {
        const updatedCheckpoints = activeProblemDetail.checkpoints.map(cp => 
          cp.id === checkpointId ? { ...cp, completed: res.completed ? 1 : 0 } : cp
        );
        setActiveProblemDetail({
          ...activeProblemDetail,
          checkpoints: updatedCheckpoints,
          problem: {
            ...activeProblemDetail.problem,
            mastery_score: res.mastery_score,
            status: res.status
          }
        });
      }

      // 更新列表项状态
      setProblems(prev => prev.map(p => {
        if (p.id === res.problem_id) {
          const delta = res.completed ? 1 : -1;
          return {
            ...p,
            mastery_score: res.mastery_score,
            status: res.status,
            completed_checkpoints: Math.max(0, (p.completed_checkpoints || 0) + delta)
          };
        }
        return p;
      }));

      // 更新全局统计
      if (res.overview) {
        setOverview(res.overview);
      }
      loadActivity();
    } catch (err) {
      alert(`操作检查点失败: ${err.message}`);
    }
  };

  // 批量全选 / 重置
  const handleBatchToggle = async (problemId, completed) => {
    try {
      const res = await batchToggleCheckpoints(problemId, completed);
      // 更新当前抽屉
      if (activeProblemDetail && activeProblemDetail.problem.id === problemId) {
        const updatedCheckpoints = activeProblemDetail.checkpoints.map(cp => ({
          ...cp,
          completed: completed ? 1 : 0
        }));
        setActiveProblemDetail({
          ...activeProblemDetail,
          checkpoints: updatedCheckpoints,
          problem: {
            ...activeProblemDetail.problem,
            mastery_score: res.mastery_score,
            status: res.status
          }
        });
      }

      // 更新列表项
      setProblems(prev => prev.map(p => {
        if (p.id === problemId) {
          return {
            ...p,
            mastery_score: res.mastery_score,
            status: res.status,
            completed_checkpoints: completed ? (p.total_checkpoints || 5) : 0
          };
        }
        return p;
      }));

      if (res.overview) {
        setOverview(res.overview);
      }
      loadActivity();
    } catch (err) {
      alert(`批量操作失败: ${err.message}`);
    }
  };

  // 保存个人手记
  const handleSaveNotes = async (problemId, notes) => {
    await updateProblemNotes(problemId, notes);
    if (activeProblemDetail && activeProblemDetail.problem.id === problemId) {
      setActiveProblemDetail({
        ...activeProblemDetail,
        problem: { ...activeProblemDetail.problem, notes }
      });
    }
  };

  // 导出数据为 JSON 文件
  const handleExport = async () => {
    try {
      const data = await exportProgressData();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `hot100_progress_backup_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err) {
      alert(`导出进度失败: ${err.message}`);
    }
  };

  // 导入备份数据
  const handleImport = async (data) => {
    try {
      const res = await importProgressData(data);
      if (res) setOverview(res);
      await loadProblems();
      await loadActivity();
      alert('🎉 历史做题进度、手记与修行热力图已成功恢复！');
    } catch (err) {
      alert(`导入失败: ${err.message}`);
    }
  };

  // 重置筛选
  const handleResetFilters = () => {
    setSearch('');
    setDifficulty('');
    setStatus('all');
    setSelectedCategory('');
    setSelectedDay(null);
  };

  // 弹窗内上下题顺序导航
  const activeProblemIndex = activeProblemDetail
    ? problems.findIndex(p => p.id === activeProblemDetail.problem?.id)
    : -1;

  const handleNavigatePrev = activeProblemIndex > 0
    ? () => handleOpenDetail(problems[activeProblemIndex - 1])
    : null;

  const handleNavigateNext = (activeProblemIndex >= 0 && activeProblemIndex < problems.length - 1)
    ? () => handleOpenDetail(problems[activeProblemIndex + 1])
    : null;

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col font-sans transition-colors duration-150">
      {/* 顶部全局导航栏 */}
      <Header 
        overview={overview} 
        onExport={handleExport}
        onImport={handleImport}
        theme={theme}
        onToggleTheme={handleToggleTheme}
        viewMode={viewMode}
        onViewModeChange={handleViewModeChange}
      />

      {/* 主体容器 */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* 每日修行热力图 (Activity Heatmap) */}
        <ActivityHeatmap activityHistory={activityHistory} />

        {viewMode === 'progressive' ? (
          /* 🚀 渐进闯关专注模式 */
          <ProgressiveView
            problems={problems}
            overview={overview}
            onOpenDetail={handleOpenDetail}
          />
        ) : (
          /* 📋 看板网格全览模式 */
          <>
            {/* 7 天攻坚日历导航 */}
            <SprintNav
              selectedDay={selectedDay}
              onSelectDay={setSelectedDay}
              dayStats={overview?.day_stats || []}
            />

            {/* 搜索与分类综合筛选器 */}
            <Filters
              search={search}
              onSearchChange={setSearch}
              difficulty={difficulty}
              onDifficultyChange={setDifficulty}
              status={status}
              onStatusChange={setStatus}
              selectedCategory={selectedCategory}
              onCategoryChange={setSelectedCategory}
              categories={overview?.category_stats || []}
              onResetFilters={handleResetFilters}
            />

            {/* 题目列表卡片网格 */}
            {loading ? (
              <div className="flex flex-col items-center justify-center py-20 text-slate-500">
                <Loader2 className="w-8 h-8 animate-spin text-emerald-500 mb-3" />
                <p className="text-sm">正在加载题目列表与原子化拆解数据...</p>
              </div>
            ) : error ? (
              <div className="flex flex-col items-center justify-center py-16 text-rose-500 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/20 border border-rose-200 dark:border-rose-800/40 rounded-2xl p-6">
                <AlertCircle className="w-8 h-8 mb-2" />
                <p className="text-sm">{error}</p>
                <button
                  onClick={loadProblems}
                  className="mt-4 px-4 py-1.5 text-xs bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-xl border border-slate-300 dark:border-slate-700 transition"
                >
                  重新加载
                </button>
              </div>
            ) : problems.length === 0 ? (
              <div className="text-center py-20 bg-white/60 dark:bg-slate-900/30 rounded-2xl border border-slate-200 dark:border-slate-800/80 p-8 shadow-sm">
                <Sparkles className="w-8 h-8 text-slate-400 dark:text-slate-600 mx-auto mb-2" />
                <h4 className="text-base font-bold text-slate-700 dark:text-slate-400">未找到符合条件的题目</h4>
                <p className="text-xs text-slate-500 mt-1">可以尝试更换筛选条件或点击“清空筛选”</p>
                <button
                  onClick={handleResetFilters}
                  className="mt-4 px-4 py-2 text-xs font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-500/10 hover:bg-emerald-100 dark:hover:bg-emerald-500/20 border border-emerald-300 dark:border-emerald-500/30 rounded-xl transition"
                >
                  重置所有条件
                </button>
              </div>
            ) : (
              <div>
                <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 mb-3 px-1">
                  <span>共筛选出 <strong className="text-emerald-600 dark:text-emerald-400 font-semibold">{problems.length}</strong> 道题目</span>
                  <span>点击卡片展开原子拆解、破题口诀与最优解代码</span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {problems.map((p) => (
                    <ProblemCard
                      key={p.id}
                      problem={p}
                      onOpenDetail={handleOpenDetail}
                    />
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </main>

      {/* 底部版权与声明 */}
      <footer className="border-t border-slate-200 dark:border-slate-900 py-6 text-center text-xs text-slate-500 dark:text-slate-600 transition-colors">
        <p>LeetCode Hot 100 Mastery Dashboard · {overview?.summary?.total_checkpoints || 520} 深度检查点 · Local SQLite & Browser Persistence</p>
      </footer>

      {/* 题目原子拆解与最优解居中大弹窗 */}
      <ProblemDetailModal
        problemDetail={activeProblemDetail}
        onClose={() => setActiveProblemDetail(null)}
        onToggleCheckpoint={handleToggleCheckpoint}
        onBatchToggle={handleBatchToggle}
        onSaveNotes={handleSaveNotes}
        onNavigatePrev={handleNavigatePrev}
        onNavigateNext={handleNavigateNext}
        currentIndex={activeProblemIndex >= 0 ? activeProblemIndex : undefined}
        totalProblems={problems.length}
      />
    </div>
  );
}
