"""Day 1 JavaScript Solutions with Junior-level explanations, JS helpers, descriptions, and code-aligned checkpoints.
Auto-generated and strictly validated for LeetCode Hot 100 Mastery.
"""

DAY_1_JS_DATA = {
    1: {
        "title_cn": '两数之和',
        "title_en": 'Two Sum',
        "slug": 'two-sum',
        "difficulty": 'Easy',
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
                "name": 'new Map()',
                "what_it_does": '创建一个哈希映射字典，用来存储键值对 (key => value)。',
                "junior_tip": "小白常问：为什么不用普通对象 `{}`？因为在 JS 中，对象的 key 会被强制转成字符串（比如数字 1 变成字符串 '1'），而 Map 的 key 可以保持原始数字类型；并且 Map 在高频增删查改时底层引擎优化更好，判断存在直接用 map.has()，干净又高效。",
            },
            {
                "name": 'map.has(key) 与 map.get(key)',
                "what_it_does": 'map.has() 返回布尔值检查 key 是否存在；map.get() 获取该 key 对应存储的值。',
                "junior_tip": '哈希表的查找时间复杂度是 O(1)，近乎瞬间完成。这是本算法把两重暴力嵌套循环缩减为单层线性遍历的关键武器。',
            },
            {
                "name": 'map.set(key, value)',
                "what_it_does": '往 Map 中添加或更新一条记录。',
                "junior_tip": '这里用来把当前数字当 key，把它的数组下标 i 当 value 存起来，方便后续数字来相亲配对。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：哈希映射数据结构选取',
                "detail": '使用 ES6 Map 而非普通 Object，利用 Map 保持数字键类型的特性，规避对象隐式将数字键转换为字符串带来的微小性能开销与潜在类型混乱。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：单趟遍历与补数动态计算',
                "detail": '将暴力枚举 O(N^2) 降至 O(N) 的关键是将 a + b = target 转化为 target - a = b，在向前遍历的同时动态计算期待的互补数字 diff。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：哈希表 O(1) 瞬时探测',
                "detail": '利用 map.has(diff) 进行常数级别复杂度的存在性校验，一旦命中即刻通过 map.get(diff) 提取历史索引并返回，实现早停机制。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：边查边存彻底杜绝自身复用',
                "detail": "严格遵守'先查询、后入表'的顺序。若提前把当前元素放入 Map，在 target - current === current（如 target=6, nums[0]=3）时会直接匹配到自身造成致命 Bug。",
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：负数与大数边界鲁棒性',
                "detail": '该解法天然支持负数与零（例如 nums=[-3,4,3,90], target=0），算术差值计算在 JS 安全整数范围内完全准确，空间复杂度严格为 O(N)。',
                "weight": 20,
            },
        ],
    },
    49: {
        "title_cn": '字母异位词分组',
        "title_en": 'Group Anagrams',
        "slug": 'group-anagrams',
        "difficulty": 'Medium',
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
                "junior_tip": "JS 中字符串是不可变数据（Primitive Type），不能直接调用 str.sort()。必须先调用 .split('') 变成数组，排完序之后再 .join('') 拼回字符串作为唯一标识 Key。",
            },
            {
                "name": 'arr.sort()',
                "what_it_does": '对数组进行原地排序。',
                "junior_tip": "对纯字母字符数组排序，直接调用 .sort() 默认就是按照 UTF-16 码点 / 字母表升序排序（'a' < 'b' < 'c'），恰好满足归一化需求。",
            },
            {
                "name": 'Array.from(map.values()) 或 [...map.values()]',
                "what_it_does": '把 Map 里面所有的值迭代器（Iterator）收集并转换为真正的二维数组。',
                "junior_tip": 'map.values() 返回的是 MapIterator，不是 Array。通过 Array.from() 可以轻松转成符合 LeetCode 返回签名的二维数组。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：异位词归一化特征键设计',
                "detail": '识别字母异位词的核心不变量——字符组成及频次一致。将字符串拆解排序后重组作为 Key，确保所有异位词哈希映射到同一桶中。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：字符串不可变性与链式转换',
                "detail": "熟练掌握 str.split('').sort().join('') 的经典模式，规避对只读字符串直接操作 sort 的类型错误。",
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：哈希桶防御性初始化',
                "detail": '通过 if (!map.has(key)) map.set(key, []) 进行安全兜底，严防向 undefined 上执行 .push() 导致的运行时异常崩溃。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：空串与单字符极端边界覆盖',
                "detail": "处理如 strs=[''] 或 strs=['a'] 时，split('').sort().join('') 仍为 '' 或 'a'，能正确建立空桶或单字符桶，逻辑极其稳健。",
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：时空开销分析与迭代器导出',
                "detail": '时间复杂度为 O(N * K log K)（N 为单词数，K 为单词最长长度），空间复杂度为 O(N * K)。最后利用 Array.from(map.values()) 优雅输出二维数组。',
                "weight": 20,
            },
        ],
    },
    128: {
        "title_cn": '最长连续序列',
        "title_en": 'Longest Consecutive Sequence',
        "slug": 'longest-consecutive-sequence',
        "difficulty": 'Medium',
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
                "name": 'new Set(nums)',
                "what_it_does": '将数组一次性去重并构造成哈希集合。',
                "junior_tip": 'Set 最大的优势在于 set.has(val) 操作耗时仅为 O(1)，相比数组的 arr.includes()（O(N) 耗时）性能高出成百上千倍！',
            },
            {
                "name": '!set.has(num - 1)',
                "what_it_does": '检查集合中是否存在当前数字的前驱数，用于识别连续序列的起点。',
                "junior_tip": '这是本题的核心剪枝开关！没有这个判断就会退化为 O(N^2) 超时；有了它就是严格的均摊 O(N)。',
            },
            {
                "name": 'Math.max(a, b)',
                "what_it_does": '比较两个数值并返回较大者。',
                "junior_tip": '用于在找到每条连续序列后，动态刷新历史最长记录 maxStreak = Math.max(maxStreak, currentStreak)。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：Set 哈希去重与 O(1) 检索支持',
                "detail": '使用 new Set(nums) 消除海量重复数字干扰，同时将数值存在性检测从数组的 O(N) 线性检索压低至哈希集合的 O(1) 瞬时查询。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：前驱数探测与起点剪枝哲学',
                "detail": '通过 !set.has(num - 1) 精准定位序列领头羊。唯有不存在前驱数时才进入累加统计，彻底消除中间节点的冗余重复扫描。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：while 单向链条持续探测',
                "detail": '从起点出发，在循环中以 currentNum + 1 持续在 Set 中探测后继元素并递增 currentStreak，直至链条中断。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：均摊复杂度证明与两遍访问界限',
                "detail": '理解外层 for 虽嵌套内层 while，但每个数字作为龙头被访问一次，作为链中后续元素在 while 中被探测一次，整体均摊严格为 O(N)。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：空数组与单元素极端边界防守',
                "detail": '输入为空数组 [] 时直接遍历 0 次返回 0；输入单元素数组时自然进入一次判断并返回 1，无需额外边界特判。',
                "weight": 20,
            },
        ],
    },
    283: {
        "title_cn": '移动零',
        "title_en": 'Move Zeroes',
        "slug": 'move-zeroes',
        "difficulty": 'Easy',
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
                "name": '[nums[slow], nums[fast]] = [nums[fast], nums[slow]]',
                "what_it_does": 'ES6 数组解构赋值，实现原地交换两数。',
                "junior_tip": '现代 JavaScript 最优雅的原地交换写法，省去定义临时变量 `const temp = nums[slow]`，代码更具现代感与可读性。',
            },
            {
                "name": '快慢指针模型 (Fast & Slow Pointers)',
                "what_it_does": '快指针遍历探路，慢指针维护非零序列的右边界。',
                "junior_tip": '慢指针 slow 左侧（[0, slow - 1]）始终为已经处理好的非零元素集合，这是双指针算法的不变量（Invariant）。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：慢指针循环不变量维护',
                "detail": '明确 slow 指针语义：[0, slow - 1] 区间恒为非零元素的保序集合，slow 当前位置即为下一个非零元素入驻的待填槽位。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：快指针线性巡检探路',
                "detail": 'fast 指针从 0 遍历至 nums.length - 1，严格单层循环扫描，保证算法时间复杂度为 O(N)。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：ES6 解构原地交换两数',
                "detail": '熟练运用 [nums[slow], nums[fast]] = [nums[fast], nums[slow]]，避免传统三步法中间变量 temp，原地空间复杂度 O(1)。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：相对次序保全机理',
                "detail": 'fast 从前往后遇到的第一个非零数必定优先填入 slow=0，第二个填入 slow=1，天然保全所有非零元素原本的先后相对顺序。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：全零与无零边界自愈性',
                "detail": '当数组全为 0 时，fast 始终不满足条件，slow 恒为 0 无任何写操作；当数组无 0 时，fast 与 slow 同步递增自身原地对调，安全无害。',
                "weight": 20,
            },
        ],
    },
    11: {
        "title_cn": '盛最多水的容器',
        "title_en": 'Container With Most Water',
        "slug": 'container-with-most-water',
        "difficulty": 'Medium',
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
                "name": 'Math.min(height[left], height[right])',
                "what_it_does": '获取左右两根垂直线中较矮的一根作为有效蓄水高度。',
                "junior_tip": '严密吻合木桶短板效应，任何超出短板的水都会从两侧溢出，因此容器高只能取最小值。',
            },
            {
                "name": 'Math.max(maxWater, h * w)',
                "what_it_does": '计算当前容积并滚动刷新全局最大蓄水量。',
                "junior_tip": '避免繁琐的书写 if (current > maxWater) maxWater = current，简洁高效。',
            },
            {
                "name": '对撞双指针 (Two Pointers Colliding)',
                "what_it_does": '双指针 left=0 与 right=n-1 向中间夹逼收敛。',
                "junior_tip": '时间复杂度从暴力两两组合的 O(N^2) 戏剧性降低到单次遍历的 O(N)，空间复杂度为极致的 O(1)。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：首尾双指针最大底宽起步',
                "detail": '初始化 left = 0, right = height.length - 1，从底边宽度极限最大处出发，形成基准搜索空间。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：木桶短板决定有效高度',
                "detail": '明确蓄水量公式 Math.min(height[left], height[right]) * (right - left)，高度必须由二者较矮者决定。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：移动短板的贪心证明',
                "detail": '深刻理解若移动长板，底宽缩小的同时高度上限不增反降，容积单调递减；唯有移动短板才可能提升上限获取更大容积。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：等高情况下的移动策略',
                "detail": '当 height[left] === height[right] 时，两边任移一边（或同时内缩）均正确，不影响最终全局最大值的收敛。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：O(N) 遍历保证与空间最优',
                "detail": '每个循环步必有一指针移动，总计移动 N-1 次后双指针相遇终止，时间复杂度严格 O(N)，无额外辅助空间开销（O(1)）。',
                "weight": 20,
            },
        ],
    },
    15: {
        "title_cn": '三数之和',
        "title_en": '3Sum',
        "slug": '3sum',
        "difficulty": 'Medium',
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
                "name": 'nums.sort((a, b) => a - b)',
                "what_it_does": '对数值数组进行真正的升序数值排序。',
                "junior_tip": '【JS 核心必踩坑】千万不要直接写 nums.sort()！JS 的 sort 默认把数字转字符串按 Unicode 码点排，数组 [10, 2] 会排成 [10, 2]！必须传入比较函数 (a, b) => a - b 才是真正的升序。',
            },
            {
                "name": 'while 循环跳过重复元素',
                "what_it_does": '在命中目标后，快速推进指针跳过数值相同的元素。',
                "junior_tip": 'while (left < right && nums[left] === nums[left + 1]) left++，避免把重复的相同数值推进解集。',
            },
            {
                "name": 'res.push([a, b, c])',
                "what_it_does": '将满足条件的合法三元组推入二维结果集中。',
                "junior_tip": '无需额外构造 Set 进行去重，双指针结合有序性原地跳重效率极高。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：JS 数组数字排序比较器严密性',
                "detail": '严格调用 nums.sort((a, b) => a - b)，杜绝无参 sort 默认字典序导致负数与两位数排列紊乱的经典语法深坑。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：基准数剪枝 (nums[i] > 0)',
                "detail": '首个数字大于 0 时直接 break，利用有序数组单调性大幅提前截断无解分支，提升运行性能。',
                "weight": 15,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：基准数去重逻辑判定 (nums[i] === nums[i - 1])',
                "detail": '比较 nums[i] 与 nums[i - 1] 而非 nums[i + 1]，确保允许同值元素在三元组内部并存（如 [-1, -1, 2]），仅去重跨三元组的起点。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：左右双指针对撞求和与单调收敛',
                "detail": '根据 sum 与 0 的大小关系分别单调推进 left++ 或 right--，在 O(N) 内扫描完该基准下的所有二元对。',
                "weight": 15,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：命中目标后的双向连续跳重',
                "detail": '命中后通过 while 循环跳过重复相同值再收敛（left++、right--），杜绝结果集产生重复三元组，彻底免除哈希去重的空间与计算开销。',
                "weight": 15,
            },
            {
                "dimension": 'point6',
                "title": '知识点 6：整体时间复杂度 O(N^2) 分析',
                "detail": '排序耗时 O(N log N)，外层循环遍历 N 次，内层双指针扫描 O(N)，总耗时严格为 O(N^2)，满足规模限制。',
                "weight": 15,
            },
        ],
    },
    42: {
        "title_cn": '接雨水',
        "title_en": 'Trapping Rain Water',
        "slug": 'trapping-rain-water',
        "difficulty": 'Hard',
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
                "name": 'leftMax 与 rightMax 动态挡板',
                "what_it_does": '记录遍历过程中左右两侧已探测到的最高柱子高度。',
                "junior_tip": '无需开辟前后缀数组，两个普通数字变量即可维护全局极值状态，把空间消耗压制在 O(1)。',
            },
            {
                "name": '短板优先结算机制',
                "what_it_does": '根据 height[left] < height[right] 判定哪一侧的挡板是绝对受限短板。',
                "junior_tip": '矮的一侧其水线高度已经确定，不受另一侧未知区域更高柱子的干扰，具备严格的局部确定性。',
            },
            {
                "name": 'water += leftMax - height[left]',
                "what_it_does": '结算当前柱子顶部的积水量并累加至总容积。',
                "junior_tip": '若当前柱子比历史挡板更高，则刷新挡板；若低于历史挡板，差值即为当前凹坑积蓄的雨水量。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：蓄水微元物理模型推导',
                "detail": '识别下标 i 的接水量为 Math.max(0, Math.min(leftMax, rightMax) - height[i])，将二维面雨水解耦为各列独立计算的累加和。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：双指针两侧动态挡板初始化',
                "detail": '设立 left=0, right=n-1 以及 leftMax=0, rightMax=0，利用局部短板决定性替代全局前后缀数组扫描。',
                "weight": 15,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：height[left] 与 height[right] 比较分支',
                "detail": '当 height[left] < height[right] 时，leftMax 必然小于右侧某种界限，左侧短板确立，从而安全结算 left 列。',
                "weight": 15,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：挡板高度更新与雨水结算互斥逻辑',
                "detail": '当 height[left] >= leftMax 时只更新挡板不存水；当 height[left] < leftMax 时当前列必然蓄水 leftMax - height[left]。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：单趟双向收敛直至汇合',
                "detail": '左右指针逐步向中间收敛直至相遇，无多余循环，时间复杂度为严格单趟 O(N)。',
                "weight": 15,
            },
            {
                "dimension": 'point6',
                "title": '知识点 6：常数空间 O(1) 优越性证明',
                "detail": '无需申请前后缀 max 辅助数组或单调栈节点内存，空间复杂度严格常数级 O(1)，面试答辩表现完美。',
                "weight": 15,
            },
        ],
    },
    3: {
        "title_cn": '无重复字符的最长子串',
        "title_en": 'Longest Substring Without Repeating Characters',
        "slug": 'longest-substring-without-repeating-characters',
        "difficulty": 'Medium',
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
                "name": 'new Map()',
                "what_it_does": '存储 { 字符 => 该字符最后一次出现的位置下标 }。',
                "junior_tip": '比遍历查找快极多，配合 map.has() 与 map.get() 达成 O(1) 瞬时位置检索。',
            },
            {
                "name": 'Math.max(left, map.get(ch) + 1)',
                "what_it_does": '更新左指针位置，确保左指针只能向前跳跃，绝不向后倒退！',
                "junior_tip": '【高频易错点】如果之前出现过的字符早在当前窗口左边界之前（已经被滑过去了），如果不做 Math.max，left 会倒退回到老位置导致死循环或算错。',
            },
            {
                "name": 'Math.max(maxLen, right - left + 1)',
                "what_it_does": '动态结算当前无重复窗口的长度并刷新历史最大值。',
                "junior_tip": '窗口闭区间 [left, right] 的元素个数公式为 right - left + 1。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：滑动窗口双指针状态机模型',
                "detail": '确立 [left, right] 始终为无重复字符的合法子串区间，right 负责进窗勘测，left 负责违规收缩。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：哈希表字符最近坐标动态映射',
                "detail": '使用 Map 记录每个字符最新出现的索引下标，实现检测到冲突时的 O(1) 跃迁跳跃。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：Math.max 防左指针历史回退',
                "detail": '深刻理解 left = Math.max(left, map.get(ch) + 1) 的防御机制，规避历史淘汰字符将 left 拽回窗口之外的经典陷阱。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：动态区间长度计算与极值更新',
                "detail": '在每一步无冲突确认后，以 right - left + 1 准确度量当前子串跨度，并使用 Math.max 持续跟踪全局最优解。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：单趟 O(N) 线性时间与极端边界安全',
                "detail": 'right 指针单调遍历一次，字符串为空时循环 0 次返回 0，单字符输入返回 1，时空复杂度达到工业级最优。',
                "weight": 20,
            },
        ],
    },
    438: {
        "title_cn": '找到字符串中所有字母异位词',
        "title_en": 'Find All Anagrams in a String',
        "slug": 'find-all-anagrams-in-a-string',
        "difficulty": 'Medium',
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
                "name": 'new Array(26).fill(0)',
                "what_it_does": "创建一个长度为 26 的数组并初始化为 0，用于统计 'a' 到 'z' 出现的频次。",
                "junior_tip": '相比频繁 new Map() 和序列化对象，纯数字数组内存连续、寻址极快，是字符频次统计的最优解法。',
            },
            {
                "name": "str.charCodeAt(i) - 'a'.charCodeAt(0)",
                "what_it_does": '将字符转换为 0 到 25 的数字索引下标。',
                "junior_tip": "'a'.charCodeAt(0) 是固定整数 97。'a' 对应 0，'b' 对应 1，'z' 对应 25。",
            },
            {
                "name": '定长滑动窗口 (Fixed-size Sliding Window)',
                "what_it_does": '右边界进一个元素、左边界出一个元素，保持窗口宽度恒等于 p.length。',
                "junior_tip": '无需嵌套 while 循环，单个 for 循环线性滑完即可。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：母串长度劣势防御特判',
                "detail": '检测 sLen < pLen 时直接 return []，避免后续无意义的负向索引截取与越界初始化操作。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：26 位定长计数数组构建',
                "detail": '使用 new Array(26).fill(0) 替代哈希字典，利用 ASCII 码偏移量 ch.charCodeAt(0) - 97 实现高效 O(1) 原地累加。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：初始首窗建立与基准匹配',
                "detail": '先填充模式串 p 的全量计数与母串 s 的前 pLen 个字符，完成首个长度为 pLen 窗口的建立与初始结果判定。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：定长滑动窗口进出平衡机制',
                "detail": '在单层循环中执行 sCount[新]++ 与 sCount[老]--，维持窗口内部字符数量恒等于 pLen，更新开销严格 O(1)。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：常数级频次比对与时间复杂度收敛',
                "detail": '比对函数在固定 26 维空间运行，全过程总时间复杂度为 O(26 * N) = O(N)，额外空间为常数 O(1)。',
                "weight": 20,
            },
        ],
    },
    560: {
        "title_cn": '和为 K 的子数组',
        "title_en": 'Subarray Sum Equals K',
        "slug": 'subarray-sum-equals-k',
        "difficulty": 'Medium',
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
                "name": 'map.set(0, 1) 的重大意义',
                "what_it_does": '初始化前缀和为 0 的频次为 1。',
                "junior_tip": "【必背哨兵】代表'前缀和为 0 在初始未出发状态下已经发生过 1 次'。若不加，所有从下标 0 开始且和刚好为 k 的子数组都不会被统计入答案！",
            },
            {
                "name": 'map.has(currentSum - k)',
                "what_it_does": '检查是否存在历史前缀和等于当前前缀和减去 k。',
                "junior_tip": '根据数学公式：prefix[right] - prefix[left] = k 等价于 prefix[left] = prefix[right] - k。',
            },
            {
                "name": 'map.set(currentSum, (map.get(currentSum) || 0) + 1)',
                "what_it_does": '将当前累加的前缀和频次加 1 记录进 Map。',
                "junior_tip": '使用 (map.get(x) || 0) 优雅处理 key 首次出现的默认值 0，无需写繁琐的 if-else。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：负数存在对滑动窗口的否定',
                "detail": '透彻理解当数组包含负数时，区间和与窗口长度丧失单调关系，滑窗双指针失效，必须转向哈希前缀和体系。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：连续子数组向两数之差转换',
                "detail": '将连续子数组和 sum(nums[i..j]) = k 转化为 prefix[j] - prefix[i-1] = k，即在历史前缀集合中寻找 prefix[j] - k。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：map.set(0, 1) 初始哨兵必要性',
                "detail": '初始化 prefix=0 出现 1 次，用于正确统计从数组索引 0 开始、自身和直接等于 k 的整段前缀子数组。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：先查后存的顺序与无后效性',
                "detail": "严格保持'先检查历史差值累加 count，再将当前前缀和入表'的时序，防止 k=0 时当前前缀和自身与自身误配。",
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：单变量累加与 O(N) 线性性能',
                "detail": '使用 currentSum 单变量实时累加，无需开辟 N 长度的前缀和数组，时间与空间复杂度均为极佳的 O(N)。',
                "weight": 20,
            },
        ],
    },
    239: {
        "title_cn": '滑动窗口最大值',
        "title_en": 'Sliding Window Maximum',
        "slug": 'sliding-window-maximum',
        "difficulty": 'Hard',
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
                "name": '单调双端队列 (Monotonic Deque)',
                "what_it_does": '队列两端均可操作：队尾 push/pop，队头 shift。',
                "junior_tip": '维护队列中元素单调递减，队头始终指向当前窗口内最大元素的索引。',
            },
            {
                "name": '队列存储索引下标而非元素值',
                "what_it_does": '在队列中存储下标 i，而非 nums[i]。',
                "junior_tip": '【核心考点】存储下标既可以通过 nums[i] 获取数值比大小，又能通过 q[0] <= i - k 瞬间判断是否超出当前滑窗边界。',
            },
            {
                "name": 'q.pop() 与 q.shift()',
                "what_it_does": 'q.pop() 从尾部移除劣汰元素；q.shift() 从头部弹出过期元素。',
                "junior_tip": 'JS 中小规模 shift 性能优异；超大规模追求极致时亦可用双指针 head 偏移量模拟避免数组重排开销。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：单调队列单调递减性质维护',
                "detail": '新元素入队前通过 while 循环不断 pop 队尾更小或相等元素，确保队列内对应数值严格单调递减。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：下标索引存贮与超期判定',
                "detail": '队列存储索引而非数值，使得窗口左边界越界判断 if (q[0] <= i - k) 能在 O(1) 内精确判定并 shift 队头。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：窗口成型时机 (i >= k - 1)',
                "detail": '前 k - 1 步仅负责构建初始单调队列而不收集结果，直至第 k - 1 个元素开始每步收集一次窗口最大值。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：均摊复杂度 O(N) 严格证明',
                "detail": '虽然内层存在 while 循环，但数组中每个元素最多被 push 进队一次、pop/shift 出队一次，操作总次数不超过 2N，总时间严格 O(N)。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：极端窗口 k = 1 与 k = N 鲁棒性',
                "detail": '当 k = 1 时每步自成窗口立即收集；当 k = N 时直到最后一步收集一次全局最大值，逻辑覆盖无缝。',
                "weight": 20,
            },
        ],
    },
    76: {
        "title_cn": '最小覆盖子串',
        "title_en": 'Minimum Window Substring',
        "slug": 'minimum-window-substring',
        "difficulty": 'Hard',
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
                "name": 'need 哈希表与 need.size',
                "what_it_does": '统计 t 中各字符的目标需求量，need.size 代表需要达标的不同字符种类总数。',
                "junior_tip": "以'种类数'作为判断达标的依据，比每次循环都去遍历一遍字典高效成千上万倍！",
            },
            {
                "name": 'window.get(c) === need.get(c)',
                "what_it_does": '当窗口内某种字符数量恰好等于需求量时触发 matched++。',
                "junior_tip": '【关键考点】必须使用严格相等 === 触发，只有刚好达标那一瞬间才给 matched 加 1，避免重复多算。',
            },
            {
                "name": 's.slice(startIdx, startIdx + minLen)',
                "what_it_does": '根据记录的最优起点和最小跨度提取最终子串。',
                "junior_tip": '循环内只记录整数数字下标，绝不频繁调用 slice 截取字符串，避免巨大的字符串垃圾回收开销。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：需求字典与字符种类计数模型',
                "detail": '构造 need 哈希表记录频次，定义 matched 追踪种类达标数，用 matched === need.size 代替耗时的全表比对。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：右指针扩窗与精准达标触发',
                "detail": '右指针吞字符，唯有 window.get(c) === need.get(c) 临界达成时刻才 matched++，防止多余重复字符导致种类数虚高。',
                "weight": 15,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：全满状态下左指针极限收缩',
                "detail": '在 matched === need.size 条件下启动 while 收缩循环，利用挤水分机制动态剥离非必要前导多余字符。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：最优解记录与下标延迟截取',
                "detail": '在收缩内部仅以 startIdx 与 minLen 记录最优坐标区间，不在循环中调用 slice，避免产生高频垃圾对象。',
                "weight": 15,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：字符移出与达标状态破损判定',
                "detail": '吐出字符时判断 window.get(leftChar) < need.get(leftChar)，精准令 matched-- 跳出收缩循环，恢复扩窗探索。',
                "weight": 15,
            },
            {
                "dimension": 'point6',
                "title": '知识点 6：Infinity 兜底与 O(M+N) 时间分析',
                "detail": '初始化 minLen = Infinity 优雅识别无解情景；每个字符最多进窗一次出窗一次，整体复杂度达到神级 O(M+N)。',
                "weight": 15,
            },
        ],
    },
    53: {
        "title_cn": '最大子数组和',
        "title_en": 'Maximum Subarray',
        "slug": 'maximum-subarray',
        "difficulty": 'Medium',
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
                "name": 'Math.max(nums[i], currentSum + nums[i])',
                "what_it_does": 'Kadane 算法的核心状态转移方程。',
                "junior_tip": '如果之前的累计和 currentSum < 0，两者取大就会果断舍弃过去，以 nums[i] 作为新起点开始累加。',
            },
            {
                "name": '初始值设为 nums[0] 而非 0',
                "what_it_does": '令 currentSum 与 maxSum 初始均等于 nums[0]。',
                "junior_tip": '【常见死穴】如果把初始值设为 0，当数组全为负数（如 [-2, -1]）时，算法会错误返回 0！必须初始化为 nums[0]。',
            },
            {
                "name": 'O(1) 滚动变量空间压缩',
                "what_it_does": '无需开辟 dp 数组存储每个状态，仅用两个变量在单趟扫描中完成全部计算。',
                "junior_tip": '将空间复杂度从 O(N) 压缩至 O(1)，极为精炼优雅。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：初始值对准 nums[0] 规避负数死穴',
                "detail": '坚决禁止初始化为 0，防范全为负数（例如 [-3, -1, -2]）时误输出 0 的典型逻辑漏洞。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：Kadane 状态转移与断舍离决策',
                "detail": '理解 currentSum = Math.max(nums[i], currentSum + nums[i]) 本质为动态规划，识别前驱为负时重开子数组起点的必要性。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：单趟 O(N) 线性扫描机制',
                "detail": '从下标 1 循环到 n - 1，每个元素仅访问一次，时间复杂度严格为 O(N)。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：全局历史极值动态追踪',
                "detail": '使用 maxSum = Math.max(maxSum, currentSum) 独立维护历史见过的最优解，与局部最优状态更新解耦。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：常数空间 O(1) 优化与单元素覆盖',
                "detail": '单元素数组输入自然跳过循环返回 nums[0]，空间复杂度 O(1)，逻辑严密完备。',
                "weight": 20,
            },
        ],
    },
    56: {
        "title_cn": '合并区间',
        "title_en": 'Merge Intervals',
        "slug": 'merge-intervals',
        "difficulty": 'Medium',
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
                "name": 'intervals.sort((a, b) => a[0] - b[0])',
                "what_it_does": '对二维区间数组按照左端点（起始时间）进行升序排序。',
                "junior_tip": '【核心前提】排序消除了后效性，保证了在遍历到区间 i 时，前面所有区间的起始时间必定不大于当前区间。',
            },
            {
                "name": 'merged[merged.length - 1]',
                "what_it_does": '获取已合并结果集中的最后一个区间进行对比与原地修改。',
                "junior_tip": 'JavaScript 中利用引用类型对象的特性，直接修改 last[1] 即可就地延长结果集里的区间右边界。',
            },
            {
                "name": 'Math.max(last[1], current[1])',
                "what_it_does": '合并重叠区间时更新右端点最大值。',
                "junior_tip": '防止完全包含（如 [1, 10] 与 [2, 6]），必须取二者右端点的最大值。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：区间左端点排序消除后效性',
                "detail": '使用 intervals.sort((a, b) => a[0] - b[0]) 顺排时间线，将原本两两比较的二维网状关系转化为一维顺序扫描。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：结果集首项基准初始化',
                "detail": '声明 const merged = [intervals[0]]，以首个区间为锚点，为后续连续增量合并提供比对实体。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：重叠判定临界条件 (current[0] <= last[1])',
                "detail": '深刻理解端点相接（例如 [1, 4] 与 [4, 5]）亦属重叠，必须采用 <= 判定而非严格 <。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：Math.max 右边界延伸融合同步',
                "detail": '通过 last[1] = Math.max(last[1], current[1]) 就地拉伸右端点，兼容完全包含嵌套区间的场景。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：独立区间推入与时空性能证明',
                "detail": '不重叠时执行 merged.push(current)；总耗时为排序 O(N log N) + 线性合并 O(N)，额外空间为 O(N)。',
                "weight": 20,
            },
        ],
    },
    189: {
        "title_cn": '轮转数组',
        "title_en": 'Rotate Array',
        "slug": 'rotate-array',
        "difficulty": 'Medium',
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
                "name": 'k = k % nums.length (取模防溢出)',
                "what_it_does": '防止轮转步数 k 大于或等于数组实际长度 n。',
                "junior_tip": '【必加防线】如果数组长度为 5，轮转 7 步其实等价于轮转 7 % 5 = 2 步；如果 k 是 5 的倍数则相当于完全不动。',
            },
            {
                "name": '双指针 reverse(start, end) 翻转辅助函数',
                "what_it_does": '用 while (start < end) 和解构赋值就地对调指定区间段。',
                "junior_tip": '[nums[start], nums[end]] = [nums[end], nums[start]]，优雅原地置换。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：k %= n 模运算周期性规整',
                "detail": '识别轮转周期的等价性，防范 k >= n 甚至远大于 n 时引发的非法越界截断异常。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：双指针 reverse 工具函数闭环',
                "detail": '熟练实现基于 while (start < end) 与 ES6 解构的原地闭区间反转逻辑，空间纯度 O(1)。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：全数组翻转将后置块置前',
                "detail": '第一步 reverse(0, n - 1) 颠倒全局，使得原本位于末端的后 k 个元素成功换至前 k 个槽位。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：前后两段分段局部复原',
                "detail": '先后调用 reverse(0, k - 1) 与 reverse(k, n - 1)，分别修正前段与后段内部被反转颠倒的次序。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：原地原地修改与 O(1) 空间达标',
                "detail": '全过程无需额外数组分配，时间复杂度为 2N 即 O(N)，严格达成进阶原地空间 O(1) 指标。',
                "weight": 20,
            },
        ],
    },
    238: {
        "title_cn": '除自身以外数组的乘积',
        "title_en": 'Product of Array Except Self',
        "slug": 'product-of-array-except-self',
        "difficulty": 'Medium',
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
                "name": 'new Array(n).fill(1)',
                "what_it_does": '开辟长度为 n 的结果数组，所有位置初始化为乘法单位元 1。',
                "junior_tip": '乘法的基底必须是 1（如果误填成 0，任何数乘 0 都是 0，全盘皆输）。',
            },
            {
                "name": '单变量 leftProduct 与 rightProduct 滚动累乘',
                "what_it_does": '分别维护从左往右和从右往左的动态乘积值。',
                "junior_tip": '无需开辟两个长为 n 的前后缀数组，直接就地复用输出数组 res，满足进阶 O(1) 额外空间要求。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：除法禁令与零除异常痛点分析',
                "detail": '识别除法在此题中的禁用规定，以及数组含单个 0 或多个 0 时除法失效的致命缺陷，确立前后缀分解基调。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：乘法单位元 1 初始化基底',
                "detail": '使用 new Array(n).fill(1) 并设置初始乘积变量为 1，杜绝误置 0 导致的清零逻辑灾难。',
                "weight": 20,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：正向遍历沉淀左侧前缀积',
                "detail": '第一趟循环中先执行 res[i] = leftProduct 后更新 leftProduct *= nums[i]，严守除自身外的排他原则。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：反向遍历滚动融合右侧后缀积',
                "detail": '第二趟倒序扫描中通过 res[i] *= rightProduct 原地结合，无需额外申请后缀数组内存空间。',
                "weight": 20,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：O(N) 线性耗时与 O(1) 额外空间合规',
                "detail": '两次单层循环总耗时 2N，额外辅助内存除题目允许的返回值 res 外仅有两个标量变量，严格达成进阶规范。',
                "weight": 20,
            },
        ],
    },
    41: {
        "title_cn": '缺失的第一个正数',
        "title_en": 'First Missing Positive',
        "slug": 'first-missing-positive',
        "difficulty": 'Hard',
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
                "name": 'targetIdx = nums[i] - 1',
                "what_it_does": '将正整数数值 x 映射为数组索引下标 x - 1。',
                "junior_tip": '数值 1 归位至索引 0，数值 n 归位至索引 n - 1，实现原地自映射。',
            },
            {
                "name": 'while 原地置换循环',
                "what_it_does": '交换后新换到当前位置的数字可能仍然需要继续归位，通过 while 持续置换直至无法归位。',
                "junior_tip": '每个数字一旦归位后就再也不会被移走，因此全数组置换总次数不超过 N 次，均摊时间依然是严格 O(N)。',
            },
            {
                "name": 'nums[nums[i] - 1] !== nums[i] (死循环防线)',
                "what_it_does": '检查目标坑位上的数字是否已经与当前数字相同。',
                "junior_tip": '【最高频死循环坑】当数组存在重复数字（如 [1, 1]）时，若不加此判断，nums[0] 和 nums[0] 会无限对调引发进程卡死。',
            },
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
                "dimension": 'point1',
                "title": '知识点 1：鸽巢原理界定答案值域 [1, n + 1]',
                "detail": '深刻理解长度为 n 的数组最多容纳 n 个互异正整数，缺失的最小正数必然落在 [1, n + 1] 的闭区间内部。',
                "weight": 20,
            },
            {
                "dimension": 'point2',
                "title": '知识点 2：原地自哈希映射规则 (x => x - 1)',
                "detail": '复用输入数组充当哈希桶，将正整数 x 安置于下标 x - 1 处，省去常规哈希表的 O(N) 空间分配开销。',
                "weight": 15,
            },
            {
                "dimension": 'point3',
                "title": '知识点 3：while 持续安置与死循环防御',
                "detail": '置换条件必须包含 nums[nums[i] - 1] !== nums[i]，彻底防范重复数字在同一坑位导致的死锁无限循环。',
                "weight": 20,
            },
            {
                "dimension": 'point4',
                "title": '知识点 4：均摊复杂度严格 O(N) 证明',
                "detail": '每次有效置换必然使得至少一个萝卜回到终身正确的坑位，置换上限为 N 次，结合两轮遍历总耗时稳稳为 O(N)。',
                "weight": 15,
            },
            {
                "dimension": 'point5',
                "title": '知识点 5：二次遍历识别首个未就绪坑位',
                "detail": '从左向右扫描，若 nums[i] !== i + 1 则即刻 return i + 1，体现局部贪心与首个极小正数查找原理。',
                "weight": 15,
            },
            {
                "dimension": 'point6',
                "title": '知识点 6：全量完备情形兜底返回 n + 1',
                "detail": '当数组恰为 [1, 2, ..., n] 完整连续正整数时，顺利通过二次遍历，末尾兜底返回 n + 1，逻辑圆满无死角。',
                "weight": 15,
            },
        ],
    },
}
