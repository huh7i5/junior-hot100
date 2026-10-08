DAY_4_PROBLEMS = [
    {
        "frontend_id": 46,
        "title_cn": "全排列",
        "title_en": "Permutations",
        "slug": "permutations",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "经典回溯：维护已使用元素的 visited 集合或布尔数组。每次从未选元素中挑一个加入 path，递归下一层；回溯时弹出 path 末尾并恢复 visited 状态。",
            "traps": "添加进结果列表时必须使用 `path[:]` 进行浅拷贝，否则后续回溯会把结果里的列表全清空为 `[]`。",
            "time_complexity": "O(N * N!)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False
                    
        backtrack()
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "回溯决策树与状态还原", "detail": "破题眼：做选择 -> 递归下探 -> 撤销选择。三位一体形成标准回溯模版。", "weight": 25},
            {"dimension": "corner_case", "title": "path[:] 浅拷贝引用死穴", "detail": "防守点：牢记 Python 列表对象引用机制，收集结果务必复制切片 path[:]。", "weight": 25},
            {"dimension": "solution", "title": "布尔标记数组手写", "detail": "手写点：使用 used 数组实现 O(1) 去重选择，结构清晰。", "weight": 25},
            {"dimension": "complexity", "title": "原地交换法省空间口述", "detail": "演练点：口述如何通过 nums[first], nums[i] 原地交换省略 used 数组与 path 空间。", "weight": 25}
        ]
    },
    {
        "frontend_id": 78,
        "title_cn": "子集",
        "title_en": "Subsets",
        "slug": "subsets",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "组合类回溯（无重复元素）：用 start 变量控制搜索起始位置，防止出现重复组合。每个节点都是一个合法子集，一进入 backtrack 就将 `path[:]` 存入结果。",
            "traps": "不需要判断 `len(path) == len(nums)` 才添加，树的所有节点都是子集，一进递归直接 `res.append(path[:])`。",
            "time_complexity": "O(N * 2^N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "节点即结果与起始指针推进", "detail": "破题眼：区别于排列题，子集是所有递归节点的集合；start 指针避免回头产生重复项。", "weight": 25},
            {"dimension": "corner_case", "title": "包含空集与自身", "detail": "防守点：初始调用 backtrack(0) 时先入空集 []，递归到底入全集，天然全覆盖。", "weight": 25},
            {"dimension": "solution", "title": "10 行极简递归手写", "detail": "手写点：优雅的 start 推进，进入即记录，极其精炼。", "weight": 25},
            {"dimension": "complexity", "title": "二进制位掩码映射法口述", "detail": "演练点：口述 0 到 2^N-1 的二进制掩码解法，分析时空为严格 O(N * 2^N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 17,
        "title_cn": "电话号码的字母组合",
        "title_en": "Letter Combinations of a Phone Number",
        "slug": "letter-combinations-of-a-phone-number",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "多叉树递归：维护数字到字母的映射表。递归参数 index 代表当前处理到的数字下标。当 index == len(digits) 时收集路径字符串。",
            "traps": "输入为空字符串 `\"\"` 时必须返回空列表 `[]`，不能返回 `[\"\"]`。",
            "time_complexity": "O(3^M * 4^N)",
            "space_complexity": "O(M + N)",
            "code_python": '''class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        path = []
        def backtrack(index):
            if index == len(digits):
                res.append("".join(path))
                return
            for ch in phone_map[digits[index]]:
                path.append(ch)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "多集合笛卡尔积递归遍历", "detail": "破题眼：层级对应 digits 的第 index 位，每层分支为对应按键所有候选字母。", "weight": 25},
            {"dimension": "corner_case", "title": "空串特判早退", "detail": "防守点：if not digits: return [] 防止返回 [\"\"] 造成错误判题。", "weight": 25},
            {"dimension": "solution", "title": "字符拼接与回溯手写", "detail": "手写点：使用 path 列表维护路径，触底时 \"\".join(path) 收集。", "weight": 25},
            {"dimension": "complexity", "title": "队列 BFS 迭代替代方案口述", "detail": "演练点：口述如何利用队列从 [\"\"] 开始逐个字母轮转扩展生成笛卡尔积。", "weight": 25}
        ]
    },
    {
        "frontend_id": 39,
        "title_cn": "组合总和",
        "title_en": "Combination Sum",
        "slug": "combination-sum",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "可重复选择元素的组合回溯：先对数组升序排序以支持剪枝。递归传递当前的 remain 余额。在循环中若 candidate > remain 直接 break 剪枝；下一次递归仍然传入 `i`（因为当前元素可复用）。",
            "traps": "递归时调用 `backtrack(remain - candidates[i], i)`，而不是 `i + 1`，这样实现无限复用当前元素且不出现逆向重复。",
            "time_complexity": "O(N * 2^target)",
            "space_complexity": "O(target / min(candidates))",
            "code_python": '''class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []
        def backtrack(remain, start):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], i)
                path.pop()
        backtrack(target, 0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "元素复用与排序提前剪枝", "detail": "破题眼：candidates.sort() 使其有序，candidates[i] > remain 直接 break 截断整棵子树。", "weight": 25},
            {"dimension": "corner_case", "title": "复用同一元素索引保持 i", "detail": "防守点：下一层传 i 而非 i+1 允许重复使用自己，传 start 杜绝选回头元素导致的无序重复。", "weight": 25},
            {"dimension": "solution", "title": "减法替代加法清爽手写", "detail": "手写点：传 remain 递减到 0 代替维护 current_sum，代码更精炼省事。", "weight": 25},
            {"dimension": "complexity", "title": "与 40 题（含重复且每数限用一次）对比", "detail": "演练点：口述 40 题如何通过 candidates[i] == candidates[i-1] 树层去重。", "weight": 25}
        ]
    },
    {
        "frontend_id": 22,
        "title_cn": "括号生成",
        "title_en": "Generate Parentheses",
        "slug": "generate-parentheses",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "左括号只要没超过 n 就可以放；右括号只要数量小于当前已放的左括号数量就可以放。任何时刻都不可能出现非法括号闭合，无需事后校验合法性。",
            "traps": "千万不要全部生成 2n 个括号后再用栈检查合法性，那样时间复杂度高达 2^(2n)，必须在递归入口剪枝合法性。",
            "time_complexity": "O(4^N / sqrt(N)) 卡特兰数",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []
        def backtrack(left, right):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()
        backtrack(0, 0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "左右配额约束剪枝", "detail": "破题眼：left < n 随时可加左括号，right < left 才可加右括号，边走边防守。", "weight": 25},
            {"dimension": "corner_case", "title": "终止条件 2n 严格对齐", "detail": "防守点：len(path) == 2 * n 时必定是一个且唯一合法的闭合括号串。", "weight": 25},
            {"dimension": "solution", "title": "无废支回溯高分模板手写", "detail": "手写点：双 if 并列结构，不生成任何一条死胡同路径。", "weight": 25},
            {"dimension": "complexity", "title": "卡特兰数 (Catalan Number) 口述", "detail": "演练点：向面试官流利说出答案数量等于第 n 个卡特兰数 C(2n, n)/(n+1)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 79,
        "title_cn": "单词搜索",
        "title_en": "Word Search",
        "slug": "word-search",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "网格图回溯 DFS：遍历每个格子作为起点。DFS 匹配当前字符，匹配成功后将当前格子暂改为空字符 '#' 防止重复访问，向四周探索匹配下一字符，最后回溯恢复原字符。",
            "traps": "离开该分支时必须将当前字符恢复！因为在另一个起点的探索中该格子可能依然可以使用。",
            "time_complexity": "O(M * N * 3^L)",
            "space_complexity": "O(L) 递归深度",
            "code_python": '''class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False
            temp = board[r][c]
            board[r][c] = '#'  # 标记已访问
            found = (dfs(r + 1, c, k + 1) or
                     dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or
                     dfs(r, c - 1, k + 1))
            board[r][c] = temp  # 回溯恢复
            return found
            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "原地修改状态与回溯恢复", "detail": "破题眼：board[r][c] = '#' 原地占坑省 visited 空间，退出时还原原字符。", "weight": 25},
            {"dimension": "corner_case", "title": "长度命中早停 k == len(word)", "detail": "防守点：k == len(word) 优先判断置顶返回 True，防止越界读 word。", "weight": 25},
            {"dimension": "solution", "title": "短路四方向或逻辑手写", "detail": "手写点：使用 found = dfs or dfs or ... 短路逻辑，一旦找到立即终止后续探索。", "weight": 25},
            {"dimension": "complexity", "title": "词频倒转剪枝高级技巧", "detail": "演练点：口述若 word 首字符在 board 中出现次数远大于尾字符，可反转 word 降低搜索树大小。", "weight": 25}
        ]
    },
    {
        "frontend_id": 131,
        "title_cn": "分割回文串",
        "title_en": "Palindrome Partitioning",
        "slug": "palindrome-partitioning",
        "difficulty": "Medium",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "回溯切分：从 start 开始枚举切分点 i。若 `s[start:i+1]` 是回文串，则将该子串加入 path，并递归切分剩余串 `backtrack(i + 1)`。回文检测可用双指针或 DP 预处理。",
            "traps": "切片是左闭右闭子串 `s[start:i+1]`，下一次递归传入的是 `i + 1`。",
            "time_complexity": "O(N * 2^N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        n = len(s)
        
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            for i in range(start, n):
                if is_palindrome(start, i):
                    path.append(s[start:i + 1])
                    backtrack(i + 1)
                    path.pop()
                    
        backtrack(0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "前缀回文判定与后缀递归切分", "detail": "破题眼：逐位切出前缀，只要前缀是回文就深入切分后缀，树形回溯展开。", "weight": 25},
            {"dimension": "corner_case", "title": "单字符天生回文与触底", "detail": "防守点：start == n 说明全字符串被合法分割成各次回文子串，收集结果。", "weight": 25},
            {"dimension": "solution", "title": "双指针辅函数嵌入回溯手写", "detail": "手写点：is_palindrome 双指针极简校验，整体递归逻辑一目了然。", "weight": 25},
            {"dimension": "complexity", "title": "DP 预处理 O(1) 回文查询扩展", "detail": "演练点：口述如何用二维 DP 表预处理 dp[i][j] 让回文判定从 O(N) 降为 O(1)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 51,
        "title_cn": "N 皇后",
        "title_en": "N-Queens",
        "slug": "n-queens",
        "difficulty": "Hard",
        "category": "回溯",
        "day": 4,
        "solution": {
            "core_insight": "逐行放置 + 三重集合剪枝：每行必须且只能放一个皇后。用三个集合记录已被占领的列 `cols`、主对角线 `diag1 (r - c)`、副对角线 `diag2 (r + c)`。枚举当前行的每一列，若不冲突则放置并递归下一行。",
            "traps": "同一主对角线上的坐标差 `r - c` 为定值；同一副对角线上的坐标和 `r + c` 为定值。",
            "time_complexity": "O(N!)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        queens = [-1] * n  # queens[r] = c
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        
        def backtrack(r):
            if r == n:
                board = []
                for c in queens:
                    row_str = '.' * c + 'Q' + '.' * (n - c - 1)
                    board.append(row_str)
                res.append(board)
                return
            for c in range(n):
                if c not in cols and (r - c) not in diag1 and (r + c) not in diag2:
                    queens[r] = c
                    cols.add(c)
                    diag1.add(r - c)
                    diag2.add(r + c)
                    backtrack(r + 1)
                    cols.remove(c)
                    diag1.remove(r - c)
                    diag2.remove(r + c)
                    
        backtrack(0)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "对角线数学不变量常数级剪枝", "detail": "破题眼：利用 r-c 和 r+c 的数学恒等性，用 set 实现 O(1) 冲突校验。", "weight": 25},
            {"dimension": "corner_case", "title": "回溯三重集合严格同步移除", "detail": "防守点：add 了三项必须在递归返回后 remove 三项，漏一个导致全盘死锁。", "weight": 25},
            {"dimension": "solution", "title": "一维 queens 数组转换棋盘手写", "detail": "手写点：queens[r] = c 维护每行皇后列号，触底时优雅生成点阵字符串。", "weight": 25},
            {"dimension": "complexity", "title": "位运算优化超高频面试加分项", "detail": "演练点：口述如何用三个整数的位掩码 (cols, diag1, diag2) 极致压榨运算性能。", "weight": 25}
        ]
    },
    {
        "frontend_id": 35,
        "title_cn": "搜索插入位置",
        "title_en": "Search Insert Position",
        "slug": "search-insert-position",
        "difficulty": "Easy",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "寻找第一个 >= target 的位置（lower_bound）。左闭右闭区间 `[left, right]`：若 `nums[mid] >= target`，答案在左半部分 `right = mid - 1`；否则 `left = mid + 1`。最终返回 `left`。",
            "traps": "循环结束时 left 即为应插入的正确索引，甚至当 target 大于所有元素时 left 正好等于 n。",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "二分查找 lower_bound 模板", "detail": "破题眼：找第一个大于等于 target 的下标，left <= right 终止时 left 必定是插入点。", "weight": 25},
            {"dimension": "corner_case", "title": "插在最左端与最右端", "detail": "防守点：target 比所有数小返回 0；比所有数大返回 len(nums)，统一自洽。", "weight": 25},
            {"dimension": "solution", "title": "6 行双闭区间无脑默写", "detail": "手写点：极其稳健的二分标杆，拒绝循环内 return mid，统一出口在 return left。", "weight": 25},
            {"dimension": "complexity", "title": "溢出防范与时空演练", "detail": "演练点：口述 (left + right) // 2 在 Java/C++ 中用 left + (right - left) // 2 防溢出。", "weight": 25}
        ]
    },
    {
        "frontend_id": 74,
        "title_cn": "搜索二维矩阵",
        "title_en": "Search a 2D Matrix",
        "slug": "search-a-2d-matrix",
        "difficulty": "Medium",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "二维变一维经典二分：整个矩阵严格单调递增，可视为长度为 `M * N` 的有序一维数组。虚拟索引 mid 对应的矩阵元素为 `matrix[mid // n][mid % n]`。",
            "traps": "不要做两次二分（先搜行再搜列），一次一维二分即可完成，代码极简且时间复杂度最优。",
            "time_complexity": "O(log(M * N))",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "行列解构映射一维二分", "detail": "破题眼：row = mid // n, col = mid % n，将全局有序矩阵直接虚拟展平成一维。", "weight": 25},
            {"dimension": "corner_case", "title": "单行单列退化情形", "detail": "防守点：空矩阵保护；m=1 或 n=1 时模运算与整除运算依旧严格正确。", "weight": 25},
            {"dimension": "solution", "title": "无缝标准二分手写", "detail": "手写点：10 行内标准二分模板，一次性准确写出坐标换算。", "weight": 25},
            {"dimension": "complexity", "title": "与 240 题（每行每列各自有序）界限区分", "detail": "演练点：口述本题全局有序可用一维二分，240 题局部有序需从右上角 BST 搜索。", "weight": 25}
        ]
    },
    {
        "frontend_id": 34,
        "title_cn": "在排序数组中查找元素的第一个和最后一个位置",
        "title_en": "Find First and Last Position of Element in Sorted Array",
        "slug": "find-first-and-last-position-of-element-in-sorted-array",
        "difficulty": "Medium",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "复用两次二分查找：第一次找第一个 >= target 的位置（左边界），第二次找第一个 >= target + 1 的位置再减 1（右边界）。",
            "traps": "找到左边界后必须检查它是否在数组范围内并且数值确实等于 target，若不等于说明 target 不存在直接返回 [-1, -1]。",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        return [find_bound(True), find_bound(False)]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "命中后向左右侧继续挤压", "detail": "破题眼：nums[mid] == target 时不停止，记录候选值，找左界向左挤，找右界向右挤。", "weight": 25},
            {"dimension": "corner_case", "title": "目标不存在与全数组相同", "detail": "防守点：不存在时 ans 保持初始值 -1 正确返回；全数组相同时两端点覆盖 0 和 n-1。", "weight": 25},
            {"dimension": "solution", "title": "单个辅助函数复用两次手写", "detail": "手写点：提取 find_bound(is_left) 传参布尔控制收缩方向，避免写两份冗余二分。", "weight": 25},
            {"dimension": "complexity", "title": "两次对数耗时严格性证明", "detail": "演练点：口述 2 * log N 依然是严格对数时间，常数项可忽略。", "weight": 25}
        ]
    },
    {
        "frontend_id": 33,
        "title_cn": "搜索旋转排序数组",
        "title_en": "Search in Rotated Sorted Array",
        "slug": "search-in-rotated-sorted-array",
        "difficulty": "Medium",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "二分必然将数组分成一半有序、一半无序。比较 nums[mid] 与 nums[left]：若 `nums[left] <= nums[mid]`，则左半段单调递增，检查 target 是否在左半段范围内；否则右半段单调递增，检查 target 是否在右半段范围内。",
            "traps": "判定左侧有序时是 `<=` 而不能只写 `<`，因为只有两个元素时 mid 算出来等于 left。",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "局部单调断崖二分", "detail": "破题眼：旋转数组切一半必有一半完整递增，在有序半区锁定区间范围。", "weight": 25},
            {"dimension": "corner_case", "title": "nums[left] <= nums[mid] 等号陷阱", "detail": "防守点：两元素时 mid==left，必须带等号判定左半段有序，防逻辑掉进无序分支。", "weight": 25},
            {"dimension": "solution", "title": "四分支双层 if 结构手写", "detail": "手写点：准确判断 target 在有序区还是无序区，两重二选一收缩指针。", "weight": 25},
            {"dimension": "complexity", "title": "含重复元素（81 题）退化辨析", "detail": "演练点：口述若数组有重复元素（如 [1,0,1,1,1]）时无法区分哪边有序，退化为 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 153,
        "title_cn": "寻找旋转排序数组中的最小值",
        "title_en": "Find Minimum in Rotated Sorted Array",
        "slug": "find-minimum-in-rotated-sorted-array",
        "difficulty": "Medium",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "将 mid 处的数值与最右侧端点 `nums[right]` 比较：若 `nums[mid] > nums[right]`，说明断崖在右侧，最小值必在右半部分 `left = mid + 1`；否则断崖在左侧或自身就是最小值 `right = mid`。循环条件为 `left < right`，退出时 `nums[left]` 即是最小值。",
            "traps": "必须与 `nums[right]` 比，不能与 `nums[left]` 比，因为完全未旋转的递增数组会把逻辑搞混；`right = mid` 不能减 1，因为 mid 本身可能是最小值。",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "锚定右端点探测断崖", "detail": "破题眼：nums[mid] 与 nums[right] 比对，大于右端点必在右半边，否则在左半边。", "weight": 25},
            {"dimension": "corner_case", "title": "right = mid 保留潜在极小值", "detail": "防守点：mid 自身可能是波谷，不可贸然 right = mid - 1 越过解。", "weight": 25},
            {"dimension": "solution", "title": "while left < right 极简模板手写", "detail": "手写点：循环出口两指针汇合在同一个点，直接 return nums[left]。", "weight": 25},
            {"dimension": "complexity", "title": "未旋转有序数组兼容性", "detail": "演练点：口述当整个数组原本升序未旋转时，算法每轮都走 right = mid，正确收敛到 nums[0]。", "weight": 25}
        ]
    },
    {
        "frontend_id": 4,
        "title_cn": "寻找两个正序数组的中位数",
        "title_en": "Median of Two Sorted Arrays",
        "slug": "median-of-two-sorted-arrays",
        "difficulty": "Hard",
        "category": "二分查找",
        "day": 4,
        "solution": {
            "core_insight": "在较短数组上二分分割线：设短数组在 i 处切开，长数组在 j 处切开，满足左半部分总数等于右半部分（或多 1）。二分 i 直到满足 `max_left_A <= min_right_B` 且 `max_left_B <= min_right_A`。边界用无穷大/负无穷大处理。",
            "traps": "确保 A 数组长度 <= B 数组长度，否则在短数组上二分会溢出；边界点为空时用 `-inf` 和 `inf` 充当守护哨兵。",
            "time_complexity": "O(log(min(M, N)))",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = total_left - i
            
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
        return 0.0
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "短数组划分与交叉对齐", "detail": "破题眼：中位数本质是将总集合切成等长两半，在短数组二分切分点 i，j 由总长恒等推出。", "weight": 25},
            {"dimension": "corner_case", "title": "无穷大/小哨兵守卫切分边缘", "detail": "防守点：切在端点 0 或 m 时，虚拟填入 -inf/+inf，消除各种数组越界特判。", "weight": 25},
            {"dimension": "solution", "title": "Hard 级二分切分线手写", "detail": "手写点：熟练写出 total_left = (m+n+1)//2 以及奇偶分类输出，从容不迫。", "weight": 25},
            {"dimension": "complexity", "title": "第 K 小元素二分分治解法口述", "detail": "演练点：口述寻找第 K 小数字的递归排除法（每次排除 k//2 个元素），对比两种思路。", "weight": 25}
        ]
    }
]
