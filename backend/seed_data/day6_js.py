"""Day 6 JavaScript Solutions with Junior-level explanations, JS helpers, code-aligned checkpoints, and complete problem descriptions."""

DAY_6_JS_DATA = {
    70: {
        "title_cn": "爬楼梯",
        "title_en": "Climbing Stairs",
        "slug": "climbing-stairs",
        "difficulty": "Easy",
        "description": """假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

提示：
- 1 <= n <= 45""",
        "plain_explanation": "爬楼梯是动态规划入门的第一道神题！想象你正站在第 n 级台阶上，回头看一眼，你最后这一步是怎么迈上来的？因为规则规定每次只能迈 1 步或 2 步，所以到达第 n 级台阶的唯一可能只有两种：要么从第 n-1 级迈 1 步上来，要么从第 n-2 级跨 2 步上来！绝不可能有第三种跨法。因此，到达第 n 级的总方案数，就完完全全等于到达第 n-1 级的方案数加上到达第 n-2 级的方案数：dp[n] = dp[n-1] + dp[n-2]。这不就是大名鼎鼎的斐波那契数列嘛！初学者常犯的毛病是直接开一个长度为 n+1 的大数组存所有中间结果，或者用傻递归导致指数级超时。其实算第 n 阶时，我们只需要知道紧挨着的“前一阶”和“前前阶”就足够了。用两个变量 a（前前阶）和 b（前一阶），像滚雪球一样交替往前滚动更新，利用 ES6 解构赋值 [a, b] = [b, a + b]，一行搞定状态滚动，空间复杂度达到极致的 O(1)！",
        "js_helpers": [
            {
                "name": "解构赋值 [a, b] = [b, a + b]",
                "what_it_does": "ES6 解构特性，一行实现两个变量同时交替更新。",
                "junior_tip": "完全不需要声明中间临时变量 temp，代码极其清爽且能防止赋值顺序写反的手滑 Bug！"
            },
            {
                "name": "if (n <= 2) return n",
                "what_it_does": "边界条件极速特判，1 阶 1 种走法，2 阶 2 种走法。",
                "junior_tip": "先处理最小边界情况，不仅避免了无效循环，还让主循环从第 3 阶起跑更清晰。"
            },
            {
                "name": "滚动状态压缩模式",
                "what_it_does": "用有限的常数个变量代替线性数组，空间复杂度从 O(N) 压缩到 O(1)。",
                "junior_tip": "动态规划只要当前状态只依赖前有限项，都可以用滚动变量压榨空间，面试必考加分项！"
            }
        ],
        "code_js": '''/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // 边界特判：1 阶有 1 种走法，2 阶有 2 种走法
    if (n <= 2) return n;

    // a 代表到达第 1 阶的走法数，b 代表到达第 2 阶的走法数
    let a = 1, b = 2;

    // 从第 3 阶一直滚动累加推演到第 n 阶
    for (let i = 3; i <= n; i++) {
        // 利用 ES6 解构赋值，实现双变量交替滚动推进
        [a, b] = [b, a + b];
    }

    return b;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：n <= 2 基础台阶特判返回", "detail": "细扣：1 阶 1 种，2 阶 2 种，小于等于 2 直接返回 n，规避无效循环。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：初始化滚动双指针 a = 1, b = 2", "detail": "细扣：分别代表到达第 1 阶和第 2 阶的走法总数，确立起跑基石。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：for 循环区间从 3 遍历到 n", "detail": "细扣：从第 3 阶开始逐级递推，每一次循环计算出新台阶方案数。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：解构赋值 [a, b] = [b, a + b] 状态滚动", "detail": "细扣：一行原子化更新前两阶状态，免去临时变量 temp 介入。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：循环结束直接 return b 达到 O(1) 空间", "detail": "细扣：最终 b 即为到达第 n 阶的总走法，时间 O(N)，额外空间 O(1)。", "weight": 20}
        ]
    },
    118: {
        "title_cn": "杨辉三角",
        "title_en": "Pascal's Triangle",
        "slug": "pascals-triangle",
        "difficulty": "Easy",
        "description": """给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

示例 2:
输入: numRows = 1
输出: [[1]]

提示:
- 1 <= numRows <= 30""",
        "plain_explanation": "杨辉三角在视觉上就像一座叠罗汉金字塔：第 0 行有 1 个数 [1]，第 1 行有 2 个数 [1, 1]，第 2 行有 3 个数 [1, 2, 1]，第 i 行共有 i+1 个数。仔细观察规律：每一行的最左边开头和最右边结尾永远都是固定的 1！而中间除了两端的每一个数字，都严格等于上一行正上方的数字加上左上方的数字：row[j] = res[i - 1][j - 1] + res[i - 1][j]。初学者写这道题往往会写一堆 if-else 去判断是不是两头，容易下标越界且代码冗长。写出优雅 JS 代码的秘诀是“预先铺平”：在生成第 i 行时，直接用 new Array(i + 1).fill(1) 创建一个全是 1 的数组！这样头和尾的 1 自动就位了。接下来，内层循环只需要从下标 1 跑到 i-1（刚好避开了两头），把中间的值替换成上一行对应两数之和。最后把整行 push 进结果数组 res，整齐、优美、零越界风险！",
        "js_helpers": [
            {
                "name": "new Array(len).fill(val)",
                "what_it_does": "快速创建一个指定长度的数组并将所有位置填充为初始值。",
                "junior_tip": "这里填充的是基本数据类型数值 1，不存在引用对象浅拷贝踩坑的问题，非常安全且高效！"
            },
            {
                "name": "res[i - 1][j - 1] + res[i - 1][j]",
                "what_it_does": "二维数组递推访问，取得上一行相邻两个位置的数字加和。",
                "junior_tip": "必须严格保证 i >= 1 且 j >= 1，否则会导致读取 undefined 报错。"
            },
            {
                "name": "res.push(row)",
                "what_it_does": "将当前计算完成的一维行数组加入二维结果数组末尾。",
                "junior_tip": "由于每次循环都通过 new Array 新建了独立数组引用，push 进结果集后不会互相污染。"
            }
        ],
        "code_js": '''/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const res = [];

    for (let i = 0; i < numRows; i++) {
        // 创建长度为 i + 1 的数组，全部预填 1，头尾两端自动就位
        const row = new Array(i + 1).fill(1);

        // 内部元素从索引 1 遍历到 i - 1，由上一行相邻两数之和填充
        for (let j = 1; j < i; j++) {
            row[j] = res[i - 1][j - 1] + res[i - 1][j];
        }

        res.push(row);
    }

    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：外层循环遍历行数 i 从 0 到 numRows - 1", "detail": "细扣：生成第 i 行金字塔，共计 numRows 层，自顶向下构建。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：new Array(i + 1).fill(1) 预填充两端 1", "detail": "细扣：行两端天然为 1，直接 fill(1) 省略两端打标分支判断。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：内层循环锁定中间区间 1 到 i - 1", "detail": "细扣：当 i 为 0 或 1 时，循环条件 j < i 不成立自然跳过，完美契合前两行。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：组合数递推赋值 row[j] = 上层相邻两数之和", "detail": "细扣：精确从 res[i - 1] 抓取 j - 1 与 j 索引处的值进行累加。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：res.push(row) 将当前行加入二维结果数组", "detail": "细扣：循环结束后返回完整杨辉三角，整体时间复杂度为 O(numRows^2)。", "weight": 20}
        ]
    },
    198: {
        "title_cn": "打家劫舍",
        "title_en": "House Robber",
        "slug": "house-robber",
        "difficulty": "Medium",
        "description": """你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组 nums，计算你 不触动报警装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400""",
        "plain_explanation": "小偷不能偷相邻的两家，否则报警器会响。来到第 i 家时，小偷心里只有两个相互排斥的选择：1. 【偷这家】：那前一家就绝对不能偷，收益是“前前家之前的最高收益 + 当前家的钱”（prev2 + nums[i]）；2. 【不偷这家】：收益就是“前一家之前的最高收益”（prev1）。小偷只要在这两个选择里挑个赚得更多的：curr = Math.max(prev1, prev2 + nums[i])！用两个变量 prev1 和 prev2 记录历史最优，一路像接力棒一样滚过去，空间复杂度 O(1)！更妙的是，把 prev2 和 prev1 的初始值都设为 0，这样哪怕数组只有 1 间房，或者空数组，都能自动统一处理，不需要写任何特判分支！",
        "js_helpers": [
            {
                "name": "Math.max(a, b)",
                "what_it_does": "返回两个数值中的较大者。",
                "junior_tip": "用于动态规划状态转移时在“偷”与“不偷”两个互斥决策中挑选更优收益。"
            },
            {
                "name": "虚拟零底座 let prev2 = 0, prev1 = 0",
                "what_it_does": "初始化两个前置状态变量为 0。",
                "junior_tip": "优雅避免了针对 nums.length === 1 或 2 写一堆繁琐的特判代码，极大精简逻辑！"
            },
            {
                "name": "滚动推进 prev2 = prev1; prev1 = curr;",
                "what_it_does": "将观察窗口向右平移一位，让历史最优收益持续接力递推。",
                "junior_tip": "注意顺序必须是先更新 prev2 再更新 prev1，否则 prev1 的旧值会被直接覆盖丢掉！"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (!nums || nums.length === 0) return 0;

    // prev2 记录前前间的最大收益，prev1 记录前一间的最大收益
    let prev2 = 0;
    let prev1 = 0;

    for (const num of nums) {
        // 核心抉择：不偷当前房屋（收益 prev1）vs 偷当前房屋（收益 prev2 + num）
        const curr = Math.max(prev1, prev2 + num);
        // 状态平移滚动，为下一间房屋做准备
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：判空与设置基础状态 prev2 = 0, prev1 = 0", "detail": "细扣：零值基准简化了只有 1 家或 2 家时的边界特判分支。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：for...of 遍历各房屋金额 num", "detail": "细扣：线性单趟扫描每一个房屋，构建互斥决策分支。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：Math.max 权衡偷与不偷二选一", "detail": "细扣：prev2 + num 与 prev1 互斥竞争，取收益更大者存入 curr。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：滚动平移 prev2 = prev1, prev1 = curr", "detail": "细扣：窗口向右推进一位，历史最优持续接力，注意更新先后顺序。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：遍历结束后 prev1 即为全局最高战利品", "detail": "细扣：时间复杂度 O(N) 一趟遍历，额外空间复杂度 O(1)。", "weight": 20}
        ]
    },
    279: {
        "title_cn": "完全平方数",
        "title_en": "Perfect Squares",
        "slug": "perfect-squares",
        "difficulty": "Medium",
        "description": """给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
- 1 <= n <= 10^4""",
        "plain_explanation": "题目要求用最少个完全平方数（1, 4, 9, 16...）凑出整数 n。这就是个标准的“完全背包找零”问题：背包容量是 n，商品是所有不大于 n 的完全平方数，每件商品可以无限次重复拿，求装满背包所需的最少商品件数。定义 dp[i] 表示凑出数字 i 最少需要几个平方数。初始化把数组整个填成无穷大 Infinity。那为什么 dp[0] = 0 呢？因为凑出 0 需要 0 个平方数，它是所有平方数能一步到位的基石（比如凑 4 时，选 2*2=4，dp[4] = dp[4 - 4] + 1 = dp[0] + 1 = 1）！对于每个 i，枚举所有可能的平方数底数 j（j * j <= i），用 dp[i - j * j] + 1 来挑战当前的 dp[i]，刷出最小值！最终返回 dp[n]，时间复杂度 O(n*sqrt(n))，简洁易懂且完全不会超时！",
        "js_helpers": [
            {
                "name": "new Array(n + 1).fill(Infinity)",
                "what_it_does": "初始化一个长度为 n + 1 的数组，并将每个位置预填为正无穷大哨兵。",
                "junior_tip": "寻找极小值时，初始填充 Infinity 可以确保任何真实合法解都能顺利更新覆盖它。"
            },
            {
                "name": "j * j <= i 循环终止条件",
                "what_it_does": "内层循环动态枚举所有不超过当前数字 i 的完全平方数。",
                "junior_tip": "省去了提前预生成平方数列表的额外开销，极大节约空间且逻辑自然。"
            },
            {
                "name": "Math.min(a, b)",
                "what_it_does": "比较并返回两数中的较小值。",
                "junior_tip": "状态转移时用于不断尝试不同平方数面值，贪心挑选最少件数方案。"
            }
        ],
        "code_js": '''/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    // dp[i] 表示组成整数 i 所需的最少完全平方数个数
    // 寻找最小值，初始全部填充为正无穷大
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0; // 凑出 0 需要 0 个数，作为递推基石

    // 自底向上，计算每个子目标 i 的最优解
    for (let i = 1; i <= n; i++) {
        // 枚举所有不大于 i 的完全平方数 j * j
        for (let j = 1; j * j <= i; j++) {
            dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
        }
    }

    return dp[n];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：理解完全背包模型，抽象平方数为无限件数商品", "detail": "细扣：将目标金额视为背包容量 n，平方数 1, 4, 9... 视为无限供应商品。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：创建长度 n + 1 数组并 fill(Infinity)，设置 dp[0] = 0", "detail": "细扣：dp[0]=0 是所有平方数直接一步到位的基石（如 4 - 4 = 0 得 1 件）。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：外层循环自底向上遍历容量 i 从 1 到 n", "detail": "细扣：保证在计算 dp[i] 时，所有更小的子问题 dp[i - j*j] 已经是最优解。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：内层循环动态枚举 j * j <= i 执行状态转移", "detail": "细扣：dp[i] = Math.min(dp[i], dp[i - j * j] + 1) 刷出最少数量。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：返回 dp[n]，分析时间与空间复杂度", "detail": "细扣：时间复杂度 O(n*sqrt(n))，空间复杂度 O(n)，稳健可靠。", "weight": 20}
        ]
    },
    322: {
        "title_cn": "零钱兑换",
        "title_en": "Coin Change",
        "slug": "coin-change",
        "difficulty": "Medium",
        "description": """给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

提示：
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4""",
        "plain_explanation": "给你几种面值的硬币，要凑出总金额 amount，问最少几枚硬币？很多初学者想用贪心法（每次拿最大面额），但只要 coins = [1, 3, 4] 凑 6，贪心拿 4+1+1 需 3 枚，最优解却是 3+3 仅需 2 枚！因此必须用动态规划（完全背包）。定义 dp[i] 为凑出金额 i 所需的最少硬币数。初始化把所有格子填成 amount + 1！为什么不是 Infinity？因为哪怕全用 1 块钱，最多也就 amount 枚，不可能超过它，amount + 1 就是一个绝对不可逾越的安全哨兵，既不会溢出又便于比较！dp[0] = 0。外层遍历金额 1 到 amount，内层遍历硬币 coins：如果当前金额装得下这枚硬币（i >= coin），那么 dp[i] = Math.min(dp[i], dp[i - coin] + 1)。最后检查如果 dp[amount] > amount 说明凑不出，返回 -1，否则返回 dp[amount]！",
        "js_helpers": [
            {
                "name": "amount + 1 作为安全不可达哨兵",
                "what_it_does": "设置一个理论上无法突破的上限值作为极小值初始值。",
                "junior_tip": "比 Infinity 更安全，做加法时完全不用担心精度溢出产生特殊逻辑错误。"
            },
            {
                "name": "for (const coin of coins)",
                "what_it_does": "ES6 迭代器遍历硬币数组中的每一个面值。",
                "junior_tip": "代码语义清晰，直接获取 coin 面额，避免下标索引访问的繁琐写法。"
            },
            {
                "name": "三元运算符 dp[amount] > amount ? -1 : dp[amount]",
                "what_it_does": "快速判定是否存在有效找零方案。",
                "junior_tip": "一行代码完成边界与哨兵判定，优雅返回最优解或 -1。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    // 凑成 amount 最多需要 amount 枚 1 元硬币
    // 用 amount + 1 作为哨兵初始值，代表“不可能凑出”
    const dp = new Array(amount + 1).fill(amount + 1);
    dp[0] = 0; // 凑出 0 元所需硬币为 0

    // 外层遍历目标金额 1 到 amount
    for (let i = 1; i <= amount; i++) {
        // 内层遍历每一种可选面额
        for (const coin of coins) {
            if (i >= coin) {
                // 状态转移：拿当前这枚硬币，再加上剩余金额所需的最少硬币数
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    // 若 dp[amount] 仍保持哨兵值，说明无解返回 -1；否则返回最少硬币数
    return dp[amount] > amount ? -1 : dp[amount];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：识破贪心反例，确立完全背包动态规划解法体系", "detail": "细扣：硬币可无限复选，金额由小到大递推覆盖全局解空间。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：初始化 dp 数组长度 amount + 1，哨兵值 amount + 1，dp[0] = 0", "detail": "细扣：dp[0]=0 奠定基础，哨兵防止不可达硬币组合被误用。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：双层循环，外层遍历金额 i，内层枚举所有可用硬币 coin", "detail": "细扣：完全背包标准模式，外层为容量，内层为物品面额。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：当 i >= coin 时状态转移 dp[i] = min(dp[i], dp[i - coin] + 1)", "detail": "细扣：如果拿这枚硬币，所需总枚数就是金额 i - coin 的最少枚数加 1。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：判断 dp[amount] > amount 返回 -1 或最优枚数", "detail": "细扣：若最终仍等于哨兵说明无法凑出返回 -1，时间复杂度 O(amount * N)。", "weight": 20}
        ]
    },
    139: {
        "title_cn": "单词拆分",
        "title_en": "Word Break",
        "slug": "word-break",
        "difficulty": "Medium",
        "description": """给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" + "pen" + "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

提示：
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s 和 wordDict[i] 仅由小写英文字母组成
- wordDict 中的所有字符串 互不相同""",
        "plain_explanation": "给你一个字符串 s 和一个词典，问能不能把 s 用空格切成若干截，每截都在词典里。大白话“接竹竿拼积木游戏”：定义布尔数组 dp，dp[i] 代表前 i 个字符 s[0...i-1] 能不能被完美拼出来。显然空字符串 dp[0] = true 作为初始基石。对于前 i 个字符，我们在中间找一个分割点 j（0 到 i-1）：只要前半截 dp[j] 是能拼出来的（true），而且后半截切片 s.slice(j, i) 刚好在词典里，那整个前 i 个字符就能拼出来，dp[i] = true！一旦为 true 立刻 break 剪枝！另外注意性能巨坑：wordDict 是个数组，如果在循环里用 wordDict.includes() 查词会退化为 O(M) 线性扫描，必须用 new Set(wordDict) 建立哈希集合，实现 O(1) 瞬时查词！",
        "js_helpers": [
            {
                "name": "new Set(wordDict) 与 set.has()",
                "what_it_does": "将词典数组转为 Set 集合，并在 O(1) 时间内完成单词查找。",
                "junior_tip": "千万别用数组的 indexOf 或 includes，在循环里会退化为 O(N) 线性扫描！"
            },
            {
                "name": "s.slice(j, i)",
                "what_it_does": "提取字符串从索引 j 到 i - 1 的子串切片。",
                "junior_tip": "左闭右开区间，截取出来的子串完全不修改原字符串，干净安全。"
            },
            {
                "name": "break 提前剪枝跳出",
                "what_it_does": "当找到任意一个可行的分割点使 dp[i] 为 true 时，立即终止内层枚举。",
                "junior_tip": "只要存在一种成功切分方案即说明前 i 个字符可行，提前 break 大幅提速！"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    // 将字典数组转为 Set 哈希集合，实现 O(1) 极速单词匹配
    const wordSet = new Set(wordDict);
    const n = s.length;

    // dp[i] 表示 s 的前 i 个字符组成的子串能否被完全拆分
    const dp = new Array(n + 1).fill(false);
    dp[0] = true; // 空字符串作为拆分根基，默认可拆分

    // 遍历待匹配的前缀长度 i（从 1 到 n）
    for (let i = 1; i <= n; i++) {
        // 枚举分割点 j（从 0 到 i - 1）
        for (let j = 0; j < i; j++) {
            // 前半截 dp[j] 可拼成，且后半截切片 s[j...i-1] 存在于字典中
            if (dp[j] && wordSet.has(s.slice(j, i))) {
                dp[i] = true;
                break; // 只要找到一种切分方案即可提前结束当前长度的探索
            }
        }
    }

    return dp[n];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：const wordSet = new Set(wordDict) 建立 O(1) 查词集合", "detail": "细扣：将数组转为 Set，避免内层循环反复线性扫描拖慢速度。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：创建布尔 dp 数组并将 dp[0] 置为 true 作为切分根基", "detail": "细扣：dp[i] 映射 s 的前 i 个字符能否合法拼装，dp[0]=true 守护空串。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：双层循环外层枚举长度 i，内层枚举切分点 j", "detail": "细扣：外层 i 从 1 到 n，内层 j 从 0 到 i - 1，穷举所有潜在拆分点。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：校验 dp[j] && wordSet.has(s.slice(j, i)) 与 break 剪枝", "detail": "细扣：前半段可达与后半段在字典中同时成立，置 dp[i] = true 并早停。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：最终返回 dp[n]，分析时间与空间复杂度", "detail": "细扣：时间复杂度 O(N^2)，空间复杂度 O(N)，完全胜任 300 字符长度。", "weight": 20}
        ]
    },
    300: {
        "title_cn": "最长递增子序列",
        "title_en": "Longest Increasing Subsequence",
        "slug": "longest-increasing-subsequence",
        "difficulty": "Medium",
        "description": """给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

进阶：
- 你能将算法的时间复杂度降低到 O(n log n) 吗?""",
        "plain_explanation": "从一串乱序数字里挑出一个子序列，要求严格单调递增，求能挑出的最长长度。普通 DP 复杂度是 O(N^2)，但在大厂面试中最惊艳的是“纸牌贪心接龙（Patience Sorting）+ 二分查找”，时间缩短到极速的 O(N log N)！我们维护一个牌堆数组 tails，其中 tails[k] 表示长度为 k+1 的递增子序列的“最小末尾数字”。为什么必须记最小末尾？因为贪心法则：结尾数字越小，后面越容易接上更大的数！每看到一个新数字 x，我们用二分查找在 tails 里找第一个 >= x 的位置 left。如果找不到（即所有牌都比 x 小，left === tails.length），说明可以把现有子序列延长一位，直接 tails.push(x)；如果找到，就用更小的 x 替换掉 tails[left]（贪心压低尾部元素）！最后 tails.length 就是最长递增子序列的终极长度！",
        "js_helpers": [
            {
                "name": "(left + right) >> 1 二分中点位运算",
                "what_it_does": "二进制右移 1 位，相当于 Math.floor((left + right) / 2)。",
                "junior_tip": "整型除法位运算写法，执行速度快且天然向下取整，避免浮点数坑。"
            },
            {
                "name": "手写二分查找查找首个 >= x 的位置",
                "what_it_does": "在严格单调递增的 tails 数组中定位替换或插入点。",
                "junior_tip": "区间为 [left, right]，当 mid >= x 时收缩右边界 right = mid - 1，最终 left 即为目标索引。"
            },
            {
                "name": "tails.push(x) 与 tails[left] = x",
                "what_it_does": "若当前元素最大则扩充序列长度；否则贪心替换降低末尾门槛。",
                "junior_tip": "tails 数组的长度严格等于最长上升子序列的长度，但内部内容不一定是原序列。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if (!nums || nums.length === 0) return 0;

    // tails[k] 表示长度为 k + 1 的递增子序列的最小末尾元素
    const tails = [];

    for (const x of nums) {
        // 在有序数组 tails 中通过二分查找寻找第一个 >= x 的位置
        let left = 0, right = tails.length - 1;
        while (left <= right) {
            const mid = (left + right) >> 1;
            if (tails[mid] >= x) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // 若 x 大于 tails 中的所有末尾元素，则最长长度扩展一位
        if (left === tails.length) {
            tails.push(x);
        } else {
            // 否则用更小的 x 替换原来的末尾，贪心降低该长度的接龙门槛
            tails[left] = x;
        }
    }

    return tails.length;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：理解 Patience Sorting 贪心最小末尾牌堆思想", "detail": "细扣：tails 数组严格递增，同等长度下结尾越小对后续数字越友好。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：遍历 nums，手写二分查找定位首个 >= x 的位置", "detail": "细扣：双指针 left 与 right，位运算 (left + right) >> 1 确定中点。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：若 left === tails.length 则 push 扩容延长长度", "detail": "细扣：新数字比历史所有尾巴都大，最长递增序列总长度成功加 1。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：否则 tails[left] = x 替换优化已有牌堆尾数", "detail": "细扣：贪心压低尾部元素，不改变当前序列长度，但增强后续接龙潜力。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：循环结束 return tails.length 达到 O(N log N) 复杂度", "detail": "细扣：空间占用 O(N)，时间复杂度从 O(N^2) 跃迁至 O(N log N)。", "weight": 20}
        ]
    },
    152: {
        "title_cn": "乘积最大子数组",
        "title_en": "Maximum Product Subarray",
        "slug": "maximum-product-subarray",
        "difficulty": "Medium",
        "description": """给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的多样性可以保证答案是一个 32-位 整数。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是连续子数组。

提示:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- nums 的任何子数组的乘积都 保证 是一个 32-位 整数""",
        "plain_explanation": "求连续子数组的最大乘积。加法只有正负，但乘法有个巨大的变数：负负得正！一个极小的负数乘以另一个负数，瞬间可能反转变成超级大正数！所以我们不能只记“最大值”，必须“双轨并行”：同时记录以当前数字结尾的“最大乘积 maxProd”和“最小乘积 minProd”。当遇到一个负数时，最大的会变成最小的，最小的会变成最大的，所以先用 ES6 解构把它俩来个乾坤大挪移互换：[maxProd, minProd] = [minProd, maxProd]！然后当前位置只有两条路可选：要么跟前面的连乘接上，要么自立门户从当前数重新开始。用 Math.max(x, maxProd * x) 和 Math.min(x, minProd * x) 更新两者，并同步刷新全局最大值 res！空间复杂度达到极简的 O(1)！",
        "js_helpers": [
            {
                "name": "[maxProd, minProd] = [minProd, maxProd]",
                "what_it_does": "遇到负数时，用解构赋值一行对调最大值和最小值。",
                "junior_tip": "必须在乘上当前数之前先对调，因为负数会让极小负数反弹为极大正数！"
            },
            {
                "name": "Math.max(x, maxProd * x)",
                "what_it_does": "在自立门户（x 本身）与接续连乘之间选出最大乘积。",
                "junior_tip": "当之前的乘积为 0 或由于负数缩小后，当前元素可以果断截断自成新起点。"
            },
            {
                "name": "Math.min(x, minProd * x)",
                "what_it_does": "维护以当前数结尾的最小乘积。",
                "junior_tip": "留存极小负数作为伏笔，等待下一个负数到来时实现“负负得正”惊天大逆转！"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    // 全局最大值初始为首个元素
    let res = nums[0];
    // 维护当前位置结尾的最大乘积与最小乘积（双轨并行）
    let maxProd = nums[0];
    let minProd = nums[0];

    // 从第二个元素开始向后推演
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];

        // 遇到负数，符号颠倒：原极小值翻转为潜在极大值，原极大值跌落为极小值
        if (x < 0) {
            [maxProd, minProd] = [minProd, maxProd];
        }

        // 决策：与历史乘积相连，还是以当前元素作为子数组起点（自立门户）
        maxProd = Math.max(x, maxProd * x);
        minProd = Math.min(x, minProd * x);

        // 刷新全局最大连续子数组乘积
        res = Math.max(res, maxProd);
    }

    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：初始化全局最大 res 与滚动变量 maxProd, minProd 为 nums[0]", "detail": "细扣：以首个元素建立双轨 DP 起跑线，避免额外的零值陷阱。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：遍历后续元素，若 x < 0 则解构对调 maxProd 与 minProd", "detail": "细扣：负负得正机制，极小负数是潜在最大正数之母，解构一行完成互换。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：Math.max 计算当前最大乘积 maxProd = max(x, maxProd * x)", "detail": "细扣：自立门户（x）或接续连乘（maxProd * x）二选一。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：Math.min 计算当前最小乘积 minProd = min(x, minProd * x)", "detail": "细扣：保留极限负值储备，为后续连续乘积提供反转可能。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：刷新全局最大值 res = Math.max(res, maxProd) 并返回", "detail": "细扣：时间复杂度 O(N)，空间复杂度 O(1) 滚动更新极其紧凑高效。", "weight": 20}
        ]
    },
    416: {
        "title_cn": "分割等和子集",
        "title_en": "Partition Equal Subset Sum",
        "slug": "partition-equal-subset-sum",
        "difficulty": "Medium",
        "description": """给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1, 5, 11, 5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1, 2, 3, 5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100""",
        "plain_explanation": "问能不能把一个数组分成两个和相等的子集？大白话转换：先算出全数组的总和 total。如果 total 是奇数，俩整数怎么加都不可能等分，直接返回 false！如果 total 是偶数，问题就变成了：能不能从数组里挑出若干个数，让它们的和恰好等于背包容量 target = total / 2！这就是经典的“0-1 背包可达性问题”。用一个一维布尔数组 dp，dp[j] 表示容量 j 能不能被恰好凑出来。外层遍历每个数 num，内层容量 j 必须从 target 倒着循环到 num！【为什么要倒着走？】因为如果正着走，当前物品 num 会在同一次外层循环中被重复累加多次，直接退化成完全背包；只有倒着走，dp[j - num] 才是上一轮的老值，确保每个数字至多被使用一次！如果 dp[target] 变成 true，说明能凑出来，直接提前 return true 收工！",
        "js_helpers": [
            {
                "name": "nums.reduce((sum, val) => sum + val, 0)",
                "what_it_does": "数组求和函数式优雅写法，累加数组所有元素。",
                "junior_tip": "第二个参数初始值 0 别漏写，能防止空数组或类型隐式转换异常。"
            },
            {
                "name": "total % 2 !== 0 快速剪枝",
                "what_it_does": "判断总和是否为奇数。",
                "junior_tip": "奇数无法平分成两个相等的整数，一行代码提前返回 false，极大提升运行效率。"
            },
            {
                "name": "倒序循环 for (let j = target; j >= num; j--)",
                "what_it_does": "0-1 背包空间压缩的核心生命线。",
                "junior_tip": "必须从大到小倒着算！如果正序，计算 dp[j] 时用到的 dp[j - num] 会被当前数字污染，导致同一数字被重复使用多次！"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    // 计算数组总和
    const total = nums.reduce((sum, val) => sum + val, 0);

    // 奇数和绝不可能平分成两个相等的整数部分，直接剪枝
    if (total % 2 !== 0) return false;

    // 目标背包容量：总和的一半
    const target = total / 2;

    // dp[j] 表示是否能够恰好凑出容量 j
    const dp = new Array(target + 1).fill(false);
    dp[0] = true; // 容量为 0 默认可达成

    // 外层遍历每一个数字（物品）
    for (const num of nums) {
        // 核心：容量必须倒序遍历，确保每个数字至多被使用一次（0-1 背包法则）
        for (let j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }

        // 剪枝优化：如果目标容量已经被成功凑出，提前返回 true
        if (dp[target]) return true;
    }

    return dp[target];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：reduce 算总和，total % 2 !== 0 奇数提前判 false", "detail": "细扣：奇数和无法平分，一行代码快速剪枝防守。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：设立目标容量 target = total / 2，创建布尔 dp 数组", "detail": "细扣：将问题精确等价转换为 0-1 背包凑数问题，dp[0] = true 守护基底。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：外层枚举 num，内层从 target 倒序遍历至 num", "detail": "细扣：必须倒序遍历容量，防止当前数字在同一次迭代中被复选多次。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：状态转移 dp[j] = dp[j] || dp[j - num] 与早停检查", "detail": "细扣：可达性逻辑或运算，检测到 dp[target] 为真立即提前 return true。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：最终返回 dp[target]，分析时间与空间复杂度", "detail": "细扣：时间复杂度 O(N * Target)，空间压缩至 O(Target)，空间利用率极高。", "weight": 20}
        ]
    },
    32: {
        "title_cn": "最长有效括号",
        "title_en": "Longest Valid Parentheses",
        "slug": "longest-valid-parentheses",
        "difficulty": "Hard",
        "description": """给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0

提示：
- 0 <= s.length <= 3 * 10^4
- s[i] 为 '(' 或 ')'""",
        "plain_explanation": "求只包含括号的字符串中，最长的连续有效闭合括号子串长度。难点在于括号可能嵌套也可能并列，还可能被多余的右括号截断。大白话“栈底哨兵定边界法”：我们在栈底初始放一个 -1，作为“上一次断裂的无效右括号下标”！遇到左括号 '('，把它在字符串里的下标压入栈；遇到右括号 ')'，弹出栈顶（意味着尝试抵消一对括号）。弹出后看一眼栈：如果栈空了，说明刚才弹出的根本不是左括号，而是原本垫底的哨兵，意味着当前的右括号无法匹配，它成了新的断裂点，把它的下标压入栈顶当新的哨兵；如果栈没空，说明刚才成功配对了一对括号，有效长度就是 当前下标 i - 弹出后的新栈顶下标 stack[stack.length - 1]！一趟线性扫描就能求出全局最长，极其神妙高效！",
        "js_helpers": [
            {
                "name": "stack = [-1] 栈底初始哨兵",
                "what_it_does": "在栈底初始压入 -1 虚拟下标，作为首个未匹配阻断点。",
                "junior_tip": "巧妙让从索引 0 开始的合法括号对能通过 i - (-1) 算出真实连续长度！"
            },
            {
                "name": "栈存下标而非字符",
                "what_it_does": "栈中存储字符所在的位置索引 i 而不是字符 '(' 本身。",
                "junior_tip": "存下标不仅能判断是否匹配，还能直接通过当前下标减去栈顶下标计算跨度长度！"
            },
            {
                "name": "stack[stack.length - 1] 获取栈顶",
                "what_it_does": "读取栈顶元素而不弹出，获取上一个未配对有效断裂点的下标。",
                "junior_tip": "当前下标 i 减去新栈顶下标，就是当前这段连续有效闭合括号的绝对真实跨度！"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    // 栈底哨兵：初始压入 -1，代表最后一个未匹配的截断右括号位置
    const stack = [-1];
    let maxLen = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            // 遇到左括号，将其索引入栈，等待匹配
            stack.push(i);
        } else {
            // 遇到右括号，弹出栈顶（匹配对应的左括号或原哨兵）
            stack.pop();

            if (stack.length === 0) {
                // 栈为空说明没有左括号与当前右括号匹配，当前索引成为新的截断哨兵
                stack.push(i);
            } else {
                // 栈非空，有效长度为当前索引减去弹出后的新栈顶索引
                maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
            }
        }
    }

    return maxLen;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：stack = [-1] 压入虚拟哨兵，maxLen = 0", "detail": "细扣：栈底 -1 让从索引 0 开始的合法段能被 i - (-1) 正常结算。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：遇到 '(' 压入当前下标 i，保留匹配种子", "detail": "细扣：栈中存索引而非字符，便于后续 O(1) 跨度减法计算。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：遇到 ')' 执行 stack.pop() 弹出栈顶尝试配对", "detail": "细扣：抵消对应的左括号或原断裂哨兵，开启分支校验。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：若栈空将 i 压栈充当新哨兵；若非空计算 i - stack 栈顶更新 maxLen", "detail": "细扣：未匹配右括号自立为新左护栏，已匹配右括号计算当前区间跨度。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：遍历结束后直接返回 maxLen，时间 O(N) 空间 O(N)", "detail": "细扣：一趟扫描完成 Hard 题秒杀，并演练正反双向计数的 O(1) 空间进阶解法。", "weight": 20}
        ]
    }
}
