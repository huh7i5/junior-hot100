import staticData from '../data/hot100Data.json';

const STORAGE_KEY_CHECKPOINTS = 'hot100_user_checkpoints';
const STORAGE_KEY_NOTES = 'hot100_user_notes';
const STORAGE_KEY_ACTIVITY = 'hot100_user_activity';

function getTodayStr() {
  const d = new Date();
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function getUserActivity() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_ACTIVITY) || '{}');
  } catch (e) {
    return {};
  }
}

function saveUserActivity(map) {
  try {
    localStorage.setItem(STORAGE_KEY_ACTIVITY, JSON.stringify(map));
  } catch (e) {}
}

function recordActivityDelta(delta) {
  if (!delta) return;
  const today = getTodayStr();
  const activity = getUserActivity();
  const current = activity[today] || 0;
  const updated = Math.max(0, current + delta);
  if (updated > 0) {
    activity[today] = updated;
  } else {
    delete activity[today];
  }
  saveUserActivity(activity);
}

function getUserCheckpoints() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_CHECKPOINTS) || '{}');
  } catch (e) {
    return {};
  }
}

function saveUserCheckpoints(map) {
  try {
    localStorage.setItem(STORAGE_KEY_CHECKPOINTS, JSON.stringify(map));
  } catch (e) {}
}

function getUserNotes() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_NOTES) || '{}');
  } catch (e) {
    return {};
  }
}

function saveUserNotes(map) {
  try {
    localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(map));
  } catch (e) {}
}

// 缓存基础数据
const { problems = [], checkpoints = [], solutions = [] } = staticData;

// 构建快速索引
const problemMap = new Map();
problems.forEach(p => problemMap.set(p.id, p));

const checkpointsByProblem = new Map();
checkpoints.forEach(cp => {
  if (!checkpointsByProblem.has(cp.problem_id)) {
    checkpointsByProblem.set(cp.problem_id, []);
  }
  checkpointsByProblem.get(cp.problem_id).push(cp);
});

const solutionMap = new Map();
solutions.forEach(s => solutionMap.set(s.problem_id, s));

/**
 * 计算单道题目的掌握度和状态
 */
function getProblemState(problemId, userCheckpoints) {
  const cps = checkpointsByProblem.get(problemId) || [];
  let score = 0;
  let completedCount = 0;

  cps.forEach(cp => {
    if (userCheckpoints[cp.id]) {
      score += (cp.weight || 0);
      completedCount += 1;
    }
  });

  score = Math.min(100, Math.round(score));
  let status = 'todo';
  if (score >= 100) {
    status = 'mastered';
  } else if (score > 0) {
    status = 'in_progress';
  }

  return {
    score,
    status,
    completedCount,
    totalCount: cps.length
  };
}

/**
 * 获取全局统计数据
 */
export function fetchOverviewLocal() {
  const userCheckpoints = getUserCheckpoints();

  let masteredProblems = 0;
  let inProgressProblems = 0;
  let todoProblems = 0;
  let totalScoreSum = 0;
  let completedCheckpoints = 0;

  const dayStatsMap = {};
  for (let d = 1; d <= 7; d++) {
    dayStatsMap[d] = { day: d, total: 0, mastered: 0, total_score: 0 };
  }

  const catStatsMap = {};

  problems.forEach(p => {
    const { score, status, completedCount } = getProblemState(p.id, userCheckpoints);
    totalScoreSum += score;
    completedCheckpoints += completedCount;

    if (status === 'mastered') masteredProblems++;
    else if (status === 'in_progress') inProgressProblems++;
    else todoProblems++;

    // Day stats
    if (dayStatsMap[p.day]) {
      dayStatsMap[p.day].total++;
      if (status === 'mastered') dayStatsMap[p.day].mastered++;
      dayStatsMap[p.day].total_score += score;
    }

    // Category stats
    if (!catStatsMap[p.category]) {
      catStatsMap[p.category] = { category: p.category, total: 0, mastered: 0 };
    }
    catStatsMap[p.category].total++;
    if (status === 'mastered') catStatsMap[p.category].mastered++;
  });

  const day_stats = Object.values(dayStatsMap).map(s => ({
    day: s.day,
    total: s.total,
    mastered: s.mastered,
    avg_score: s.total ? Math.round(s.total_score / s.total) : 0
  }));

  const category_stats = Object.values(catStatsMap).sort((a, b) => b.total - a.total);

  const overall_progress = problems.length 
    ? parseFloat((totalScoreSum / problems.length).toFixed(1))
    : 0;

  return {
    summary: {
      total_problems: problems.length,
      mastered_problems: masteredProblems,
      in_progress_problems: inProgressProblems,
      todo_problems: todoProblems,
      total_checkpoints: checkpoints.length,
      completed_checkpoints: completedCheckpoints,
      overall_progress
    },
    day_stats,
    category_stats
  };
}

/**
 * 筛选题目列表
 */
