DAY_5_PROBLEMS = [
    {
        "frontend_id": 20,
        "title_cn": "有效的括号",
        "title_en": "Valid Parentheses",
        "slug": "valid-parentheses",
        "difficulty": "Easy",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "后进先出栈匹配：遇到左括号入栈对应的右括号；遇到右括号时若栈为空或栈顶不等于当前右括号，立即返回 False。遍历结束时栈必须恰好为空。",
            "traps": "若字符串长度为奇数直接返回 False；最后一定要 `return not stack`，不能只依赖中途没报错。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "栈顶最近匹配与后进先出", "detail": "破题眼：括号嵌套匹配天然符合 LIFO 栈模型，哈希表做左右映射字典。", "weight": 25},
            {"dimension": "corner_case", "title": "奇数长度提前剪枝与栈残留", "detail": "防守点：len(s) % 2 != 0 极速返回；return not stack 校验左括号多余场景。", "weight": 25},
            {"dimension": "solution", "title": "映射表单栈优雅手写", "detail": "手写点：10 行清晰逻辑，左括号入栈右括号弹栈比对，滴水不漏。", "weight": 25},
            {"dimension": "complexity", "title": "工程应用场景口述", "detail": "演练点：口述编译器语法解析、HTML/XML 标签闭合校验的工业界实际应用。", "weight": 25}
        ]
    },
    {
        "frontend_id": 155,
        "title_cn": "最小栈",
        "title_en": "Min Stack",
        "slug": "min-stack",
        "difficulty": "Medium",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "同步辅助栈 / 双栈法：主栈存储所有数据，辅助栈 `min_stack` 栈顶始终存储当前状态下的最小值。push 时，辅助栈压入 `min(val, min_stack[-1])`；pop 时两栈同步弹出。",
            "traps": "辅助栈初始化可放入正无穷，或者空时直接将 val 压入两栈，保证两栈高度永远完全同步。",
            "time_complexity": "所有操作 O(1)",
            "space_complexity": "O(N)",
            "code_python": '''class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "辅助栈同步快照历史极值", "detail": "破题眼：用空间换时间，辅助栈每个高度记录对应时刻的全局最小值，同步出入栈。", "weight": 25},
            {"dimension": "corner_case", "title": "空栈初始化入栈", "detail": "防守点：首个元素入栈时辅助栈为空，直接双入 val，避免对空列表取 [-1]。", "weight": 25},
            {"dimension": "solution", "title": "四方法完整手写", "detail": "手写点：push/pop/top/getMin 四方法严格遵守 O(1)，无冗余逻辑。", "weight": 25},
            {"dimension": "complexity", "title": "单栈存差值 (diff) 极限省空间法口述", "detail": "演练点：口述如何通过单栈存储 val - min_val 差值做到无需辅助栈的进阶解法。", "weight": 25}
        ]
    },
    {
        "frontend_id": 394,
        "title_cn": "字符串解码",
        "title_en": "Decode String",
        "slug": "decode-string",
        "difficulty": "Medium",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "双栈/单栈存储上下文：遇到数字累加 multi；遇到普通字符累加 res；遇到 '[' 时，将当前的 `(res, multi)` 作为一个环境元组入栈，并重置 res 和 multi；遇到 ']' 时出栈上一层的上下文，`res = last_res + last_multi * res`。",
            "traps": "数字可能有多位（如 100[a]），必须 `multi = multi * 10 + int(c)` 累加。",
            "time_complexity": "O(S) 解码后字符串总长",
            "space_complexity": "O(S)",
            "code_python": '''class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                last_str, repeat_num = stack.pop()
                curr_str = last_str + repeat_num * curr_str
            else:
                curr_str += ch
        return curr_str
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "栈保存作用域上下文", "detail": "破题眼：'[' 触发上下文压栈，']' 触发结算与拼合，完美解决多层括号嵌套递归。", "weight": 25},
            {"dimension": "corner_case", "title": "多位数解析与连续嵌套", "detail": "防守点：curr_num * 10 + int(ch) 解决多位数字；进栈后立即置空当前变量。", "weight": 25},
            {"dimension": "solution", "title": "四分支清晰循环手写", "detail": "手写点：数字、左括号、右括号、普通字符四大分支井井有条。", "weight": 25},
            {"dimension": "complexity", "title": "递归调用栈等价性演练", "detail": "演练点：口述本题将迭代栈改写为 DFS 递归函数以 '[' 为子递归入口的设计方法。", "weight": 25}
        ]
    },
    {
        "frontend_id": 739,
        "title_cn": "每日温度",
        "title_en": "Daily Temperatures",
        "slug": "daily-temperatures",
        "difficulty": "Medium",
        "category": "单调栈",
        "day": 5,
        "solution": {
            "core_insight": "单调递减栈：栈中存储元素下标。遍历温度，当当前温度大于栈顶下标对应的温度时，说明找到了栈顶元素的第一个更高温度，弹出栈顶下标 `prev_idx` 并记录天数差 `res[prev_idx] = i - prev_idx`。最后将当前下标压栈。",
            "traps": "单调栈中必须存下标而非温度值，因为题目要求返回的是天数间隔（索引差）。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # 存索引
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "下一个更大元素单调栈母题", "detail": "破题眼：寻找右侧第一个比自己大的数，利用单调递减栈遇大即弹结算。", "weight": 25},
            {"dimension": "corner_case", "title": "无法升温默认置零", "detail": "防守点：结果数组初始化为 [0]*n，留在栈中的无解元素自然为 0，无需二次处理。", "weight": 25},
            {"dimension": "solution", "title": "8 行标准单调栈手写", "detail": "手写点：单调栈最纯粹的工业标准模板，必须做到 2 分钟内 Bug-free。", "weight": 25},
            {"dimension": "complexity", "title": "摊还复杂度 O(N) 解释", "detail": "演练点：口述虽然有 while，但每个索引只入栈一次出栈一次，整体耗时为严格 2N。", "weight": 25}
        ]
    },
    {
        "frontend_id": 84,
        "title_cn": "柱状图中最大的矩形",
        "title_en": "Largest Rectangle in Histogram",
        "slug": "largest-rectangle-in-histogram",
        "difficulty": "Hard",
        "category": "单调栈",
        "day": 5,
        "solution": {
            "core_insight": "单调递增栈 + 首尾哨兵 0：以每根柱子的高度作为矩形高，需要找到左右两侧第一个比它矮的柱子确定宽度。在数组两端各添加一个 0 哨兵，保证所有柱子最后全部出栈结算。当遇到较矮柱子时，弹栈计算面积 `h * (i - stack[-1] - 1)`。",
            "traps": "首尾哨兵 0 是神来之笔：首部的 0 避免了栈为空时的繁琐边界特判；尾部的 0 强制将栈中所有剩余递增柱子弹出结算。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # 添加首尾哨兵 0
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                cur_h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, cur_h * w)
            stack.append(i)
        return max_area
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "固定高度寻找左右宽度边界", "detail": "破题眼：以当前柱为高的最大矩形受限于左右首个更矮的柱子，单调递增栈定位两界。", "weight": 25},
            {"dimension": "corner_case", "title": "首尾哨兵 0 化繁为简", "detail": "防守点：[0] + heights + [0] 消除判空与残余结算，避免边界越界与漏算。", "weight": 25},
            {"dimension": "solution", "title": "宽度计算 w = i - stack[-1] - 1 手写", "detail": "手写点：明确弹出后新的栈顶就是左边界，当前 i 就是右边界，公式精准无误。", "weight": 25},
            {"dimension": "complexity", "title": "与 85 题最大矩形升维联动演练", "detail": "演练点：口述如何将 85 题全 1 矩阵通过每行向上统计高度转化为本题的多行柱状图求解。", "weight": 25}
        ]
    },
    {
        "frontend_id": 215,
        "title_cn": "数组中的第 K 个最大元素",
        "title_en": "Kth Largest Element in an Array",
        "slug": "kth-largest-element-in-an-array",
        "difficulty": "Medium",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "1. 快速选择算法 (Quick Select)：类似快排切分，每次切分后基准点归位。若基准点索引恰好等于 target 则返回；否则只递归进入包含 target 的那一半，平均时间 O(N)。2. 容量为 k 的小顶堆，时间 O(N log K)。",
            "traps": "快速选择必须使用随机化基准 pivot，否则遇到极端单调用例会退化成 O(N^2) 超时。",
            "time_complexity": "平均 O(N)，最坏 O(N^2)",
            "space_complexity": "O(log N)",
            "code_python": '''import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target_idx = len(nums) - k
        
        def quick_select(left, right):
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            i = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            
            if i == target_idx:
                return nums[i]
            elif i < target_idx:
                return quick_select(i + 1, right)
            else:
                return quick_select(left, i - 1)
                
        return quick_select(0, len(nums) - 1)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "快速选择与单侧分治", "detail": "破题眼：快排二分治，快选单侧分治，将 T(N) = 2T(N/2) + O(N) 削减为 T(N) = T(N/2) + O(N)。", "weight": 25},
            {"dimension": "corner_case", "title": "随机主元防御最坏情况", "detail": "防守点：必须 random.randint(left, right) 随机打乱，防止升序/降序用例击穿 O(N^2)。", "weight": 25},
            {"dimension": "solution", "title": "Lomuto/Hoare 切分标准手写", "detail": "手写点：熟练手写快排单侧划分与递归重定向，无数组切片拷贝。", "weight": 25},
            {"dimension": "complexity", "title": "等比数列求和证明均摊 O(N)", "detail": "演练点：口述 N + N/2 + N/4 + ... = 2N，证明时间复杂度数学期望严格为 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 347,
        "title_cn": "前 K 个高频元素",
        "title_en": "Top K Frequent Elements",
        "slug": "top-k-frequent-elements",
        "difficulty": "Medium",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "1. 桶排序法：先用哈希表统计频次；建立长度为 N+1 的桶列表，以频次作为下标；从后向前倒序收集元素直到满 k 个，时间严格 O(N)。2. 或者容量为 k 的小顶堆 O(N log K)。",
            "traps": "桶排序的桶大小必须是 len(nums) + 1，因为单一元素最高出现频次就是全部长度 N。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        # 桶排序：下标代表频次，值为该频次的元素列表
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in counts.items():
            buckets[freq].append(val)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for val in buckets[freq]:
                res.append(val)
                if len(res) == k:
                    return res
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "频次下界与桶排序降维", "detail": "破题眼：频次上限为 N，以频次为下标放入桶，倒序扫描天然具备 O(N) 排序效果。", "weight": 25},
            {"dimension": "corner_case", "title": "多个元素同频与满额立即返回", "detail": "防守点：同频元素追加在同一个桶内，len(res) == k 时立即 return 剪枝。", "weight": 25},
            {"dimension": "solution", "title": "Counter + 桶阵列手写", "detail": "手写点：15 行内不借助优先队列，实现严格 O(N) 性能吊打库函数的解法。", "weight": 25},
            {"dimension": "complexity", "title": "小顶堆 vs 桶排序 Tradeoff 口述", "detail": "演练点：口述小顶堆 O(N log K) 适合数据流在线场景，桶排序 O(N) 适合离线批量场景。", "weight": 25}
        ]
    },
    {
        "frontend_id": 295,
        "title_cn": "数据流的中位数",
        "title_en": "Find Median from Data Stream",
        "slug": "find-median-from-data-stream",
        "difficulty": "Hard",
        "category": "栈与堆",
        "day": 5,
        "solution": {
            "core_insight": "对顶堆设计：大顶堆 `max_heap` 存较小的一半（Python 存负数），小顶堆 `min_heap` 存较大的一半。维持不变量：`len(max_heap) == len(min_heap)` 或 `len(max_heap) == len(min_heap) + 1`。中位数为大堆顶或两堆顶均值。",
            "traps": "添加新数时，先压入大顶堆，将大堆顶弹出压入小顶堆；若小堆长度超过大堆，再从小堆弹出压回大堆。这样自动维持大小分布与高度平衡。",
            "time_complexity": "addNum 为 O(log N)，findMedian 为 O(1)",
            "space_complexity": "O(N)",
            "code_python": '''import heapq

class MedianFinder:
    def __init__(self):
        # Python 默认是小顶堆，存负数模拟大顶堆
        self.max_heap = []  # 存较小半区
        self.min_heap = []  # 存较大半区

    def addNum(self, num: int) -> None:
        # 先进大顶堆，再将大顶堆最大值过桥进入小顶堆
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # 维持平衡：大顶堆元素数量始终 >= 小顶堆数量
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "大小对顶堆动态中位数平衡", "detail": "破题眼：大顶堆守左半区，小顶堆守右半区，堆顶紧紧咬住中位数分割线。", "weight": 25},
            {"dimension": "corner_case", "title": "Python 负数模拟大顶堆取反", "detail": "防守点：牢记 heapq 只有 min-heap，进大堆加负号，取大堆顶再加负号还原。", "weight": 25},
            {"dimension": "solution", "title": "过桥平衡法优雅手写", "detail": "手写点：先入 max_heap 弹给 min_heap，再视长度调配，三步确保数值严格分层。", "weight": 25},
            {"dimension": "complexity", "title": "插入对数与查询 O(1) 优势", "detail": "演练点：口述相比二分插入 O(N) 移动成本，对顶堆插入降至 O(log N)，查询为 O(1)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 121,
        "title_cn": "买卖股票的最佳时机",
        "title_en": "Best Time to Buy and Sell Stock",
        "slug": "best-time-to-buy-and-sell-stock",
        "difficulty": "Easy",
        "category": "贪心",
        "day": 5,
        "solution": {
            "core_insight": "单次遍历维护历史最低价：遍历每天的价格，动态更新截至当天的最低买入价 `min_price`。并在每天假设卖出，更新全局最大利润 `max(max_profit, price - min_price)`。",
            "traps": "利润最小为 0（不能在赔钱时卖出，不买卖即为 0）。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "历史前缀极值动态追踪", "detail": "破题眼：卖出的最大收益必定对应之前某天的历史最低价，单次遍历双变量滚动。", "weight": 25},
            {"dimension": "corner_case", "title": "持续单调下跌不交易", "detail": "防守点：如果股价一路下跌，max_profit 维持初始值 0，绝不产生负收益。", "weight": 25},
            {"dimension": "solution", "title": "5 行精炼单遍遍历手写", "detail": "手写点：无需动态规划数组，两个标量在循环中实时更新。", "weight": 25},
            {"dimension": "complexity", "title": "股票买卖系列状态机 DP 演进", "detail": "演练点：口述买卖多次（贪心累加所有正差值）、含冷冻期、含手续费的 DP 状态定义。", "weight": 25}
        ]
    },
    {
        "frontend_id": 55,
        "title_cn": "跳跃游戏",
        "title_en": "Jump Game",
        "slug": "jump-game",
        "difficulty": "Medium",
        "category": "贪心",
        "day": 5,
        "solution": {
            "core_insight": "贪心维护最远可达边界：遍历下标 i。若当前 `i > max_reach`，说明当前位置根本无法到达，返回 False。否则更新最远可达位置 `max_reach = max(max_reach, i + nums[i])`。若 `max_reach >= n - 1` 可提前返回 True。",
            "traps": "遍历范围不需要到最后一个元素，遇到无法到达点提前阻断。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True
        return True
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "最远覆盖范围覆盖一切", "detail": "破题眼：不用纠结究竟落脚在哪个格，只要最远能覆盖到的闭区间包含终点即可。", "weight": 25},
            {"dimension": "corner_case", "title": "原地踩 0 陷阱与单元素数组", "detail": "防守点：len(nums)==1 时无需跳跃直接 True；i > max_reach 捕获掉进 0 的死穴。", "weight": 25},
            {"dimension": "solution", "title": "循环早停极简手写", "detail": "手写点：8 行循环手撕，max_reach >= len(nums)-1 触发提前打卡。", "weight": 25},
            {"dimension": "complexity", "title": "贪心可行性反证法说明", "detail": "演练点：口述只要更远的范围能被覆盖，其内部所有点皆必定可达，无后效性成立。", "weight": 25}
        ]
    },
    {
        "frontend_id": 45,
        "title_cn": "跳跃游戏 II",
        "title_en": "Jump Game II",
        "slug": "jump-game-ii",
        "difficulty": "Medium",
        "category": "贪心",
        "day": 5,
        "solution": {
            "core_insight": "正向贪心维护当前步边界：维护两个边界：`end`（当前跳跃步数能到达的最远边界）和 `max_pos`（下一步能到达的最远边界）。遍历到 `end` 时步数 +1，并更新 `end = max_pos`。",
            "traps": "循环只遍历到 `len(nums) - 2`（不访问最后一个下标），因为一旦到达终点无需再跳一步增加计数。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def jump(self, nums: list[int]) -> int:
        steps = 0
        end = 0
        max_pos = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                steps += 1
        return steps
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "波次推进与跳跃右边界", "detail": "破题眼：类似 BFS 的按层展开，当前一步的 end 到头必须多耗费一步步数。", "weight": 25},
            {"dimension": "corner_case", "title": "循环上界 len(nums) - 1 关键防守", "detail": "防守点：必须循环到 len-2 为止，若遍历到最后一个元素会导致多算一次跳跃。", "weight": 25},
            {"dimension": "solution", "title": "7 行双指针边界推进手写", "detail": "手写点：变量 end 与 max_pos 协同演进，代码简短洗练。", "weight": 25},
            {"dimension": "complexity", "title": "反向贪心 O(N^2) 与正向 O(N) 对比", "detail": "演练点：口述反向找能到达终点的最左位置需要 O(N^2)，正向边界推进只需 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 763,
        "title_cn": "划分字母区间",
        "title_en": "Partition Labels",
        "slug": "partition-labels",
        "difficulty": "Medium",
        "category": "贪心",
        "day": 5,
        "solution": {
            "core_insight": "贪心字符最后出现下标：先预处理每个字符最后出现的下标 `last[ch]`。二次遍历字符串，动态更新当前片段所包含字符的最远下标 `end = max(end, last[ch])`。当遍历到 `i == end` 时，切断为一个片段，收集长度 `end - start + 1`。",
            "traps": "同一字母只能出现在同一个片段，所以只要区间内某个字母的最后出现位置更远，片段就必须向右延展。",
            "time_complexity": "O(N)",
            "space_complexity": "O(Σ) 仅 26 个字母",
            "code_python": '''class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "字符最后阵地作为强制边界", "detail": "破题眼：同一字符不跨段，段的右界由段内所有字符的最大最后位置共同决定。", "weight": 25},
            {"dimension": "corner_case", "title": "切断后 start 重置对齐", "detail": "防守点：收集长度后 start = i + 1 切换下一段起点，末端 i == end 自然收口。", "weight": 25},
            {"dimension": "solution", "title": "字典预处理 + 单趟收割手写", "detail": "手写点：10 行内写出字典推导式与切片统计，清晰自然。", "weight": 25},
            {"dimension": "complexity", "title": "与 56 题合并区间的等价性", "detail": "演练点：口述若把每个字符的 [first_idx, last_idx] 看作区间，本题就是合并区间的特例。", "weight": 25}
        ]
    }
]
