"""Day 4 JavaScript Solutions with Junior-level explanations, JS helpers, code-aligned checkpoints, and detailed descriptions."""

DAY_4_JS_DATA = {
    46: {
        "title_cn": "全排列",
        "title_en": "Permutations",
        "slug": "permutations",
        "difficulty": "Medium",
        "description": """给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

### 示例 1:
- 输入: nums = [1,2,3]
- 输出: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

### 示例 2:
- 输入: nums = [0,1]
- 输出: [[0,1],[1,0]]

### 示例 3:
- 输入: nums = [1]
- 输出: [[1]]

### 提示/约束:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- nums 中的所有整数 互不相同""",
        "plain_explanation": "想象你有 3 件不同的衣服（红、绿、蓝），你要把它们挂在衣架上排出所有可能的出场顺序。回溯法的灵魂就是“做选择 -> 下探递归 -> 撤销选择（恢复案发现场）”。我们手里拿一个试衣篮 path，用来放当前排好的衣服；再拿一张打卡清单 used（布尔数组），记录哪件衣服已经被选过了。每次从没选过的人里挑一个加入 path，并在打卡单上标记 used[i] = true，然后进入下一层继续选下一个人。当选满 n 个人时（path.length === nums.length），必须用 [...path] 拍一张快照存进结果相册里！退出递归回溯时，必须把 path.pop() 弹出来，并把 used[i] 恢复成 false，把衣服还回原位，这样下一个分支才能重新选择它！",
        "js_helpers": [
            {
                "name": "res.push([...path]) (浅拷贝快照防空引用)",
                "what_it_does": "使用扩展运算符 [...path] 或 path.slice() 克隆数组快照。",
                "junior_tip": "【JS 核心致命死穴】在 JS 中，数组是引用数据类型。如果直接写 res.push(path)，放进去的只是对同一个内存地址的引用！后续回溯不断执行 path.pop() 最终把 path 彻底清空成 []，最后你的 res 里全是一堆空数组 []！因此必须使用 [...path] 或 path.slice() 复制独立切片快照！"
            },
            {
                "name": "path.push(val) 与 path.pop() (回溯进出站机制)",
                "what_it_does": "push 向数组末尾追加元素（做选择），pop 弹出数组末尾元素（撤销选择）。",
                "junior_tip": "回溯代码必须严格对称成对出现：递归调用前 push 状态进栈，递归返回后立即 pop 弹栈复原，维持各分支搜索的纯净独立。"
            },
            {
                "name": "new Array(nums.length).fill(false) (布尔访问标记表)",
                "what_it_does": "创建一个长度为 n 且元素全部初始化为 false 的布尔数组。",
                "junior_tip": "切记不要只写 new Array(n)，因为未初始化的数组每一项都是 empty（空槽），for 循环遍历或读写容易出现诡异 Bug；必须链式调用 .fill(false) 确保每个下标都有初值。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const res = [];
    const path = [];
    const used = new Array(nums.length).fill(false);

    const backtrack = () => {
        // 第 1 步：终止条件——选满 n 个数字，收获一种全排列
        if (path.length === nums.length) {
            res.push([...path]); // 必须浅拷贝拍快照！
            return;
        }

        // 第 2 步：遍历所有候选数字
        for (let i = 0; i < nums.length; i++) {
            // 如果该数字已被使用过，直接跳过
            if (used[i]) continue;

            // 第 3 步：做选择
            used[i] = true;
            path.push(nums[i]);

            // 第 4 步：递归下探，继续挑选下一个位置的数字
            backtrack();

            // 第 5 步：撤销选择（回溯恢复现场）
            path.pop();
            used[i] = false;
        }
    };

    backtrack();
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：初始化结果集、路径栈与布尔标记数组", "detail": "细扣：new Array(n).fill(false) 建立 O(1) 访问状态表，path 维护动态决策链条。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：终止条件 path.length === n 与快照收集", "detail": "细扣：牢记 JS 引用传递机制，必须 res.push([...path]) 浅拷贝克隆切片防变空。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：循环候选池与 used[i] 状态守卫", "detail": "细扣：if (used[i]) continue 过滤已选人员，锁定未使用的有效分支。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：做选择并推进递归深入下一层", "detail": "细扣：used[i] = true 配合 path.push(nums[i]) 推进决策树向下延伸。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：对称撤销选择 path.pop() 与状态复原", "detail": "细扣：对称清理复原现场，搜索树叶子共 N! 个，时间 O(N * N!) 空间 O(N)。", "weight": 20}
        ]
    },
    78: {
        "title_cn": "子集",
        "title_en": "Subsets",
        "slug": "subsets",
        "difficulty": "Medium",
        "description": """给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

### 示例 1:
- 输入: nums = [1,2,3]
- 输出: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

### 示例 2:
- 输入: nums = [0]
- 输出: [[],[0]]

### 提示/约束:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- nums 中的所有元素 互不相同""",
        "plain_explanation": "去冰淇淋店选配料（草莓、奥利奥、芒果）。你可以一种都不要（空集 []），可以只要一种，可以要任意两件组合，也可以全都要！子集问题是组合（[1, 2] 和 [2, 1] 算同一种），而且每个中间状态都是合法子集！大白话核心口诀：“一进门就拍照，永远只往前看不吃回头草”。写个 backtrack(start) 函数，参数 start 告诉递归从第几个数往后选，坚决不回头选前面的数，从根本上杜绝生成逆序重复子集。一进递归函数，不管三七二十一，先把当前 path 拍个照放进答案里（res.push([...path])，初始空集 [] 自然进门就收了）。然后 for 循环从 start 扫到末尾，挑一个加进 path，递归 backtrack(i + 1)，然后 pop 出来回溯！",
        "js_helpers": [
            {
                "name": "start 索引指针推进 (backtrack(i + 1))",
                "what_it_does": "下一层递归传递 backtrack(i + 1)，控制选择范围只能单调向后。",
                "junior_tip": "排列问题每次从 0 扫并靠 used 数组查漏；组合/子集问题不需要 used 数组，直接靠 start 游标单向右移，彻底消灭顺序颠倒导致的重复组合。"
            },
            {
                "name": "res.push([...path]) 树枝节点全量收集策略",
                "what_it_does": "无需判定长度达标，一进入 backtrack 函数立刻拍照收集。",
                "junior_tip": "子集问题的解空间大小是 2^N。根节点对应空集，叶子节点对应全集，搜索树上的每一个中间节点自身都是合法子集，必须进门即收。"
            },
            {
                "name": "path.push 与 path.pop 配对维护",
                "what_it_does": "数组尾部增删，精准维护递归路径当前深度。",
                "junior_tip": "单次调用 push 入栈，下探返回后立即 pop 出栈，使 path 的长度和深度严格同步。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const res = [];
    const path = [];

    const backtrack = (start) => {
        // 第 1 步：每个节点都是合法子集，一进入函数立刻拍快照收集
        res.push([...path]);

        // 第 2 步：从 start 开始往后选，绝不走回头路
        for (let i = start; i < nums.length; i++) {
            // 第 3 步：做选择
            path.push(nums[i]);

            // 第 4 步：深入下一层，注意必须传 i + 1
            backtrack(i + 1);

            // 第 5 步：撤销选择（回溯）
            path.pop();
        }
    };

    backtrack(0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：入口即刻快照收集全部中间节点", "detail": "细扣：树上所有节点皆合法子集，包括初始空集 []，进门立刻 res.push([...path])。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：for 循环从 start 起跳防逆流重复", "detail": "细扣：for (let i = start; i < n; i++) 锁定单向选择，杜绝选回头元素。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：做选择将当前候选数压入 path", "detail": "细扣：path.push(nums[i]) 扩展当前子集长度，继续向下试探。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：深入下一层递归传递 i + 1", "detail": "细扣：backtrack(i + 1) 保证每个元素在同一分支中最多只选一次。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：对称弹栈 path.pop() 与 2^N 复杂度分析", "detail": "细扣：恢复 path 长度，共生成 2^N 个子集，时间严格 O(N * 2^N) 空间 O(N)。", "weight": 20}
        ]
    },
    17: {
        "title_cn": "电话号码的字母组合",
        "title_en": "Letter Combinations of a Phone Number",
        "slug": "letter-combinations-of-a-phone-number",
        "difficulty": "Medium",
        "description": """给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
2 -> "abc", 3 -> "def", 4 -> "ghi", 5 -> "jkl", 6 -> "mno", 7 -> "pqrs", 8 -> "tuv", 9 -> "wxyz"

### 示例 1:
- 输入: digits = "23"
- 输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

### 示例 2:
- 输入: digits = ""
- 输出: []

### 示例 3:
- 输入: digits = "2"
- 输出: ["a","b","c"]

### 提示/约束:
- 0 <= digits.length <= 4
- digits[i] 是范围 ['2', '9'] 的一个数字""",
        "plain_explanation": "九宫格手机打字拼音。你按了数字 2（对应 'abc'），接着按了数字 3（对应 'def'），屏幕上要把所有可能拼出的拼音组合全部打出来（笛卡尔积）。大白话多叉树递归：建立一个映射表 phoneMap。递归参数 index 代表当前手指正在按第几个数字键。如果手指按完了全部数字（index === digits.length），说明这一轮单词拼装完成，用 path.join('') 拼成完整单词收录！否则，取出当前按键对应的所有候选字母（比如 'abc'），挑一个字母装进 path，然后递归 index + 1 去按下一个数字键。按完了回来把刚才挑的字母 pop 出来，换下一个候选字母继续试！注意防守坑：输入空串必须直接返回 []，绝不能返回 ['']！",
        "js_helpers": [
            {
                "name": "path.join('') (字符数组拼成单词字符串)",
                "what_it_does": "将字符数组中的各个字符无缝拼接成完整字符串返回。",
                "junior_tip": "在递归中用字符数组 path 进行 push/pop，比频繁使用字符串连接（str + ch）性能好得多，减少了大量底层临时字符串对象的内存分配与垃圾回收。"
            },
            {
                "name": "数字到字母映射表 (phoneMap)",
                "what_it_does": "配置字典对象将 '2'-'9' 映射为对应字符集合字符串。",
                "junior_tip": "用常量对象存放映射，查询时间为 O(1)。"
            },
            {
                "name": "空输入早退防护 if (!digits || digits.length === 0) return []",
                "what_it_does": "处理 LeetCode 空输入边界。",
                "junior_tip": "【高频丢分坑】若不加此防守，digits 为空串时会进入 backtrack(0)，因 index===0 直接将 [''] 误当作答案返回导致判错！"
            }
        ],
        "code_js": '''/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    // 第 1 步：防守空输入，直接返回空数组
    if (!digits || digits.length === 0) return [];

    const phoneMap = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    };

    const res = [];
    const path = [];

    const backtrack = (index) => {
        // 第 2 步：终止条件——所有按键按完，收集拼好的单词
        if (index === digits.length) {
            res.push(path.join(''));
            return;
        }

        // 取出当前按键对应的所有候选字母串
        const letters = phoneMap[digits[index]];

        // 第 3 步：遍历当前按键对应的每一个候选字母
        for (let i = 0; i < letters.length; i++) {
            path.push(letters[i]); // 做选择
            backtrack(index + 1);   // 递归处理下一个按键
            path.pop();             // 撤销选择（回溯）
        }
    };

    backtrack(0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：空串输入 if (!digits.length) return [] 特判", "detail": "细扣：坚决拦截空串直接返回 []，防误返回 [''] 造成评测错误。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：递归深度 index 触底与 join 字符串收集", "detail": "细扣：index === digits.length 意味着全按键就绪，path.join('') 成词收割。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：提取当前按键候选字母并展开多叉分支", "detail": "细扣：letters = phoneMap[digits[index]] 获取当层 3 或 4 个候选字符。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：做选择并推进 index + 1 深入下一层", "detail": "细扣：path.push 压入字符，backtrack(index + 1) 单向推进处理下一按键。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：对称弹栈 path.pop() 与乘法原理复杂度", "detail": "细扣：弹栈复原，组合总数为 3^M * 4^N，时间 O(3^M * 4^N) 空间 O(M + N)。", "weight": 20}
        ]
    },
    39: {
        "title_cn": "组合总和",
        "title_en": "Combination Sum",
        "slug": "combination-sum",
        "difficulty": "Medium",
        "description": """给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

### 示例 1:
- 输入: candidates = [2,3,6,7], target = 7
- 输出: [[2,2,3],[7]]
- 解释: 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。7 也是一个候选，7 = 7 。仅有这两种组合。

### 示例 2:
- 输入: candidates = [2,3,5], target = 8
- 输出: [[2,2,2,2],[2,3,3],[3,5]]

### 示例 3:
- 输入: candidates = [2], target = 1
- 输出: []

### 提示/约束:
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- candidates 的所有元素 互不相同
- 1 <= target <= 40""",
        "plain_explanation": "从零钱包里挑硬币凑出目标金额 target，同一个面额可以无限次重复选！大白话带剪枝回溯：先给数组升序排序（candidates.sort((a,b)=>a-b)）。我们手里拿个账单余额 remain（初始为 target）。每次挑一个数字 x：如果 x 比当前余额还大（x > remain），因为数组升序排列，后面的数字更大更不可能凑成，直接 break 砍掉整棵树枝（剪枝，省去几万次无用计算）！如果可以选，余额减去 x，关键精髓在于：“下一次递归依然传当前下标 i”（backtrack(remain - x, i)），这样就能允许继续复用当前数字！当 remain === 0 时说明刚好凑齐了，收集！",
        "js_helpers": [
            {
                "name": "candidates.sort((a, b) => a - b) (数值升序排序)",
                "what_it_does": "对原数组原地升序排序，为后续 break 强力剪枝铺平道路。",
                "junior_tip": "【JS 默认排序大坑】直接调用 arr.sort() 会默认按 ASCII 字典序排序（例如 10 会排在 2 前面！），必须显式传入 (a, b) => a - b 进行真数值升序排序！"
            },
            {
                "name": "传递当前索引 i 允许重复选自身",
                "what_it_does": "下一层递归传入 backtrack(remain - candidates[i], i)。",
                "junior_tip": "如果传 i + 1 就只能用一次自身；传 i 允许继续用自己，同时因为不选前面的数字（由 start 约束），天然避免了 [2, 3] 和 [3, 2] 的逆向重复组合！"
            },
            {
                "name": "remain 递减思维替代 sum 累加思维",
                "what_it_does": "维护差额 remain 从 target 递减到 0。",
                "junior_tip": "比维护 sum 累加少传一个参数，且直接与 candidates[i] > remain 剪枝条件无缝对齐。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    // 第 1 步：必须数值升序排序，为 break 剪枝铺路
    candidates.sort((a, b) => a - b);
    const res = [];
    const path = [];

    const backtrack = (remain, start) => {
        // 第 2 步：恰好凑满目标和，拍快照收录
        if (remain === 0) {
            res.push([...path]);
            return;
        }

        // 第 3 步：从 start 开始遍历候选数字
        for (let i = start; i < candidates.length; i++) {
            // 核心剪枝：当前数字已大于剩余所需，后续更大数字绝不可能凑成，直接 break 截断
            if (candidates[i] > remain) break;

            path.push(candidates[i]); // 做选择
            // 第 4 步：传递当前索引 i，允许再次挑选自己
            backtrack(remain - candidates[i], i);
            path.pop(); // 撤销选择（回溯）
        }
    };

    backtrack(target, 0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：candidates.sort((a,b)=>a-b) 升序排序", "detail": "细扣：为 break 提前截断树枝奠定单调递增基础，防 ASCII 字典序坑。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：remain 差额递减与 remain===0 触底收获", "detail": "细扣：传 remain 递减至 0 收集快照，比维护 currentSum 更轻爽易读。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：candidates[i] > remain 立即 break 剪枝", "detail": "细扣：彻底砍断整棵无用搜索分支，避免进入深层负数递归死胡同。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：下探传递当前索引 i 允许复用自身", "detail": "细扣：backtrack(remain - x, i) 允许当前数字无限重复，同时锁死顺序防重。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：对称弹栈 path.pop() 与搜索树空间深度", "detail": "细扣：对称回溯还原，递归树深度为 target / min(candidates)，空间 O(target/min)。", "weight": 20}
        ]
    },
    22: {
        "title_cn": "括号生成",
        "title_en": "Generate Parentheses",
        "slug": "generate-parentheses",
        "difficulty": "Medium",
        "description": """数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

### 示例 1:
- 输入: n = 3
- 输出: ["((()))","(()())","(())()","()(())","()()()"]

### 示例 2:
- 输入: n = 1
- 输出: ["()"]

### 提示/约束:
- 1 <= n <= 8""",
        "plain_explanation": "生成 n 对合法的括号组合。建筑师砌砖盖房子，左括号 '(' 代表“开工建一个新房间”，右括号 ')' 代表“封顶闭合一个房间”。你手头总共有 n 个开工额度和 n 个封顶额度。千万不要生成全部 2n 个字符后再用栈去验证（那样复杂度高达 2^(2n)，傻透了）。大白话“边建边防守，一条死路都不走”：拿两个计数器 left 和 right 分别记录已放的左括号和右括号个数。规则只有两条铁律：1. 只要 left < n，就可以随时放左括号 '('；2. 封顶右括号必须严格服从：只要 right < left（右括号个数比左括号少），才能放右括号 ')'！这样走出来的每一步都必定是绝对合法的！当 path 长度达到 2n 时，直接收集！",
        "js_helpers": [
            {
                "name": "right < left 合法性铁律守卫",
                "what_it_does": "严格控制右括号的放入时机，确保任意前缀中左括号数量 >= 右括号数量。",
                "junior_tip": "右括号永远不能单方面多于左括号，否则无法闭合必定非法。此守卫从源头扼杀不合法解，做到真正零废支回溯。"
            },
            {
                "name": "path.length === 2 * n 触底收集",
                "what_it_does": "总共放置了 2n 个括号时，收集当前拼合完整的有效串。",
                "junior_tip": "n 对括号最终字符串长度必为 2n，直接通过 path.join('') 转为字符串入库。"
            },
            {
                "name": "卡特兰数 (Catalan Number)",
                "what_it_does": "合法括号组合的总数正好等于第 n 个卡特兰数 C(2n, n) / (n + 1)。",
                "junior_tip": "面试时口述时间复杂度为 O(4^n / sqrt(n))，体现深厚的算法理论储备。"
            }
        ],
        "code_js": '''/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const res = [];
    const path = [];

    const backtrack = (left, right) => {
        // 第 1 步：放置了 2n 个括号，收集闭合串
        if (path.length === 2 * n) {
            res.push(path.join(''));
            return;
        }

        // 第 2 步：规则 1——只要左括号配额未用完，随时可放左括号
        if (left < n) {
            path.push('(');
            backtrack(left + 1, right);
            path.pop(); // 回溯
        }

        // 第 3 步：规则 2——右括号数量少于左括号时，才能放右括号闭合
        if (right < left) {
            path.push(')');
            backtrack(left, right + 1);
            path.pop(); // 回溯
        }
    };

    backtrack(0, 0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：path.length === 2*n 满额收获", "detail": "细扣：2n 个有效括号闭合，path.join('') 格式化收集入库。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：left < n 自由放入左括号", "detail": "细扣：左括号配额未用完随时可开新作用域，backtrack(left + 1, right)。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：right < left 严格防守闭合", "detail": "细扣：右括号严禁超前左括号，源头扼杀不合法解，backtrack(left, right + 1)。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：双 if 独立分支与对称 push/pop 回溯", "detail": "细扣：两分支独立试探，递归返回后立即 pop 保持现场纯净。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：零废支剪枝原理与卡特兰数复杂度剖析", "detail": "细扣：输出总数为第 n 个卡特兰数，时间复杂度严格 O(4^N / sqrt(N)) 空间 O(N)。", "weight": 20}
        ]
    },
    79: {
        "title_cn": "单词搜索",
        "title_en": "Word Search",
        "slug": "word-search",
        "difficulty": "Medium",
        "description": """给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母 不允许被重复使用 。

### 示例 1:
- 输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
- 输出: true

### 示例 2:
- 输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
- 输出: true

### 示例 3:
- 输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
- 输出: false

### 提示/约束:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board 和 word 仅由大小写英文字母组成""",
        "plain_explanation": "在密室地砖上走迷宫寻宝。你手里拿着藏宝密码 word，必须一格一格相邻走，踩出密码上的每一个字母。大白话核心妙计：“踩下脚印，原路返回时擦掉脚印（网格回溯）”！遍历棋盘的每一个格子作为起点。DFS 匹配当前第 k 个字符：如果越界或者当前格子里的字不等于 word[k]，返回 false。如果刚好匹配到单词的最后一个字母（k === word.length - 1），直接返回 true 宣告寻宝成功！为了防止转圈重复走自己刚才踩过的格子，把当前格子的字暂时改成占位符 '#'（踩脚印）。然后朝上下左右四向探索下一位。无论找到与否，在退出这个分支时，必须把原来的字符恢复回去（擦掉脚印，board[r][c] = temp），因为其他起点的搜索可能还会借道这个格子！",
        "js_helpers": [
            {
                "name": "board[r][c] = '#' (原地占坑与还原回溯)",
                "what_it_does": "原地修改当前网格为特殊占位符，免去开辟 visited 二维矩阵开销。",
                "junior_tip": "【必须回溯复原】退出当前探索前必须执行 board[r][c] = temp 擦除脚印！否则后续其他起点或分支路过时会看到 '#' 而无法走通，导致漏解！"
            },
            {
                "name": "短路求值 || (Short-circuit Evaluation)",
                "what_it_does": "dfs(r+1, c, k+1) || dfs(r-1, c, k+1) || ...",
                "junior_tip": "一旦某个方向率先找到了 true，后面的方向立刻短路不再执行，极大减少无谓的搜索开销。"
            },
            {
                "name": "网格越界卫语句安全防护",
                "what_it_does": "r < 0 || r >= m || c < 0 || c >= n || board[r][c] !== word[k]",
                "junior_tip": "先校验行列范围在合法下标内，再访问 board[r][c]，防止 JS 抛出 Cannot read property of undefined 运行时异常。"
            }
        ],
        "code_js": '''/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const m = board.length;
    const n = board[0].length;

    const dfs = (r, c, k) => {
        // 第 1 步：越界防守与字符失配拦截
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] !== word[k]) {
            return false;
        }

        // 第 2 步：单词的所有字母已经全部匹配成功！
        if (k === word.length - 1) return true;

        // 第 3 步：做选择——暂存并踩脚印打标，防止回头路
        const temp = board[r][c];
        board[r][c] = '#';

        // 第 4 步：短路四方向探索下一个字母
        const found = dfs(r + 1, c, k + 1) ||
                      dfs(r - 1, c, k + 1) ||
                      dfs(r, c + 1, k + 1) ||
                      dfs(r, c - 1, k + 1);

        // 第 5 步：撤销选择（回溯）——擦掉脚印，恢复原貌
        board[r][c] = temp;

        return found;
    };

    // 尝试以每一个格子作为起点
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === word[0] && dfs(i, j, 0)) {
                return true;
            }
        }
    }

    return false;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：网格边界越界防护与字符不匹配拦截", "detail": "细扣：越界或字符不等于 word[k] 立即返回 false，卫语句置顶。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：末位字符命中即刻通关 k === word.length - 1", "detail": "细扣：字母匹配满额即刻返回 true 提前截断全局搜索。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：board[r][c]='#' 原地占坑防回头路", "detail": "细扣：暂存 temp 字符并覆写 '#'，省去 O(M*N) 额外 visited 空间。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：上下左右四向探索与 || 逻辑短路剪枝", "detail": "细扣：一旦任一方向命中为 true，立即截断后续分支探索。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：board[r][c]=temp 原地回溯擦脚印", "detail": "细扣：撤销当前格子修改复原棋盘，时间 O(M*N * 3^L) 空间 O(L)。", "weight": 20}
        ]
    },
    131: {
        "title_cn": "分割回文串",
        "title_en": "Palindrome Partitioning",
        "slug": "palindrome-partitioning",
        "difficulty": "Medium",
        "description": """给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 （正着读和反着读都一样的字符串）。返回 s 所有可能的分割方案。

### 示例 1:
- 输入: s = "aab"
- 输出: [["a","a","b"],["aa","b"]]

### 示例 2:
- 输入: s = "a"
- 输出: [["a"]]

### 提示/约束:
- 1 <= s.length <= 16
- s 仅由小写英文字母组成""",
        "plain_explanation": "切火腿肠。你拿着一把小刀从左往右切，每一段切下来的火腿肠都必须是“回文肉块”（正反看都一模一样）。大白话核心：“前面是回文，小刀才去切后面”！从 start 位置开始往后枚举下刀点 i，切下来的前缀肉块是 s[start..i]。拿双指针查一下这个前缀子串是不是回文串。如果不是，切坏了，直接跳过不浪费时间；如果是回文串，把它装进 path 盒子里（path.push(s.slice(start, i + 1))），然后递归切分剩下的后缀串（backtrack(i + 1)）。当 start 推进到字符串末尾（start === s.length）时，说明整条字符串被成功全切成了合法回文块，拍快照收录！回溯时 pop 出来，尝试在更靠后的位置切更大的块！",
        "js_helpers": [
            {
                "name": "s.slice(start, i + 1) (左闭右开区间切片)",
                "what_it_does": "提取当前切分出的子串装入路径数组。",
                "junior_tip": "【JS 核心必知】JS 的 slice(begin, end) 是左闭右开区间，截取到下标 i 必须传入 i + 1，否则会少截最后一个字符！"
            },
            {
                "name": "双指针对撞判回文 isPalindrome(left, right)",
                "what_it_does": "左右指针从两端向中间对撞比对字符是否一致。",
                "junior_tip": "无需生成颠倒新字符串（如 split('').reverse().join('')），原串双指针比对 O(L) 速度极快且零内存分配。"
            },
            {
                "name": "start === n 触底收集机制",
                "what_it_does": "当切割点推进到字符串末尾，说明全串被完整切成回文段。",
                "junior_tip": "只有每一步都合法才能走到末尾，因此触底时无需再次校验，直接 res.push([...path]) 收集。"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const res = [];
    const path = [];
    const n = s.length;

    // 双指针校验回文串辅助函数
    const isPal = (left, right) => {
        while (left < right) {
            if (s[left] !== s[right]) return false;
            left++;
            right--;
        }
        return true;
    };

    const backtrack = (start) => {
        // 第 1 步：全串被完整切分为回文段，收集方案
        if (start === n) {
            res.push([...path]);
            return;
        }

        // 第 2 步：在 [start, n - 1] 范围内枚举下刀位置 i
        for (let i = start; i < n; i++) {
            // 关键剪枝：只有当前前缀是回文才继续切
            if (isPal(start, i)) {
                // 做选择：切下 [start, i] 这一段
                path.push(s.slice(start, i + 1));

                // 第 3 步：递归切分后续剩余子串
                backtrack(i + 1);

                // 第 4 步：撤销选择（回溯）
                path.pop();
            }
        }
    };

    backtrack(0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：isPal 双指针原地对撞回文检测工具", "detail": "细扣：双向对撞比较字符，O(L) 快速校验无需新建字符串。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：切割线抵达末尾 start === n 触底收集", "detail": "细扣：全串分割完毕，res.push([...path]) 浅拷贝快照收录结果。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：isPal(start, i) 守门与 s.slice 截取", "detail": "细扣：s.slice(start, i+1) 取闭区间子串装入 path，不合规直接跳过。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：深入下一截起割点 backtrack(i + 1)", "detail": "细扣：单向后推切割起点，递归树形逐步分解剩余子串。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：对称弹栈 path.pop() 回溯与复杂度分析", "detail": "细扣：弹栈撤销选择，搜索树分支总数 2^N，时间 O(N * 2^N) 空间 O(N)。", "weight": 20}
        ]
    },
    51: {
        "title_cn": "N 皇后",
        "title_en": "N-Queens",
        "slug": "n-queens",
        "difficulty": "Hard",
        "description": """按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

### 示例 1:
- 输入: n = 4
- 输出: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
- 解释: 4 皇后问题存在两个不同的解法。

### 示例 2:
- 输入: n = 1
- 输出: [["Q"]]

### 提示/约束:
- 1 <= n <= 9""",
        "plain_explanation": "在 n x n 棋盘上放 n 个皇后，彼此不能同行、同列、同对角线。大白话数学不变量剪枝：“一行只放一个皇后，顺着行号 0 到 n-1 逐行往下安排”！同行冲突天然解决，怎么快速判断列和对角线冲突？1. 列冲突：用集合 cols 记录占用的列号；2. 主对角线冲突（左上到右下）：同一个主对角线上的坐标，行减列（r - c）是恒定定值，用 diag1 集合记录；3. 副对角线冲突（右上到左下）：同一副对角线上的坐标，行加列（r + c）是恒定定值，用 diag2 集合记录！放一个皇后在三个集合里打勾（add），回溯退出来时在三个集合里删掉（delete），O(1) 瞬时剪除所有攻击冲突！",
        "js_helpers": [
            {
                "name": "new Set() 记录占用列与两条对角线",
                "what_it_does": "cols, diag1 (r - c), diag2 (r + c) 三集合。",
                "junior_tip": "数学公式恒等性直接省去 O(N) 遍历棋盘检查冲突的巨大开销！主对角线 r - c 差恒定，副对角线 r + c 和恒定。"
            },
            {
                "name": "'.'.repeat(c) + 'Q' + '.'.repeat(n - c - 1) 棋盘构造",
                "what_it_does": "利用 String 原生 repeat 方法单行构造棋盘字符串。",
                "junior_tip": "代码极简优雅，避免写双层循环去拼凑单行棋盘字符。"
            },
            {
                "name": "queens[r] = c 一维状态压缩数组",
                "what_it_does": "queens[r] 记录第 r 行的皇后安放在第几列。",
                "junior_tip": "无需维护沉重的 n x n 二维字符数组，只用一个长度为 n 的一维数组记录列索引，触底时一次性格式化输出。"
            }
        ],
        "code_js": '''/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const res = [];
    const queens = new Array(n).fill(-1); // queens[r] = c 记录每行皇后的列
    const cols = new Set();
    const diag1 = new Set(); // 记录 r - c (主对角线)
    const diag2 = new Set(); // 记录 r + c (副对角线)

    const backtrack = (r) => {
        // 第 1 步：所有 n 行都合法安放了皇后，绘制棋盘输出
        if (r === n) {
            const board = [];
            for (let i = 0; i < n; i++) {
                const c = queens[i];
                board.push('.'.repeat(c) + 'Q' + '.'.repeat(n - c - 1));
            }
            res.push(board);
            return;
        }

        // 第 2 步：尝试放在当前行 r 的每一列 c
        for (let c = 0; c < n; c++) {
            // 关键剪枝：三线冲突检测
            if (cols.has(c) || diag1.has(r - c) || diag2.has(r + c)) {
                continue;
            }

            // 第 3 步：做选择
            queens[r] = c;
            cols.add(c);
            diag1.add(r - c);
            diag2.add(r + c);

            // 第 4 步：递归安放下一行
            backtrack(r + 1);

            // 第 5 步：撤销选择（回溯）
            cols.delete(c);
            diag1.delete(r - c);
            diag2.delete(r + c);
        }
    };

    backtrack(0);
    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：逐行推进与 queens[r]=c 一维状态压缩", "detail": "细扣：逐行放置天然杜绝同行冲突，简化决策维度。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：Set 记录 cols/diag1(r-c)/diag2(r+c)", "detail": "细扣：利用几何对称恒等式 O(1) 检测列与两条对角线冲突。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：做选择登记三大警戒线与递归下一行", "detail": "细扣：queens[r]=c 登记并同步 add 入三集合，backtrack(r+1) 下探。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：三重集合严格同步回溯 delete", "detail": "细扣：弹栈撤销列与对角线占位，时间 O(N!) 空间 O(N)。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：r === n 触底 repeat 优雅拼接棋盘", "detail": "细扣：'.'.repeat(c) + 'Q' + '.'.repeat(n-c-1) 优雅格式化生成棋盘。", "weight": 20}
        ]
    },
    35: {
        "title_cn": "搜索插入位置",
        "title_en": "Search Insert Position",
        "slug": "search-insert-position",
        "difficulty": "Easy",
        "description": """给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

### 示例 1:
- 输入: nums = [1,3,5,6], target = 5
- 输出: 2

### 示例 2:
- 输入: nums = [1,3,5,6], target = 2
- 输出: 1

### 示例 3:
- 输入: nums = [1,3,5,6], target = 7
- 输出: 4

### 提示/约束:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 为 无重复元素 的 升序 排列数组
- -10^4 <= target <= 10^4""",
        "plain_explanation": "在升序排队的身高队伍里找 target，如果不存在，返回他应该按顺序插队的位置。二分查找最标准模板（左闭右闭区间 [left, right]）。大白话规则：只要 left <= right，取中点 mid。如果 nums[mid] >= target，说明目标在左半边或者就是 mid，收缩右界（right = mid - 1）；否则在右半边，收缩左界（left = mid + 1）。当循环结束两针错开（left > right）时，left 停下来的那个位置，不偏不倚，刚好就是 target 应当插入的完美位置！甚至当 target 比全数组都大时，left 刚好一步步推到数组长度 nums.length 上，完美全覆盖！",
        "js_helpers": [
            {
                "name": "Math.floor((left + right) / 2) 或 (left + right) >> 1",
                "what_it_does": "二分中点向下取整。",
                "junior_tip": "【JS 核心必知】JS 所有数字全为 64 位双精度浮点数，除法不自动取整（例如 3/2=1.5）！必须 Math.floor 或右移位运算符 >> 1，否则 nums[1.5] 为 undefined 会导致死循环崩溃！"
            },
            {
                "name": "双闭区间 while (left <= right) 循环守卫",
                "what_it_does": "双闭区间标准二分循环出口条件。",
                "junior_tip": "必须带 <=，因为当 left === right 时区间内还有一个元素必须检验，漏掉等号会导致单元素未检查就提前跳出。"
            },
            {
                "name": "return left 为什么恰好是插入点？",
                "what_it_does": "循环不变量：nums[0...left-1] < target，nums[right+1...n-1] >= target。",
                "junior_tip": "当 left > right 退出时，left 天然停留在首个 >= target 的位置，完美契合插入点定义。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    // 双闭区间 [left, right] 标准二分模版
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] >= target) {
            right = mid - 1; // 答案在左侧或就是 mid，压缩右边界
        } else {
            left = mid + 1;  // 答案在右侧，推进左边界
        }
    }

    // 循环退出时 left > right，left 即为首个 >= target 的正确插入索引
    return left;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：双闭区间 left=0, right=n-1 初始化", "detail": "细扣：while (left <= right) 标准二分出口，确保最后一个单元素得到检验。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：Math.floor((left+right)/2) 算中点", "detail": "细扣：显式向下取整，规避 JS 浮点数小数下标导致死循环崩溃。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：nums[mid] >= target 压缩右边界", "detail": "细扣：right = mid - 1 持续逼近下界，收缩搜索空间。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：nums[mid] < target 单调右推 left 指针", "detail": "细扣：left = mid + 1 排除过小的左半区间。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：循环不变量论证与统一出口 return left", "detail": "细扣：left 天然对应首个 >= target 插入点，时间严格 O(log N) 空间 O(1)。", "weight": 20}
        ]
    },
    74: {
        "title_cn": "搜索二维矩阵",
        "title_en": "Search a 2D Matrix",
        "slug": "search-a-2d-matrix",
        "difficulty": "Medium",
        "description": """给你一个满足下述两条属性的 m x n 整数矩阵：
- 每行中的整数从左到右按非严格递增顺序排列。
- 每行的第一个整数大于前一行的最后一个整数。

给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。

### 示例 1:
- 输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
- 输出: true

### 示例 2:
- 输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
- 输出: false

### 提示/约束:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4""",
        "plain_explanation": "整个二维矩阵从左到右、从上到下全盘严格升序。大白话降维打击：“把二维矩阵拉直成一根一维大面条”！总共有 m * n 个数字，虚拟索引从 0 到 m * n - 1。直接做一次标准的一维二分查找！唯一的魔法是一维虚拟索引 mid 怎么转换回二维坐标？行号就是 mid 包含了几个整行（row = Math.floor(mid / n)），列号就是除不尽的余数（col = mid % n）！十行代码直接搞定，不需要分两阶段搞两次二分！",
        "js_helpers": [
            {
                "name": "Math.floor(mid / n) 与 mid % n (一维向二维坐标映射)",
                "what_it_does": "一维平铺虚拟索引向二维矩阵坐标完美映射。",
                "junior_tip": "row = Math.floor(mid / n), col = mid % n，计算机图形学与算法通用坐标换算公式！切勿将列数 n 误写成行数 m！"
            },
            {
                "name": "矩阵判空防御性编程",
                "what_it_does": "if (!matrix || matrix.length === 0 || matrix[0].length === 0) return false;",
                "junior_tip": "防范空二维数组访问 matrix[0].length 抛出 TypeError。"
            },
            {
                "name": "left = 0, right = m * n - 1 虚拟边界",
                "what_it_does": "将 M x N 矩阵平铺为长度为 m*n 的升序空间。",
                "junior_tip": "时间复杂度严格为 O(log(m * n))，单次对数检索，代码结构极其干净。"
            }
        ],
        "code_js": '''/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return false;
    const m = matrix.length;
    const n = matrix[0].length;

    let left = 0;
    let right = m * n - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        // 一维虚拟索引转换为二维矩阵坐标
        const val = matrix[Math.floor(mid / n)][mid % n];

        if (val === target) {
            return true;
        } else if (val < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return false;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：一维虚拟范围 left=0, right=m*n-1 初始化", "detail": "细扣：将全局有序矩阵视为长度 m*n 的一维有序数组并判空防守。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：坐标换算 Math.floor(mid/n) 和 mid%n", "detail": "细扣：整除列数取行，求模列数取列，O(1) 访问虚拟中点值。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：提取 val 进行标准三路分支比对", "detail": "细扣：命中即刻 return true，小于则 left=mid+1，大于则 right=mid-1。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：单调收缩指针与循环正常跳出", "detail": "细扣：指针交错跳出表示目标不存在，单次二分无需拆分两阶段。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：未查到安全返回 false 与时空分析", "detail": "细扣：一次性对数时间 O(log(M*N))，空间 O(1)。", "weight": 20}
        ]
    },
    34: {
        "title_cn": "在排序数组中查找元素的第一个和最后一个位置",
        "title_en": "Find First and Last Position of Element in Sorted Array",
        "slug": "find-first-and-last-position-of-element-in-sorted-array",
        "difficulty": "Medium",
        "description": """给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

### 示例 1:
- 输入: nums = [5,7,7,8,8,10], target = 8
- 输出: [3,4]

### 示例 2:
- 输入: nums = [5,7,7,8,8,10], target = 6
- 输出: [-1,-1]

### 示例 3:
- 输入: nums = [], target = 0
- 输出: [-1,-1]

### 提示/约束:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums 是一个非递减数组
- -10^9 <= target <= 10^9""",
        "plain_explanation": "在排序数组里找 target 的起始和结束下标（比如 [5,7,7,8,8,10] 找 8，返回 [3, 4]）。普通二分一命中 target 就急着返回，但你不知道它究竟是第几个 8。大白话复用思想：“命中目标不停止，暂存答案继续向两翼挤压（找极值边界）”！写一个通用的二分辅函数 findBound(isLeft)：遇到 nums[mid] === target 时千万不要立刻返回，把答案暂存下来（ans = mid）。如果要找最左边的下标（isLeft=true），我们把右边界往左压（right = mid - 1）继续向左挖；如果要找最右边的下标（isLeft=false），把左边界往右推（left = mid + 1）继续向右挖！调用两次搞定！",
        "js_helpers": [
            {
                "name": "命中后不停止，继续向两翼挤压 (ans = mid)",
                "what_it_does": "ans = mid; isLeft ? right = mid - 1 : left = mid + 1;",
                "junior_tip": "找极值边界的标准手段：暂存当前候选解后主动收缩边界，逼迫二分探针向极端位置收敛。"
            },
            {
                "name": "findBound(isLeft) 布尔参数复用机制",
                "what_it_does": "一个函数兼顾左侧查找与右侧查找。",
                "junior_tip": "杜绝在代码里重复写两个长得几乎一样的二分查找，体现高质量模块化封装意识。"
            },
            {
                "name": "初始值 ans = -1 天然覆盖未找到",
                "what_it_does": "若未搜索到目标，默认返回 -1。",
                "junior_tip": "自动兼顾空数组和元素不存在的情况，返回 [-1, -1]。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    const findBound = (isLeft) => {
        let left = 0, right = nums.length - 1;
        let ans = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);

            if (nums[mid] === target) {
                ans = mid; // 暂存候选答案
                if (isLeft) {
                    right = mid - 1; // 找最左侧，向左挤压
                } else {
                    left = mid + 1;  // 找最右侧，向右挤压
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ans;
    };

    return [findBound(true), findBound(false)];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：构造 findBound(isLeft) 复用函数", "detail": "细扣：布尔参数控制收缩方向，杜绝冗余重复代码。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：nums[mid] === target 暂存候选 ans = mid", "detail": "细扣：命中不终止，保留当前索引作为最佳候选值。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：isLeft 分流向左挤压 right = mid - 1", "detail": "细扣：isLeft 缩小 right 逼近最左端始端。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：非 isLeft 驱动 left = mid + 1 逼近最右端", "detail": "细扣：放大 left 逼近最右端末端，精准锁尾。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：调用两次返回 [leftBound, rightBound]", "detail": "细扣：不存在返回 [-1, -1]，两次对数时间仍为严格 O(log N) 空间 O(1)。", "weight": 20}
        ]
    },
    33: {
        "title_cn": "搜索旋转排序数组",
        "title_en": "Search in Rotated Sorted Array",
        "slug": "search-in-rotated-sorted-array",
        "difficulty": "Medium",
        "description": """整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向右旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

### 示例 1:
- 输入: nums = [4,5,6,7,0,1,2], target = 0
- 输出: 4

### 示例 2:
- 输入: nums = [4,5,6,7,0,1,2], target = 3
- 输出: -1

### 示例 3:
- 输入: nums = [1], target = 0
- 输出: -1

### 提示/约束:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums 中的每个值都 独一无二
- 题目数据保证 nums 在预先未知的某个下标上进行了旋转
- -10^4 <= target <= 10^4""",
        "plain_explanation": "有序数组在某个断点旋转了（比如 [4,5,6,7,0,1,2]），找 target。这题最神奇的几何定理：“旋转数组砍成两半，必定有一半是完全规整升序的，另一半包含断崖”！怎么看哪半边规整？比对 nums[left] 和 nums[mid]：如果 nums[left] <= nums[mid]，那左半边就是铁板一块的规整升序！我们一眼就能看出 target 是不是在左半边范围里（nums[left] <= target < nums[mid]），在就去左边找，不在就去右边找；反之右半边规整也是一样的道理！无论如何都能果断扔掉一半，稳稳的 O(log N)！",
        "js_helpers": [
            {
                "name": "nums[left] <= nums[mid] 等号防漏",
                "what_it_does": "判断左半段是否单调升序。",
                "junior_tip": "【易错致命点】必须带 <=！因为只有两个元素时 mid 算出来刚好等于 left，漏了等号会误进右半段导致死胡同！"
            },
            {
                "name": "nums[left] <= target && target < nums[mid] 严格区间判别",
                "what_it_does": "利用有序区间的单调性精确圈定 target。",
                "junior_tip": "注意 target < nums[mid] 是严格小于，因为等于的情况已经在前面 if (nums[mid] === target) return mid 提前通关捕获了。"
            },
            {
                "name": "局部单调折半常数空间",
                "what_it_does": "二分折半不可逆舍弃无用半区。",
                "junior_tip": "始终维持 O(1) 辅助空间与严格 O(log N) 对数级时间复杂度。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;

        // 判定左半段是否是完全单调升序的（必须带 <=）
        if (nums[left] <= nums[mid]) {
            // target 在左半边有序区间范围内
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // 右半段是完全单调升序的
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：mid 命中立即 return mid 提前通关", "detail": "细扣：只要二分探针命中直接交卷，优先拦截正解。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：nums[left] <= nums[mid] 锁定有序半区", "detail": "细扣：两数时 left===mid 必须带等号判定左半段有序，防逻辑漏网。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：有序左半区范围区间判定收缩", "detail": "细扣：nums[left] <= target < nums[mid] 确认在左侧压缩 right，否则转向右侧。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：右半区单调升序判定与指针收缩", "detail": "细扣：nums[mid] < target <= nums[right] 锁定右半段收缩指针。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：出界未找返回 -1 与对数复杂度分析", "detail": "细扣：局部单调二分神技，时间复杂度严格 O(log N) 空间 O(1)。", "weight": 20}
        ]
    },
    153: {
        "title_cn": "寻找旋转排序数组中的最小值",
        "title_en": "Find Minimum in Rotated Sorted Array",
        "slug": "find-minimum-in-rotated-sorted-array",
        "difficulty": "Medium",
        "description": """已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
- 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
- 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

### 示例 1:
- 输入: nums = [3,4,5,1,2]
- 输出: 1
- 解释: 原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

### 示例 2:
- 输入: nums = [4,5,6,7,0,1,2]
- 输出: 0
- 解释: 原数组为 [0,1,2,4,5,6,7] 旋转 4 次得到输入数组。

### 示例 3:
- 输入: nums = [11,13,15,17]
- 输出: 11
- 解释: 原数组为 [11,13,15,17] 旋转 4 次得到输入数组。

### 提示/约束:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- nums 中的所有整数 互不相同
- nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转""",
        "plain_explanation": "旋转排序数组里找最小的那个数（波谷断崖点）。大白话核心：“永远拿中点的值 nums[mid] 和最右端的值 nums[right] 比高低”！为什么不跟 nums[left] 比？因为未旋转数组分不清！但跟 nums[right] 比永远不会错：如果 nums[mid] > nums[right]，说明左半边还在高高的山峰上，断崖波谷必定在右半边，且 mid 不可能是最小值，左指针直接跨过中点（left = mid + 1）；否则说明波谷在左半边或者 mid 自己就是波谷，把右指针收缩到中点（right = mid，【千万注意不能减 1】，因为 mid 自己可能是最小值！）。当 left 和 right 碰头（left === right）时，指向的那个数必定是唯一的最小值！",
        "js_helpers": [
            {
                "name": "right = mid 保留最小值候选",
                "what_it_does": "不能写 right = mid - 1。",
                "junior_tip": "【核心考点】因为 mid 本身可能正好踩在最小值上，减 1 会把它跳过丢失造成 Bug！"
            },
            {
                "name": "while (left < right) 指针汇聚循环条件",
                "what_it_does": "两指针逼近收敛，碰头时自动退出循环。",
                "junior_tip": "与 right = mid 紧密搭配，退出时必定有 left === right，指向全局唯一的波谷值。"
            },
            {
                "name": "锚定最右端点 nums[right] 的单调基准性",
                "what_it_does": "以右端点为基准判定断崖所在区间。",
                "junior_tip": "完美兼顾未旋转（升序）与旋转数组两种形态，逻辑最简最稳。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;

    // 当两指针未碰头时收敛
    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        // 如果中点比右端点大，说明波谷断崖在右侧
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // 波谷在左侧，或者中点自己就是最小值
            right = mid;
        }
    }

    return nums[left];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：while (left < right) 碰头汇聚出口", "detail": "细扣：两指针最终汇聚在同一个谷底坐标，防死循环。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：nums[mid] > nums[right] 锚定右半边", "detail": "细扣：断崖在右半段，mid 绝非最小值，left = mid + 1 稳妥推进。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：right = mid 绝对防守保留潜在极小值", "detail": "细扣：切忌 right = mid - 1，防止将正解最小值跳过抹杀。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：以 nums[right] 为基准统摄全形态", "detail": "细扣：未旋转单调升序数组同样天然兼容，边界无缝自洽。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：返回 nums[left] 收割结果与复杂度", "detail": "细扣：汇聚点即最小值，时间严格 O(log N) 空间 O(1)。", "weight": 20}
        ]
    },
    4: {
        "title_cn": "寻找两个正序数组的中位数",
        "title_en": "Median of Two Sorted Arrays",
        "slug": "median-of-two-sorted-arrays",
        "difficulty": "Hard",
        "description": """给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

### 示例 1:
- 输入: nums1 = [1,3], nums2 = [2]
- 输出: 2.00000
- 解释: 合并数组 = [1,2,3] ，中位数 2

### 示例 2:
- 输入: nums1 = [1,2], nums2 = [3,4]
- 输出: 2.50000
- 解释: 合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

### 提示/约束:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6""",
        "plain_explanation": "两个有序数组，要求 O(log(min(m, n))) 找到中位数。合并排序是 O(M+N) 复杂度太高不合题意。大白话神级大招：“在较短的数组上划一刀（二分切分线）”！中位数的物理本质是什么？是把两个数组的所有数字切成等长的“左半大杂烩”和“右半大杂烩”，且左半边所有人必须全都 <= 右半边所有人！因为总长度固定，我们在短数组切一刀在位置 i，长数组对应的一刀位置 j = (m + n + 1) / 2 - i 就自动定死了！我们二分微调短数组上的这一刀，直到交叉比对全部满足（左上 <= 右下，且左下 <= 右上）。如果切在边界上，用 -Infinity 和 Infinity 充当保镖守卫，极其从容！",
        "js_helpers": [
            {
                "name": "优先确保 nums1 长度较短",
                "what_it_does": "if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);",
                "junior_tip": "在短数组上二分，二分次数只有 log(min(m, n))，速度最快且 j 永远不会算成负数，杜绝数组越界！"
            },
            {
                "name": "-Infinity 与 Infinity 极值哨兵守卫",
                "what_it_does": "切线切在数组两端时，用无穷大哨兵填充。",
                "junior_tip": "无需写繁琐的边界 if 判断，三元表达式 i===0 ? -Infinity : nums1[i-1] 极其优美自洽。"
            },
            {
                "name": "totalLeft = Math.floor((m + n + 1) / 2) 天平平衡式",
                "what_it_does": "奇数时左半边多分 1 个，偶数时平分左右两半。",
                "junior_tip": "加 1 的整除设计保证无论是奇数还是偶数，奇数时的中位数必定是左半边的最大值。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // 第 1 步：保证在较短的数组上做二分切分，确保 j 不越界
    if (nums1.length > nums2.length) {
        return findMedianSortedArrays(nums2, nums1);
    }

    const m = nums1.length;
    const n = nums2.length;
    // 左半部分应分配的总元素个数
    const totalLeft = Math.floor((m + n + 1) / 2);

    let left = 0, right = m;

    while (left <= right) {
        // nums1 切在 i，nums2 相应切在 j
        const i = Math.floor((left + right) / 2);
        const j = totalLeft - i;

        // 切线左右两侧的 4 个关键数字（边界用无穷大守护）
        const nums1LeftMax = i === 0 ? -Infinity : nums1[i - 1];
        const nums1RightMin = i === m ? Infinity : nums1[i];
        const nums2LeftMax = j === 0 ? -Infinity : nums2[j - 1];
        const nums2RightMin = j === n ? Infinity : nums2[j];

        // 交叉比对满足条件：左半边全员 <= 右半边全员
        if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
            // 奇数个元素，中位数就是左半边最大的那个
            if ((m + n) % 2 === 1) {
                return Math.max(nums1LeftMax, nums2LeftMax);
            } else {
                // 偶数个元素，中位数是左半最大和右半最小的均值
                return (Math.max(nums1LeftMax, nums2LeftMax) + Math.min(nums1RightMin, nums2RightMin)) / 2;
            }
        } else if (nums1LeftMax > nums2RightMin) {
            // nums1 切太靠右了，往左收缩
            right = i - 1;
        } else {
            // nums1 切太靠左了，往右推进
            left = i + 1;
        }
    }

    return 0.0;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：优先确保短数组在前启动二分", "detail": "细扣：调换参数确保二分在较短数组，j 恒定不越界。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：totalLeft 与切分线 i/j 联动公式", "detail": "细扣：j = totalLeft - i，确保左右两半集合等长平衡。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：-Infinity 与 Infinity 边界守护", "detail": "细扣：i===0 或 i===m 填入无穷哨兵，消除切在端点的越界判断。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：交叉比较双不等式判定与二分方向微调", "detail": "细扣：nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin 完美判定。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：奇偶分类输出与对数时间复杂度分析", "detail": "细扣：奇数取 max，偶数取 (max+min)/2，时间严格 O(log(min(M, N)))。", "weight": 20}
        ]
    }
}
