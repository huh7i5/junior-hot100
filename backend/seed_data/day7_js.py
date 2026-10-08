"""Day 7 JavaScript Solutions with Junior-level explanations, JS helpers, and code-aligned checkpoints."""

DAY_7_JS_DATA = {
    62: {
        "title_cn": "不同路径",
        "title_en": "Unique Paths",
        "slug": "unique-paths",
        "difficulty": "Medium",
        "description": """一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

提示：
- 1 <= m, n <= 100
- 题目数据保证答案小于等于 2 * 10^9""",
        "plain_explanation": "【大白话拆解·网格加法与一维滚动压缩】\n想象一个小机器人在 m 行 n 列的方格棋盘上，从左上角 (0, 0) 出发去右下角寻宝。因为题目规定小机器人“只能往右走”或者“往下走”，绝不能回头，所以它到达任意一个格子 (i, j) 的途径必定只有两条：\n1. 从它头顶正上方的格子 (i-1, j) 往下迈一步到达；\n2. 从它左手边的格子 (i, j-1) 往右迈一步到达。\n这就是初中数学里的加法原理：到达当前格子的总走法 = 到达上方格子的走法 + 到达左方格子的走法（即 dp[i][j] = dp[i-1][j] + dp[i][j-1]）。\n如果开辟一个 m x n 的二维大表格，空间复杂度是 O(m * n)。但仔细观察，我们在推导第 i 行的某一格时，其实只需要两样东西：刚刚算好的“同一行左边格子的新走法”，以及上一行同一列的“老走法”。\n因此我们可以用一个长度为 n 的一维数组 dp 进行滚动覆盖：\n首先初始化 dp 数组全为 1（因为第一行只能一路向右滑行，到达每个格子都只有 1 种路径）。\n然后逐行向下推导，在每一行中让列 j 从 1 遍历到 n - 1，执行 `dp[j] += dp[j - 1]`。\n这里的 `dp[j]` 恰好存着上一行的值（上方来路），而 `dp[j - 1]` 是刚更新完的本行值（左侧来路），两者相加直接原地覆盖！遍历完 m - 1 行后，终点 `dp[n - 1]` 就是全局总路径数，空间复杂度被极致压缩到 O(n)！",
        "js_helpers": [
            {
                "name": "new Array(n).fill(1)",
                "what_it_does": "快速创建一个长度为 n 且所有元素初始值全为 1 的一维数组。",
                "junior_tip": "用于初始化网格第 0 行的状态：因为最上面一行只能一直向右走，走到任何位置都只有 1 种走法。"
            },
            {
                "name": "dp[j] += dp[j - 1] (一维滚动累加)",
                "what_it_does": "原地累加：将左边格子的最新路径数 dp[j-1] 累加到原本暂存上方格子路径数的 dp[j] 中。",
                "junior_tip": "无需开辟 m * n 二维矩阵，用单行数组原地复用旧状态，把空间复杂度从 O(M*N) 降维到 O(N)。"
            },
            {
                "name": "双层 for 循环下标边界 (i = 1, j = 1)",
                "what_it_does": "从第 1 行第 1 列开始推进动态规划转移。",
                "junior_tip": "第 0 行已由 fill(1) 预填充，第 0 列因为永远只能一路向下所以走法始终为 1（保持 dp[0] = 1 不变），跳过它们能免去所有繁琐的边界 if 判断。"
            }
        ],
        "code_js": '''/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    // 空间压缩：只用一个长度为 n 的一维数组记录到达当前行各列的路径数
    // 第 0 行所有位置都只有 1 种走法（一路向右不回头），全部初始化为 1
    const dp = new Array(n).fill(1);

    // 外层循环：从第 1 行逐行推演至第 m - 1 行
    for (let i = 1; i < m; i++) {
        // 内层循环：从第 1 列推进至第 n - 1 列（第 0 列一路向下始终为 1，无需更新）
        for (let j = 1; j < n; j++) {
            // 当前格路径数 = 上方格子路径数（原 dp[j]）+ 左方格子路径数（新 dp[j-1]）
            dp[j] += dp[j - 1];
        }
    }

    // 最终右下角终点的累计路径数
    return dp[n - 1];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：一维滚动数组构建与 fill(1) 初始化首行", "detail": "细扣：第一行只能向右单向滑行路径数为 1，将空间开销直接从 O(M*N) 压缩至 O(N)。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：外层循环逐行向下遍历 i 从 1 到 m - 1", "detail": "细扣：逐行向下推演，每一行状态依赖上一行的计算沉淀。", "weight": 15},
            {"dimension": "step3", "title": "代码第 3 步：内层循环列从 1 到 n - 1 执行 dp[j] += dp[j - 1]", "detail": "细扣：加法原理在原地生效，原 dp[j] 代表上方来路，新 dp[j-1] 代表左方来路。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：第 0 列天然保持为 1 的边界保护机制", "detail": "细扣：最左侧一列只能一路垂直向下，无左侧来路，跳过 j=0 省去分支判断。", "weight": 15},
            {"dimension": "step5", "title": "代码第 5 步：返回右下角终点 dp[n - 1] 达成最优状态收敛", "detail": "细扣：循环结束后 dp[n-1] 汇聚所有合法路线，时间 O(M*N)，空间 O(N)。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：数学组合数公式 C(m+n-2, m-1) 对齐口述", "detail": "细扣：口述机器人总共需要走 m+n-2 步，其中向下走 m-1 步，也可用组合公式 O(M) 解答。", "weight": 15}
        ]
    },
    64: {
        "title_cn": "最小路径和",
        "title_en": "Minimum Path Sum",
        "slug": "minimum-path-sum",
        "difficulty": "Medium",
        "description": """给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1 -> 3 -> 1 -> 1 -> 1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

提示：
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200""",
        "plain_explanation": "【大白话拆解·原地记账与局部择优】\n想象你在一个收费格子的迷宫里，从左上角出发去右下角，踩到每个格子都要支付上面的过路费，目标是把总过路费压到最低。因为规定每次只能向右走或向下走，所以到达任何一个内部格子 (i, j)，你只有两条可行的来路：\n1. 从正上方的格子 (i-1, j) 走下来；\n2. 从正左方的格子 (i, j-1) 走过来。\n作为一个理性人，你显然会对比这两个来路之前累计的花费，挑便宜的那条走！\n因此核心转移公式就是：当前格子的累计最小花费 = 当前格子本身的过路费 + Math.min(上方格子的最小花费, 左方格子的最小花费)。\n最优雅的实现是“原地记账法”：我们可以直接在输入的原矩阵 grid 上进行累加修改，不需要额外申请任何内存（辅助空间复杂度严格达到 O(1)）！\n具体三步走：\n1. 初始化第 0 行：最顶上一行由于头顶没有格子，只能一路向右累加（grid[0][j] += grid[0][j-1]）；\n2. 初始化第 0 列：最左侧一列由于左边没有格子，只能一路向下累加（grid[i][0] += grid[i-1][0]）；\n3. 内部格子双重遍历：对 1 <= i < m 和 1 <= j < n，每个格子累加上 Math.min(上方, 左方)；\n遍历完成后，右下角的 grid[m-1][n-1] 记录的就是全局最小路径和！",
        "js_helpers": [
            {
                "name": "Math.min(grid[i - 1][j], grid[i][j - 1])",
                "what_it_does": "返回上方格子和左方格子两者中累计花费较小的值。",
                "junior_tip": "动态规划局部最优择优的核心，确保走到当前格子时选取的来路成本最低。"
            },
            {
                "name": "原地修改二维矩阵 (In-place Grid Update)",
                "what_it_does": "直接在入参 grid 上累加中间状态，复用传入的二维数据结构。",
                "junior_tip": "将额外空间复杂度直接优化至 O(1)。若面试官要求不可修改原入参，则开辟一个长度为 n 的一维数组滚动记录即可。"
            },
            {
                "name": "前缀和单向累加 (grid[0][j] += grid[0][j - 1])",
                "what_it_does": "对首行首列边界进行一维前缀和预处理。",
                "junior_tip": "将边界与内部双层循环解耦，避免在双层嵌套中写复杂的 if (i === 0) 或 if (j === 0) 分支判断。"
            }
        ],
        "code_js": '''/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;

    // 1. 初始化第 0 行前缀和（只能一路向右走）
    for (let j = 1; j < n; j++) {
        grid[0][j] += grid[0][j - 1];
    }

    // 2. 初始化第 0 列前缀和（只能一路向下走）
    for (let i = 1; i < m; i++) {
        grid[i][0] += grid[i - 1][0];
    }

    // 3. 内部格子状态转移：从上方与左方择优选取较小路径并累加
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
        }
    }

    // 4. 右下角终点即为全局最小路径总和
    return grid[m - 1][n - 1];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：获取网格维度 m 与 n 建立矩阵视野", "detail": "细扣：确认网格大小，为后续前缀累加和内部遍历提供边界基准。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：第 0 行单向向右前缀和累加初始化", "detail": "细扣：上边缘格子只能从左侧进入，grid[0][j] += grid[0][j-1] 单向累加。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：第 0 列单向向下前缀和累加初始化", "detail": "细扣：左边缘格子只能从上方进入，grid[i][0] += grid[i-1][0] 垂直累加。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：双重循环内部格子累加 Math.min(上方, 左方)", "detail": "细扣：对比两条可能来路挑花销更小者，局部最优推进为全局最优。", "weight": 15},
            {"dimension": "step5", "title": "代码第 5 步：返回右下角 grid[m-1][n-1] 与 O(1) 空间特性", "detail": "细扣：原地修改原矩阵，不占用任何额外堆内存，时间 O(M*N)，空间 O(1)。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：防入参污染之滚动数组替代方案口述", "detail": "细扣：口述若面试官禁止污染原数组，可用一维数组 dp = new Array(n) 滚动实现空间 O(N)。", "weight": 15}
        ]
    },
    5: {
        "title_cn": "最长回文子串",
        "title_en": "Longest Palindromic Substring",
        "slug": "longest-palindromic-substring",
        "difficulty": "Medium",
        "description": """给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

提示：
- 1 <= s.length <= 1000
- s 仅由数字和英文字母组成""",
        "plain_explanation": "【大白话拆解·中心双向扩散法】\n回文串是指正着读和反着读完全一模一样的字符串（比如 'level', 'noon'）。回文串最显著的几何特征就是“关于中心严格对称”！\n虽然这题可以用动态规划填网格，但“中心双向扩散法”在空间上更加无敌——辅助空间只需要 O(1)，而且逻辑极其符合直觉！\n想象我们在字符串中选定一个中心点，左右各派出一名侦察兵（指针 left 和 right）。只要两名侦察兵看到的字符完全相同（s[left] === s[right]），就说明回文可以继续往两边撑大（left--, right++）；一旦发现两边字符不一样或者撞到了字符串边界，就停下来！\n注意：中心对称有两种情况：\n1. 奇数长度中心：以单个字符为中心向两边扩散（如 \"aba\"，以字符 'b' 为中心，初始 left = i, right = i）；\n2. 偶数长度中心：以两字符之间的缝隙为中心向两边扩散（如 \"abba\"，以两个 'b' 为中心，初始 left = i, right = i + 1）。\n因为一个长度为 n 的字符串，一共有 2n - 1 个可能的中心点（n 个单字符 + n-1 个字符间隙），我们只要一层 for 循环遍历每个位置 i，分别尝试奇数扩散和偶数扩散。\n扩散结束时，两指针都已经往外多走了一步，真实回文长度是 `right - left - 1`，真实起点是 `left + 1`。\n我们全局只维护 `start` 和 `maxLen`，遍历完全部中心后，最后调用一次 `s.slice(start, start + maxLen)` 截取输出，比反复创建临时字符串高效百倍！",
        "js_helpers": [
            {
                "name": "s.slice(start, start + maxLen)",
                "what_it_does": "从原始字符串中截取指定起始位置与长度的最长回文子串。",
                "junior_tip": "只在算法全部运行结束后做一次切片截取，避免在循环体内产生大量中间临时字符串造成的垃圾回收开销。"
            },
            {
                "name": "辅助闭包函数 expand(left, right)",
                "what_it_does": "接收左右中心起点，向两翼双向扩散并更新全局最优区间。",
                "junior_tip": "一次封装同时供给奇数扩散 expand(i, i) 和偶数扩散 expand(i, i + 1) 调用，逻辑高度复用。"
            },
            {
                "name": "回文长度公式 right - left - 1",
                "what_it_does": "双指针停止扩展后计算内部合法回文串的有效长度。",
                "junior_tip": "while 退出时 left 和 right 均越过了合法边界，有效区间是 [left + 1, right - 1]，长度为 (right - 1) - (left + 1) + 1 = right - left - 1。"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    // 边界特判：长度小于 2 的字符串天然是回文，直接早退
    if (!s || s.length < 2) return s;

    let start = 0;   // 最长回文子串在原字符串中的起始索引
    let maxLen = 1;  // 最长回文子串的最大长度（至少为 1）

    // 辅助函数：以 left 和 right 为对称中心向两翼双指针扩散
    const expand = (left, right) => {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        // 循环终止时两指针均越界多走了一步，有效回文长度为 right - left - 1
        const len = right - left - 1;
        if (len > maxLen) {
            maxLen = len;
            start = left + 1; // 真实回文子串的起始索引为 left + 1
        }
    };

    // 遍历每一个可能的对称中心（共有 2n - 1 个中心）
    for (let i = 0; i < s.length; i++) {
        expand(i, i);     // 奇数长度中心扩散（如 "aba"）
        expand(i, i + 1); // 偶数长度中心扩散（如 "abba"）
    }

    // 根据最终记录的起点与最大长度一次性切片返回
    return s.slice(start, start + maxLen);
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：边界判断 s.length < 2 直接早退返回原串", "detail": "细扣：空串或单字符天然为回文，直接早退省去后续开销。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：构建 expand(left, right) 双向对称扩散核心", "detail": "细扣：while 循环核对 s[left] === s[right]，两翼同步外推扩界。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：越界校准与有效长度 len = right - left - 1 换算", "detail": "细扣：退出时双指针均超界一步，真实起点为 left + 1，长度为 right - left - 1。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：动态刷新全局最优起点 start 与最长长度 maxLen", "detail": "细扣：len > maxLen 时更新数值，全程零内存字符串拷贝。", "weight": 15},
            {"dimension": "step5", "title": "代码第 5 步：主循环遍历奇数 (i, i) 与偶数 (i, i+1) 中心", "detail": "细扣：枚举全部 2n - 1 个可能中心点，无死角覆盖所有回文形态。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：末尾 s.slice 单次切片输出与 O(1) 空间优势分析", "detail": "细扣：时间 O(N^2)，辅助空间 O(1)，相较于 O(N^2) 空间的二维 DP 方案极具工程实用价值。", "weight": 15}
        ]
    },
    1143: {
        "title_cn": "最长公共子序列",
        "title_en": "Longest Common Subsequence",
        "slug": "longest-common-subsequence",
        "difficulty": "Medium",
        "description": """给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

提示：
- 1 <= text1.length, text2.length <= 1000
- text1 和 text2 仅由小写英文字符组成""",
        "plain_explanation": "【大白话拆解·双序列网格对角线匹配】\n子串和子序列的最大区别是：子串必须紧紧挨在一起，而子序列不需要连续，只要保持先后相对顺序不乱即可（例如 'ace' 是 'abcde' 的子序列）。\n最长公共子序列（LCS）是多维动态规划的基石题！我们采用“二维网格对角线匹配 DP”：\n定义一个二维表格 `dp[i][j]`，它的大白话含义是：`text1` 的前 i 个字符和 `text2` 的前 j 个字符，能拼出的最长公共子序列长度是多少。\n设想我们正同时拿着放大镜看两个子串的最后一个字符：`text1[i-1]` 和 `text2[j-1]`。\n此时只有两种对决可能：\n1. 尾巴字符匹配成功（text1[i-1] === text2[j-1]）：\n太棒了！既然这两个字符完全相同，那它们一定可以作为公共子序列的新末尾！当前的最高战绩，直接在“各自退回一格的战绩”（即左上方对角线 dp[i-1][j-1]）的基础上加 1！公式：`dp[i][j] = dp[i-1][j-1] + 1`。\n2. 尾巴字符不匹配（text1[i-1] !== text2[j-1]）：\n既然不同，说明这两个末尾字符不可能同时作为公共子序列的新成员。我们面临二选一抉择：要么扔掉 text1 的末尾字符看前 i-1 个（对应正上方 dp[i-1][j]），要么扔掉 text2 的末尾字符看前 j-1 个（对应正左方 dp[i][j-1]）。我们挑战绩更好的那个继承过来：`dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1])`！\n为什么数组开辟 (m+1) x (n+1)？因为下标 0 代表“空字符串”，空字符串与任何字符串的 LCS 显然都是 0。多开一行一列充当天然缓冲区，能让代码彻底摆脱越界处理！",
        "js_helpers": [
            {
                "name": "Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0))",
                "what_it_does": "安全创建大小为 (m + 1) * (n + 1) 的二维独立全零矩阵。",
                "junior_tip": "千万不要用 new Array(m+1).fill(new Array(n+1))，那会导致每一行引用同一个数组对象，修改一行直接污染全表！"
            },
            {
                "name": "Math.max(dp[i - 1][j], dp[i][j - 1])",
                "what_it_does": "在放弃 text1 当前字符或放弃 text2 当前字符两种决策中择优继承更大值。",
                "junior_tip": "双序列匹配不相等时的标准贪心状态转移。"
            },
            {
                "name": "1-based 状态网格与 0-based 字符串索引对齐",
                "what_it_does": "dp[i][j] 代表前 i 和前 j 个字符，而字符串中对应的字符下标是 i - 1 和 j - 1。",
                "junior_tip": "这种 +1 偏移量设计是动态规划避免处理负数下标的经典工业界写法。"
            }
        ],
        "code_js": '''/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const m = text1.length;
    const n = text2.length;

    // 创建 (m + 1) * (n + 1) 二维 DP 矩阵，第 0 行第 0 列代表与空字符串匹配，天然全为 0
    const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

    // 双层循环逐格填表：i 表示 text1 的前 i 个字符，j 表示 text2 的前 j 个字符
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            // 末尾字符匹配成功：对角线（各自退一格的历史最高战绩）+ 1
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // 末尾字符不匹配：从放弃 text1 末尾字符或放弃 text2 末尾字符中择优继承
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // 矩阵右下角即为两完整字符串的最长公共子序列长度
    return dp[m][n];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：Array.from 安全构建 (m+1)*(n+1) 二维全零矩阵", "detail": "细扣：确保每一行具有独立的数组内存引用，防止浅拷贝共享引用 Bug。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：第 0 行第 0 列代表空串前缀的天然零缓冲边界", "detail": "细扣：多开一行一列代表空字符串，自然满足 dp[i][0] = 0 和 dp[0][j] = 0。", "weight": 15},
            {"dimension": "step3", "title": "代码第 3 步：双层循环核对当前字符 text1[i-1] === text2[j-1]", "detail": "细扣：注意 1-based 状态矩阵与 0-based 字符串字符索针对齐。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：字符相同沿对角线 dp[i-1][j-1] + 1 状态转移", "detail": "细扣：尾巴字符握手成功，直接在上一个公共子状态基础上加 1 长度。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：字符不同取上方与左方 Math.max 较大值继承", "detail": "细扣：分别尝试丢弃 text1 或 text2 当前字符，保留历史最优战绩。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：右下角 dp[m][n] 结果收敛与单行滚动优化思路", "detail": "细扣：时间 O(M*N)，空间 O(M*N)；可口述用 pre 变量保存左上角将空间压缩至 O(N)。", "weight": 15}
        ]
    },
    72: {
        "title_cn": "编辑距离",
        "title_en": "Edit Distance",
        "slug": "edit-distance",
        "difficulty": "Hard",
        "description": """给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
- 0 <= word1.length, word2.length <= 500
- word1 和 word2 由小写英文字母组成""",
        "plain_explanation": "【大白话拆解·三路操作几何投影法】\n编辑距离（Levenshtein 距离）是大厂高频面试中的 Hard 级天花板题目，在搜索引擎模糊匹配、拼写纠错和基因比对中广泛应用。\n题目要求：把 word1 变成 word2，只允许“插入”、“删除”、“替换”三种动作，求最少需要几步。\n定义状态 `dp[i][j]` 为把 word1 的前 i 个字符变成 word2 的前 j 个字符所需要的最少操作步数。\n观察当前字符 `word1[i-1]` 与 `word2[j-1]`：\n1. 字符本身就相同（word1[i-1] === word2[j-1]）：\n喜大普奔！这两个末尾字符天然一致，完全不需要任何修改操作，操作步数直接等于各自少看一个字符时的步数，即继承左上方对角线：`dp[i][j] = dp[i-1][j-1]`！\n2. 字符不同（word1[i-1] !== word2[j-1]）：\n我们必须付出 1 次操作代价（+1），此时有三种捷径可以选择：\n- 替换字符：把 word1[i-1] 替换成 word2[j-1]，改完后末尾对齐了，对应对角线 `dp[i-1][j-1] + 1`；\n- 删除字符：把 word1[i-1] 直接删掉，相当于看 word1 前 i-1 个字符怎么变成 word2 前 j 个字符，对应正上方 `dp[i-1][j] + 1`；\n- 插入字符：在 word1 末尾插入一个与 word2[j-1] 相同的字符，相当于看 word1 前 i 个字符怎么变成 word2 前 j-1 个字符，对应正左方 `dp[i][j-1] + 1`。\n我们挑这三条路里代价最小的一个：`Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`！\n边界初始化：\n把 word1 变为空串，只能全靠删，故 `dp[i][0] = i`；\n把空串变成 word2，只能全靠插，故 `dp[0][j] = j`。\n自顶向下填完表格，右下角 `dp[m][n]` 就是最少操作步数！",
        "js_helpers": [
            {
                "name": "Math.min(a, b, c)",
                "what_it_does": "JavaScript 原生支持在 Math.min 中传入任意数量的参数。",
                "junior_tip": "一次性比较删除（上方）、插入（左方）、替换（左上方）三个转移状态并选出最小值，代码极其紧凑。"
            },
            {
                "name": "边界初始化 dp[i][0] = i 与 dp[0][j] = j",
                "what_it_does": "初始化矩阵第 0 列（全删操作）和第 0 行（全插操作）。",
                "junior_tip": "明确空字符串转换的天然基准代价，为后续网格逐步推演奠定坚实底座。"
            },
            {
                "name": "Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0))",
                "what_it_does": "开辟大小为 (m+1) x (n+1) 的独立二维动态规划数组。",
                "junior_tip": "避免由于数组浅拷贝导致的不同行之间相互篡改数据。"
            }
        ],
        "code_js": '''/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const m = word1.length;
    const n = word2.length;

    // 创建 (m + 1) * (n + 1) 二维 DP 状态转移矩阵
    const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

    // 边界初始化：word1 前 i 个字符变为空串，只能连续删除 i 次
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    // 边界初始化：空串变为 word2 前 j 个字符，只能连续插入 j 次
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    // 双重嵌套循环遍历内部网格填表
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (word1[i - 1] === word2[j - 1]) {
                // 字符相同，无需任何额外编辑，直接继承对角线状态
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // 字符不同，在删、插、改三者中取最小值并 + 1
                dp[i][j] = Math.min(
                    dp[i - 1][j],     // 删除操作（来自上方）
                    dp[i][j - 1],     // 插入操作（来自左方）
                    dp[i - 1][j - 1]  // 替换操作（来自左上方对角线）
                ) + 1;
            }
        }
    }

    // 最终全局最少编辑步数
    return dp[m][n];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：创建 (m+1)*(n+1) 二维 DP 矩阵并明确物理含义", "detail": "细扣：dp[i][j] 记录 word1 前 i 个字母变换到 word2 前 j 个字母的最少步数。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：初始化第 0 列 dp[i][0]=i 与第 0 行 dp[0][j]=j 边界", "detail": "细扣：全删与全插的天然代价奠定动态规划推演地基。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：字符相同零成本继承对角线 dp[i-1][j-1]", "detail": "细扣：word1[i-1] === word2[j-1] 时无需操作，对角线直通传递。", "weight": 15},
            {"dimension": "step4", "title": "代码第 4 步：字符不同三路几何映射：上方删、左方插、对角线改", "detail": "细扣：理清三种基本操作与二维网格拓扑方位的对应关系。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：Math.min 三者取极小值 + 1 状态转移落地", "detail": "细扣：局部最优决策保证全局步数最少，结构严谨清晰。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：右下角 dp[m][n] 结果导出与 O(M*N) 复杂度全面评估", "detail": "细扣：时间 O(M*N)，空间 O(M*N)，掌握经典 Hard 题目的核心通用模型。", "weight": 15}
        ]
    },
    136: {
        "title_cn": "只出现一次的数字",
        "title_en": "Single Number",
        "slug": "single-number",
        "difficulty": "Easy",
        "description": """给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度 O(n) 且使用常数额外空间 O(1) 的算法解决此问题。

示例 1 ：
输入：nums = [2,2,1]
输出：1

示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4

示例 3 ：
输入：nums = [1]
输出：1

提示：
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- 除了某个元素只出现一次以外，其余每个元素均出现两次。""",
        "plain_explanation": "【大白话拆解·神奇的异或消消乐】\n如果允许开辟哈希表，这道题大家都会；但题目给出了死命令：时间必须 O(N)，而且额外空间必须严格 O(1)！这直接封死了哈希表和数组排序的退路。\n唯一的破局神兵是位运算中的——按位异或运算符 `^`！\n异或在二进制位上的规则极其简单：“相同为 0，不同为 1”。由于这个物理特性，它具备三大神仙法则：\n1. 归零律（自反消消乐）：任何数字和自己异或，必定化为 0！即 `a ^ a === 0`；\n2. 恒等律（零是空气）：任何数字和 0 异或，依然等于它自己！即 `a ^ 0 === a`；\n3. 交换律与结合律：一堆数字连续异或，顺序随便调换都不影响最终结果！即 `a ^ b ^ a === (a ^ a) ^ b === 0 ^ b === b`。\n把这三条法则拼在一起，魔术就诞生了：\n我们将结果变量 `res` 初始化为 0，然后从头到尾把数组里的所有数字连续 `^` 起来：\n所有出现过两次的数字，不论它们在数组里隔得多远，在异或运算的大锅里相遇时，通通都会被触发消消乐变为 0！\n而那个只出现了一次的数字，最后跟一大堆 0 进行异或（0 ^ x === x），最终完整无损地存活并留在了 `res` 中！\n一行核心运算，无需任何额外内存开销，空间 O(1)，时间 O(N)，秒杀！",
        "js_helpers": [
            {
                "name": "按位异或运算符 (^)",
                "what_it_does": "二进制位操作符，相同位得 0，相异位得 1。",
                "junior_tip": "具有 a ^ a = 0 以及 a ^ 0 = a 的绝妙自反性，是单身数字秒杀神器。"
            },
            {
                "name": "复合赋值运算符 res ^= num",
                "what_it_does": "将变量 res 与当前数字 num 进行异或后原地赋回给 res。",
                "junior_tip": "等价于 res = res ^ num，书写精练且执行高效。"
            },
            {
                "name": "for...of 数组迭代",
                "what_it_does": "简洁直观地遍历数组中的每一个元素值。",
                "junior_tip": "不需要维护传统的索引变量 i，代码可读性极佳。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    // 初始基底设为 0：因为 0 ^ x === x，不会对任何后续数字产生副作用
    let res = 0;

    // 线性遍历数组中的每一个数字进行异或消消乐
    for (const num of nums) {
        // 利用成对数字异或为 0 的特性做两两抵消
        res ^= num;
    }

    // 遍历结束，成双成对的数字全部化为 0，唯一留存的就是落单数字
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：初始化累积结果变量 res = 0", "detail": "细扣：0 ^ x = x，以 0 为初始基底不会污染任何后续位运算结果。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：for...of 单趟线性遍历数组中每个数字 num", "detail": "细扣：时间复杂度严格控制为 O(N)，仅需单次正向扫描。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：执行 res ^= num 成对数字异或抵消为 0", "detail": "细扣：利用 a ^ a = 0，成对出现的数值无论先后在二进制位上全抵消归零。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：交换律与结合律确保乱序配对完整消解", "detail": "细扣：异或运算顺序无关紧要，消除效果等价于相邻成对消除。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：返回唯一存留的落单数字 res 并达成 O(1) 空间", "detail": "细扣：不需要额外哈希表与排序，空间复杂度达到极致的常数级别 O(1)。", "weight": 20}
        ]
    },
    169: {
        "title_cn": "多数元素",
        "title_en": "Majority Element",
        "slug": "majority-element",
        "difficulty": "Easy",
        "description": """给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2

提示：
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。""",
        "plain_explanation": "【大白话拆解·摩尔投票一换一对拼消耗】\n什么叫多数元素？它的出现次数严格大于总长度的一半（> ⌊n / 2⌋）！\n常规解法可以用哈希表统计频次（需要 O(N) 空间），或者排序后取中位数（需要 O(N log N) 时间）。但本题进阶要求：时间 O(N)，空间严格 O(1)！\n为此，罗伯特·博耶和 J·斯特罗瑟·摩尔提出了名震天下的“摩尔投票算法（Boyer-Moore Voting Algorithm）”！\n大白话比喻：“武林大会一换一同归于尽”！\n想象各个门派在打擂台。因为多数派别的弟子人数严格超过了全场总人数的一半，这就意味着：即使其他所有门派联手组成统一战线，采取极限“一换一”（一个杂牌门派弟子拉着一个多数派弟子同归于尽）的战术，到最后擂台上站着的也必定是多数派的人！\n算法维护两个寄存器变量：\n1. `candidate`：当前守擂的候选擂主；\n2. `count`：该擂主当前的护体兵力值。\n从头到尾遍历数组：\n- 当兵力值 `count === 0` 时，说明上一任擂主的兵力已经被彻底拼光了，此时登台的数字立刻当选为新擂主（`candidate = num`）；\n- 如果登台的数字是同门师兄弟（`num === candidate`），兵力大增，`count++`；\n- 如果登台的数字是敌方门派（`num !== candidate`），那就一换一抵消，兵力削弱，`count--`。\n遍历全场后，由于多数元素享有压倒性的绝对过半优势，最终站在台上的 `candidate` 必定是多数元素！时间 O(N)，空间 O(1)，震撼人心的简洁与精妙！",
        "js_helpers": [
            {
                "name": "三元运算符 count += (num === candidate ? 1 : -1)",
                "what_it_does": "一行代码根据阵营匹配状态递增或递减票数。",
                "junior_tip": "比繁琐的 if-else 嵌套更加优雅，极其贴合投票对拼的物理模型。"
            },
            {
                "name": "count === 0 触发换届选举",
                "what_it_does": "当票数归零时，说明之前遍历的子序列中所有派系已经完全相互抵消，原问题等价于在剩余序列中继续寻找多数元素。",
                "junior_tip": "状态机的自动重启机制，是摩尔投票空间占用仅为 O(1) 的关键所在。"
            },
            {
                "name": "流式计算思想 (Streaming Algorithm)",
                "what_it_does": "数据仅需单趟流过，无需保存任何历史数据即可得出全局统计结论。",
                "junior_tip": "这种思想可直接扩展应用至大数据海量流式日志的主频计算中。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candidate = null; // 当前擂主候选人
    let count = 0;        // 候选人当前净胜票数（兵力值）

    for (const num of nums) {
        // 当兵力耗尽归零时，说明前序子区间已同归于尽，当前数字自立为新擂主
        if (count === 0) {
            candidate = num;
        }

        // 同阵营支持票 +1，异阵营对拼抵消 -1
        count += (num === candidate ? 1 : -1);
    }

    // 题目保证多数元素必然存在（占比 > n/2），最终留存的候选人即为答案
    return candidate;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：初始化 candidate = null 与 count = 0 投票状态机", "detail": "细扣：双变量极简寄存器，空间复杂度从一开始就锁定在 O(1)。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：count === 0 兵力耗尽触发换届选举任命名义新擂主", "detail": "细扣：前序子序列完全抵消，新数字接管候选人席位。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：num === candidate 时 count++ 否则 count-- 对拼消耗", "detail": "细扣：一换一对拼机制，同盟加兵敌对减兵，核心物理逻辑落地。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：数学证明过半优势必然抵消全场并存活到最后", "detail": "细扣：多数派占比 > 1/2，异己总数严格小于多数派，无法彻底抹杀多数元素。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：遍历结束直接返回 winner，时间 O(N) 空间 O(1) 验证", "detail": "细扣：题目保证多数元素必存在，免去二次校验扫描，耗时 O(N)。", "weight": 20}
        ]
    },
    75: {
        "title_cn": "颜色分类",
        "title_en": "Sort Colors",
        "slug": "sort-colors",
        "difficulty": "Medium",
        "description": """给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

提示：
- n == nums.length
- 1 <= n <= 300
- nums[i] 为 0、1 或 2

进阶：
你能想出一个仅使用常数空间的一趟扫描算法吗？""",
        "plain_explanation": "【大白话拆解·荷兰国旗三路巡逻切分】\n数组里只有 0（红）、1（白）、2（蓝）三种数字，要求不使用内置 sort，在原数组上把它们排成 0, 1, 2 的顺序，且只扫描一趟，额外空间 O(1)！\n这是计算机先驱 Dijkstra（迪杰斯特拉）提出的经典“荷兰国旗问题（Dutch National Flag problem）”！\n大白话比喻：“数组操场划地盘”：\n我们在数组上划分出四个明确的动态领地：\n- `[0, p0)` 存放归位的 0（红色领地）；\n- `[p0, curr)` 存放归位的 1（白色领地）；\n- `[curr, p2]` 尚未受审的未知探查区；\n- `(p2, n-1]` 存放归位的 2（蓝色领地）。\n我们派遣三位指针长官：\n- `p0 = 0`：0 的右边界（下一个 0 应该存放的位置）；\n- `p2 = nums.length - 1`：2 的左边界（下一个 2 应该存放的位置）；\n- `curr = 0`：从左往右一路巡逻查岗的巡检员。\n巡检员 `curr` 审查当前位置 `nums[curr]`：\n1. 如果遇到 0：抓到红牌！与 `p0` 处的元素对调归位，双方各进一步（`p0++`, `curr++`。因为换到 curr 的元素原本必定是 1，已知合格）；\n2. 如果遇到 1：白牌本来就该在中间，无需任何挪动，巡检员直接前进一步（`curr++`）；\n3. 如果遇到 2：抓到蓝牌！与 `p2` 处的元素对调归位，把 2 送去右侧大本营，`p2--`。\n【全题核心生死防守点】：此时 `curr` 绝对不能自增！因为从 `p2` 换回来的新元素是谁尚未可知（可能是 0、1 或 2），还没被审阅过！巡检员必须原地待命，下一轮循环对换过来的新元素重新定夺！\n当 `curr > p2` 时，整个未知探查区被压缩为 0，原地排序大功告成！",
        "js_helpers": [
            {
                "name": "[nums[a], nums[b]] = [nums[b], nums[a]] (解构赋值原地交换)",
                "what_it_does": "ES6 数组解构语法，一行代码实现两元素原地对调。",
                "junior_tip": "彻底告别传统的 let temp 临时变量，书写极简且降低出错概率。"
            },
            {
                "name": "荷兰国旗三指针区间定义与循环不变量",
                "what_it_does": "严格维护 [0, p0) 为 0、[p0, curr) 为 1、(p2, len-1] 为 2 的分区规则。",
                "junior_tip": "三路划分是快速排序应对海量重复元素（3-way QuickSort）的核心基石。"
            },
            {
                "name": "遇到 2 交换后 curr 原地待命机制",
                "what_it_does": "与 p2 交换后仅 p2--，不执行 curr++。",
                "junior_tip": "最容易手滑写错的 Bug 点！未受审的未知元素不可直接放行，必须停在原地下一轮复查。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let p0 = 0;                  // 0 的右边界（下一个 0 应归位的位置）
    let curr = 0;                // 巡检指针（当前审查的元素位置）
    let p2 = nums.length - 1;    // 2 的左边界（下一个 2 应归位的位置）

    // 只要待审区间 [curr, p2] 依然存在，持续推进巡检
    while (curr <= p2) {
        if (nums[curr] === 0) {
            // 抓到 0：与 p0 处元素交换归位，两指针同步前进
            [nums[curr], nums[p0]] = [nums[p0], nums[curr]];
            p0++;
            curr++;
        } else if (nums[curr] === 2) {
            // 抓到 2：与 p2 处元素交换归位，p2 左移扩大领地
            [nums[curr], nums[p2]] = [nums[p2], nums[curr]];
            p2--;
            // 极其关键：此时 curr 绝不能自增！换回来的新元素尚未受审，下一轮原地复查
        } else {
            // 抓到 1：留在中间白区放行，curr 正常向前推进
            curr++;
        }
    }
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：定义三指针 p0 = 0, curr = 0, p2 = nums.length - 1", "detail": "细扣：建立三路切分区划不变量，[0, p0) 为 0，(p2, n-1] 为 2，中间待审。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：while curr <= p2 循环出口与探测边界设定", "detail": "细扣：包含等于号，确保最后一个处于 p2 边界上的元素同样接受审阅。", "weight": 15},
            {"dimension": "step3", "title": "代码第 3 步：nums[curr] === 0 时与 p0 交换并双指针同步推进", "detail": "细扣：将 0 归位到左侧领地，p0++ 且 curr++（换过来的必为已审阅合格的 1）。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：nums[curr] === 2 时与 p2 交换且 curr 原地待命", "detail": "细扣：换过来的元素未知，curr 不前移是防漏判的核心生命线！", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：nums[curr] === 1 时居中放行 curr++ 穿梭推进", "detail": "细扣：白色元素天然处于中间地带，无需移动直接越过。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：ES6 解构交换、纯单趟扫描与空间 O(1) 终极特性", "detail": "细扣：原地修改无额外数组，时间 O(N)，空间严格 O(1)，满足进阶全部要求。", "weight": 15}
        ]
    },
    31: {
        "title_cn": "下一个排列",
        "title_en": "Next Permutation",
        "slug": "next-permutation",
        "difficulty": "Medium",
        "description": """整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。

给你一个整数数组 nums ，必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

提示：
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100""",
        "plain_explanation": "【大白话拆解·三步换出最小增量】\n什么是下一个排列？把数组里的数字拼在一起看成一个大数，我们要找一个在字典序上“刚好比当前组合大一点点、增幅最小”的下一个数字。如果已经是最大组合了（比如 3, 2, 1），就轮回重置回最小组合（1, 2, 3）。\n怎样才能让变大的幅度“尽可能小”？\n原则一：尽量在靠右边的低位（个位、十位）动手术，高位尽量不动；\n原则二：把一个“较小数”和一个“刚好比它大一点点的较大数”对换；\n原则三：交换之后，把该位置后面的一长串数字降到最小（排成升序）！\n标准三部曲算法：\n第一步【从右往左找转折点 i】：倒序扫描，找到第一个破坏单调递增规律的数字 i（即满足 `nums[i] < nums[i+1]`）。此时 i 后面的一整串数字必定是单调递减的极值形态；\n第二步【从右往左找稍大数 j 并交换】：如果找到了合法的 i（i >= 0），再次从数组最右端倒序扫描，找到第一个严格大于 nums[i] 的数字 nums[j]，将 nums[i] 与 nums[j] 对换！此时字典序已经完成了关键抬升；\n第三步【双指针翻转后缀】：交换之后，i 后面的后缀依然保持着单调递减形态。为了让整体增幅最小，我们需要把递减后缀变成单调递增（最小化）！用双指针 left = i + 1, right = n - 1 头尾对调翻转即可！\n如果第一步连转折点 i 都找不到（即 i 减到了 -1），说明整个数组已经是全降序的最大值（如 3, 2, 1），直接跳过第二步执行第三步把整个数组翻转，就完美回归到了最小升序排列（1, 2, 3）！",
        "js_helpers": [
            {
                "name": "倒序双指针扫描定位转折点",
                "what_it_does": "while (i >= 0 && nums[i] >= nums[i + 1]) i--，寻找从右向左第一个下降拐点。",
                "junior_tip": "定位需要被替换调大的最靠右有效位，确保高位数字保持不变。"
            },
            {
                "name": "[nums[left], nums[right]] = [nums[right], nums[left]] 后缀翻转",
                "what_it_does": "首尾对调双指针逐步向中间收拢。",
                "junior_tip": "后缀原为单调递减，通过 O(N) 双指针翻转直接变为单调递增，无需调用昂贵的 sort()。"
            },
            {
                "name": "原地修改无返回值 (In-place & void)",
                "what_it_does": "直接在入参 nums 上修改元素排布。",
                "junior_tip": "符合题目原地常数级空间要求，避免任何新数组对象的开辟。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    const n = nums.length;
    let i = n - 2;

    // 1. 从右往左寻找第一个破坏升序的转折点 i（即满足 nums[i] < nums[i + 1]）
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // 2. 如果存在合法的转折点（说明不是全降序的最大排列）
    if (i >= 0) {
        let j = n - 1;
        // 从右往左寻找第一个严格大于 nums[i] 的较小数 j
        while (j >= 0 && nums[j] <= nums[i]) {
            j--;
        }
        // 交换 nums[i] 与 nums[j]，以最小幅度提升字典序高位
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // 3. 将 i + 1 之后的单调递减后缀双指针就地翻转为单调递增序列，以最小化后续增幅
    // 若原数组全降序（i === -1），则此处将整个数组直接翻转为最小升序排列
    let left = i + 1;
    let right = n - 1;
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：从右向左倒序寻找首个相邻递减转折点 i", "detail": "细扣：nums[i] < nums[i+1]，锁定需要调大的最靠右有效位，保持高位稳定。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：全降序极大值（i === -1）识别与整串翻转轮回分支", "detail": "细扣：未找到转折点说明已经是字典序最大组合，直接跳过交换阶段。", "weight": 15},
            {"dimension": "step3", "title": "代码第 3 步：从右向左倒序寻找首个严格大于 nums[i] 的数 j", "detail": "细扣：nums[j] > nums[i]，挑选尽可能小的大数做替换，确保增量最小化。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：解构交换 nums[i] 与 nums[j] 保证字典序增幅克制", "detail": "细扣：对调两数后，i 之后的后缀依然保持单调递减性质。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：双指针原地翻转 i+1 后缀将降序置换为最小升序", "detail": "细扣：left=i+1 与 right=n-1 头尾相向对调，将后缀恢复为极小值升序。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：原地反转替代排序之数学证明与 O(1) 空间特性", "detail": "细扣：后缀原本单调递减，直接反转即可递增，无需 O(NlogN) 排序，时间严格 O(N)。", "weight": 15}
        ]
    },
    287: {
        "title_cn": "寻找重复数",
        "title_en": "Find the Duplicate Number",
        "slug": "find-the-duplicate-number",
        "difficulty": "Medium",
        "description": """给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3 :
输入：nums = [3,3,3,3,3]
输出：3

提示：
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次

进阶：
- 如何证明 nums 中至少存在一个重复的数字？
- 你可以设计一个线性时间复杂度 O(n) 的解决方案吗？""",
        "plain_explanation": "【大白话拆解·数组隐式链表化与龟兔赛跑找环入口】\n数组长度为 n + 1，里面的数字范围都在 1 到 n 之间。根据鸽巢原理（把 n+1 只鸽子放进 n 个笼子，必定至少有一个笼子挤了两只以上的鸽子），重复数字必然存在。\n但本题有着令人发指的严苛限制：\n1. 不能修改原数组（不能原样排序，不能打负号标记）；\n2. 只能使用 O(1) 额外空间（不能开 Set/Map，不能开布尔数组）；\n3. 时间复杂度必须是 O(N)！\n破局的旷世奇思是：“把数组看成带环链表”！\n我们将数组的“下标”看成是链表节点的编号，把数组里存的“数值 nums[i]”看成是这个节点指向下一个节点的指针 `next`！\n因为数字都在 1 到 n 之间，所以下标 0 绝对不会被任何数字指向（没有任何数字是 0），下标 0 就是链表天然的入口虚拟起点！\n当数组中存在重复的数字时（例如数字 2 在下标 1 和下标 4 都出现过），就意味着节点 1 和节点 4 都伸出箭头指向了同一个节点 2——这在链表里就是经典的“多入度闭环”！\n而那个被重复指向的节点，正是这个有向环的“入口节点”！\n本题直接无缝转化为 LeetCode 142 题（环形链表 II）！\n利用 Floyd 判圈算法（龟兔赛跑）：\n阶段一【环内追及相遇】：慢指针乌龟一次走一步（`slow = nums[slow]`），快指针兔子一次走两步（`fast = nums[nums[fast]]`）。因为有环存在，兔子一定会在环里追上乌龟相遇（`slow === fast`）；\n阶段二【步调一致寻访环入口】：乌龟和兔子相遇后，派出一名新侦察兵 `p` 从起点 0 出发，慢指针 `slow` 留在相遇点。然后两人步调一致，每次都各走一步（`p = nums[p], slow = nums[slow]`）。根据经典的环形链表几何数学推导，他们再次碰头的那个点，必定就是环的入口——也就是我们要找的那个重复数字！",
        "js_helpers": [
            {
                "name": "数组下标隐式指针跳转 (slow = nums[slow])",
                "what_it_does": "将数组值作为下一个访问的下标，模拟链表中的 node = node.next。",
                "junior_tip": "无需真正创建任何 ListNode 对象，利用原生数组下标完成链表图谱的有向遍历。"
            },
            {
                "name": "快指针两倍速前进 (fast = nums[nums[fast]])",
                "what_it_does": "连续做两次下标嵌套跳转，模拟链表中的 fast = fast.next.next。",
                "junior_tip": "快慢指针步长差为 1，在环中必定在有限步数内撞车相遇。"
            },
            {
                "name": "Floyd 判圈算法阶段二 (p = nums[p], slow = nums[slow])",
                "what_it_does": "重置指针回起点 0，与慢指针同速单步前进。",
                "junior_tip": "数学定理：起点到环入口距离 a 等于相遇点到环入口距离 (k-1)L + (L-b)，两指针同速前进必在入口相撞。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    // 阶段一：Floyd 判圈算法，快慢双指针寻找环内相遇点
    // 将下标 0 视为链表起点，nums[i] 视为 node.next 指针
    let slow = nums[0];
    let fast = nums[nums[0]];

    // 慢指针每次走 1 步，快指针每次走 2 步，直至环内相遇
    while (slow !== fast) {
        slow = nums[slow];           // slow = slow.next
        fast = nums[nums[fast]];     // fast = fast.next.next
    }

    // 阶段二：重置一个指针 p 回起点 0，与相遇点 slow 同速（每次 1 步）前进寻找环入口
    let p = 0;
    while (p !== slow) {
        p = nums[p];
        slow = nums[slow];
    }

    // 再次相遇点即为环入口，也就是重复出现的整数
    return p;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：鸽巢原理与数组数值到链表指针 next 隐式映射构建", "detail": "细扣：下标为节点索引，nums[i] 为 next 指针，重复值对应入度 >= 2 的环入口。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：下标 0 作为链表虚拟头节点（无入度）的安全性分析", "detail": "细扣：数值在 1 到 n 之间，0 不在环中，从 0 出发保证安全单向入环。", "weight": 15},
            {"dimension": "step3", "title": "代码第 3 步：阶段一 fast 走两步 slow 走一步在环内追击相遇", "detail": "细扣：while (slow !== fast)，两倍速在有限环长步数内必定完成超车相遇。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：阶段二重置 p=0 与 slow 同速单步前进探寻环入口", "detail": "细扣：相遇后将 p 置 0，两指针每次前进一步，相遇处即为环入口。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：数学定理证明相遇点与起点到环入口距离严格相等", "detail": "细扣：2(a + b) = a + kL + b => a = kL - b，两指针走 a 步必在环入口碰头。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：严格满足不修改原数组、O(1) 空间与 O(N) 时间约束", "detail": "细扣：不破坏原数组，零额外内存堆栈开销，完美通过全部苛刻限制条件。", "weight": 15}
        ]
    }
}
