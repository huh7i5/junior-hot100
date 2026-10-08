# LeetCode Hot 100 原子化突破体系 (Hot100 Mastery)

> 将 100 道力扣核心题目细化为 **400 个原子检查点**，通过**本地 SQLite 数据库持久化**与**高颜值交互式 Web 看板**，实现从“刷过”到“真正掌握”的全量化闭环系统。

---

## 🌟 项目亮点

1. **原子化微检查点（Micro-Checkpoints）**：
   - 每道题拒绝简单的“已做/未做”二元标记，拆分为 4 个标准维度（各占 25% 权重）：
     - 🎯 **破题眼 (Pattern Recognition)**：模式识别与算法分类。
     - 🛡️ **边界防守 (Corner Cases)**：极端用例防守与踩坑预警。
     - ✍️ **最优实现 (Optimal Bug-free Code)**：最优复杂度标准实现代码。
     - ⏱️ **时空演练 (Complexity & Tradeoff)**：复杂度推演与面试口述问答。
2. **7天专题冲刺时间线 (7-Day Sprint Roadmap)**：
   - **Day 1**：哈希表、双指针与滑动窗口（17题）
   - **Day 2**：矩阵与链表全解（18题）
   - **Day 3**：二叉树与图论搜索遍历（19题）
   - **Day 4**：回溯搜索与二分查找（14题）
   - **Day 5**：栈/堆与贪心思维（12题）
   - **Day 6**：动态规划一维经典核心（10题）
   - **Day 7**：多维动态规划与技巧收官（10题）
3. **本地持久化与数据可导出**：
   - 基于轻量可靠的 **SQLite 数据库 (`backend/hot100.db`)**，所有打勾状态、分数和个人手记永不丢失。
   - 提供一键导出 JSON 备份功能，可随时在多台设备间迁移或作为 GitHub 仓库展示。
4. **单进程全栈交付**：
   - 前端 React 静态资产构建后由 FastAPI 统一托管，双击 `start.bat` 即可一键拉起服务并在浏览器打开，无需开启多个终端。

---

## 🚀 极速启动指南

### 方式一：双击一键启动（推荐）
在项目根目录下，直接双击运行：
```bash
start.bat
```
系统将自动启动后端服务并弹出浏览器访问：`http://127.0.0.1:8765`。

### 方式二：命令行手动启动
```bash
# 进入后端目录
cd backend

# 运行服务器 (端口 8765)
python server.py
```
在浏览器打开：[http://127.0.0.1:8765](http://127.0.0.1:8765)

---

## 🛠️ 前端二次开发与构建

若需要自定义修改前端界面或扩展组件：

```bash
cd frontend

# 安装依赖
npm install

# 启动 Vite 热更新开发服务器 (自带 /api 代理)
npm run dev
# 浏览器访问 http://localhost:5173

# 生产环境编译构建
npm run build
```
构建产物会自动输出至 `frontend/dist`，FastAPI 后端会自动同步加载最新的编译页面。

---

## 📂 项目结构

```
hot100-mastery/
├── backend/
│   ├── hot100.db                 # SQLite 本地数据库 (包含100题与400检查点)
│   ├── database.py               # 数据库初始化、数据统计与状态重算引擎
│   ├── seeder.py                 # 全量题库、4维检查点与最优解灌库脚本
│   ├── server.py                 # FastAPI RESTful API 服务 (兼托管前端 SPA)
│   ├── test_api.py               # 后端自动化接口测试套件
│   └── seed_data/                # Day 1 到 Day 7 的结构化题解与检查点源数据
│       ├── day1.py ... day7.py
├── frontend/
│   ├── src/
│   │   ├── components/           # UI 交互组件 (Header, SprintNav, Filters, ProblemCard, DetailDrawer)
│   │   ├── services/api.js       # 后端 API 请求服务
│   │   ├── App.jsx               # 主应用核心状态管理
│   │   └── index.css             # Tailwind CSS 与暗色系毛玻璃样式
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
├── start.bat                     # Windows 一键启动脚本
└── README.md                     # 项目技术文档
```

---

## 🌐 上线外网部署指南

1. **纯静态部署 (Vercel / GitHub Pages)**：
   - 前端已打包至 `frontend/dist`，可直接将其作为静态站点托管。
2. **全栈独立部署 (Railway / Render / 个人轻量云服务器)**：
   - 直接把本仓库推送到 GitHub，在平台中执行 `python backend/server.py`，配置端口环境变量即可。