export function fetchProblemsLocal({ day, category, difficulty, status, search } = {}) {
  const userCheckpoints = getUserCheckpoints();
  const searchLower = (search || '').trim().toLowerCase();

  return problems
    .map(p => {
      const state = getProblemState(p.id, userCheckpoints);
      return {
        ...p,
        mastery_score: state.score,
        status: state.status,
        completed_checkpoints: state.completedCount,
        total_checkpoints: state.totalCount
      };
    })
    .filter(p => {
      if (day !== undefined && day !== null && day !== '' && p.day !== Number(day)) {
        return false;
      }
      if (category && p.category !== category) {
        return false;
      }
      if (difficulty && p.difficulty !== difficulty) {
        return false;
      }
      if (status && status !== 'all' && p.status !== status) {
        return false;
      }
      if (searchLower) {
        const matchesTitleCn = p.title_cn?.toLowerCase().includes(searchLower);
        const matchesTitleEn = p.title_en?.toLowerCase().includes(searchLower);
        const matchesId = String(p.frontend_id).includes(searchLower);
        if (!matchesTitleCn && !matchesTitleEn && !matchesId) return false;
      }
      return true;
    });
}

/**
 * 获取单道题目详情
 */
export function fetchProblemDetailLocal(problemId) {
  const p = problemMap.get(Number(problemId));
  if (!p) throw new Error(`未找到题目 ${problemId}`);

  const userCheckpoints = getUserCheckpoints();
  const userNotes = getUserNotes();
  const state = getProblemState(p.id, userCheckpoints);

  const cps = (checkpointsByProblem.get(p.id) || []).map(cp => ({
    ...cp,
    completed: userCheckpoints[cp.id] ? 1 : 0
  }));

  const sol = solutionMap.get(p.id) || null;

  return {
    problem: {
      ...p,
      notes: userNotes[p.id] || '',
      mastery_score: state.score,
      status: state.status
    },
    checkpoints: cps,
    solution: sol
  };
}

/**
 * 单项检查点打卡切换
 */
export function toggleCheckpointLocal(checkpointId) {
  const userCheckpoints = getUserCheckpoints();
  const cpId = Number(checkpointId);
  const cp = checkpoints.find(c => c.id === cpId);
  if (!cp) throw new Error(`未找到检查点 ${checkpointId}`);

  const newState = !userCheckpoints[cpId];
  if (newState) {
    userCheckpoints[cpId] = true;
    recordActivityDelta(1);
  } else {
    delete userCheckpoints[cpId];
    recordActivityDelta(-1);
  }
  saveUserCheckpoints(userCheckpoints);

  const state = getProblemState(cp.problem_id, userCheckpoints);
  const overview = fetchOverviewLocal();

  return {
    success: true,
    checkpoint_id: cpId,
    completed: newState,
    problem_id: cp.problem_id,
    mastery_score: state.score,
    status: state.status,
    overview
  };
}

/**
 * 批量全选 / 重置
 */
export function batchToggleCheckpointsLocal(problemId, completed) {
  const pId = Number(problemId);
  const cps = checkpointsByProblem.get(pId) || [];
  const userCheckpoints = getUserCheckpoints();

  let delta = 0;
  cps.forEach(cp => {
    const was = !!userCheckpoints[cp.id];
    if (completed && !was) {
      userCheckpoints[cp.id] = true;
      delta++;
    } else if (!completed && was) {
      delete userCheckpoints[cp.id];
      delta--;
    }
  });

  saveUserCheckpoints(userCheckpoints);
  if (delta !== 0) {
    recordActivityDelta(delta);
  }

  const state = getProblemState(pId, userCheckpoints);
  const overview = fetchOverviewLocal();

  return {
    success: true,
    problem_id: pId,
    completed,
    mastery_score: state.score,
    status: state.status,
    overview
  };
}

/**
 * 保存笔记
 */
export function updateProblemNotesLocal(problemId, notes) {
  const userNotes = getUserNotes();
  userNotes[Number(problemId)] = notes;
  saveUserNotes(userNotes);
  return { success: true };
}

/**
 * 获取用户做题活跃热力图历史
 */
export function fetchActivityHistoryLocal() {
  const activity = getUserActivity();
  const userCheckpoints = getUserCheckpoints();
  const totalCompleted = Object.keys(userCheckpoints).length;

  // 如果从未记录过活动，但已有做完的检查点，则默认归属到今天
  if (Object.keys(activity).length === 0 && totalCompleted > 0) {
    const today = getTodayStr();
    activity[today] = totalCompleted;
    saveUserActivity(activity);
  }

  return activity;
}

/**
 * 导出全部做题进度与手记为备份数据
 */
export function exportProgressDataLocal() {
  const userCheckpoints = getUserCheckpoints();
  const userNotes = getUserNotes();
  const userActivity = getUserActivity();
  const overview = fetchOverviewLocal();

  return {
    exported_at: new Date().toISOString(),
    version: '1.0.0',
    storage_type: 'local_storage',
    overview,
    user_checkpoints: userCheckpoints,
    user_notes: userNotes,
    user_activity: userActivity
  };
}

/**
 * 导入历史备份数据
 */
export function importProgressDataLocal(data) {
  if (!data || typeof data !== 'object') {
    throw new Error('无效的备份文件内容');
  }
  if (data.user_checkpoints) {
    saveUserCheckpoints(data.user_checkpoints);
  }
  if (data.user_notes) {
    saveUserNotes(data.user_notes);
  }
  if (data.user_activity) {
    saveUserActivity(data.user_activity);
  }
  return fetchOverviewLocal();
}
