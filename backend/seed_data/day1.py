DAY_1_PROBLEMS = [
    {
        "frontend_id": 1,
        "title_cn": "两数之和",
        "title_en": "Two Sum",
        "slug": "two-sum",
        "difficulty": "Easy",
        "category": "哈希表",
        "day": 1,
        "solution": {
            "core_insight": "用哈希表存储已遍历元素及其下标。遍历到 x 时，查 target - x 是否已在表中，若在即刻返回，一次遍历搞定。",
            "traps": "同一个元素不能使用两遍；必须边查边存，防止查到自身。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "哈希映射换取时间", "detail": "破题眼：将原本 O(N^2) 的配对搜索，通过哈希表记录补数转化为 O(1) 查找。", "weight": 25},
            {"dimension": "corner_case", "title": "防重复引用与边界", "detail": "防守点：避免把当前元素自身当成匹配项；负数与零的加和正确性验证。", "weight": 25},
            {"dimension": "solution", "title": "单遍哈希手写 Bug-free", "detail": "手写点：enumerate 遍历边查找边插入，10 行内清晰整洁写出最优解。", "weight": 25},
            {"dimension": "complexity", "title": "时空分析与进阶追问", "detail": "演练点：熟练解释为什么时空均为 O(N)；被问及有序数组时如何改用对撞双指针。", "weight": 25}
        ]
    },
    {
        "frontend_id": 49,
        "title_cn": "字母异位词分组",
        "title_en": "Group Anagrams",
        "slug": "group-anagrams",
        "difficulty": "Medium",
        "category": "哈希表",
        "day": 1,
        "solution": {
            "core_insight": "异位词由相同字符与频次组成。可将排序后的字符串或 26 位字符计数元组作为哈希键，值存分组列表。",
            "traps": "字典的 key 必须是不可变对象（tuple 或 str），不能直接拿 list 当 key。",
            "time_complexity": "O(N * K log K) 或 O(N * K)",
            "space_complexity": "O(N * K)",
            "code_python": '''from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "同构模式归一化 Key", "detail": "破题眼：识别异位词本质是不变量，选用排序字符串或计数元组作为统一 key。", "weight": 25},
            {"dimension": "corner_case", "title": "空字符串与单字符边界", "detail": "防守点：输入为 [\"\"] 或单个字符时的哈希正常分类，避免字典抛 KeyError。", "weight": 25},
            {"dimension": "solution", "title": "defaultdict 优雅代码", "detail": "手写点：熟练运用 collections.defaultdict 避免繁琐的 if key not in 逻辑。", "weight": 25},
            {"dimension": "complexity", "title": "排序与计数方案 Tradeoff", "detail": "演练点：口述比较排序 key O(K log K) 与 26 位计数元组 O(K) 的性能权衡。", "weight": 25}
        ]
    },
    {
        "frontend_id": 128,
        "title_cn": "最长连续序列",
        "title_en": "Longest Consecutive Sequence",
        "slug": "longest-consecutive-sequence",
        "difficulty": "Medium",
        "category": "哈希表",
        "day": 1,
        "solution": {
            "core_insight": "将所有数丢进哈希集合去重。只有当 num - 1 不在集合中时，num 才是序列起点，往后递增统计长度，保证每个数最多访问两次。",
            "traps": "若不对 num - 1 判空，会导致内部循环重复扫描，退化为 O(N^2)。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                streak = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    streak += 1
                max_streak = max(max_streak, streak)
        return max_streak
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "起点剪枝思维", "detail": "破题眼：利用 num - 1 not in set 精准判断序列起点，防止多余遍历。", "weight": 25},
            {"dimension": "corner_case", "title": "空数组与大量重复值", "detail": "防守点：nums 为空时返回 0；利用 set(nums) 自然去除重复数的干扰。", "weight": 25},
            {"dimension": "solution", "title": "双层循环伪装的 O(N)", "detail": "手写点：清晰写出 while 循环向前探测，无冗余变量，代码优雅。", "weight": 25},
            {"dimension": "complexity", "title": "均摊时间复杂度证明", "detail": "演练点：向面试官证明为什么有 while 却依然是严格 O(N)（每个数字进出循环常数次）。", "weight": 25}
        ]
    },
    {
        "frontend_id": 283,
        "title_cn": "移动零",
        "title_en": "Move Zeroes",
        "slug": "move-zeroes",
        "difficulty": "Easy",
        "category": "双指针",
        "day": 1,
        "solution": {
            "core_insight": "同向双指针：slow 指针维护非零元素应该安放的位置，fast 遍历数组。遇到非零元素交换到 slow 并让 slow 前进。",
            "traps": "直接填非零值后面补 0 也可以，但原地交换法能保持最小写操作数。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "快慢指针切分不变量", "detail": "破题眼：明确 slow 之前全是非零有序区，slow 到 fast 之间是零区。", "weight": 25},
            {"dimension": "corner_case", "title": "全是0或全非0", "detail": "防守点：数组全为 0 或完全没有 0 时，原地自交换不会越界且保持相对顺序。", "weight": 25},
            {"dimension": "solution", "title": "原地交换与无额外空间", "detail": "手写点：4 行核心循环，一次遍历，不需要二次补零遍历。", "weight": 25},
            {"dimension": "complexity", "title": "原地操作与写开销分析", "detail": "演练点：口述对比赋值法与交换法在底层写入缓存层面的微观差异。", "weight": 25}
        ]
    },
    {
        "frontend_id": 11,
        "title_cn": "盛最多水的容器",
        "title_en": "Container With Most Water",
        "slug": "container-with-most-water",
        "difficulty": "Medium",
        "category": "双指针",
        "day": 1,
        "solution": {
            "core_insight": "首尾对撞双指针：容量由较矮板决定 (min(h[l], h[r]) * (r - l))。每次移动较矮的那一侧，因为移动较长板宽度变小高度上限不增，容量必定减小。",
            "traps": "两板高度相同时移动任意一侧均可，最终结果不受影响。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            h = min(height[left], height[right])
            max_water = max(max_water, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "对撞双指针与贪心短板效应", "detail": "破题眼：木桶效应决定容量上限，贪心移动短板以期探索更高的高度。", "weight": 25},
            {"dimension": "corner_case", "title": "首尾极值与等高板", "detail": "防守点：两端等高情况下的安全收缩，单调递减或递增序列的边界验证。", "weight": 25},
            {"dimension": "solution", "title": "精简收敛逻辑", "detail": "手写点：while left < right 架构，单次计算面积并比较，干净利索。", "weight": 25},
            {"dimension": "complexity", "title": "反证法严格证明单调移动", "detail": "演练点：能现场口述反证法说明为什么“移动较长板必然错过可能的最大值”。", "weight": 25}
        ]
    },
    {
        "frontend_id": 15,
        "title_cn": "三数之和",
        "title_en": "3Sum",
        "slug": "3sum",
        "difficulty": "Medium",
        "category": "双指针",
        "day": 1,
        "solution": {
            "core_insight": "先排序。固定第一个数 nums[i]，若 nums[i] > 0 直接剪枝跳出。在 [i+1, n-1] 上进行双指针夹逼，重点对 i、left、right 三处做彻底去重。",
            "traps": "去重逻辑写错是面试挂掉的高发区！对 i 应该和 i-1 比，而不是 i+1；找到解后必须跳过连续重复值再收缩。",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(1)（忽略排序栈空间）",
            "code_python": '''class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "排序降维 + 夹逼搜索", "detail": "破题眼：将 3Sum 降维成有序数组的 2Sum，利用有序性双向夹逼。", "weight": 25},
            {"dimension": "corner_case", "title": "三重去重死穴防守", "detail": "防守点：精准区分 i 与 i-1 判重，以及命中 target 后 left/right 的连续重复消除。", "weight": 25},
            {"dimension": "solution", "title": "无哈希集合的原地去重解", "detail": "手写点：手写时不依赖 set 去重，完全依靠指针控制输出唯一三元组。", "weight": 25},
            {"dimension": "complexity", "title": "剪枝效率与复杂度口述", "detail": "演练点：口述 nums[i] > 0 提前 break 的剪枝优化点，分析 O(N^2) 瓶颈。", "weight": 25}
        ]
    },
    {
        "frontend_id": 42,
        "title_cn": "接雨水",
        "title_en": "Trapping Rain Water",
        "slug": "trapping-rain-water",
        "difficulty": "Hard",
        "category": "双指针",
        "day": 1,
        "solution": {
            "core_insight": "每个位置能接的水由 min(left_max, right_max) - height[i] 决定。双指针从两端向中间汇拢，维护左侧最高和右侧最高，谁小就结算谁并向中间移动。",
            "traps": "单调栈是横向切片算水，双指针是纵向列算水。双指针法空间 O(1)，是面试官最期望看到的解答。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "纵向列积分与双指针极值", "detail": "破题眼：看透单列雨水由左右两侧短板决定的本质，左低算左，右低算右。", "weight": 25},
            {"dimension": "corner_case", "title": "两端递减/递增无积水", "detail": "防守点：V字形谷底蓄水，倒V字或阶梯单调形无法存水，边界安全返回 0。", "weight": 25},
            {"dimension": "solution", "title": "极致 O(1) 空间双指针手写", "detail": "手写点：15 行内不借助辅助数组，纯双指针边走边累加水量。", "weight": 25},
            {"dimension": "complexity", "title": "三种解法对比演练", "detail": "演练点：能熟练横向对比三次遍历前后缀法 O(N) 空间、单调栈法与双指针法。", "weight": 25}
        ]
    },
    {
        "frontend_id": 3,
        "title_cn": "无重复字符的最长子串",
        "title_en": "Longest Substring Without Repeating Characters",
        "slug": "longest-substring-without-repeating-characters",
        "difficulty": "Medium",
        "category": "滑动窗口",
        "day": 1,
        "solution": {
            "core_insight": "滑动窗口右移扩大，哈希表记录字符最新出现下标。若遇到重复且上一次下标 >= left，left 直接跳到 last_idx + 1，无需逐步缩小。",
            "traps": "更新 left 时必须取 max(left, last_idx + 1)，否则可能把 left 往回拉导致错误。",
            "time_complexity": "O(N)",
            "space_complexity": "O(min(N, Σ))",
            "code_python": '''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in char_map:
                left = max(left, char_map[ch] + 1)
            char_map[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "滑窗扩展与跳跃式收缩", "detail": "破题眼：窗口维护无重复子串，遇重复直接借助哈希表记录的索引跳跃。", "weight": 25},
            {"dimension": "corner_case", "title": "left 倒退陷阱", "detail": "防守点：必须通过 max(left, last_idx + 1) 保证左指针只能单向向右，绝不回退。", "weight": 25},
            {"dimension": "solution", "title": "极简哈希滑窗手写", "detail": "手写点：8 行核心逻辑，右指针每走一步更新一次全局 max_len。", "weight": 25},
            {"dimension": "complexity", "title": "字符集与时空口述", "detail": "演练点：说明字符集大小有限（ASCII 128），哈希表实际占用常数级空间。", "weight": 25}
        ]
    },
    {
        "frontend_id": 438,
        "title_cn": "找到字符串中所有字母异位词",
        "title_en": "Find All Anagrams in a String",
        "slug": "find-all-anagrams-in-a-string",
        "difficulty": "Medium",
        "category": "滑动窗口",
        "day": 1,
        "solution": {
            "core_insight": "定长滑动窗口，窗口大小固定为 len(p)。维护一个长度 26 的频次差数组或 match 计数，右进左出，完全一致时记录左指针。",
            "traps": "当 s 长度小于 p 长度时直接返回空列表。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)（仅 26 个小写字母）",
            "code_python": '''class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(p_len):
            p_cnt[ord(p[i]) - ord('a')] += 1
            s_cnt[ord(s[i]) - ord('a')] += 1
        res = []
        if s_cnt == p_cnt:
            res.append(0)
        for i in range(p_len, s_len):
            s_cnt[ord(s[i]) - ord('a')] += 1
            s_cnt[ord(s[i - p_len]) - ord('a')] -= 1
            if s_cnt == p_cnt:
                res.append(i - p_len + 1)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "定长滑动窗口与频次阵列", "detail": "破题眼：窗口宽度恒为 len(p)，右端滑入一个字符，左端必然滑出一个字符。", "weight": 25},
            {"dimension": "corner_case", "title": "母串短于模式串", "detail": "防守点：len(s) < len(p) 防御性提前返回；首个窗口与后续窗口的衔接判断。", "weight": 25},
            {"dimension": "solution", "title": "固定数组切片比较", "detail": "手写点：使用固定 26 长度数组实现 O(1) 状态比较，不用反复构造 dict。", "weight": 25},
            {"dimension": "complexity", "title": "定长滑窗的时空不变量", "detail": "演练点：说明每次窗口更新为 O(1) 增量操作，整体是 O(N) 遍历。", "weight": 25}
        ]
    },
    {
        "frontend_id": 560,
        "title_cn": "和为 K 的子数组",
        "title_en": "Subarray Sum Equals K",
        "slug": "subarray-sum-equals-k",
        "difficulty": "Medium",
        "category": "哈希表",
        "day": 1,
        "solution": {
            "core_insight": "前缀和 + 哈希表。子数组 sum(i..j) = prefix[j] - prefix[i-1] = k。转化为查哈希表中 prefix[j] - k 出现的次数。初始化 {0: 1}。",
            "traps": "注意数组中有负数，不能用滑动窗口（不具备单调性）！必须前缀和+哈希。别忘了前缀和为 0 的基础频次 1。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for num in nums:
            curr_sum += num
            count += prefix_counts[curr_sum - k]
            prefix_counts[curr_sum] += 1
        return count
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "前缀和差分转化为两数之和", "detail": "破题眼：连续子数组求和问题 = 前缀和的两数之差，哈希统计频次。", "weight": 25},
            {"dimension": "corner_case", "title": "负数破坏单调性与空前缀", "detail": "防守点：必须初始化 prefix_counts[0] = 1 处理刚好从下标 0 开始的前缀和等于 k。", "weight": 25},
            {"dimension": "solution", "title": "边查边存避免包含自身", "detail": "手写点：先累加 count 再将 curr_sum 记入字典，保证逻辑严格无误。", "weight": 25},
            {"dimension": "complexity", "title": "为什么不能用双指针滑窗", "detail": "演练点：向面试官明确口述“有负数存在导致窗口和非单调递增，滑窗失效”。", "weight": 25}
        ]
    },
    {
        "frontend_id": 239,
        "title_cn": "滑动窗口最大值",
        "title_en": "Sliding Window Maximum",
        "slug": "sliding-window-maximum",
        "difficulty": "Hard",
        "category": "滑动窗口",
        "day": 1,
        "solution": {
            "core_insight": "单调双端队列：队列中存数组下标，保持对应元素单调递减。新元素加入时，将队尾所有小于它的元素弹出；若队首下标超出窗口左界，从队首弹出。",
            "traps": "队列存的是下标而不是元素值，这样才能通过下标差方便地判断元素是否过期出了窗口。",
            "time_complexity": "O(N)",
            "space_complexity": "O(K)",
            "code_python": '''from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        res = []
        for i, val in enumerate(nums):
            while q and nums[q[-1]] <= val:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "单调双端队列维系极值", "detail": "破题眼：新加入的较大元素会让之前更小的旧元素永无出头之日，果断淘汰尾部。", "weight": 25},
            {"dimension": "corner_case", "title": "窗口形成前与下标过期", "detail": "防守点：前 k-1 个元素只进不出结果；队头下标 q[0] <= i - k 时及时出队。", "weight": 25},
            {"dimension": "solution", "title": "双端队列下标存储手写", "detail": "手写点：利用 deque 存索引，保持队头始终是当前窗口最大值下标。", "weight": 25},
            {"dimension": "complexity", "title": "摊还分析 O(N) 证明", "detail": "演练点：口述每个元素最多进队一次出队一次，尽管有 while 均摊仍然是严格 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 76,
        "title_cn": "最小覆盖子串",
        "title_en": "Minimum Window Substring",
        "slug": "minimum-window-substring",
        "difficulty": "Hard",
        "category": "滑动窗口",
        "day": 1,
        "solution": {
            "core_insight": "变长双指针滑动窗口：维护 need 字典和 match_count 变量。右指针扩展直到所有字符达标；然后左指针尽可能收缩，更新最短子串，直到打破平衡。",
            "traps": "注意 need 统计的是字符种类还是字符总数；当 s[l] 的频次多于需要时可以放心收缩。",
            "time_complexity": "O(M + N)",
            "space_complexity": "O(Σ)",
            "code_python": '''from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        need = Counter(t)
        window = defaultdict(int)
        left = 0
        matched = 0
        min_len = float('inf')
        best_left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                matched += 1
            while matched == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    matched -= 1
                left += 1
        return "" if min_len == float('inf') else s[best_left:best_left + min_len]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "变长滑窗与匹配计数器", "detail": "破题眼：右扩找可行解，左缩找最优解；利用 matched == len(need) 进行 O(1) 判定。", "weight": 25},
            {"dimension": "corner_case", "title": "无解判定与字符频次相等点", "detail": "防守点：找不到解时返回空串；window[ch] == need[ch] 时 matched 才自增，避免重复计数。", "weight": 25},
            {"dimension": "solution", "title": "高难度滑窗模板手写", "detail": "手写点：完整熟练写出 need、window、matched 联动结构，控制最佳起始点与长度。", "weight": 25},
            {"dimension": "complexity", "title": "时空分析与指针单调性", "detail": "演练点：口述左右指针各遍历字符串最多一遍，总时间严格 O(N+M)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 53,
        "title_cn": "最大子数组和",
        "title_en": "Maximum Subarray",
        "slug": "maximum-subarray",
        "difficulty": "Medium",
        "category": "动态规划",
        "day": 1,
        "solution": {
            "core_insight": "Kadane 算法 / 动态规划：dp[i] = max(nums[i], dp[i-1] + nums[i])。若前序和为负，则直接舍弃从当前数字重新开始累加。",
            "traps": "全是负数时不能返回 0，最大子数组必须至少包含一个元素，返回最大的那个负数。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            max_sum = max(max_sum, curr_sum)
        return max_sum
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "Kadane 算法状态压缩", "detail": "破题眼：当前累加和如果为负数则必定拖累后续，果断断舍离重置起点。", "weight": 25},
            {"dimension": "corner_case", "title": "全负数数组边界", "detail": "防守点：全局初始值设为 nums[0] 而非 0，防止全负数时误输出 0。", "weight": 25},
            {"dimension": "solution", "title": "滚动变量 O(1) 空间手写", "detail": "手写点：5 行循环实现单变量滚动更新，代码精简无可挑剔。", "weight": 25},
            {"dimension": "complexity", "title": "分治法进阶扩展", "detail": "演练点：能说明若要求区间任意子数组和（如线段树维护 lsum, rsum, msum）的分治思路。", "weight": 25}
        ]
    },
    {
        "frontend_id": 56,
        "title_cn": "合并区间",
        "title_en": "Merge Intervals",
        "slug": "merge-intervals",
        "difficulty": "Medium",
        "category": "区间合并",
        "day": 1,
        "solution": {
            "core_insight": "先按区间左端点升序排序。遍历区间，若当前区间的左端点 <= 上一个区间的右端点，则发生重叠，合并右端点；否则直接开启新区间。",
            "traps": "合并右端点时是 max(last_end, curr_end)，因为后一个区间可能被前一个完全包含。",
            "time_complexity": "O(N log N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "端点排序消除后效性", "detail": "破题眼：将无序区间按 start 排序后，相邻关系具备单调性，一次线性合并。", "weight": 25},
            {"dimension": "corner_case", "title": "完全包含与单点重叠", "detail": "防守点：[1,4] 与 [2,3] 完全包含时 end 取 max；[1,4] 与 [4,5] 接壤合并为 [1,5]。", "weight": 25},
            {"dimension": "solution", "title": "原地更新末尾元素", "detail": "手写点：借助 merged[-1][1] = max(...) 动态更新结果集最后项。", "weight": 25},
            {"dimension": "complexity", "title": "排序瓶颈时空分析", "detail": "演练点：口述排序 O(N log N) 占主要开销，合并仅需 O(N) 遍历。", "weight": 25}
        ]
    },
    {
        "frontend_id": 189,
        "title_cn": "轮转数组",
        "title_en": "Rotate Array",
        "slug": "rotate-array",
        "difficulty": "Medium",
        "category": "双指针",
        "day": 1,
        "solution": {
            "core_insight": "三次翻转法：k %= n。1. 翻转整个数组；2. 翻转前 k 个元素；3. 翻转后 n-k 个元素。空间复杂度 O(1)。",
            "traps": "k 可能大于数组长度 n，必须先进行 k %= n 取模。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "三次翻转的对称几何意义", "detail": "破题眼：整体反转改变前后段相对顺序，局部反转恢复两段各自内部正序。", "weight": 25},
            {"dimension": "corner_case", "title": "k 大于数组长度取模", "detail": "防守点：必须显式 k %= n；k == 0 或 n == 1 时不产生多余移动。", "weight": 25},
            {"dimension": "solution", "title": "双指针辅助反转函数手写", "detail": "手写点：手写干净的双指针 reverse 闭包函数，三行调用完成就地轮转。", "weight": 25},
            {"dimension": "complexity", "title": "环状替换 vs 三次翻转", "detail": "演练点：口述环状替换（数学公约数）与三次翻转法在编码复杂度与写次数上的权衡。", "weight": 25}
        ]
    },
    {
        "frontend_id": 238,
        "title_cn": "除自身以外数组的乘积",
        "title_en": "Product of Array Except Self",
        "slug": "product-of-array-except-self",
        "difficulty": "Medium",
        "category": "数组",
        "day": 1,
        "solution": {
            "core_insight": "利用结果数组存前缀积，然后用一个动态变量 R 从右向左滚动累乘后缀积并与前缀积相乘。不使用除法且空间 O(1)。",
            "traps": "题目明确要求不能使用除法，且输出数组不计入额外空间复杂度。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)（除输出数组外）",
            "code_python": '''class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        # 计算前缀积
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        # 滚动累乘后缀积
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "前缀积与后缀积拆解", "detail": "破题眼：任何数除了自己的乘积 = 其左侧所有数的乘积 * 右侧所有数的乘积。", "weight": 25},
            {"dimension": "corner_case", "title": "数组含多个零的场景", "detail": "防守点：如果有两个零结果全为零；有一个零仅零对应位置非零。前后缀积自然正确处理。", "weight": 25},
            {"dimension": "solution", "title": "复用返回数组压榨空间", "detail": "手写点：先正向填入 prefix，再反向用单变量 suffix 累乘，杜绝开辟两张辅助表。", "weight": 25},
            {"dimension": "complexity", "title": "严格两遍遍历时空论证", "detail": "演练点：解释为何不产生额外空间开销，双趟遍历耗时 2N 依旧是严格 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 41,
        "title_cn": "缺失的第一个正数",
        "title_en": "First Missing Positive",
        "slug": "first-missing-positive",
        "difficulty": "Hard",
        "category": "哈希表",
        "day": 1,
        "solution": {
            "core_insight": "原地哈希（萝卜填坑）：长度为 n 的数组，缺失的最小正整数必在 [1, n+1] 之间。遍历将元素 x 尽量交换到下标 x - 1 上。二次遍历首个 nums[i] != i+1 的即为答案。",
            "traps": "原地交换时使用 while 循环持续安置当前数字，注意防死循环：nums[i] 与 nums[nums[i]-1] 相等时必须停止交换！",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "鸽巢原理与原地哈希填坑", "detail": "破题眼：利用数组下标本身充当哈希桶，让数值为 x 的数字归位到下标 x-1。", "weight": 25},
            {"dimension": "corner_case", "title": "死循环与越界防守", "detail": "防守点：重复元素（如 [1, 1]）时若判定条件写错会导致死循环；负数与超出 n 的数字直接跳过。", "weight": 25},
            {"dimension": "solution", "title": "while 原地归位稳健手写", "detail": "手写点：先提取 target_idx = nums[i] - 1 再交换，避免 Python 连续解构赋值中的索引变更坑。", "weight": 25},
            {"dimension": "complexity", "title": "置换次数均摊 O(N) 证明", "detail": "演练点：口述每个数归位后便不会再次被移走，总置换次数不会超过 N 次。", "weight": 25}
        ]
    }
]
