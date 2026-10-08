import * as local from './localAdapter';

const API_BASE = '/api';
let backendAvailable = null; // null: 探测中, true: 后端在线, false: 纯本地模式

/**
 * 自动探测后端 FastAPI 服务是否可达
 */
async function checkBackend() {
  if (backendAvailable !== null) return backendAvailable;
  try {
    const res = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(1200) });
    backendAvailable = res.ok;
  } catch (e) {
    backendAvailable = false;
  }
  return backendAvailable;
}

export async function fetchOverview() {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/overview`);
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.fetchOverviewLocal();
}

export async function fetchProblems({ day, category, difficulty, status, search } = {}) {
  if (await checkBackend()) {
    try {
      const query = new URLSearchParams();
      if (day !== undefined && day !== null && day !== '') query.append('day', day);
      if (category) query.append('category', category);
      if (difficulty) query.append('difficulty', difficulty);
      if (status) query.append('status', status);
      if (search) query.append('search', search);

      const res = await fetch(`${API_BASE}/problems?${query.toString()}`);
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.fetchProblemsLocal({ day, category, difficulty, status, search });
}

export async function fetchProblemDetail(problemId) {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/problems/${problemId}`);
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.fetchProblemDetailLocal(problemId);
}

export async function toggleCheckpoint(checkpointId) {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/checkpoints/${checkpointId}/toggle`, {
        method: 'POST'
      });
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.toggleCheckpointLocal(checkpointId);
}

export async function batchToggleCheckpoints(problemId, completed) {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/problems/${problemId}/batch-toggle`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed })
      });
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.batchToggleCheckpointsLocal(problemId, completed);
}

export async function updateProblemNotes(problemId, notes) {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/problems/${problemId}/notes`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ notes })
      });
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.updateProblemNotesLocal(problemId, notes);
}

export async function exportProgressData() {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/export`);
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.exportProgressDataLocal();
}

export async function fetchActivityHistory() {
  if (await checkBackend()) {
    try {
      const res = await fetch(`${API_BASE}/activity`);
      if (res.ok) return await res.json();
    } catch (e) {
      backendAvailable = false;
    }
  }
  return local.fetchActivityHistoryLocal();
}

export async function importProgressData(data) {
  return local.importProgressDataLocal(data);
}

