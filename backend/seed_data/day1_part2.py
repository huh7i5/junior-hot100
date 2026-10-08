# -*- coding: utf-8 -*-
"""Day 1 Part 2 Problems: 11, 15, 42, 3."""

DAY_1_PART2 = {
    11: {
        "title_cn": "盛最多水的容器",
        "title_en": "Container With Most Water",
        "slug": "container-with-most-water",
        "difficulty": "Medium",
        "description": """### 题目描述
给定一个长度为 `n` 的整数数组 `height`。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])`。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回该容器可以容纳的最大水量。

**说明**：你不能倾斜容器。

### 示例 1
- **输入**：`[1,8,6,2,5,4,8,3,7]`
- **输出**：`49`
- **解释**：图中垂直线代表输入数组 `[1,8,6,2,5,4,8,3,7]`。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49（在下标 1 与 8 之间，宽为 7，高为 min(8, 7) = 7，容积 7 * 7 = 49）。

### 示例 2
- **输入**：`height = [1,1]`
- **输出**：`1`

### 提示与约束条件
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`""",
        "plain_explanation": """大家一定都听过著名的【木桶短板理论】：
一个木桶能装多少水，并不取决于最长的那块木板，而是取决于最矮的那块木板！
在由两条垂线构成的容器中，蓄水量公式为：`容积 = 较矮板的高度 * 两条线之间的底边宽度`。
一开始，我们把左右双指针分别放在数组的最左端和最右端（底边宽度达到理论最大值）。
接下来关键抉择来了：下一步应该移动谁？
【必须移动矮的那根柱子！】
为什么不能移动高柱子？因为你往中间挪一步，底边宽度肯定在缩窄；如果你留着矮柱子，容积的高度上限已经被它封死了，无论内侧高柱子怎么变，新容积只可能更小，绝不可能变大！
唯有把矮柱子往内侧挪动，才有一线生机遇到一根超高柱子，把整体高度提上去，从而逆风翻盘创造更大的蓄水面积！""",
        "js_helpers": [
            {
                "name": "Math.min(height[left], height[right])",
                "what_it_does": "获取左右两根垂直线中较矮的一根作为有效蓄水高度。",
                "junior_tip": "严密吻合木桶短板效应，任何超出短板的水都会从两侧溢出，因此容器高只能取最小值。"
            },
            {
                "name": "Math.max(maxWater, h * w)",
                "what_it_does": "计算当前容积并滚动刷新全局最大蓄水量。",
                "junior_tip": "避免繁琐的书写 if (current > maxWater) maxWater = current，简洁高效。"
            },
            {
                "name": "对撞双指针 (Two Pointers Colliding)",
                "what_it_does": "双指针 left=0 与 right=n-1 向中间夹逼收敛。",
                "junior_tip": "时间复杂度从暴力两两组合的 O(N^2) 戏剧性降低到单次遍历的 O(N)，空间复杂度为极致的 O(1)。"
            }
        ],
        "code_js": """/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    // 步骤 1：左右双指针从两端最大宽度起步
    let left = 0;
    let right = height.length - 1;
    let maxWater = 0;

    // 步骤 2：对撞夹逼，当 left < right 时持续计算
    while (left < right) {
        // 木桶短板高度
        const h = Math.min(height[left], height[right]);
        // 宽度即为两指针索引下标差
        const w = right - left;
        // 步骤 3：刷新全局最大水容量
        maxWater = Math.max(maxWater, h * w);

        // 步骤 4：贪心决策——果断移动较矮的一侧向内探索
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    // 步骤 5：返回历史探测到的最大蓄水量
    return maxWater;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：首尾双指针最大底宽起步",
                "detail": "初始化 left = 0, right = height.length - 1，从底边宽度极限最大处出发，形成基准搜索空间。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：木桶短板决定有效高度",
                "detail": "明确蓄水量公式 Math.min(height[left], height[right]) * (right - left)，高度必须由二者较矮者决定。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：移动短板的贪心证明",
                "detail": "深刻理解若移动长板，底宽缩小的同时高度上限不增反降，容积单调递减；唯有移动短板才可能提升上限获取更大容积。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：等高情况下的移动策略",
                "detail": "当 height[left] === height[right] 时，两边任移一边（或同时内缩）均正确，不影响最终全局最大值的收敛。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：O(N) 遍历保证与空间最优",
                "detail": "每个循环步必有一指针移动，总计移动 N-1 次后双指针相遇终止，时间复杂度严格 O(N)，无额外辅助空间开销（O(1)）。",
                "weight": 20
            }
        ]
    },
    15: {
        "title_cn": "三数之和",
        "title_en": "3Sum",
        "slug": "3sum",
        "difficulty": "Medium",
        "description": """### 题目描述
给你一个整数数组 `nums`，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k`，同时还满足 `nums[i] + nums[j] + nums[k] == 0`。

请你返回所有和为 `0` 且不重复的三元组。

**注意**：答案中不可以包含重复的三元组。

### 示例 1
- **输入**：`nums = [-1,0,1,2,-1,-4]`
- **输出**：`[[-1,-1,2],[-1,0,1]]`
- **解释**：
  - `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`。
  - `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`。
  - `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`。
  - 不同的三元组是 `[-1,0,1]` 和 `[-1,-1,2]`。注意输出的顺序和三元组内部的顺序无关。

### 示例 2
- **输入**：`nums = [0,1,1]`
- **输出**：`[]`
- **解释**：唯一可能的三元组和为 2，不等于 0。

### 示例 3
- **输入**：`nums = [0,0,0]`
- **输出**：`[[0,0,0]]`
- **解释**：唯一可能的三元组和为 0。

### 提示与约束条件
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
- 暴力三重循环的时间复杂度为 `O(N^3)` 会直接超出时间限制 (TLE)""",
        "plain_explanation": """要在数组里找三个加起来等于 0 的数，而且结果不能重复。
如果无脑写三重嵌套循环（O(N^3)），面试官和力扣评测机会直接判你超时。
高手的破题套路叫【排队定锚点，左右两端相亲】：
1. 第一步：先给数组升序排个序！有序性是所有双指针算法的基石。
2. 第二步：用一个指针 i 从头到尾固定第一个人作为【锚点】。
   如果这个锚点 nums[i] 已经大于 0，那因为排过序，后面的所有人也都大于 0，三个正数相加绝不可能等于 0，直接打道回府（提前 break 剪枝）！
3. 第三步：在 i 右边的剩余人群中，放两个相亲指针：左指针 left 守着最小值，右指针 right 守着最大值。
   三数之和为 sum = nums[i] + nums[left] + nums[right]。
   - 如果 sum > 0：太大了，右指针向左迈一步（挑小一点的数）；
   - 如果 sum < 0：太小了，左指针向右迈一步（挑大一点的数）；
   - 如果 sum === 0：命中天命三元组！
4. 本题灵魂大坑【去重】：
   锚点 i 如果和上一个锚点长得一模一样，必须直接跳过；
   找到三元组后，left 和 right 如果碰到和自己相邻相同的数字，也必须通过 while 循环一口气跳过去！否则会收集到重复的一模一样的三元组！""",
        "js_helpers": [
            {
                "name": "nums.sort((a, b) => a - b)",
                "what_it_does": "对数值数组进行真正的升序数值排序。",
                "junior_tip": "【JS 核心必踩坑】千万不要直接写 nums.sort()！JS 的 sort 默认把数字转字符串按 Unicode 码点排，数组 [10, 2] 会排成 [10, 2]！必须传入比较函数 (a, b) => a - b 才是真正的升序。"
            },
            {
                "name": "while 循环跳过重复元素",
                "what_it_does": "在命中目标后，快速推进指针跳过数值相同的元素。",
                "junior_tip": "while (left < right && nums[left] === nums[left + 1]) left++，避免把重复的相同数值推进解集。"
            },
            {
                "name": "res.push([a, b, c])",
                "what_it_does": "将满足条件的合法三元组推入二维结果集中。",
                "junior_tip": "无需额外构造 Set 进行去重，双指针结合有序性原地跳重效率极高。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    // 步骤 1：必须进行数值升序排序（注意传入比较函数）
    nums.sort((a, b) => a - b);
    const res = [];
    const n = nums.length;

    // 步骤 2：外层循环固定第一个基准数字 nums[i]
    for (let i = 0; i < n - 2; i++) {
        // 核心剪枝：若首个基准数已经大于 0，后续数字全为正数，不可能凑出 0，直接终止循环
        if (nums[i] > 0) break;

        // 去重 1：当前基准数若与前一个完全相同，直接跳过，防止生成重复三元组
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        // 步骤 3：在剩余区间 [i + 1, n - 1] 建立对撞双指针
        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                // 命中目标，存入结果集
                res.push([nums[i], nums[left], nums[right]]);

                // 去重 2：跳过所有连续相同的 left 和 right
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;

                // 指针同步向内收缩，寻找下一组可能
                left++;
                right--;
            } else if (sum < 0) {
                // 和太小，左指针右移以增大总和
                left++;
            } else {
                // 和太大，右指针左移以减小总和
                right--;
            }
        }
    }

    return res;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：JS 数组数字排序比较器严密性",
                "detail": "严格调用 nums.sort((a, b) => a - b)，杜绝无参 sort 默认字典序导致负数与两位数排列紊乱的经典语法深坑。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：基准数剪枝 (nums[i] > 0)",
                "detail": "首个数字大于 0 时直接 break，利用有序数组单调性大幅提前截断无解分支，提升运行性能。",
                "weight": 15
            },
            {
                "dimension": "point3",
                "title": "知识点 3：基准数去重逻辑判定 (nums[i] === nums[i - 1])",
                "detail": "比较 nums[i] 与 nums[i - 1] 而非 nums[i + 1]，确保允许同值元素在三元组内部并存（如 [-1, -1, 2]），仅去重跨三元组的起点。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：左右双指针对撞求和与单调收敛",
                "detail": "根据 sum 与 0 的大小关系分别单调推进 left++ 或 right--，在 O(N) 内扫描完该基准下的所有二元对。",
                "weight": 15
            },
            {
                "dimension": "point5",
                "title": "知识点 5：命中目标后的双向连续跳重",
                "detail": "命中后通过 while 循环跳过重复相同值再收敛（left++、right--），杜绝结果集产生重复三元组，彻底免除哈希去重的空间与计算开销。",
                "weight": 15
            },
            {
                "dimension": "point6",
                "title": "知识点 6：整体时间复杂度 O(N^2) 分析",
                "detail": "排序耗时 O(N log N)，外层循环遍历 N 次，内层双指针扫描 O(N)，总耗时严格为 O(N^2)，满足规模限制。",
                "weight": 15
            }
        ]
    },
    42: {
        "title_cn": "接雨水",
        "title_en": "Trapping Rain Water",
        "slug": "trapping-rain-water",
        "difficulty": "Hard",
        "description": """### 题目描述
给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

### 示例 1
- **输入**：`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- **输出**：`6`
- **解释**：上面是由数组 `[0,1,0,2,1,0,1,3,2,1,2,1]` 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

### 示例 2
- **输入**：`height = [4,2,0,3,2,5]`
- **输出**：`9`

### 提示与约束条件
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`
- 进阶目标：能否在 `O(n)` 时间复杂度与 `O(1)` 额外空间复杂度内完成？""",
        "plain_explanation": """接雨水虽然标着 Hard，但只要看透物理本质，大白话特别通透：
想象地上凹凸不平的柱子。你在任何一根柱子 i 上站着，你头顶上能积多少水？
只取决于：【你左边的最高柱子】 和 【你右边的最高柱子】 中，比较矮的那堵墙！
水面最高只能漫到矮墙的高度，再减去你脚下柱子自身的高度，就是这格能存的雨水净体积！
传统做法要开两个数组提前算出每个人左边最高和右边最高（空间 O(N)）。
但极致聪明的【双指针左右夹逼法】可以直接做到 O(1) 空间：
让左指针 left 和右指针 right 从两端往中间缩，实时记录左侧已见最高墙 leftMax 和右侧最高墙 rightMax。
如果 `height[left] < height[right]`，说明当前局势下【左边这堵墙必定是整体木桶的真正短板】！
此时右边哪怕后面有一千米高的天柱，也救不了左边，左边这格能接的水被 leftMax 彻底焊死！
所以我们放心大胆地结算左边：`water += leftMax - height[left]`，然后 left++！
反之如果右边矮，就放心大胆结算右边！一路向中间会师，既快又完全不占内存！""",
        "js_helpers": [
            {
                "name": "leftMax 与 rightMax 动态挡板",
                "what_it_does": "记录遍历过程中左右两侧已探测到的最高柱子高度。",
                "junior_tip": "无需开辟前后缀数组，两个普通数字变量即可维护全局极值状态，把空间消耗压制在 O(1)。"
            },
            {
                "name": "短板优先结算机制",
                "what_it_does": "根据 height[left] < height[right] 判定哪一侧的挡板是绝对受限短板。",
                "junior_tip": "矮的一侧其水线高度已经确定，不受另一侧未知区域更高柱子的干扰，具备严格的局部确定性。"
            },
            {
                "name": "water += leftMax - height[left]",
                "what_it_does": "结算当前柱子顶部的积水量并累加至总容积。",
                "junior_tip": "若当前柱子比历史挡板更高，则刷新挡板；若低于历史挡板，差值即为当前凹坑积蓄的雨水量。"
            }
        ],
        "code_js": """/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if (!height || height.length === 0) return 0;

    // 步骤 1：左右双指针从数组两端出发
    let left = 0;
    let right = height.length - 1;

    // 记录左右两侧目前看到过的最高挡板高度
    let leftMax = 0;
    let rightMax = 0;
    let totalWater = 0;

    // 步骤 2：双指针向中间靠拢汇合
    while (left < right) {
        // 步骤 3：短板效应——较矮那一侧的高度决定了该侧柱子的蓄水上限
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                // 遇到新高柱子，刷新左侧最高挡板
                leftMax = height[left];
            } else {
                // 当前柱子低于左侧最高挡板，雨水灌满差额部分
                totalWater += leftMax - height[left];
            }
            // 推进左指针
            left++;
        } else {
            if (height[right] >= rightMax) {
                // 遇到新高柱子，刷新右侧最高挡板
                rightMax = height[right];
            } else {
                // 当前柱子低于右侧最高挡板，雨水灌满差额部分
                totalWater += rightMax - height[right];
            }
            // 推进右指针
            right--;
        }
    }

    // 步骤 4：返回累加得到的总接雨水量
    return totalWater;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：蓄水微元物理模型推导",
                "detail": "识别下标 i 的接水量为 Math.max(0, Math.min(leftMax, rightMax) - height[i])，将二维面雨水解耦为各列独立计算的累加和。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：双指针两侧动态挡板初始化",
                "detail": "设立 left=0, right=n-1 以及 leftMax=0, rightMax=0，利用局部短板决定性替代全局前后缀数组扫描。",
                "weight": 15
            },
            {
                "dimension": "point3",
                "title": "知识点 3：height[left] 与 height[right] 比较分支",
                "detail": "当 height[left] < height[right] 时，leftMax 必然小于右侧某种界限，左侧短板确立，从而安全结算 left 列。",
                "weight": 15
            },
            {
                "dimension": "point4",
                "title": "知识点 4：挡板高度更新与雨水结算互斥逻辑",
                "detail": "当 height[left] >= leftMax 时只更新挡板不存水；当 height[left] < leftMax 时当前列必然蓄水 leftMax - height[left]。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：单趟双向收敛直至汇合",
                "detail": "左右指针逐步向中间收敛直至相遇，无多余循环，时间复杂度为严格单趟 O(N)。",
                "weight": 15
            },
            {
                "dimension": "point6",
                "title": "知识点 6：常数空间 O(1) 优越性证明",
                "detail": "无需申请前后缀 max 辅助数组或单调栈节点内存，空间复杂度严格常数级 O(1)，面试答辩表现完美。",
                "weight": 15
            }
        ]
    },
    3: {
        "title_cn": "无重复字符的最长子串",
        "title_en": "Longest Substring Without Repeating Characters",
        "slug": "longest-substring-without-repeating-characters",
        "difficulty": "Medium",
        "description": """### 题目描述
给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

### 示例 1
- **输入**: `s = "abcabcbb"`
- **输出**: `3` 
- **解释**: 因为无重复字符的最长子串是 `"abc"`，所以其长度为 3。

### 示例 2
- **输入**: `s = "bbbbb"`
- **输出**: `1`
- **解释**: 因为无重复字符的最长子串是 `"b"`，所以其长度为 1。

### 示例 3
- **输入**: `s = "pwwkew"`
- **输出**: `3`
- **解释**: 因为无重复字符的最长子串是 `"wke"`，所以其长度为 3。
  请注意，你的答案必须是 **子串** 的长度，`"pwke"` 是一个子序列，不是子串。

### 提示与约束条件
- `0 <= s.length <= 5 * 10^4`
- `s` 由英文字母、数字、符号和空格组成""",
        "plain_explanation": """这是滑动窗口（Sliding Window）思想的绝对基石经典题！
想象一个可以伸缩的滑动照相机镜头：
左指针 left 是镜头的左边框，右指针 right 是镜头的右边框。
右指针不断向右扩展，把新的字符一个接一个吞进镜头里。
同时我们准备一个 Map 备忘录，随时记录：【每个字符最近一次在哪个下标露过脸】。
如果新吞进来的字符 ch 在 Map 里查到了，说明镜头里'撞车'了，出现了重复字符！
这时候怎么办？
最笨的办法是把左边框一格一格往右挪，直到把撞车的字符挤出去（时间较慢）。
最帅的办法是【瞬移大法】：直接把左指针 left 瞬移到撞车字符上一次露面位置的下一位！
但这里有一个超级致命细节：
【如果撞车的字符已经在当前镜头的左边框外面了（比 left 还小），绝对不能把 left 往回拉！】
所以必须写成：`left = Math.max(left, map.get(ch) + 1)`，保证左边框永远单调向前冲！
镜头每走一步，量一下当前的镜头宽度 `right - left + 1`，历史最大宽度就是答案！""",
        "js_helpers": [
            {
                "name": "new Map()",
                "what_it_does": "存储 { 字符 => 该字符最后一次出现的位置下标 }。",
                "junior_tip": "比遍历查找快极多，配合 map.has() 与 map.get() 达成 O(1) 瞬时位置检索。"
            },
            {
                "name": "Math.max(left, map.get(ch) + 1)",
                "what_it_does": "更新左指针位置，确保左指针只能向前跳跃，绝不向后倒退！",
                "junior_tip": "【高频易错点】如果之前出现过的字符早在当前窗口左边界之前（已经被滑过去了），如果不做 Math.max，left 会倒退回到老位置导致死循环或算错。"
            },
            {
                "name": "Math.max(maxLen, right - left + 1)",
                "what_it_does": "动态结算当前无重复窗口的长度并刷新历史最大值。",
                "junior_tip": "窗口闭区间 [left, right] 的元素个数公式为 right - left + 1。"
            }
        ],
        "code_js": """/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // 步骤 1：准备 Map 记录 { 字符 => 该字符最近一次出现的下标 }
    const map = new Map();
    let left = 0;
    let maxLen = 0;

    // 步骤 2：右指针逐步单向扩大窗口
    for (let right = 0; right < s.length; right++) {
        const ch = s[right];

        // 步骤 3：若字符此前出现过，左指针瞬移到上一次出现位置的下一个位置
        // 注意：必须使用 Math.max 严防左指针倒退到当前窗口左侧的历史废弃区域
        if (map.has(ch)) {
            left = Math.max(left, map.get(ch) + 1);
        }

        // 步骤 4：在 Map 中更新该字符最新的坐标记录
        map.set(ch, right);

        // 步骤 5：刷新无重复子串的历史最大长度
        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：滑动窗口双指针状态机模型",
                "detail": "确立 [left, right] 始终为无重复字符的合法子串区间，right 负责进窗勘测，left 负责违规收缩。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：哈希表字符最近坐标动态映射",
                "detail": "使用 Map 记录每个字符最新出现的索引下标，实现检测到冲突时的 O(1) 跃迁跳跃。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：Math.max 防左指针历史回退",
                "detail": "深刻理解 left = Math.max(left, map.get(ch) + 1) 的防御机制，规避历史淘汰字符将 left 拽回窗口之外的经典陷阱。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：动态区间长度计算与极值更新",
                "detail": "在每一步无冲突确认后，以 right - left + 1 准确度量当前子串跨度，并使用 Math.max 持续跟踪全局最优解。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：单趟 O(N) 线性时间与极端边界安全",
                "detail": "right 指针单调遍历一次，字符串为空时循环 0 次返回 0，单字符输入返回 1，时空复杂度达到工业级最优。",
                "weight": 20
            }
        ]
    }
}
