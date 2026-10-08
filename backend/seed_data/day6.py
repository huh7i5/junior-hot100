DAY_6_PROBLEMS = [
    {
        "frontend_id": 70,
        "title_cn": "爬楼梯",
        "title_en": "Climbing Stairs",
        "slug": "climbing-stairs",
        "difficulty": "Easy",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "斐波那契状态转移：dp[i] = dp[i-1] + dp[i-2]。到达第 i 阶只能从 i-1 阶跨 1 步或从 i-2 阶跨 2 步。使用两个变量滚动更新，空间压缩至 O(1)。",
            "traps": "n <= 2 时的边界值：1 阶 1 种，2 阶 2 种。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "最基础无后效性状态机", "detail": "破题眼：最后一步二选一（跨1步或2步），划分互斥集合，相加得全集。", "weight": 25},
            {"dimension": "corner_case", "title": "n <= 2 小输入特判", "detail": "防守点：n=1 返回 1，n=2 返回 2，滚动变量循环安全跳过。", "weight": 25},
            {"dimension": "solution", "title": "双变量滚动压榨空间手写", "detail": "手写点：使用 a, b = b, a + b 一行实现状态滚动更新。", "weight": 25},
            {"dimension": "complexity", "title": "矩阵快速幂 O(log N) 扩展", "detail": "演练点：口述如何构造 [[1,1],[1,0]] 状态转移矩阵用快速幂达到对数复杂度。", "weight": 25}
        ]
    },
    {
        "frontend_id": 118,
        "title_cn": "杨辉三角",
        "title_en": "Pascal's Triangle",
        "slug": "pascals-triangle",
        "difficulty": "Easy",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "组合数逐行生成：第 i 行有 i+1 个元素，两端为 1。中间元素 `row[j] = prev_row[j-1] + prev_row[j]`。",
            "traps": "两端元素索引为 0 和 i，中间循环范围是 `1` 到 `i-1`。",
            "time_complexity": "O(numRows^2)",
            "space_complexity": "O(1)（除返回值外）",
            "code_python": '''class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "加法原理自顶向下展开", "detail": "破题眼：数学二项式定理系数推导，上一层相邻两数加和填充当前层。", "weight": 25},
            {"dimension": "corner_case", "title": "前两行无内层运算", "detail": "防守点：i=0,1 时 range(1, i) 自动为空，天然保持两端全 1。", "weight": 25},
            {"dimension": "solution", "title": "预填 1 结构极简手写", "detail": "手写点：row = [1] * (i+1) 省略两端补 1 逻辑，直接对内层赋值。", "weight": 25},
            {"dimension": "complexity", "title": "第 k 行直接计算公式口述", "detail": "演练点：口述若只求第 k 行如何用乘除法组合数 C(k, i) 达到 O(k) 空间。", "weight": 25}
        ]
    },
    {
        "frontend_id": 198,
        "title_cn": "打家劫舍",
        "title_en": "House Robber",
        "slug": "house-robber",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "选择不相邻状态转移：对于第 i 间房屋，若偷则不能偷 i-1 间，收益 `dp[i-2] + nums[i]`；若不偷收益为 `dp[i-1]`。因此 `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`。滚动变量 O(1) 空间。",
            "traps": "只有一间房屋直接返回 `nums[0]`；两间返回 `max(nums[0], nums[1])`。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "偷与不偷决策二选一", "detail": "破题眼：当前房偷与不偷产生互斥子问题，历史最优递推保证全局收益最大。", "weight": 25},
            {"dimension": "corner_case", "title": "虚拟零底座简化初始化", "detail": "防守点：prev2=0, prev1=0 起步，无需对 len(nums) == 1 或 2 写一堆分支。", "weight": 25},
            {"dimension": "solution", "title": "6 行滚动变量手撕", "detail": "手写点：curr = max(prev1, prev2 + num) 单行状态转移，清晰精湛。", "weight": 25},
            {"dimension": "complexity", "title": "环形房屋（213 题）解法演练", "detail": "演练点：口述环形打家劫舍如何通过切分首尾为 nums[1:] 和 nums[:-1] 分别调用本题。", "weight": 25}
        ]
    },
    {
        "frontend_id": 279,
        "title_cn": "完全平方数",
        "title_en": "Perfect Squares",
        "slug": "perfect-squares",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "完全背包 / 动态规划：设 `dp[i]` 为和为 i 的最少完全平方数数量。状态转移方程：`dp[i] = 1 + min(dp[i - j*j])`，其中 `j*j <= i`。初始化 `dp[0] = 0`，其余为无穷大。",
            "traps": "平方数底数 j 从 1 遍历到 `int(sqrt(i))`；四平方和定理可做到 O(sqrt(N))，但面试中 DP 更通用。",
            "time_complexity": "O(N * sqrt(N))",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "完全背包物品无限选模型", "detail": "破题眼：完全平方数 1, 4, 9... 就是重量无限的物品，凑成目标重量 n 的最小件数。", "weight": 25},
            {"dimension": "corner_case", "title": "dp[0] = 0 边界守门", "detail": "防守点：dp[0]=0 使得当 i 本身是完全平方数时（如 4-4=0），dp[4]=dp[0]+1=1。", "weight": 25},
            {"dimension": "solution", "title": "嵌套 while 计算平方数手写", "detail": "手写点：无需预生成平方数列表，内层 j*j <= i 动态枚举，空间占用少。", "weight": 25},
            {"dimension": "complexity", "title": "广度优先搜索 (BFS) 最短路口述", "detail": "演练点：口述把该问题看作从 0 到 n 每次走平方数的最短路径 BFS 解法。", "weight": 25}
        ]
    },
    {
        "frontend_id": 322,
        "title_cn": "零钱兑换",
        "title_en": "Coin Change",
        "slug": "coin-change",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "经典完全背包：`dp[i]` 表示凑成金额 i 所需的最少硬币数。遍历金额 1 到 amount，枚举硬币 coin：若 `i >= coin`，则 `dp[i] = min(dp[i], dp[i - coin] + 1)`。初始化 `dp[0] = 0`，其余设为 `amount + 1`。",
            "traps": "不可达金额最终维持 `amount + 1`，判断如果 `dp[amount] > amount` 则返回 -1。",
            "time_complexity": "O(Amount * N)",
            "space_complexity": "O(Amount)",
            "code_python": '''class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "完全背包最小值状态转移", "detail": "破题眼：背包容量为 amount，物品为硬币，每种可用无限次，外层金额内层硬币。", "weight": 25},
            {"dimension": "corner_case", "title": "金额为 0 与无法凑出返回 -1", "detail": "防守点：amount == 0 时返回 0；最终判断大于 amount 说明不可达返回 -1。", "weight": 25},
            {"dimension": "solution", "title": "哨兵无穷大 amount + 1 手写", "detail": "手写点：使用 amount + 1 替代 float('inf') 防止加一溢出与比对整洁。", "weight": 25},
            {"dimension": "complexity", "title": "为什么不能用贪心找零钱", "detail": "演练点：举反例（如 coins=[1,3,4], amount=6，贪心选 4+1+1=3 枚，最优是 3+3=2 枚）。", "weight": 25}
        ]
    },
    {
        "frontend_id": 139,
        "title_cn": "单词拆分",
        "title_en": "Word Break",
        "slug": "word-break",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "布尔型前缀 DP：`dp[i]` 表示 `s[:i]` 是否可以被空格拆分为字典单词。遍历 i 从 1 到 n，枚举切分点 j 从 0 到 i-1：若 `dp[j]` 为 True 且 `s[j:i] in word_set`，则 `dp[i] = True` 并提前 break。",
            "traps": "切分前缀必须先判断 `dp[j]` 是否为真，只有当左半部分可拆，右半部分查字典才有意义；将 wordDict 转为 set 达到 O(1) 查询。",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "前缀可达性与子串字典验证", "detail": "破题眼：dp[i] = dp[j] and (s[j:i] in word_set)，只要存在一个合法切分点 j 即置 True。", "weight": 25},
            {"dimension": "corner_case", "title": "dp[0] = True 奠定空串拆分", "detail": "防守点：空串默认可拆，确保整个词正好在字典中时（j=0）能转移成功。", "weight": 25},
            {"dimension": "solution", "title": "命中提前 break 剪枝手写", "detail": "手写点：一旦发现 dp[i] 为 True 立即 break，显著提升大用例运行速度。", "weight": 25},
            {"dimension": "complexity", "title": "最长词长截断剪枝口述", "detail": "演练点：口述若记录字典中最大单词长度 max_len，可将内层循环缩短至 i-max_len 到 i。", "weight": 25}
        ]
    },
    {
        "frontend_id": 300,
        "title_cn": "最长递增子序列",
        "title_en": "Longest Increasing Subsequence",
        "slug": "longest-increasing-subsequence",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "贪心 + 二分查找（耐心排序 Patience Sort）：维护一个数组 `tails`，`tails[k]` 表示长度为 k+1 的递增子序列的末尾元素的最小值。遍历 nums，用二分查找定位当前数字在 tails 中的插入位置：若在末尾则扩展长度，否则替换较小的末尾以增强后效潜力。",
            "traps": "tails 数组本身并不一定是最终的最长递增子序列！但它的长度严格等于最长子序列长度。",
            "time_complexity": "O(N log N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for x in nums:
            # 二分查找第一个 >= x 的位置
            left, right = 0, len(tails) - 1
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(tails):
                tails.append(x)
            else:
                tails[left] = x
        return len(tails)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "贪心压低末尾潜力与二分插入", "detail": "破题眼：同样长度的上升子序列，结尾数字越小越利于后续接龙，tails 数组严格递增。", "weight": 25},
            {"dimension": "corner_case", "title": "严格递增替换同值元素", "detail": "防守点：寻找 >= x 的位置替换，确保严格大于；新数最大时 left == len(tails) 追加。", "weight": 25},
            {"dimension": "solution", "title": "手写二分结合 tails 数组", "detail": "手写点：不依赖 bisect 库，纯手撕二分插入点定位，展示扎实功底。", "weight": 25},
            {"dimension": "complexity", "title": "O(N^2) 基础 DP 与 O(N log N) 进阶对比", "detail": "演练点：口述传统 dp[i] = max(dp[j]) + 1 的 O(N^2) 逻辑，并说明二分优化的必然性。", "weight": 25}
        ]
    },
    {
        "frontend_id": 152,
        "title_cn": "乘积最大子数组",
        "title_en": "Maximum Product Subarray",
        "slug": "maximum-product-subarray",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "双状态机滚动维护正负极值：负负得正，所以负数乘以原本的极小值可能反转为极大值。同时维护两个滚动变量：以当前元素结尾的最大乘积 `curr_max` 和最小乘积 `curr_min`。遇到负数时先交换两者。",
            "traps": "遇到负数时 `curr_max` 与 `curr_min` 必须先交换；或者同时计算出 `(num, num*curr_max, num*curr_min)` 再取 max 和 min。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        for x in nums[1:]:
            if x < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(x, curr_max * x)
            curr_min = min(x, curr_min * x)
            res = max(res, curr_max)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "负负得正双状态协同滚动", "detail": "破题眼：符号翻转机制，前序最小负值是潜在最大正值之母，维持双轨 DP。", "weight": 25},
            {"dimension": "corner_case", "title": "x < 0 触发极值颠倒", "detail": "防守点：遇到负数先做 curr_max, curr_min = curr_min, curr_max 交换，防止覆盖。", "weight": 25},
            {"dimension": "solution", "title": "6 行紧凑状态压缩手写", "detail": "手写点：从第二个元素开始迭代，全局最大值动态吃进每个阶段的 curr_max。", "weight": 25},
            {"dimension": "complexity", "title": "包含零时的重置效应", "detail": "演练点：口述当遇到 0 时，max(0, 0) 使连乘断裂重置，完全符合连续子数组定义。", "weight": 25}
        ]
    },
    {
        "frontend_id": 416,
        "title_cn": "分割等和子集",
        "title_en": "Partition Equal Subset Sum",
        "slug": "partition-equal-subset-sum",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "0-1 背包可达性问题：数组总和为 sum。若 sum 为奇数直接 False。转化为：能否从数组中挑出若干个数，其和恰好等于 `target = sum // 2`。一维布尔 DP，倒序遍历容量防重复选择：`dp[j] = dp[j] or dp[j - num]`。",
            "traps": "内层循环容量 j 必须从 target 倒序遍历到 num，正序遍历会导致同一个元素被选择多次（退化为完全背包）。",
            "time_complexity": "O(N * Target)",
            "space_complexity": "O(Target)",
            "code_python": '''class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True
        return dp[target]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "等和切分等价于 0-1 背包凑数", "detail": "破题眼：总和的一半即为背包目标，每个数字只能用一次，标准 0-1 背包模型。", "weight": 25},
            {"dimension": "corner_case", "title": "奇数和快速剪枝", "detail": "防守点：total % 2 != 0 必然无法平分成两个整数子集，一行提前返回。", "weight": 25},
            {"dimension": "solution", "title": "倒序遍历一维数组手写", "detail": "手写点：range(target, num - 1, -1) 倒序遍历，防多重使用，发现 dp[target] 早停。", "weight": 25},
            {"dimension": "complexity", "title": "位运算 bitset 极致秒杀口述", "detail": "演练点：口述如何用 Python 大整数 bits |= (bits << num) 2 行代码实现位运算秒解。", "weight": 25}
        ]
    },
    {
        "frontend_id": 32,
        "title_cn": "最长有效括号",
        "title_en": "Longest Valid Parentheses",
        "slug": "longest-valid-parentheses",
        "difficulty": "Hard",
        "category": "动态规划",
        "day": 6,
        "solution": {
            "core_insight": "栈底存最后未匹配右括号下标：栈底初始化为 -1 作为基准。遇到 '(' 将其下标入栈；遇到 ')' 弹出栈顶。若栈为空，说明当前右括号无法匹配，将当前下标压入作为新的基准；若栈非空，计算长度 `i - stack[-1]` 更新最大值。",
            "traps": "初始压入 -1 极其重要，这样遇到首个有效括号对时（如索引 0 和 1），1 - (-1) = 2 计算出的长度才正确。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 新的无效截断点
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "栈底基准线定位连续有效段", "detail": "破题眼：栈中始终保留最后一次未匹配右括号的下标，充当有效子串的左护栏。", "weight": 25},
            {"dimension": "corner_case", "title": "栈底初始 -1 守护首端", "detail": "防守点：stack = [-1] 让从下标 0 开始的合法段能够被 i - (-1) 正常结算。", "weight": 25},
            {"dimension": "solution", "title": "栈判空转变为新哨兵手写", "detail": "手写点：pop 后 if not stack: append(i) 角色转换极具美感。", "weight": 25},
            {"dimension": "complexity", "title": "左右双向贪心计数 O(1) 空间口述", "detail": "演练点：口述正反两次遍历统计 left/right 括号个数实现 O(1) 空间解法的思路。", "weight": 25}
        ]
    }
]
