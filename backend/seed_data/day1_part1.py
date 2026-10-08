# -*- coding: utf-8 -*-
"""Day 1 Part 1 Problems: 1, 49, 128, 283."""

DAY_1_PART1 = {
    1: {
        "title_cn": "两数之和",
        "title_en": "Two Sum",
        "slug": "two-sum",
        "difficulty": "Easy",
        "description": """### 题目描述
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target` 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

### 示例 1
- **输入**：`nums = [2,7,11,15], target = 9`
- **输出**：`[0,1]`
- **解释**：因为 `nums[0] + nums[1] == 9`，返回 `[0, 1]`。

### 示例 2
- **输入**：`nums = [3,2,4], target = 6`
- **输出**：`[1,2]`
- **解释**：因为 `nums[1] + nums[2] == 6`，返回 `[1, 2]`。

### 示例 3
- **输入**：`nums = [3,3], target = 6`
- **输出**：`[0,1]`
- **解释**：因为 `nums[0] + nums[1] == 6`，返回 `[0, 1]`。

### 提示与约束条件
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **只会存在一个有效答案**""",
        "plain_explanation": """想象你去超市买东西，口袋里揣着一张目标总金额 target 的清单。
货架上自左向右摆放着一排商品，标价分别为 nums[i]。
你推着购物车往前走，每看到一件标价为 x 的商品，脑子里立刻心算：'我还需要一件标价为 diff = target - x 的商品来凑单'。
最笨的办法是每拿一件商品，都把整个超市从头到尾再逛一遍（双重暴力循环 O(N^2)，太消耗体力）。
最聪明的办法是准备一本随身记事本（JavaScript 的 Map）：
每经过一个商品 x，先翻开记事本查一查：'之前有没有见过标价为 diff 的商品？'
如果记事本里记录过，说明天作之合找到了！立刻把记事本里记录的那个商品货架号与当前货架号一起打包返回；
如果没查到，就把当前商品的价格 x 与货架号 i 记入本子，继续往前看。
整趟旅程只需走一遍超市（时间 O(N)），这就是空间换时间的极致精髓！""",
        "js_helpers": [
            {
                "name": "new Map()",
                "what_it_does": "创建一个哈希映射字典，用来存储键值对 (key => value)。",
                "junior_tip": "小白常问：为什么不用普通对象 `{}`？因为在 JS 中，对象的 key 会被强制转成字符串（比如数字 1 变成字符串 '1'），而 Map 的 key 可以保持原始数字类型；并且 Map 在高频增删查改时底层引擎优化更好，判断存在直接用 map.has()，干净又高效。"
            },
            {
                "name": "map.has(key) 与 map.get(key)",
                "what_it_does": "map.has() 返回布尔值检查 key 是否存在；map.get() 获取该 key 对应存储的值。",
                "junior_tip": "哈希表的查找时间复杂度是 O(1)，近乎瞬间完成。这是本算法把两重暴力嵌套循环缩减为单层线性遍历的关键武器。"
            },
            {
                "name": "map.set(key, value)",
                "what_it_does": "往 Map 中添加或更新一条记录。",
                "junior_tip": "这里用来把当前数字当 key，把它的数组下标 i 当 value 存起来，方便后续数字来相亲配对。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // 步骤 1：准备一个哈希表 Map，用来存 { 遍历过的数字 => 它的下标 }
    const map = new Map();

    // 步骤 2：单层循环遍历数组中的每一个数字
    for (let i = 0; i < nums.length; i++) {
        const current = nums[i];
        // 计算当前数字想要凑成 target，还差几？
        const diff = target - current;

        // 步骤 3：翻看备忘录，看看差值 diff 之前有没有出现过
        if (map.has(diff)) {
            // 找到了！返回备忘录里记录的那个数字的下标，以及当前数字的下标
            return [map.get(diff), i];
        }

        // 步骤 4：没找到就把自己存进备忘录，等待后面的数字来配对
        map.set(current, i);
    }

    // 兜底返回空数组（按题意必定有解）
    return [];
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：哈希映射数据结构选取",
                "detail": "使用 ES6 Map 而非普通 Object，利用 Map 保持数字键类型的特性，规避对象隐式将数字键转换为字符串带来的微小性能开销与潜在类型混乱。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：单趟遍历与补数动态计算",
                "detail": "将暴力枚举 O(N^2) 降至 O(N) 的关键是将 a + b = target 转化为 target - a = b，在向前遍历的同时动态计算期待的互补数字 diff。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：哈希表 O(1) 瞬时探测",
                "detail": "利用 map.has(diff) 进行常数级别复杂度的存在性校验，一旦命中即刻通过 map.get(diff) 提取历史索引并返回，实现早停机制。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：边查边存彻底杜绝自身复用",
                "detail": "严格遵守'先查询、后入表'的顺序。若提前把当前元素放入 Map，在 target - current === current（如 target=6, nums[0]=3）时会直接匹配到自身造成致命 Bug。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：负数与大数边界鲁棒性",
                "detail": "该解法天然支持负数与零（例如 nums=[-3,4,3,90], target=0），算术差值计算在 JS 安全整数范围内完全准确，空间复杂度严格为 O(N)。",
                "weight": 20
            }
        ]
    },
    49: {
        "title_cn": "字母异位词分组",
        "title_en": "Group Anagrams",
        "slug": "group-anagrams",
        "difficulty": "Medium",
        "description": """### 题目描述
给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

**字母异位词** 是由重新排列源单词的所有字母得到的一个新单词。

### 示例 1
- **输入**: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **输出**: `[["bat"],["nat","tan"],["ate","eat","tea"]]`
- **解释**: 
  - `"bat"` 没有其他字母异位词，独占一组。
  - `"nat"` 和 `"tan"` 字母组成相同（1个a，1个n，1个t）。
  - `"ate"`, `"eat"`, `"tea"` 字母组成相同（1个a，1个e，1个t）。

### 示例 2
- **输入**: `strs = [""]`
- **输出**: `[[""]]`

### 示例 3
- **输入**: `strs = ["a"]`
- **输出**: `[["a"]]`

### 提示与约束条件
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` 仅包含小写英文字母""",
        "plain_explanation": """什么是字母异位词？比如 'eat', 'tea', 'ate'，虽然字母排列顺序不同，但它们包含的字母种类和数量完全一样（都是 1个a、1个e、1个t）。
把它们归类，就好像班主任给学生分宿舍：
不管学生们入场时怎么排队，只要把每个人的名字拼音按字母表升序重新排个序，排完后的新名字都叫做 'aet'。
这个唯一的规范化名字 'aet' 就是这个宿舍的【门牌号】（Map 的 Key）。
所有算出门牌号相同的单词，统统住进这个宿舍的列表里！
当所有单词都报到完毕，班主任把所有宿舍里的名单集中打包交上去，就完成了分组！""",
        "js_helpers": [
            {
                "name": "str.split('') 与 arr.join('')",
                "what_it_does": "split('') 把字符串拆成单字符数组；join('') 把数组重新拼回字符串。",
                "junior_tip": "JS 中字符串是不可变数据（Primitive Type），不能直接调用 str.sort()。必须先调用 .split('') 变成数组，排完序之后再 .join('') 拼回字符串作为唯一标识 Key。"
            },
            {
                "name": "arr.sort()",
                "what_it_does": "对数组进行原地排序。",
                "junior_tip": "对纯字母字符数组排序，直接调用 .sort() 默认就是按照 UTF-16 码点 / 字母表升序排序（'a' < 'b' < 'c'），恰好满足归一化需求。"
            },
            {
                "name": "Array.from(map.values()) 或 [...map.values()]",
                "what_it_does": "把 Map 里面所有的值迭代器（Iterator）收集并转换为真正的二维数组。",
                "junior_tip": "map.values() 返回的是 MapIterator，不是 Array。通过 Array.from() 可以轻松转成符合 LeetCode 返回签名的二维数组。"
            }
        ],
        "code_js": """/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // 步骤 1：准备一个哈希表 Map，用来存 { 排序后的标准化门牌号 => [原始单词数组] }
    const map = new Map();

    // 步骤 2：遍历输入的每一个单词
    for (const str of strs) {
        // 关键归一化操作：把单词字母排序作为特征 Key
        // 例如 'eat' -> ['e','a','t'] -> ['a','e','t'] -> 'aet'
        const sortedKey = str.split('').sort().join('');

        // 步骤 3：如果该门牌号尚不存在，先初始化一个空房间
        if (!map.has(sortedKey)) {
            map.set(sortedKey, []);
        }

        // 步骤 4：把原始单词存入对应的房间中
        map.get(sortedKey).push(str);
    }

    // 步骤 5：把所有房间里的单词列表打包为二维数组输出
    return Array.from(map.values());
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：异位词归一化特征键设计",
                "detail": "识别字母异位词的核心不变量——字符组成及频次一致。将字符串拆解排序后重组作为 Key，确保所有异位词哈希映射到同一桶中。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：字符串不可变性与链式转换",
                "detail": "熟练掌握 str.split('').sort().join('') 的经典模式，规避对只读字符串直接操作 sort 的类型错误。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：哈希桶防御性初始化",
                "detail": "通过 if (!map.has(key)) map.set(key, []) 进行安全兜底，严防向 undefined 上执行 .push() 导致的运行时异常崩溃。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：空串与单字符极端边界覆盖",
                "detail": "处理如 strs=[''] 或 strs=['a'] 时，split('').sort().join('') 仍为 '' 或 'a'，能正确建立空桶或单字符桶，逻辑极其稳健。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：时空开销分析与迭代器导出",
                "detail": "时间复杂度为 O(N * K log K)（N 为单词数，K 为单词最长长度），空间复杂度为 O(N * K)。最后利用 Array.from(map.values()) 优雅输出二维数组。",
                "weight": 20
            }
        ]
    },
    128: {
        "title_cn": "最长连续序列",
        "title_en": "Longest Consecutive Sequence",
        "slug": "longest-consecutive-sequence",
        "difficulty": "Medium",
        "description": """### 题目描述
给定一个未排序的整数数组 `nums`，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

### 示例 1
- **输入**：`nums = [100,4,200,1,3,2]`
- **输出**：`4`
- **解释**：最长数字连续序列是 `[1, 2, 3, 4]`。它的长度为 4。

### 示例 2
- **输入**：`nums = [0,3,7,2,5,8,4,6,0,1]`
- **输出**：`9`
- **解释**：连续序列为 `[0, 1, 2, 3, 4, 5, 6, 7, 8]`，长度为 9。

### 提示与约束条件
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- **必须达到严格的 O(n) 时间复杂度**（因此绝不能对全数组排序，排序最快为 O(n log n)）""",
        "plain_explanation": """题目要求找最长的连续数字（比如 1, 2, 3, 4 长度为 4），但限制必须在 O(N) 时间搞定，这就判了'排序算法'的死刑。
怎么在无序的数字堆里一眼找出最长长龙？
大白话秘诀叫【寻龙点穴找龙头】：
1. 先把所有数字倒进一个 JavaScript Set（哈希集合）里去重并建立 O(1) 索引。
2. 怎样避免盲目数数导致的超时？关键在于：'只从一条链条的开门老大（龙头）开始数'！
   如果集合里已经有 num - 1，说明当前 num 充其量只是个小弟，前面还有老大罩着它，我们直接跳过！
   只有当 num - 1 不在集合里时，才证明当前这个数是一个崭新连续序列的绝对起点（龙头）。
3. 抓到龙头后，才启动 while 循环顺藤摸瓜：num + 1、num + 2、num + 3... 一路数下去。
因为非龙头的数全部被瞬间剪枝，数组里的每一个数字最多只会被访问两次，稳稳达成神仙级别的 O(N)！""",
        "js_helpers": [
            {
                "name": "new Set(nums)",
                "what_it_does": "将数组一次性去重并构造成哈希集合。",
                "junior_tip": "Set 最大的优势在于 set.has(val) 操作耗时仅为 O(1)，相比数组的 arr.includes()（O(N) 耗时）性能高出成百上千倍！"
            },
            {
                "name": "!set.has(num - 1)",
                "what_it_does": "检查集合中是否存在当前数字的前驱数，用于识别连续序列的起点。",
                "junior_tip": "这是本题的核心剪枝开关！没有这个判断就会退化为 O(N^2) 超时；有了它就是严格的均摊 O(N)。"
            },
            {
                "name": "Math.max(a, b)",
                "what_it_does": "比较两个数值并返回较大者。",
                "junior_tip": "用于在找到每条连续序列后，动态刷新历史最长记录 maxStreak = Math.max(maxStreak, currentStreak)。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    // 步骤 1：利用 Set 自动去重，并获得 O(1) 复杂度的瞬时查询能力
    const set = new Set(nums);
    let maxStreak = 0;

    // 步骤 2：遍历集合中的每一个数字
    for (const num of set) {
        // 核心剪枝点：只有当前数字的前驱数 (num - 1) 不存在时，它才是序列的真正起点（龙头）！
        // 如果 num - 1 存在，说明它后面会被它前面的老大统计到，这里直接跳过
        if (!set.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            // 步骤 3：顺藤摸瓜，不断向后探测连续递增的下一个数字
            while (set.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            // 步骤 4：刷新历史最长连续序列的长度
            maxStreak = Math.max(maxStreak, currentStreak);
        }
    }

    return maxStreak;
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：Set 哈希去重与 O(1) 检索支持",
                "detail": "使用 new Set(nums) 消除海量重复数字干扰，同时将数值存在性检测从数组的 O(N) 线性检索压低至哈希集合的 O(1) 瞬时查询。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：前驱数探测与起点剪枝哲学",
                "detail": "通过 !set.has(num - 1) 精准定位序列领头羊。唯有不存在前驱数时才进入累加统计，彻底消除中间节点的冗余重复扫描。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：while 单向链条持续探测",
                "detail": "从起点出发，在循环中以 currentNum + 1 持续在 Set 中探测后继元素并递增 currentStreak，直至链条中断。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：均摊复杂度证明与两遍访问界限",
                "detail": "理解外层 for 虽嵌套内层 while，但每个数字作为龙头被访问一次，作为链中后续元素在 while 中被探测一次，整体均摊严格为 O(N)。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：空数组与单元素极端边界防守",
                "detail": "输入为空数组 [] 时直接遍历 0 次返回 0；输入单元素数组时自然进入一次判断并返回 1，无需额外边界特判。",
                "weight": 20
            }
        ]
    },
    283: {
        "title_cn": "移动零",
        "title_en": "Move Zeroes",
        "slug": "move-zeroes",
        "difficulty": "Easy",
        "description": """### 题目描述
给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**请注意**，必须在不复制数组的情况下原地对数组进行操作。

### 示例 1
- **输入**: `nums = [0,1,0,3,12]`
- **输出**: `[1,3,12,0,0]`

### 示例 2
- **输入**: `nums = [0]`
- **输出**: `[0]`

### 提示与约束条件
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- **进阶要求**：尽量减少完成的操作次数，必须原地修改，额外空间复杂度为 `O(1)`。""",
        "plain_explanation": """要把数组里的 0 全赶到屁股后面去，而且不能创建新数组，必须原地修改。
想象队伍里有两个工人分工合作：
慢工人 slow 守在前面，专管【下一个非零好汉应该安放的坑位】；
快工人 fast 负责在前面一路小跑巡逻。
快工人一旦抓到一个不等于 0 的数字：
立刻把这个数字跟慢工人 slow 手里的坑位调换（或者搬过来）！
调换完成后，慢工人心满意足地向后挪一格（slow++），等待下一个非零数字。
当快工人巡逻完整个数组时，前面的坑位整整齐齐全坐满了非零数字，而后半段自然全被换成了 0！
整个过程仅需快工人巡逻一遍，既保住了非零数字原有的先后顺序，又一滴新内存都没多花！""",
        "js_helpers": [
            {
                "name": "[nums[slow], nums[fast]] = [nums[fast], nums[slow]]",
                "what_it_does": "ES6 数组解构赋值，实现原地交换两数。",
                "junior_tip": "现代 JavaScript 最优雅的原地交换写法，省去定义临时变量 `const temp = nums[slow]`，代码更具现代感与可读性。"
            },
            {
                "name": "快慢指针模型 (Fast & Slow Pointers)",
                "what_it_does": "快指针遍历探路，慢指针维护非零序列的右边界。",
                "junior_tip": "慢指针 slow 左侧（[0, slow - 1]）始终为已经处理好的非零元素集合，这是双指针算法的不变量（Invariant）。"
            }
        ],
        "code_js": """/**
 * @param {number[]} nums
 * @return {void} 原地修改，不要返回值
 */
var moveZeroes = function(nums) {
    // 步骤 1：慢指针 slow 记录下一个非零数字应该安放的位置
    let slow = 0;

    // 步骤 2：快指针 fast 负责向前探路，扫描所有元素
    for (let fast = 0; fast < nums.length; fast++) {
        // 步骤 3：一旦快指针探测到非零元素，立刻与 slow 位置进行交换
        if (nums[fast] !== 0) {
            // ES6 解构互换两数
            [nums[slow], nums[fast]] = [nums[fast], nums[slow]];
            // 慢指针向前推进一位
            slow++;
        }
    }
};""",
        "checkpoints": [
            {
                "dimension": "point1",
                "title": "知识点 1：慢指针循环不变量维护",
                "detail": "明确 slow 指针语义：[0, slow - 1] 区间恒为非零元素的保序集合，slow 当前位置即为下一个非零元素入驻的待填槽位。",
                "weight": 20
            },
            {
                "dimension": "point2",
                "title": "知识点 2：快指针线性巡检探路",
                "detail": "fast 指针从 0 遍历至 nums.length - 1，严格单层循环扫描，保证算法时间复杂度为 O(N)。",
                "weight": 20
            },
            {
                "dimension": "point3",
                "title": "知识点 3：ES6 解构原地交换两数",
                "detail": "熟练运用 [nums[slow], nums[fast]] = [nums[fast], nums[slow]]，避免传统三步法中间变量 temp，原地空间复杂度 O(1)。",
                "weight": 20
            },
            {
                "dimension": "point4",
                "title": "知识点 4：相对次序保全机理",
                "detail": "fast 从前往后遇到的第一个非零数必定优先填入 slow=0，第二个填入 slow=1，天然保全所有非零元素原本的先后相对顺序。",
                "weight": 20
            },
            {
                "dimension": "point5",
                "title": "知识点 5：全零与无零边界自愈性",
                "detail": "当数组全为 0 时，fast 始终不满足条件，slow 恒为 0 无任何写操作；当数组无 0 时，fast 与 slow 同步递增自身原地对调，安全无害。",
                "weight": 20
            }
        ]
    }
}
