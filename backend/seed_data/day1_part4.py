# -*- coding: utf-8 -*-
"""Day 1 Part 4 Problems: 53, 56, 189, 238, 41."""

DAY_1_PART4 = {
    53: {
        "title_cn": "最大子数组和",
        "title_en": "Maximum Subarray",
        "slug": "maximum-subarray",
        "difficulty": "Medium",
        "description": """### 题目描述
给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

### 示例 1
- **输入**：`nums = [-2,1,-3,4,-1,2,1,-5,4]`
- **输出**：`6`
- **解释**：连续子数组 `[4,-1,2,1]` 的和最大，为 `6`。

### 示例 2
- **输入**：`nums = [1]`
- **输出**：`1`

### 示例 3
- **输入**：`nums = [5,4,-1,7,8]`
- **输出**：`23`

### 提示与约束条件
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- 进阶：如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的分治法求解。""",
        "plain_explanation": """求连续子数组的最大和，这就是大名鼎鼎的 Kadane 算法。
大白话的核心原则叫【断舍离，远离负资产】：
想象你在做生意投资，从前往后一路走，账本上记录着当前累计的收益 `currentSum`。
每走到一家新公司（数字 nums[i]）：
你面临两个抉择：
1. 【带上之前的团队】：把自己当前的收益加上之前的累计收益（`currentSum + nums[i]`）；
2. 【自立门户，独立开张】：把之前的包袱全部扔掉，直接从自己这笔资金 `nums[i]` 开始从头做起！
什么时候自立门户？
【当之前的累计收益是负数的时候！】
负数就是彻头彻尾的负资产、猪队友，带上它只会拖累你当前的收益，没有任何正面贡献！
所以只要发现带上之前还不如自己单干，果断断舍离（`currentSum = Math.max(nums[i], currentSum + nums[i])`）！
每走一步，拿当前的累计收益跟历史最高峰 `maxSum` 比较一下，走到终点，历史最高峰就是答案！""",
        "js_helpers": [
            {
                "name": "Math.max(nums[i], currentSum + nums[i])",
                "what_it_does": "Kadane 算法的核心状态转移方程。",
                "junior_tip": "如果之前的累计和 currentSum < 0，两者取大就会果断舍弃过去，以 nums[i] 作为新起点开始累加。"
            },
            {
                "name": "初始值设为 nums[0] 而非 0",
                "what_it_does": "令 currentSum 与 maxSum 初始均等于 nums[0]。",
                "junior_tip": "【常见死穴】如果把初始值设为 0，当数组全为负数（如 [-2, -1]）时，算法会错误返回 0！必须初始化为 nums[0]。"
            },
            {
                "name": "O(1) 滚动变量空间压缩",
                "what_it_does": "无需开辟 dp 数组存储每个状态，仅用两个变量在单趟扫描中完成全部计算。",
                "junior_tip": "将空间复杂度从 O(N) 压缩至 O(1)，极为精炼优雅。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    // 步骤 1：初始账本从第一个数字起步（防全负数死穴）
    let currentSum = nums[0];
    let maxSum = nums[0];

    // 步骤 2：从第二个数字开始线性遍历
    for (let i = 1; i < nums.length; i++) {
        // 步骤 3：核心决策——若之前累计收益为负，果断自立门户从当前数字重新开始
        currentSum = Math.max(nums[i], currentSum + nums[i]);

        // 步骤 4：刷新历史见过的最大子数组和
        maxSum = Math.max(maxSum, currentSum);
    }

    // 步骤 5：返回全局最大和
    return maxSum;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：初始值对准 nums[0] 规避负数死穴",
                "detail": "坚决禁止初始化为 0，防范全为负数（例如 [-3, -1, -2]）时误输出 0 的典型逻辑漏洞。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：Kadane 状态转移与断舍离决策",
                "detail": "理解 currentSum = Math.max(nums[i], currentSum + nums[i]) 本质为动态规划，识别前驱为负时重开子数组起点的必要性。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：单趟 O(N) 线性扫描机制",
                "detail": "从下标 1 循环到 n - 1，每个元素仅访问一次，时间复杂度严格为 O(N)。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：全局历史极值动态追踪",
                "detail": "使用 maxSum = Math.max(maxSum, currentSum) 独立维护历史见过的最优解，与局部最优状态更新解耦。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：常数空间 O(1) 优化与单元素覆盖",
                "detail": "单元素数组输入自然跳过循环返回 nums[0]，空间复杂度 O(1)，逻辑严密完备。",
                "weight": 20
            }
        ]
    },
    56: {
        "title_cn": "合并区间",
        "title_en": "Merge Intervals",
        "slug": "merge-intervals",
        "difficulty": "Medium",
        "description": """### 题目描述
以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 **一个不重叠的区间数组**，该数组需恰好覆盖输入中的所有区间 。

### 示例 1
- **输入**：`intervals = [[1,3],[2,6],[8,10],[15,18]]`
- **输出**：`[[1,6],[8,10],[15,18]]`
- **解释**：区间 `[1,3]` 和 `[2,6]` 重叠，将它们合并为 `[1,6]`。

### 示例 2
- **输入**：`intervals = [[1,4],[4,5]]`
- **输出**：`[[1,5]]`
- **解释**：区间 `[1,4]` 和 `[4,5]` 可被视为重叠区间。

### 提示与约束条件
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`""",
        "plain_explanation": """有一堆可能互相重叠的会议时间段（比如 [1, 3] 和 [2, 6]），要求把冲突撞车的会议合并成一个大区间（[1, 6]）。
如果乱七八糟没有顺序，每次合并一个区间都得回头扫一遍，复杂度直接爆表。
破解此题的无敌招式叫【时间线上按开始时间排队】：
1. 第一步：先按每个区间的【开始时间】进行升序排序！
   排序之后，所有的区间就按照时间先后的顺序整整齐齐地排在时间轴上了。
2. 第二步：我们把第一个区间先放进结果集 `merged` 里作为基准。
3. 第三步：从第二个区间开始往后看：
   - 如果当前新区间的开始时间 `current[0]` <= 上一个区间的结束时间 `last[1]`：
     说明两个会议【撞车了】！
     合并它们！怎么合并？开始时间不变，结束时间拉长到两者的最大值（`last[1] = Math.max(last[1], current[1])`）！
     注意一定要用 Math.max，因为可能出现大区间完全包住小区间的情况（比如 [1, 5] 和 [2, 3] 合并依然是 [1, 5]）。
   - 如果当前区间的开始时间 > 上一个区间的结束时间：
     说明两者互不干扰，这是一个崭新的独立会议，直接 push 进结果集即可！
一趟看下来，所有区间合并得干干净净！""",
        "js_helpers": [
            {
                "name": "intervals.sort((a, b) => a[0] - b[0])",
                "what_it_does": "对二维区间数组按照左端点（起始时间）进行升序排序。",
                "junior_tip": "【核心前提】排序消除了后效性，保证了在遍历到区间 i 时，前面所有区间的起始时间必定不大于当前区间。"
            },
            {
                "name": "merged[merged.length - 1]",
                "what_it_does": "获取已合并结果集中的最后一个区间进行对比与原地修改。",
                "junior_tip": "JavaScript 中利用引用类型对象的特性，直接修改 last[1] 即可就地延长结果集里的区间右边界。"
            },
            {
                "name": "Math.max(last[1], current[1])",
                "what_it_does": "合并重叠区间时更新右端点最大值。",
                "junior_tip": "防止完全包含（如 [1, 10] 与 [2, 6]），必须取二者右端点的最大值。"
            }
        ],
        "code_js": """/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (intervals.length <= 1) return intervals;

    // 步骤 1：按区间的起始左端点升序排序，理顺时间线
    intervals.sort((a, b) => a[0] - b[0]);

    // 步骤 2：以第一个区间作为合并基准放入结果集
    const merged = [intervals[0]];

    // 步骤 3：单趟遍历后续所有区间
    for (let i = 1; i < intervals.length; i++) {
        const current = intervals[i];
        const last = merged[merged.length - 1];

        // 步骤 4：当前区间起点 <= 上个区间终点，说明发生重叠撞车
        if (current[0] <= last[1]) {
            // 合并右端点，取两者的较大值（兼容完全包含场景）
            last[1] = Math.max(last[1], current[1]);
        } else {
            // 无重叠，作为全新的独立区间加入结果列表
            merged.push(current);
        }
    }

    // 步骤 5：返回合并后的无重叠区间集合
    return merged;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：区间左端点排序消除后效性",
                "detail": "使用 intervals.sort((a, b) => a[0] - b[0]) 顺排时间线，将原本两两比较的二维网状关系转化为一维顺序扫描。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：结果集首项基准初始化",
                "detail": "声明 const merged = [intervals[0]]，以首个区间为锚点，为后续连续增量合并提供比对实体。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：重叠判定临界条件 (current[0] <= last[1])",
                "detail": "深刻理解端点相接（例如 [1, 4] 与 [4, 5]）亦属重叠，必须采用 <= 判定而非严格 <。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：Math.max 右边界延伸融合同步",
                "detail": "通过 last[1] = Math.max(last[1], current[1]) 就地拉伸右端点，兼容完全包含嵌套区间的场景。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：独立区间推入与时空性能证明",
                "detail": "不重叠时执行 merged.push(current)；总耗时为排序 O(N log N) + 线性合并 O(N)，额外空间为 O(N)。",
                "weight": 20
            }
        ]
    },
    189: {
        "title_cn": "轮转数组",
        "title_en": "Rotate Array",
        "slug": "rotate-array",
        "difficulty": "Medium",
        "description": """### 题目描述
给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

### 示例 1
- **输入**: `nums = [1,2,3,4,5,6,7], k = 3`
- **输出**: `[5,6,7,1,2,3,4]`
- **解释**:
  - 向右轮转 1 步: `[7,1,2,3,4,5,6]`
  - 向右轮转 2 步: `[6,7,1,2,3,4,5]`
  - 向右轮转 3 步: `[5,6,7,1,2,3,4]`

### 示例 2
- **输入**：`nums = [-1,-100,3,99], k = 2`
- **输出**：`[3,99,-1,-100]`
- **解释**: 
  - 向右轮转 1 步: `[99,-1,-100,3]`
  - 向右轮转 2 步: `[3,99,-1,-100]`

### 提示与约束条件
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`
- **进阶要求**：使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题。""",
        "plain_explanation": """把数组向右旋转 k 步，看似简单，但题目进阶要求【原地修改且额外空间为 O(1)】！
如果你用临时数组拷贝，空间是 O(N)；如果你每次往右挪一步挪 k 次，时间是 O(k * N) 直接超时！
计算机科学中最优雅神奇的解法叫【三步大翻转法】：
以 `[1, 2, 3, 4, 5, 6, 7]`, `k = 3` 为例：
1. 【第 1 步：全员大反转！】
   把整个数组彻底倒立反过来：
   `[1, 2, 3, 4, 5, 6, 7]` 变成 `[7, 6, 5, 4, 3, 2, 1]`！
   这时候你看：原本在最后面的 3 个数 `[5, 6, 7]` 已经被成功运送到了队伍的最前面 `[7, 6, 5]`！
2. 【第 2 步：前 k 个元素内部反转！】
   把前面这 k 个数 `[7, 6, 5]` 内部倒立一次，恢复正序：
   变成 `[5, 6, 7, 4, 3, 2, 1]`！
3. 【第 3 步：后半截元素内部反转！】
   把剩下的 `n - k` 个数 `[4, 3, 2, 1]` 内部倒立一次，恢复正序：
   变成 `[5, 6, 7, 1, 2, 3, 4]`！
瞬间大功告成！三步翻转，原地实现，空间干净利落的严格 O(1)！""",
        "js_helpers": [
            {
                "name": "k = k % nums.length (取模防溢出)",
                "what_it_does": "防止轮转步数 k 大于或等于数组实际长度 n。",
                "junior_tip": "【必加防线】如果数组长度为 5，轮转 7 步其实等价于轮转 7 % 5 = 2 步；如果 k 是 5 的倍数则相当于完全不动。"
            },
            {
                "name": "双指针 reverse(start, end) 翻转辅助函数",
                "what_it_does": "用 while (start < end) 和解构赋值就地对调指定区间段。",
                "junior_tip": "[nums[start], nums[end]] = [nums[end], nums[start]]，优雅原地置换。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} 原地修改，不要返回值
 */
var rotate = function(nums, k) {
    const n = nums.length;
    // 步骤 1：取模运算，过滤掉整圈循环的冗余步数
    k = k % n;
    if (k === 0) return;

    // 辅助函数：原地反转闭区间 [start, end] 内的所有元素
    const reverse = (start, end) => {
        while (start < end) {
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    };

    // 步骤 2：全员大反转——将目标末尾元素送至前部
    reverse(0, n - 1);

    // 步骤 3：前 k 个元素内部反转，恢复相对正序
    reverse(0, k - 1);

    // 步骤 4：后 n - k 个元素内部反转，恢复相对正序
    reverse(k, n - 1);
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：k %= n 模运算周期性规整",
                "detail": "识别轮转周期的等价性，防范 k >= n 甚至远大于 n 时引发的非法越界截断异常。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：双指针 reverse 工具函数闭环",
                "detail": "熟练实现基于 while (start < end) 与 ES6 解构的原地闭区间反转逻辑，空间纯度 O(1)。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：全数组翻转将后置块置前",
                "detail": "第一步 reverse(0, n - 1) 颠倒全局，使得原本位于末端的后 k 个元素成功换至前 k 个槽位。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：前后两段分段局部复原",
                "detail": "先后调用 reverse(0, k - 1) 与 reverse(k, n - 1)，分别修正前段与后段内部被反转颠倒的次序。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：原地原地修改与 O(1) 空间达标",
                "detail": "全过程无需额外数组分配，时间复杂度为 2N 即 O(N)，严格达成进阶原地空间 O(1) 指标。",
                "weight": 20
            }
        ]
    },
    238: {
        "title_cn": "除自身以外数组的乘积",
        "title_en": "Product of Array Except Self",
        "slug": "product-of-array-except-self",
        "difficulty": "Medium",
        "description": """### 题目描述
给你一个整数数组 `nums`，返回数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。

**请不要使用除法**，且在 `O(n)` 时间复杂度内完成此题。

### 示例 1
- **输入**: `nums = [1,2,3,4]`
- **输出**: `[24,12,8,6]`
- **解释**: 
  - 下标 0: 2*3*4 = 24
  - 下标 1: 1*3*4 = 12
  - 下标 2: 1*2*4 = 8
  - 下标 3: 1*2*3 = 6

### 示例 2
- **输入**: `nums = [-1,1,0,-3,3]`
- **输出**: `[0,0,9,0,0]`

### 提示与约束条件
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- 输入保证任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内
- **严格禁令**：不能使用除法！
- **进阶要求**：你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）""",
        "plain_explanation": """每个格子的答案是'除了自己以外所有人的乘积'。
正常人第一反应是：算一个所有数字的总乘积，然后遍历每个人拿总乘积除以自己。
但是！【题目明文严禁使用除法】！
而且如果数组里有 0，除法直接除以零报错崩溃；如果有两个 0，答案全为 0。
那怎么在不能做除法的情况下算出答案？
大白话秘诀叫【左右邻居前后夹击法】：
任何一个数 nums[i]，除了它自己，剩下的所有人不就是：
【它左边所有人的乘积】 乘以 【它右边所有人的乘积】 嘛！
我们分两趟漫步搞定：
1. 【第一趟：从左往右走（收集前缀积）】：
   拿一个变量 `leftProduct = 1`。走到每个位置 i，先把左边所有人的累乘积记到答案 `res[i]` 里，然后把当前的 `nums[i]` 乘进 `leftProduct`。
   走完后，每个人的格子里已经装好了它左边所有人的乘积！
2. 【第二趟：从右往左走（乘以后缀积）】：
   拿一个变量 `rightProduct = 1`。从最右边往前退，走到每个位置 i，把当前的 `res[i]` 乘上右边所有人的累乘积（`res[i] *= rightProduct`），然后把当前的 `nums[i]` 乘进 `rightProduct`。
两趟走完，每个位置刚好就是左边乘积 * 右边乘积！输出数组不算额外空间，额外辅助内存严格 O(1)！""",
        "js_helpers": [
            {
                "name": "new Array(n).fill(1)",
                "what_it_does": "开辟长度为 n 的结果数组，所有位置初始化为乘法单位元 1。",
                "junior_tip": "乘法的基底必须是 1（如果误填成 0，任何数乘 0 都是 0，全盘皆输）。"
            },
            {
                "name": "单变量 leftProduct 与 rightProduct 滚动累乘",
                "what_it_does": "分别维护从左往右和从右往左的动态乘积值。",
                "junior_tip": "无需开辟两个长为 n 的前后缀数组，直接就地复用输出数组 res，满足进阶 O(1) 额外空间要求。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    // 步骤 1：初始化答案数组为 1
    const res = new Array(n).fill(1);

    // 步骤 2：第一趟——从左向右收集每个元素左侧的所有数乘积（前缀积）
    let leftProduct = 1;
    for (let i = 0; i < n; i++) {
        // 当前位置等于左边所有人累乘的结果
        res[i] = leftProduct;
        // 把当前数字乘入前缀积，留给下一个位置使用
        leftProduct *= nums[i];
    }

    // 步骤 3：第二趟——从右向左动态累乘每个元素右侧的所有数乘积（后缀积）
    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        // 现有结果（左乘积）乘以右侧所有人的乘积
        res[i] *= rightProduct;
        // 把当前数字乘入后缀积，留给前一个位置使用
        rightProduct *= nums[i];
    }

    // 步骤 4：返回构建完成的答案数组
    return res;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：除法禁令与零除异常痛点分析",
                "detail": "识别除法在此题中的禁用规定，以及数组含单个 0 或多个 0 时除法失效的致命缺陷，确立前后缀分解基调。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：乘法单位元 1 初始化基底",
                "detail": "使用 new Array(n).fill(1) 并设置初始乘积变量为 1，杜绝误置 0 导致的清零逻辑灾难。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：正向遍历沉淀左侧前缀积",
                "detail": "第一趟循环中先执行 res[i] = leftProduct 后更新 leftProduct *= nums[i]，严守除自身外的排他原则。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：反向遍历滚动融合右侧后缀积",
                "detail": "第二趟倒序扫描中通过 res[i] *= rightProduct 原地结合，无需额外申请后缀数组内存空间。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：O(N) 线性耗时与 O(1) 额外空间合规",
                "detail": "两次单层循环总耗时 2N，额外辅助内存除题目允许的返回值 res 外仅有两个标量变量，严格达成进阶规范。",
                "weight": 20
            }
        ]
    },
    41: {
        "title_cn": "缺失的第一个正数",
        "title_en": "First Missing Positive",
        "slug": "first-missing-positive",
        "difficulty": "Hard",
        "description": """### 题目描述
给你一个未排序的整数数组 `nums` ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 `O(n)` 并且只使用常数级别额外空间 `O(1)` 的解决方案。

### 示例 1
- **输入**：`nums = [1,2,0]`
- **输出**：`3`
- **解释**：范围 [1,2] 中的数字都在数组中。

### 示例 2
- **输入**：`nums = [3,4,-1,1]`
- **输出**：`2`
- **解释**：1 在数组中，但 2 没有。

### 示例 3
- **输入**：`nums = [7,8,9,11,12]`
- **输出**：`1`
- **解释**：最小的正整数 1 缺失。

### 提示与约束条件
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- 进阶硬指标：时间复杂度必须为 `O(n)`，额外空间复杂度严格为 `O(1)`。""",
        "plain_explanation": """数组长度为 n，它里面缺失的第一个正整数，答案只可能在 `1` 到 `n + 1` 之间（抽屉鸽巢原理）！
如果允许开一个长度为 n 的布尔哈希表，这题就是入门题；但题目严禁额外空间（必须严格 O(1)）！
这就要亮出传说中的神级操作：【原地哈希（萝卜各回各坑）】！
既然我们不能买新抽屉，那就把【原数组 nums 自身当成现成的抽屉门牌号】：
- 数字 1 的家应该在 `nums[0]`；
- 数字 2 的家应该在 `nums[1]`；
- ... 数字 x 的家应该在 `nums[x - 1]`！
我们像宿管阿姨一样从第 0 个房间开始检查：
如果发现当前房间里的数字 x 是一个有效正数（在 1 到 n 之间），并且它【还没回到属于它自己的坑位】上：
阿姨立刻把它和它目标坑位 `nums[x - 1]` 上的数字对调！
【防死锁大坑】：对调之前一定要确认目标坑位上是不是已经有了一个一模一样的 x！如果已经有了，绝不能继续换，否则两个相同数字疯狂对调陷入死循环！
当前房间换完之后，可能新换过来的数字也还没回坑，所以用 while 循环继续换，直到换好或者当前数字超出 1..n 范围。
所有房间整顿完毕后，阿姨从头到尾复查一遍：
第一个满足 `nums[i] !== i + 1` 的房间，那缺失的最小正整数就是 `i + 1`！
如果 1 到 n 号坑位全部完美就位，那缺失的就是 `n + 1`！""",
        "js_helpers": [
            {
                "name": "targetIdx = nums[i] - 1",
                "what_it_does": "将正整数数值 x 映射为数组索引下标 x - 1。",
                "junior_tip": "数值 1 归位至索引 0，数值 n 归位至索引 n - 1，实现原地自映射。"
            },
            {
                "name": "while 原地置换循环",
                "what_it_does": "交换后新换到当前位置的数字可能仍然需要继续归位，通过 while 持续置换直至无法归位。",
                "junior_tip": "每个数字一旦归位后就再也不会被移走，因此全数组置换总次数不超过 N 次，均摊时间依然是严格 O(N)。"
            },
            {
                "name": "nums[nums[i] - 1] !== nums[i] (死循环防线)",
                "what_it_does": "检查目标坑位上的数字是否已经与当前数字相同。",
                "junior_tip": "【最高频死循环坑】当数组存在重复数字（如 [1, 1]）时，若不加此判断，nums[0] 和 nums[0] 会无限对调引发进程卡死。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const n = nums.length;

    // 步骤 1：原地哈希——将属于 [1, n] 范围内的正整数 x 归位到下标 x - 1
    for (let i = 0; i < n; i++) {
        // 条件：数字在 [1, n] 合法范围内，且它当前还没回到自己的坑位（且目标坑位不是相同值）
        while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] !== nums[i]) {
            const targetIdx = nums[i] - 1;
            // 原地交换：将 nums[i] 送到属于它的 targetIdx 坑位
            [nums[i], nums[targetIdx]] = [nums[targetIdx], nums[i]];
        }
    }

    // 步骤 2：二次线性遍历，寻找首个违和、未曾归位的坑位
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) {
            // 坑位 i 对应的应是 i + 1，未匹配说明 i + 1 就是缺失的最小正整数
            return i + 1;
        }
    }

    // 步骤 3：若 [1, n] 所有坑位均完美归位，则缺失的一定是 n + 1
    return n + 1;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：鸽巢原理界定答案值域 [1, n + 1]",
                "detail": "深刻理解长度为 n 的数组最多容纳 n 个互异正整数，缺失的最小正数必然落在 [1, n + 1] 的闭区间内部。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：原地自哈希映射规则 (x => x - 1)",
                "detail": "复用输入数组充当哈希桶，将正整数 x 安置于下标 x - 1 处，省去常规哈希表的 O(N) 空间分配开销。",
                "weight": 15
            },
            {
                "dimension": "point3",
                "title": "知识点 3：while 持续安置与死循环防御",
                "detail": "置换条件必须包含 nums[nums[i] - 1] !== nums[i]，彻底防范重复数字在同一坑位导致的死锁无限循环。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：均摊复杂度严格 O(N) 证明",
                "detail": "每次有效置换必然使得至少一个萝卜回到终身正确的坑位，置换上限为 N 次，结合两轮遍历总耗时稳稳为 O(N)。",
                "weight": 15
            },
            {
                "dimension": "point5",
                "title": "知识点 5：二次遍历识别首个未就绪坑位",
                "detail": "从左向右扫描，若 nums[i] !== i + 1 则即刻 return i + 1，体现局部贪心与首个极小正数查找原理。",
                "weight": 15
            },
            {
                "dimension": "point6",
                "title": "知识点 6：全量完备情形兜底返回 n + 1",
                "detail": "当数组恰为 [1, 2, ..., n] 完整连续正整数时，顺利通过二次遍历，末尾兜底返回 n + 1，逻辑圆满无死角。",
                "weight": 15
            }
        ]
    }
}
