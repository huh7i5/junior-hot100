# -*- coding: utf-8 -*-
"""Day 1 Part 3 Problems: 438, 560, 239, 76."""

DAY_1_PART3 = {
    438: {
        "title_cn": "找到字符串中所有字母异位词",
        "title_en": "Find All Anagrams in a String",
        "slug": "find-all-anagrams-in-a-string",
        "difficulty": "Medium",
        "description": """### 题目描述
给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

**字母异位词** 指由相同字母重排列形成的字符串（包括相同的字符串）。

### 示例 1
- **输入**: `s = "cbaebabacd", p = "abc"`
- **输出**: `[0,6]`
- **解释**:
  - 起始索引等于 0 的子串是 `"cba"`, 它是 `"abc"` 的异位词。
  - 起始索引等于 6 的子串是 `"bac"`, 它是 `"abc"` 的异位词。

### 示例 2
- **输入**: `s = "abab", p = "ab"`
- **输出**: `[0,1,2]`
- **解释**:
  - 起始索引等于 0 的子串是 `"ab"`, 它是 `"ab"` 的异位词。
  - 起始索引等于 1 的子串是 `"ba"`, 它是 `"ab"` 的异位词。
  - 起始索引等于 2 的子串是 `"ab"`, 它是 `"ab"` 的异位词。

### 提示与约束条件
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` 和 `p` 仅包含小写英文字母""",
        "plain_explanation": """大白话直击本质：这就像手里拿着一个固定长度等于 `p.length` 的【矩形滑动相框】！
把相框罩在长字符串 s 上，从最左边一路往右滑。
相框里装的 26 个英文字母的出现次数，如果和目标串 p 里的 26 个字母数量分毫不差，就说明相框里正是一个完美的字母异位词！立刻把相框左边缘的下标记录到答案列表里。
相框每次往右移动一格：
- 相框右边【吞进】一个新来的字母（该字母计数加 1）；
- 相框左边【吐出】一个被移出去的老字母（该字母计数减 1）；
中间的所有字母根本不用动！
每次滑动的维护成本只有 O(1)，比对两个 26 位数组的开销也是 O(26) 纯常数，总时间严格为 O(N)！""",
        "js_helpers": [
            {
                "name": "new Array(26).fill(0)",
                "what_it_does": "创建一个长度为 26 的数组并初始化为 0，用于统计 'a' 到 'z' 出现的频次。",
                "junior_tip": "相比频繁 new Map() 和序列化对象，纯数字数组内存连续、寻址极快，是字符频次统计的最优解法。"
            },
            {
                "name": "str.charCodeAt(i) - 'a'.charCodeAt(0)",
                "what_it_does": "将字符转换为 0 到 25 的数字索引下标。",
                "junior_tip": "'a'.charCodeAt(0) 是固定整数 97。'a' 对应 0，'b' 对应 1，'z' 对应 25。"
            },
            {
                "name": "定长滑动窗口 (Fixed-size Sliding Window)",
                "what_it_does": "右边界进一个元素、左边界出一个元素，保持窗口宽度恒等于 p.length。",
                "junior_tip": "无需嵌套 while 循环，单个 for 循环线性滑完即可。"
            }
        ],
        "code_js": """/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const sLen = s.length;
    const pLen = p.length;
    // 边界特判：若母串长度小于模式串，绝不可能存在异位词
    if (sLen < pLen) return [];

    const res = [];
    // 步骤 1：用长度为 26 的数组统计 26 个小写字母频次
    const pCount = new Array(26).fill(0);
    const sCount = new Array(26).fill(0);
    const codeA = 'a'.charCodeAt(0);

    // 步骤 2：初始化首个窗口（统计 p 全部字符，以及 s 前 pLen 个字符）
    for (let i = 0; i < pLen; i++) {
        pCount[p.charCodeAt(i) - codeA]++;
        sCount[s.charCodeAt(i) - codeA]++;
    }

    // 辅助函数：比对两个 26 长度频次数组是否完全吻合（26 次常数比对）
    const isMatch = (arr1, arr2) => {
        for (let i = 0; i < 26; i++) {
            if (arr1[i] !== arr2[i]) return false;
        }
        return true;
    };

    // 检查初始首个窗口是否命中
    if (isMatch(sCount, pCount)) {
        res.push(0);
    }

    // 步骤 3：定长滑动窗口，右边吞入新字符，左边吐出老字符
    for (let i = pLen; i < sLen; i++) {
        // 右边新字符入窗
        sCount[s.charCodeAt(i) - codeA]++;
        // 左边老字符出窗（老字符下标为 i - pLen）
        sCount[s.charCodeAt(i - pLen) - codeA]--;

        // 步骤 4：比对当前窗口频次，若吻合则收录窗口起始索引
        if (isMatch(sCount, pCount)) {
            res.push(i - pLen + 1);
        }
    }

    return res;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：母串长度劣势防御特判",
                "detail": "检测 sLen < pLen 时直接 return []，避免后续无意义的负向索引截取与越界初始化操作。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：26 位定长计数数组构建",
                "detail": "使用 new Array(26).fill(0) 替代哈希字典，利用 ASCII 码偏移量 ch.charCodeAt(0) - 97 实现高效 O(1) 原地累加。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：初始首窗建立与基准匹配",
                "detail": "先填充模式串 p 的全量计数与母串 s 的前 pLen 个字符，完成首个长度为 pLen 窗口的建立与初始结果判定。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：定长滑动窗口进出平衡机制",
                "detail": "在单层循环中执行 sCount[新]++ 与 sCount[老]--，维持窗口内部字符数量恒等于 pLen，更新开销严格 O(1)。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：常数级频次比对与时间复杂度收敛",
                "detail": "比对函数在固定 26 维空间运行，全过程总时间复杂度为 O(26 * N) = O(N)，额外空间为常数 O(1)。",
                "weight": 20
            }
        ]
    },
    560: {
        "title_cn": "和为 K 的子数组",
        "title_en": "Subarray Sum Equals K",
        "slug": "subarray-sum-equals-k",
        "difficulty": "Medium",
        "description": """### 题目描述
给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 **该数组中和为 `k` 的子数组的个数** 。

子数组是数组中元素的连续非空序列。

### 示例 1
- **输入**: `nums = [1,1,1], k = 2`
- **输出**: `2`
- **解释**: `[1,1]` 出现了 2 次（下标 [0,1] 和 [1,2]）。

### 示例 2
- **输入**: `nums = [1,2,3], k = 3`
- **输出**: `2`
- **解释**: 子数组 `[1,2]` 和 `[3]` 的和均为 3。

### 提示与约束条件
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`
- **致命大坑**：数组中存在负数！因此滑动窗口完全失效，必须使用前缀和 + 哈希表！""",
        "plain_explanation": """【警钟长鸣】：千万不要用双指针滑动窗口做这题！
滑动窗口能工作的前提是'数组元素全为正数'（窗口越长和越大，窗口缩短和变小，具有单调性）。
但本题数组里【包含负数】！你拉长窗口，和可能反而变小；缩短窗口，和可能反而变大，双指针直接乱套！
真正解法叫【前缀和 + 历史备忘录】：
想象你背着背包在一条路上跑步，手里拿个计步器随时累加跑过的总里程 `currentSum`。
如果从起点到当前位置的里程是 `currentSum`，而你想知道中间有没有某一段路程的总和刚好是 `k`？
其实就是在问：【在以前跑过的打卡点里，有没有哪个打卡点的里程正好等于 `currentSum - k`？】
如果有，从那个打卡点跑到你现在的位置，中间这一截的距离不正好就是 k 嘛！
所以我们准备一个 Map 备忘录：记录【每个前缀和数值出现过多少次】。
【小白最容易丢分的大坑】：出发前必须在备忘录里写上 `map.set(0, 1)`！
为什么？因为如果某次跑到当前位置，总里程恰好本身就等于 k（currentSum - k = 0），必须能从备忘录里查到从原点出发的这第 1 次，否则从下标 0 开始的子数组就全漏算了！""",
        "js_helpers": [
            {
                "name": "map.set(0, 1) 的重大意义",
                "what_it_does": "初始化前缀和为 0 的频次为 1。",
                "junior_tip": "【必背哨兵】代表'前缀和为 0 在初始未出发状态下已经发生过 1 次'。若不加，所有从下标 0 开始且和刚好为 k 的子数组都不会被统计入答案！"
            },
            {
                "name": "map.has(currentSum - k)",
                "what_it_does": "检查是否存在历史前缀和等于当前前缀和减去 k。",
                "junior_tip": "根据数学公式：prefix[right] - prefix[left] = k 等价于 prefix[left] = prefix[right] - k。"
            },
            {
                "name": "map.set(currentSum, (map.get(currentSum) || 0) + 1)",
                "what_it_does": "将当前累加的前缀和频次加 1 记录进 Map。",
                "junior_tip": "使用 (map.get(x) || 0) 优雅处理 key 首次出现的默认值 0，无需写繁琐的 if-else。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    // 步骤 1：准备 Map 存 { 前缀和 => 出现频次 }
    const map = new Map();
    // 关键初始化：前缀和为 0 默认出现过 1 次（哨兵节点）
    map.set(0, 1);

    let count = 0;
    let currentSum = 0;

    // 步骤 2：从左向右单趟遍历数组，累加当前前缀和
    for (const num of nums) {
        currentSum += num;

        // 步骤 3：查表——看之前有没有出现过差值 (currentSum - k)
        if (map.has(currentSum - k)) {
            // 累加该差值历史上出现过的全部频次
            count += map.get(currentSum - k);
        }

        // 步骤 4：将当前前缀和记录到 Map 中（频次加 1）
        map.set(currentSum, (map.get(currentSum) || 0) + 1);
    }

    // 步骤 5：返回总方案数
    return count;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：负数存在对滑动窗口的否定",
                "detail": "透彻理解当数组包含负数时，区间和与窗口长度丧失单调关系，滑窗双指针失效，必须转向哈希前缀和体系。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：连续子数组向两数之差转换",
                "detail": "将连续子数组和 sum(nums[i..j]) = k 转化为 prefix[j] - prefix[i-1] = k，即在历史前缀集合中寻找 prefix[j] - k。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：map.set(0, 1) 初始哨兵必要性",
                "detail": "初始化 prefix=0 出现 1 次，用于正确统计从数组索引 0 开始、自身和直接等于 k 的整段前缀子数组。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：先查后存的顺序与无后效性",
                "detail": "严格保持'先检查历史差值累加 count，再将当前前缀和入表'的时序，防止 k=0 时当前前缀和自身与自身误配。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：单变量累加与 O(N) 线性性能",
                "detail": "使用 currentSum 单变量实时累加，无需开辟 N 长度的前缀和数组，时间与空间复杂度均为极佳的 O(N)。",
                "weight": 20
            }
        ]
    },
    239: {
        "title_cn": "滑动窗口最大值",
        "title_en": "Sliding Window Maximum",
        "slug": "sliding-window-maximum",
        "difficulty": "Hard",
        "description": """### 题目描述
给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 **滑动窗口中的最大值** 。

### 示例 1
- **输入**：`nums = [1,3,-1,-3,5,3,6,7], k = 3`
- **输出**：`[3,3,5,5,6,7]`
- **解释**：
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       **3**
 1 [3  -1  -3] 5  3  6  7       **3**
 1  3 [-1  -3  5] 3  6  7       **5**
 1  3  -1 [-3  5  3] 6  7       **5**
 1  3  -1  -3 [5  3  6] 7       **6**
 1  3  -1  -3  5 [3  6  7]      **7**

### 示例 2
- **输入**：`nums = [1], k = 1`
- **输出**：`[1]`

### 提示与约束条件
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`""",
        "plain_explanation": """滑动窗口在往前移动，怎样在 O(1) 的时间内得知当前窗口内部谁是老大？
如果每次都在窗口里做一次 Math.max，整体时间是 O(N * k)，当 k=10^5 时必超时无疑！
大白话秘诀叫【职场残酷淘汰制（单调双端队列）】：
我们用一个队列来排队，但排队的规则极其现实：
1. 【淘汰队尾弱者】：新来了一个年轻员工（当前数字 nums[i]），如果他的能力（数值）比排在队尾的老员工还要大或一样大，
   那么这些老员工不仅资历更老（会比新人更早被滑出窗口），能力还比新人更差！
   在未来的窗口里，这些老员工【绝无出头之日，绝不可能成为最大值】！
   所以必须毫不留情地把队尾所有比新人弱的人全部开除踢出队列（q.pop()）！
2. 这样清理完后，队伍里的人从队头到队尾是【严格从大到小排列】的！队头的人永远是整个窗口的最强王者！
3. 【队头王者超期退休】：队列里存的不是数字本身，而是【数组下标】！
   这样只要看队头下标 `q[0] <= i - k`，就能立刻知道队头王者是不是已经滑出当前窗口了。如果是，光荣退休出队（q.shift()）！
4. 窗口成型（i >= k - 1）后，直接取队头 `nums[q[0]]` 存入答案列表！每个元素最多入队一次出队一次，整体时间严格 O(N)！""",
        "js_helpers": [
            {
                "name": "单调双端队列 (Monotonic Deque)",
                "what_it_does": "队列两端均可操作：队尾 push/pop，队头 shift。",
                "junior_tip": "维护队列中元素单调递减，队头始终指向当前窗口内最大元素的索引。"
            },
            {
                "name": "队列存储索引下标而非元素值",
                "what_it_does": "在队列中存储下标 i，而非 nums[i]。",
                "junior_tip": "【核心考点】存储下标既可以通过 nums[i] 获取数值比大小，又能通过 q[0] <= i - k 瞬间判断是否超出当前滑窗边界。"
            },
            {
                "name": "q.pop() 与 q.shift()",
                "what_it_does": "q.pop() 从尾部移除劣汰元素；q.shift() 从头部弹出过期元素。",
                "junior_tip": "JS 中小规模 shift 性能优异；超大规模追求极致时亦可用双指针 head 偏移量模拟避免数组重排开销。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    const q = []; // 双端单调队列，存储元素下标
    const res = [];

    // 单趟遍历所有元素
    for (let i = 0; i < nums.length; i++) {
        // 步骤 1：淘汰队尾弱者——新元素更大，队尾比它小的元素永无翻身之日，全部出队
        while (q.length > 0 && nums[q[q.length - 1]] <= nums[i]) {
            q.pop();
        }
        // 新元素下标入队尾
        q.push(i);

        // 步骤 2：检查队头王者是否已经滑出窗口左边界（超期退休）
        if (q[0] <= i - k) {
            q.shift();
        }

        // 步骤 3：当遍历步数达到 k - 1 时，滑动窗口已正式成型，收集队头最大值
        if (i >= k - 1) {
            res.push(nums[q[0]]);
        }
    }

    return res;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：单调队列单调递减性质维护",
                "detail": "新元素入队前通过 while 循环不断 pop 队尾更小或相等元素，确保队列内对应数值严格单调递减。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：下标索引存贮与超期判定",
                "detail": "队列存储索引而非数值，使得窗口左边界越界判断 if (q[0] <= i - k) 能在 O(1) 内精确判定并 shift 队头。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：窗口成型时机 (i >= k - 1)",
                "detail": "前 k - 1 步仅负责构建初始单调队列而不收集结果，直至第 k - 1 个元素开始每步收集一次窗口最大值。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：均摊复杂度 O(N) 严格证明",
                "detail": "虽然内层存在 while 循环，但数组中每个元素最多被 push 进队一次、pop/shift 出队一次，操作总次数不超过 2N，总时间严格 O(N)。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：极端窗口 k = 1 与 k = N 鲁棒性",
                "detail": "当 k = 1 时每步自成窗口立即收集；当 k = N 时直到最后一步收集一次全局最大值，逻辑覆盖无缝。",
                "weight": 20
            }
        ]
    },
    76: {
        "title_cn": "最小覆盖子串",
        "title_en": "Minimum Window Substring",
        "slug": "minimum-window-substring",
        "difficulty": "Hard",
        "description": """### 题目描述
给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

**注意**：
- 对于 `t` 中重复字符，寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

### 示例 1
- **输入**：`s = "ADOBECODEBANC", t = "ABC"`
- **输出**：`"BANC"`
- **解释**：最小覆盖子串 `"BANC"` 包含来自字符串 `t` 的 'A'、'B' 和 'C'。

### 示例 2
- **输入**：`s = "a", t = "a"`
- **输出**：`"a"`
- **解释**：整个字符串 s 是最小覆盖子串。

### 示例 3
- **输入**：`s = "a", t = "aa"`
- **输出**：`""`
- **解释**：t 中两个字符 'a' 均应包含在子串中，因此没有符合条件的子字符串，返回空字符串。

### 提示与约束条件
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` 和 `t` 由英文字母组成
- 进阶：你能设计一个在 `O(m + n)` 时间内解决此问题的算法吗？""",
        "plain_explanation": """这题是滑动窗口领域登峰造极的压轴题！
大白话比喻成【抓药凑齐方子 + 挤出多余水分】：
目标串 t 就是药方单，里面规定了需要哪些药材（字符）以及各需要几两（频次）。
我们拿着一个可拉伸的袋子（滑动窗口 [left, right]）在药架 s 上抓药：
1. 【右指针大口抓药（寻找可行解）】：
   右指针 right 不断向右跑，每抓到一个药材，袋子里的对应存量加 1。
   当袋子里某种药材的数量恰好达到了药方单的要求时，达标药材种类计数 `matched++`！
2. 【左指针极限挤水分（寻找最优解）】：
   一旦所有药材种类全集齐了（`matched === need.size`），说明当前袋子已经是一个合法的可行解！
   但现在的袋子可能太臃肿了，里面包含了很多废话！
   所以左指针 left 立刻开始向右收缩，把袋子左边的药材往外掏：
   - 只要掏出去之前当前袋子是最短的，赶紧记录下最短长度 `minLen` 和起点 `startIdx`！
   - 掏出去一个字符，看看这个字符是不是关键药材：如果是关键药材且掏出去之后导致库存不足了，那平衡被打破，`matched--`，停止收缩！
3. 接着右指针继续往前走，重复上述过程，直到终点！
整个过程双指针均单向向前走，绝不回头，时间复杂度严格 O(M + N)！""",
        "js_helpers": [
            {
                "name": "need 哈希表与 need.size",
                "what_it_does": "统计 t 中各字符的目标需求量，need.size 代表需要达标的不同字符种类总数。",
                "junior_tip": "以'种类数'作为判断达标的依据，比每次循环都去遍历一遍字典高效成千上万倍！"
            },
            {
                "name": "window.get(c) === need.get(c)",
                "what_it_does": "当窗口内某种字符数量恰好等于需求量时触发 matched++。",
                "junior_tip": "【关键考点】必须使用严格相等 === 触发，只有刚好达标那一瞬间才给 matched 加 1，避免重复多算。"
            },
            {
                "name": "s.slice(startIdx, startIdx + minLen)",
                "what_it_does": "根据记录的最优起点和最小跨度提取最终子串。",
                "junior_tip": "循环内只记录整数数字下标，绝不频繁调用 slice 截取字符串，避免巨大的字符串垃圾回收开销。"
            }
        ],
        "code_js": """/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (!s || !t || s.length < t.length) return "";

    // 步骤 1：统计目标串 t 中各字符的需求数量
    const need = new Map();
    for (const ch of t) {
        need.set(ch, (need.get(ch) || 0) + 1);
    }

    // 记录窗口内各字符的实时数量
    const window = new Map();
    let left = 0;
    let matched = 0; // 记录有多少种字符已经达到 need 要求的数量
    let minLen = Infinity;
    let startIdx = 0;

    // 步骤 2：右指针向右扩展，寻找可行解
    for (let right = 0; right < s.length; right++) {
        const c = s[right];
        window.set(c, (window.get(c) || 0) + 1);

        // 如果字符 c 是目标字符，且窗口内存量恰好达到目标需求，达标种类数加 1
        if (need.has(c) && window.get(c) === need.get(c)) {
            matched++;
        }

        // 步骤 3：当所有字符种类均已集齐，左指针极限向右收缩，寻找局部最优解
        while (matched === need.size) {
            // 刷新历史最小覆盖子串的长度与起始位置
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                startIdx = left;
            }

            // 尝试移出左边界字符
            const leftChar = s[left];
            window.set(leftChar, window.get(leftChar) - 1);

            // 若移出的是关键字符，且移出后数量已低于需求量，则打破全满状态
            if (need.has(leftChar) && window.get(leftChar) < need.get(leftChar)) {
                matched--;
            }

            left++; // 左指针向右收缩
        }
    }

    // 步骤 4：若未找到任何合法子串返回 ""，否则返回截取的最优子串
    return minLen === Infinity ? "" : s.slice(startIdx, startIdx + minLen);
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：需求字典与字符种类计数模型",
                "detail": "构造 need 哈希表记录频次，定义 matched 追踪种类达标数，用 matched === need.size 代替耗时的全表比对。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：右指针扩窗与精准达标触发",
                "detail": "右指针吞字符，唯有 window.get(c) === need.get(c) 临界达成时刻才 matched++，防止多余重复字符导致种类数虚高。",
                "weight": 15
            },
            {
                "dimension": "point3",
                "title": "知识点 3：全满状态下左指针极限收缩",
                "detail": "在 matched === need.size 条件下启动 while 收缩循环，利用挤水分机制动态剥离非必要前导多余字符。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：最优解记录与下标延迟截取",
                "detail": "在收缩内部仅以 startIdx 与 minLen 记录最优坐标区间，不在循环中调用 slice，避免产生高频垃圾对象。",
                "weight": 15
            },
            {
                "dimension": "point5",
                "title": "知识点 5：字符移出与达标状态破损判定",
                "detail": "吐出字符时判断 window.get(leftChar) < need.get(leftChar)，精准令 matched-- 跳出收缩循环，恢复扩窗探索。",
                "weight": 15
            },
            {
                "dimension": "point6",
                "title": "知识点 6：Infinity 兜底与 O(M+N) 时间分析",
                "detail": "初始化 minLen = Infinity 优雅识别无解情景；每个字符最多进窗一次出窗一次，整体复杂度达到神级 O(M+N)。",
                "weight": 15
            }
        ]
    }
}
