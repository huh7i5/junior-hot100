DAY_7_PROBLEMS = [
    {
        "frontend_id": 62,
        "title_cn": "不同路径",
        "title_en": "Unique Paths",
        "slug": "unique-paths",
        "difficulty": "Medium",
        "category": "多维动态规划",
        "day": 7,
        "solution": {
            "core_insight": "网格走格子状态转移：只能向右或向下，`dp[i][j] = dp[i-1][j] + dp[i][j-1]`。可用一维数组滚动压缩：`dp[j] += dp[j-1]`。初始化全 1。",
            "traps": "首行和首列只有一种走法（全直走），因此初始化为全 1。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "网格加法原理与行压缩", "detail": "破题眼：任何格子的路径数等于左侧与上方之和，压缩为一维 dp[j] += dp[j-1]。", "weight": 25},
            {"dimension": "corner_case", "title": "m=1 或 n=1 单行单列", "detail": "防守点：单行或单列只有 1 种走法，dp = [1]*n 直接返回 1。", "weight": 25},
            {"dimension": "solution", "title": "4 行极致空间压缩手写", "detail": "手写点：极其优美的双层循环，无二维数组开辟开销。", "weight": 25},
            {"dimension": "complexity", "title": "组合数学公式 C(m+n-2, m-1) 口述", "detail": "演练点：口述总步数 m+n-2 中挑选 m-1 步向下，直接用数学组合数 O(M) 求解。", "weight": 25}
        ]
    },
    {
        "frontend_id": 64,
        "title_cn": "最小路径和",
        "title_en": "Minimum Path Sum",
        "slug": "minimum-path-sum",
        "difficulty": "Medium",
        "category": "多维动态规划",
        "day": 7,
        "solution": {
            "core_insight": "原地修改 DP：每个格子最小路径和 `grid[i][j] += min(grid[i-1][j], grid[i][j-1])`。第一行累加前序左侧，第一列累加前序上方。空间复杂度 O(1)。",
            "traps": "第 0 行和第 0 列分别只有一条来路，需要先单独累加初始化。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "网格局部择优与原地覆盖", "detail": "破题眼：只依赖左方与上方更小的前驱累加当前格子值，复用原矩阵做到 O(1) 空间。", "weight": 25},
            {"dimension": "corner_case", "title": "首行首列前缀和累加防守", "detail": "防守点：第 0 行只能从左来，第 0 列只能从上来，前置双循环初始化边界。", "weight": 25},
            {"dimension": "solution", "title": "原地累加流式手写", "detail": "手写点：结构清晰分为边界前缀与内部双重选小，优雅紧凑。", "weight": 25},
            {"dimension": "complexity", "title": "不能原地修改时的滚动数组口述", "detail": "演练点：口述若面试官要求不污染入参 grid，如何开辟长度为 n 的数组滚动计算。", "weight": 25}
        ]
    },
    {
        "frontend_id": 5,
        "title_cn": "最长回文子串",
        "title_en": "Longest Palindromic Substring",
        "slug": "longest-palindromic-substring",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 7,
        "solution": {
            "core_insight": "中心扩展算法：回文中心可能是一个字符（奇数回文）或两个字符（偶数回文）。枚举 2n-1 个可能的中心，向两边双指针扩散比较，维护最长子串的起始位置与长度。空间 O(1)。",
            "traps": "扩散停止时左边界多减了 1，右边界多加了 1，因此子串实际为 `s[l+1 : r]`，长度为 `r - l - 1`。",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
            
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        res = ""
        for i in range(len(s)):
            # 奇数扩展
            sub1 = expand(i, i)
            # 偶数扩展
            sub2 = expand(i, i + 1)
            res = max(res, sub1, sub2, key=len)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "中心双向扩展法", "detail": "破题眼：每个字符或字符间隙向两翼扩散，比二维 DP 节省空间，编码极其简短。", "weight": 25},
            {"dimension": "corner_case", "title": "越界恢复切片 s[left+1:right]", "detail": "防守点：while 退出时 left 和 right 均已跨越合法边界，切片必须从 left+1 开始。", "weight": 25},
            {"dimension": "solution", "title": "expand 辅函数优雅调用手写", "detail": "手写点：奇偶两次 expand，用 max(res, sub1, sub2, key=len) 优雅更新。", "weight": 25},
            {"dimension": "complexity", "title": "Manacher 算法 (马拉车) O(N) 口述", "detail": "演练点：口述如何利用回文对称性与最大回文右边界臂长加速达到严格 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 1143,
        "title_cn": "最长公共子序列",
        "title_en": "Longest Common Subsequence",
        "slug": "longest-common-subsequence",
        "difficulty": "Medium",
        "category": "多维动态规划",
        "day": 7,
        "solution": {
            "core_insight": "双序列匹配二维 DP：`dp[i][j]` 表示 `text1[:i]` 与 `text2[:j]` 的 LCS 长度。若 `text1[i-1] == text2[j-1]`，则 `dp[i][j] = dp[i-1][j-1] + 1`；否则继承两者的较大值 `max(dp[i-1][j], dp[i][j-1])`。",
            "traps": "dp 数组长宽为 `(m+1) * (n+1)`，字符索引注意对齐到 `i-1` 和 `j-1`。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(M * N) 或滚动优化为 O(N)",
            "code_python": '''class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "双序列末尾匹配状态转移", "detail": "破题眼：字符相同对角线转移加一，字符相异取上方与左方较大值继承。", "weight": 25},
            {"dimension": "corner_case", "title": "空前缀补零多开一行一列", "detail": "防守点：开辟 (m+1)*(n+1) 规避复杂判断，字符下标严格取 text[i-1]。", "weight": 25},
            {"dimension": "solution", "title": "经典双序列 LCS 模板手写", "detail": "手写点：10 行标准状态转移，双层嵌套循环流畅自如。", "weight": 25},
            {"dimension": "complexity", "title": "滚动数组单行压缩演练", "detail": "演练点：口述如何用 pre 变量暂存左上角 dp[i-1][j-1] 将空间压缩至 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 72,
        "title_cn": "编辑距离",
        "title_en": "Edit Distance",
        "slug": "edit-distance",
        "difficulty": "Hard",
        "category": "多维动态规划",
        "day": 7,
        "solution": {
            "core_insight": "字符串编辑经典三操作 DP：`dp[i][j]` 表示从 `word1[:i]` 转为 `word2[:j]` 的最少操作数。若字符相同，`dp[i][j] = dp[i-1][j-1]`；若不同，可在插入 `dp[i][j-1]`、删除 `dp[i-1][j]`、替换 `dp[i-1][j-1]` 中取最小值加 1。",
            "traps": "第一行第一列的初始化表示插入或删除所有字符，`dp[i][0] = i`，`dp[0][j] = j`。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(M * N)",
            "code_python": '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "插入/删除/替换三项几何对应", "detail": "破题眼：左方对应插入、上方对应删除、左上方对应替换，三选一取极小。", "weight": 25},
            {"dimension": "corner_case", "title": "空串转换代价初始化", "detail": "防守点：dp[i][0] = i（全删）与 dp[0][j] = j（全插）严密构建基础网格。", "weight": 25},
            {"dimension": "solution", "title": "Hard 级双串 DP 稳健手写", "detail": "手写点：字符相同直接等于对角线，无需加 1；字符不同 min 三项加 1。", "weight": 25},
            {"dimension": "complexity", "title": "NLP 文本相似度工业应用口述", "detail": "演练点：口述 Levenshtein 距离在拼写纠错、基因序列比对、模糊匹配中的落地。", "weight": 25}
        ]
    },
    {
        "frontend_id": 136,
        "title_cn": "只出现一次的数字",
        "title_en": "Single Number",
        "slug": "single-number",
        "difficulty": "Easy",
        "category": "位运算",
        "day": 7,
        "solution": {
            "core_insight": "异或运算三大特性：1. `a ^ 0 = a`；2. `a ^ a = 0`；3. 满足交换律与结合律。所有成对出现的数字异或后全部抵消为 0，最后剩下的就是那个唯一的单身数字。",
            "traps": "纯位运算 O(1) 空间，不需要哈希表或额外集合。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "异或自反性与消消乐", "detail": "破题眼：x ^ x = 0，成对出现的数字无视遍历先后顺序全部抵消成 0。", "weight": 25},
            {"dimension": "corner_case", "title": "初始值 res = 0 恒等性", "detail": "防守点：0 ^ a = a，以 0 为初始基底累积异或，无任何副作用。", "weight": 25},
            {"dimension": "solution", "title": "4 行极简手写", "detail": "手写点：单变量遍历异或，代码干净到无可挑剔。", "weight": 25},
            {"dimension": "complexity", "title": "只出现一次 II（三进制位运算）口述", "detail": "演练点：口述如果其余数字出现三次（137 题）如何用位运算状态机或统计每位模 3。", "weight": 25}
        ]
    },
    {
        "frontend_id": 169,
        "title_cn": "多数元素",
        "title_en": "Majority Element",
        "slug": "majority-element",
        "difficulty": "Easy",
        "category": "摩尔投票",
        "day": 7,
        "solution": {
            "core_insight": "Boyer-Moore 摩尔投票算法（对拼消耗）：维护候选人 candidate 和票数 count。遍历数组，若 count 为 0，更换当前数字为 candidate；若当前数等于 candidate 则 count + 1，否则 count - 1。多数元素占比 > 1/2，必定战至最后。",
            "traps": "题目明确保证多数元素一定存在，因此无需二次遍历确认票数是否过半。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "一换一对拼同归于尽", "detail": "破题眼：占比严格大于一半，无论如何两两抵消，最终胜出的必定是多数元素。", "weight": 25},
            {"dimension": "corner_case", "title": "count 归零触发换届选举", "detail": "防守点：count == 0 时无条件换人，重新确立候选人身份。", "weight": 25},
            {"dimension": "solution", "title": "纯 O(1) 空间摩尔投票手写", "detail": "手写点：双变量协同，1 赋值 -1 减法，极其精妙。", "weight": 25},
            {"dimension": "complexity", "title": "出现次数超过 N/3（229 题）双候选人扩展", "detail": "演练点：口述如何维护两个候选人与两个 count 解决超过 1/3 多数元素的推广问题。", "weight": 25}
        ]
    },
    {
        "frontend_id": 75,
        "title_cn": "颜色分类",
        "title_en": "Sort Colors",
        "slug": "sort-colors",
        "difficulty": "Medium",
        "category": "双指针",
        "day": 7,
        "solution": {
            "core_insight": "荷兰国旗问题（三路划分）：维护三个指针 p0（0 的右边界）、p2（2 的左边界）、curr。curr 遇到 0，与 p0 交换，p0 和 curr 均加 1；遇到 2，与 p2 交换，p2 减 1（注意：curr 不能加 1，因为换过来的元素尚未校验）；遇到 1，curr 加 1。",
            "traps": "与 p2 交换后 curr 不能自增！因为从后面换过来的数字可能是 0 或 2，必须在下一轮继续检查处理。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def sortColors(self, nums: list[int]) -> None:
        p0 = 0
        curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "荷兰国旗三路切分指针划分", "detail": "破题眼：[0, p0) 为 0，[p0, curr) 为 1，(p2, n-1] 为 2，中间为未探测区。", "weight": 25},
            {"dimension": "corner_case", "title": "与 p2 交换后 curr 不前移死穴", "detail": "防守点：换过来未经审阅的值不能盲目越过，curr 必须停在原地继续审阅。", "weight": 25},
            {"dimension": "solution", "title": "while curr <= p2 边界手写", "detail": "手写点：循环出口为 curr <= p2，p0/curr/p2 三指针职责分明。", "weight": 25},
            {"dimension": "complexity", "title": "快速排序三路切分扩展口述", "detail": "演练点：口述如何将该思想移植到快排的 3-way partition 解决大量重复元素退化问题。", "weight": 25}
        ]
    },
    {
        "frontend_id": 31,
        "title_cn": "下一个排列",
        "title_en": "Next Permutation",
        "slug": "next-permutation",
        "difficulty": "Medium",
        "category": "数组",
        "day": 7,
        "solution": {
            "core_insight": "字典序增幅最小算法：1. 从后向前找到第一个破坏升序的降序对 `nums[i] < nums[i+1]`；2. 从后向前找到第一个 `nums[j] > nums[i]`，交换 `nums[i]` 与 `nums[j]`；3. 将 `i+1` 之后的后缀逆序反转（恢复最小升序）。若找不到 i，则说明是全逆序，直接翻转整个数组。",
            "traps": "第 2 步找的是严格大于 `nums[i]` 的最小较大数；第 3 步是反转而不是排序，因为后缀在交换前后依然保持严格降序，反转即可变为升序。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        # 1. 寻找较小数 i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # 2. 寻找较大数 j 并交换
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        # 3. 反转 i + 1 之后的后缀
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "寻找最小步幅增量三部曲", "detail": "破题眼：倒找逆序点 -> 倒找稍大数交换 -> 后缀双指针反转降序变升序。", "weight": 25},
            {"dimension": "corner_case", "title": "最大排列转最小（321 -> 123）", "detail": "防守点：i 减到 -1 时跳过第 2 步，直接反转全数组回到字典序最小，自然循环。", "weight": 25},
            {"dimension": "solution", "title": "纯双指针三段式原地手写", "detail": "手写点：逻辑清晰划分为三个 while 阶段，无额外开辟数组，原地 O(1) 空间。", "weight": 25},
            {"dimension": "complexity", "title": "为什么后缀直接反转而不是排序", "detail": "演练点：口述后缀原本是单调递减的，交换后单调性不变，双指针反转仅需 O(N) 即可升序。", "weight": 25}
        ]
    },
    {
        "frontend_id": 287,
        "title_cn": "寻找重复数",
        "title_en": "Find the Duplicate Number",
        "slug": "find-the-duplicate-number",
        "difficulty": "Medium",
        "category": "链表",
        "day": 7,
        "solution": {
            "core_insight": "数组下标跳转映射链表判圈（Floyd 龟兔赛跑）：将数组值视为链表指针 `next = nums[i]`。因为数字都在 `[1, n]` 之间，下标 0 绝不入环。两个相同的数字意味着有两个指针指向同一个节点，即链表存在环。重复数就是入环点！",
            "traps": "题目要求：不能修改数组、只能使用 O(1) 额外空间，因此不能用排序或哈希表或标记负数。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # 阶段一：快慢指针找相遇点
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        # 阶段二：寻找环的入口
        p = 0
        while p != slow:
            p = nums[p]
            slow = nums[slow]
        return p
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "数组隐式链表与环入口映射", "detail": "破题眼：下标到数值的映射构造有向图，入度 >= 2 的节点对应重复数字即为环入口。", "weight": 25},
            {"dimension": "corner_case", "title": "0 作为链表虚拟头节点", "detail": "防守点：数字取值 1 到 n，下标 0 没有入度，从 0 起步确保慢指针能安全入环。", "weight": 25},
            {"dimension": "solution", "title": "两阶段快慢指针手写", "detail": "手写点：严格遵循 142 题数学推导，相遇后 p 从 0 启动，与 slow 单步碰头。", "weight": 25},
            {"dimension": "complexity", "title": "二分查找抽屉原理替代方案口述", "detail": "演练点：口述值域二分法（统计 <= mid 的数字个数）达到 O(N log N) 时间与 O(1) 空间。", "weight": 25}
        ]
    }
]
