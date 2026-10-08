"""Day 5 JavaScript Solutions with Junior-level explanations, JS helpers, code-aligned checkpoints, and complete problem descriptions."""

DAY_5_JS_DATA = {
    20: {
        "title_cn": "有效的括号",
        "title_en": "Valid Parentheses",
        "slug": "valid-parentheses",
        "difficulty": "Easy",
        "description": """给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([])"
输出：true

提示：
- 1 <= s.length <= 10^4
- s 仅由括号 '()[]{}' 组成""",
        "plain_explanation": "检验括号匹配有效性。大白话后进先出（栈）：想象一个子弹弹夹，后塞进去的子弹必须最先打出来。最巧的解法是'见左存右，见右比对'：遍历字符串时，只要遇到左括号（'(', '{', '['），我们心里期盼的是它的另一半，所以直接把对应的右括号（')', '}', ']'）压入弹夹 stack 里！当遇到右括号时，弹夹最顶上吐出的那颗子弹必须跟我眼前看到的这个右括号一模一样（stack.pop() === ch）。如果弹夹早就空了（弹不出子弹），或者弹出来的符号对不上，说明顺序错乱，当场判定 false！全部扫完后，弹夹必须刚好打空（stack.length === 0），才是完完全全的对称闭合！另外开局检查：若字符串长度为奇数，绝不可能两两成对，直接剪枝秒退！",
        "js_helpers": [
            {
                "name": "s.length % 2 !== 0 奇偶剪枝",
                "what_it_does": "判断字符串字符总数是否为奇数。",
                "junior_tip": "奇数个字符必然无法两两闭合配对，开局一行代码直接拦截，省时省力！"
            },
            {
                "name": "对象映射表 mapping = { '(': ')', '{': '}', '[': ']' }",
                "what_it_does": "以左括号为 key，对应期待匹配的右括号为 value。",
                "junior_tip": "遇到左括号直接压入其期待的右括号，出栈比对时逻辑极度干净！"
            },
            {
                "name": "stack.push() 与 stack.pop()",
                "what_it_does": "push 将元素压入数组末尾（栈顶），pop 移除并返回末尾元素。",
                "junior_tip": "若栈为空，stack.pop() 会安全返回 undefined，与任何字符比对都是 false。"
            },
            {
                "name": "stack.length === 0 验空机制",
                "what_it_does": "检查栈内是否还有残留的未匹配左括号。",
                "junior_tip": "必须严格等于 0，防止类似 '(((' 这种只进不出的孤儿左括号蒙混过关。"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // 第 1 步：提前剪枝。如果字符串长度是奇数，绝不可能两两配对成功
    if (s.length % 2 !== 0) return false;

    // 第 2 步：构建映射表：遇到左括号，映射出它期望配对的右括号
    const map = {
        '(': ')',
        '{': '}',
        '[': ']'
    };

    // 辅助栈：后进先出 (LIFO)，存放期待被消除的右括号
    const stack = [];

    // 第 3 步：遍历字符串中的每一个字符
    for (const ch of s) {
        if (map[ch]) {
            // 如果是左括号，把期望配对的对应右括号压入栈中
            stack.push(map[ch]);
        } else {
            // 如果是右括号，从栈顶弹出一个期望值进行比对
            // 若此时栈已经空了（pop 出 undefined），或者弹出的字符与当前右括号不匹配，说明非法
            if (stack.pop() !== ch) {
                return false;
            }
        }
    }

    // 第 4 步：循环结束后，栈必须恰好为空（防止类似 "(()" 这种有多余左括号残留的情况）
    return stack.length === 0;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：s.length % 2 !== 0 奇数提前剪枝", "detail": "细扣：奇数个字符无法两两闭合配对，一行代码早退提升执行效率。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：构建左括号到期望右括号的对象映射表", "detail": "细扣：const map = { '(': ')', '{': '}', '[': ']' } 统一管理配对关系。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：遇到左括号压入期待的右括号 stack.push(map[ch])", "detail": "细扣：见左压右消除复杂的反向反查分支，使栈顶始终为当前唯一期望值。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：遇到右括号校验 stack.pop() !== ch", "detail": "细扣：空栈弹栈安全得 undefined，字符不符立即阻断返回 false。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：最终栈完全排空验证 return stack.length === 0", "detail": "细扣：防止残留未闭合的多余左括号，时间 O(N) 空间 O(N)。", "weight": 20}
        ]
    },

    155: {
        "title_cn": "最小栈",
        "title_en": "Min Stack",
        "slug": "min-stack",
        "difficulty": "Medium",
        "description": """设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:
- MinStack() 初始化堆栈对象。
- void push(int val) 将元素val推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

示例 1:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // 返回 -3
minStack.pop();
minStack.top();    // 返回 0
minStack.getMin(); // 返回 -2

示例 2:
输入：
["MinStack","push","push","getMin","pop","getMin"]
[[],[1],[2],[],[],[]]
输出：
[null,null,null,1,null,1]

解释：
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.getMin(); // 返回 1
minStack.pop();
minStack.getMin(); // 返回 1

提示：
- -2^31 <= val <= 2^31 - 1
- pop、top 和 getMin 操作总是在 非空栈 上调用
- push, pop, top, and getMin 最多被调用 3 * 10^4 次""",
        "plain_explanation": "设计一个栈，要求随时能以 O(1) 速度返回当前最小值。大白话：'双栈齐步走（同步辅助栈快照）'。准备两个平行的数组：普通栈 stack 正常存每一次 push 的数；辅助栈 minStack 记录历史各时刻的'全局最小值快照'。每次 push 一个新数 val：普通栈压入 val；辅助栈看一眼：如果辅助栈是空的，直接压入 val；否则把当前 val 和辅助栈栈顶相比，把更小的值压入辅助栈（Math.min(val, minStack栈顶)）！pop 的时候两栈同步 pop。这样 minStack 的栈顶永远记录着当前高度下的全局最小值，getMin 只要读一眼 minStack 的末尾就行，纯 O(1) 瞬时交付！",
        "js_helpers": [
            {
                "name": "minStack[minStack.length - 1] 或 minStack.at(-1)",
                "what_it_does": "读取栈顶元素而不弹出。",
                "junior_tip": "ES2022 支持 arr.at(-1) 优雅读取最后一位；传统写法用 length - 1 兼容性最好。"
            },
            {
                "name": "Math.min(val, currentMin)",
                "what_it_does": "计算当前压入值与历史最小值的极小者。",
                "junior_tip": "将这一步计算结果压入辅助栈，就是给当前时刻拍了一张历史极值快照！"
            },
            {
                "name": "双栈同步高度契约 (Parallel Stacks)",
                "what_it_does": "保持 stack 与 minStack 的高度永远保持 1:1 等高。",
                "junior_tip": "一进双进，一出一出，保证状态回滚时精准对齐，绝不产生偏差错位。"
            }
        ],
        "code_js": '''var MinStack = function() {
    // 数据栈：保存所有实际压入的数据
    this.stack = [];
    // 辅助最小栈：保存每个状态对应的历史最小值快照，栈顶始终是当前全局最小值
    this.minStack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val);

    // 如果辅助栈为空，当前元素就是最小值；
    // 否则比较当前 val 与辅助栈栈顶，将二者的较小值压入辅助栈
    if (this.minStack.length === 0) {
        this.minStack.push(val);
    } else {
        const currentMin = this.minStack[this.minStack.length - 1];
        this.minStack.push(Math.min(val, currentMin));
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    // 双栈高度完全同步，必须同时弹出
    this.stack.pop();
    this.minStack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    // 读取数据栈栈顶元素，时间复杂度 O(1)
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    // 读取辅助最小栈栈顶元素，即当前所有元素的最小值，时间复杂度 O(1)
    return this.minStack[this.minStack.length - 1];
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：构造函数初始化 stack 与 minStack 双栈", "detail": "细扣：双栈架构，主栈存数据，minStack 负责历史极值快照。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：push 同步压入当前最小值快照", "detail": "细扣：Math.min(val, currentMin) 保持两栈等高与极值跟随更新。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：pop 两栈同步弹出回滚历史状态", "detail": "细扣：一弹双弹，数据和极值同时退回到上一历史时刻。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：top 读取主栈栈顶元素", "detail": "细扣：访问 this.stack 末尾，严格 O(1) 获取最新压入值。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：getMin 返回 minStack 栈顶极值", "detail": "细扣：零耗时 O(1) 瞬时查询，空间占用 O(N) 完美达标。", "weight": 20}
        ]
    },

    394: {
        "title_cn": "字符串解码",
        "title_en": "Decode String",
        "slug": "decode-string",
        "difficulty": "Medium",
        "description": """给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

提示：
- 1 <= s.length <= 30
- s 由小写英文字母、数字和方括号 '[]' 组成
- s 保证是一个 有效 的输入。
- s 中所有整数的取值范围为 [1, 300]""",
        "plain_explanation": "把 3[a2[c]] 解码成 accaccacc。大白话：'穿越虫洞保护现场，套娃剥离重现'。像这种多层嵌套括号，最内层的 2[c] 必须先算出来变成 cc，再跟外层的 a 拼成 acc，再乘以 3 变成 accaccacc。我们手里拿两个变量：当前倍数 currentNum 和当前字符串 currentStr。碰到数字就累加进 currentNum（注意多位数乘 10 进位）；碰到普通字母就累加进 currentStr。当碰到 '[' 时，说明要跳进更深一层的括号了，我们把'外面这一层还没拼完的字符串和当前的倍数'打包成一个元组，压入栈中保护起来（stack.push([currentStr, currentNum])），然后清空当前变量轻装上阵！当碰到 ']' 时，说明内层结束了，把上一层的案发现场弹出来（[prevStr, repeat]），当前结果拼接成 prevStr + currentStr.repeat(repeat)，层层剥开！",
        "js_helpers": [
            {
                "name": "str.repeat(count)",
                "what_it_does": "将字符串重复 count 次拼接成新字符串。",
                "junior_tip": "'c'.repeat(2) 得到 'cc'，原生 ES6 神器，替代手写拼接循环！"
            },
            {
                "name": "currentNum = currentNum * 10 + Number(ch)",
                "what_it_does": "解析连续多位数字字符（例如 '100'）。",
                "junior_tip": "遇到字符数字时必须乘 10 累加，防止把 100[a] 误当作 1[a]0[a]0[a]！"
            },
            {
                "name": "const [prevStr, repeat] = stack.pop()",
                "what_it_does": "ES6 数组解构赋值，提取上一层存盘的字符串前缀与倍数。",
                "junior_tip": "一次 pop 还原两个变量，语法简洁明了。"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    // 栈中保存每一层嵌套的上下文现场：[上一层的字符串前缀 prevStr, 本层括号内容的重复次数 repeatNum]
    const stack = [];
    let currentStr = '';
    let currentNum = 0;

    for (const ch of s) {
        if (ch >= '0' && ch <= '9') {
            // 第 1 步：解析多位数字，例如 '12' 会依次计算 1 -> 1*10 + 2 = 12
            currentNum = currentNum * 10 + Number(ch);
        } else if (ch === '[') {
            // 第 2 步：遇到左括号，进入深层环境，将当前外层的字符串和倍数打包压栈保存
            stack.push([currentStr, currentNum]);
            // 现场存盘完毕，清空当前变量，用于收集内层括号里的内容
            currentStr = '';
            currentNum = 0;
        } else if (ch === ']') {
            // 第 3 步：遇到右括号，内层结束，弹栈恢复上一层现场
            const [prevStr, repeatNum] = stack.pop();
            // 将内层字符串重复 repeatNum 次，并拼接在上一层字符串之后
            currentStr = prevStr + currentStr.repeat(repeatNum);
        } else {
            // 第 4 步：普通英文字母，直接拼接到当前层字符串后
            currentStr += ch;
        }
    }

    return currentStr;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：数字处理 currentNum * 10 + Number(ch)", "detail": "细扣：解决 100[a] 这类多位数连续字符解析，防止低级按位截断错误。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：遇到 '[' 保护外层现场 stack.push([currentStr, currentNum])", "detail": "细扣：将外层未完工字符串与内层重复倍数打包进栈保存上下文。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：清空 currentStr 与 currentNum 深入内层", "detail": "细扣：轻装上阵，隔离内外两层的解析状态与字符累加。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：遇到 ']' 弹栈与 currentStr.repeat 拼合", "detail": "细扣：利用原生 repeat 方法快速复制内层字符串并与上一层前缀拼接。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：普通字母收集与返回最终解码字符串", "detail": "细扣：单次线性扫描，时间 O(解码总长) 空间 O(嵌套深度)。", "weight": 20}
        ]
    },

    739: {
        "title_cn": "每日温度",
        "title_en": "Daily Temperatures",
        "slug": "daily-temperatures",
        "difficulty": "Medium",
        "description": """给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]

提示：
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100""",
        "plain_explanation": "算算还要等几天才能碰到比今天更高的温度。单调栈母题！大白话：'高个子挡住视线排队，单调递减栈解救苦等者'。准备一个数组栈 stack，专门存数组的'日期下标 i'。栈内保持温度从栈底到栈顶单调递减。我们顺着天气预报一天天往后看：如果今天的气温比栈顶那天的气温还要高，说明栈顶那天的苦日子熬到头了！立刻把栈顶那天 pop 弹出来，天数差就是 i - 栈顶下标，记入答案！继续看新的栈顶，直到栈顶气温比今天更高，才把今天的下标压入栈中排队。留在栈里出不来的人，说明往后永远没有更暖和的一天，默认答案就是 0 天！每个元素最多进出栈一次，均摊严格 O(N)！",
        "js_helpers": [
            {
                "name": "new Array(n).fill(0)",
                "what_it_does": "创建指定长度 n 且所有元素预填充为 0 的结果数组。",
                "junior_tip": "留在栈里未被更新的元素自然保持 0 天，无需二次循环处理！"
            },
            {
                "name": "temperatures[stack[stack.length - 1]]",
                "what_it_does": "读取栈顶下标所对应的历史温度值。",
                "junior_tip": "栈里必须存下标，存温度值就无法计算相隔天数（下标差 i - prevIdx）了！"
            },
            {
                "name": "while (stack.length > 0 && currentTemp > stackTopTemp)",
                "what_it_does": "单调栈连续弹栈结算循环。",
                "junior_tip": "必须用 while 而不是 if，因为今天升温可能一口气解救前面连续好几天的低温排队者！"
            }
        ],
        "code_js": '''/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const n = temperatures.length;
    // 第 1 步：初始化答案数组，默认全为 0（代表若后续没有更高温度则保持 0）
    const res = new Array(n).fill(0);

    // 单调栈：存储天数的下标索引，栈内索引对应的温度自栈底到栈顶保持单调递减
    const stack = [];

    // 第 2 步：遍历每一天的温度
    for (let i = 0; i < n; i++) {
        const currentTemp = temperatures[i];

        // 第 3 步：如果今天的温度大于栈顶那一天的温度，说明栈顶找到了下一个更高温度
        while (stack.length > 0 && currentTemp > temperatures[stack[stack.length - 1]]) {
            const prevIdx = stack.pop();
            // 计算等待天数（下标差）
            res[prevIdx] = i - prevIdx;
        }

        // 第 4 步：将当天下标压入单调栈，等待未来的更高温度来解救
        stack.push(i);
    }

    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：结果数组 new Array(n).fill(0) 初始化", "detail": "细扣：无法升温的日子默认直接保留 0 天，消除收尾多余遍历。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：单调栈 stack 存储下标索引而非温度值", "detail": "细扣：必须存下标才能算出日期差 i - prevIdx，栈内温度单调递减。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：while 循环比对当前温度与栈顶对应温度", "detail": "细扣：使用 while 连续解救所有低于当前温度的历史日期。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：弹出栈顶并结算等待天数 res[prevIdx] = i - prevIdx", "detail": "细扣：下标相减得到第一个更高温度的天数差，赋值给对应原位置。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：当天下标压栈与 O(N) 线性时间均摊证明", "detail": "细扣：每个索引只入栈出栈各一次，整体操作严格 2N，性能远超暴力双重循环。", "weight": 20}
        ]
    },

    84: {
        "title_cn": "柱状图中最大的矩形",
        "title_en": "Largest Rectangle in Histogram",
        "slug": "largest-rectangle-in-histogram",
        "difficulty": "Hard",
        "description": """给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为高度为 5，宽度为 2 的矩形，面积为 10（即 5 * 2 = 10）。

示例 2：
输入：heights = [2,4]
输出：4

提示：
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4""",
        "plain_explanation": "在一排柱子中找能圈出的最大矩形面积。大白话核心：以每一根柱子的高度 h 作为矩形的高，我们要找这根柱子能向左向右延展的最大宽度！它向左能伸多远？直到碰到第一根比它矮的柱子被卡住；向右同理！所以我们要找左右第一个更矮的柱子。神来之笔：'单调递增栈 + 首尾各补一个 0（哨兵）'！首部的 0 避免了栈为空时的繁琐判断，宽度计算时新栈顶必然存在；尾部的 0 像清道夫一样在最后一步把栈里所有递增的柱子全部强行弹出结算面积！弹出柱子时，高就是该柱子高度，宽就是当前索引 i - 新栈顶 - 1，面积瞬间算出！单次线性扫描即可达到 O(N)！",
        "js_helpers": [
            {
                "name": "[0, ...heights, 0] 首尾双哨兵",
                "what_it_does": "在高度数组最前和最后各添加一个高度为 0 的哨兵元素。",
                "junior_tip": "【单调栈神技】首部 0 防止栈空保证左界存在，尾部 0 强制末端所有柱子出栈结算，一行代码顶 20 行边界特判！"
            },
            {
                "name": "w = i - stack[stack.length - 1] - 1",
                "what_it_does": "计算以弹出柱子为高的矩形有效延展宽度。",
                "junior_tip": "弹出后，新栈顶就是左边第一个更矮的柱子，当前 i 是右边第一个更矮的柱子，开区间宽度公式必须减 1！"
            },
            {
                "name": "Math.max(maxArea, h * w)",
                "what_it_does": "动态更新当前最大矩形面积。",
                "junior_tip": "弹出每一根柱子都当场结算并刷新历史最大值。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    // 第 1 步：在原数组首尾各添加一个高度为 0 的哨兵
    // 首部 0：防止栈空，保证计算宽度时新栈顶必然存在
    // 尾部 0：在遍历终点强制把栈内剩余的所有递增柱子全部弹出结算
    const arr = [0, ...heights, 0];
    
    // 单调栈：保存柱子的下标，栈内下标对应的高度保持单调递增
    const stack = [];
    let maxArea = 0;

    // 第 2 步：遍历带有哨兵的高度数组
    for (let i = 0; i < arr.length; i++) {
        // 当当前柱子的高度小于栈顶柱子的高度时，说明栈顶柱子找到了右侧第一个比它矮的边界
        while (stack.length > 0 && arr[i] < arr[stack[stack.length - 1]]) {
            // 弹出栈顶柱子作为矩形的高
            const h = arr[stack.pop()];
            // 弹出后，新的栈顶柱子就是该柱子左侧第一个比它矮的边界，i 是右侧第一个比它矮的边界
            // 两界之间的宽度为：i - left - 1
            const w = i - stack[stack.length - 1] - 1;
            // 计算面积并刷新最大值
            maxArea = Math.max(maxArea, h * w);
        }

        // 当前柱子下标入栈
        stack.push(i);
    }

    return maxArea;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：[0, ...heights, 0] 构造首尾双哨兵", "detail": "细扣：首 0 防栈空，尾 0 强制完全出栈清空结算，消除繁杂特判。", "weight": 15},
            {"dimension": "step2", "title": "代码第 2 步：单调递增栈维护下标高度升序", "detail": "细扣：栈内下标对应高度严格单调递增，方便定位左右边界。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：arr[i] < arr[栈顶] 触发弹栈结算", "detail": "细扣：遇到右侧更矮阻碍，以被弹出柱子为高开始结算矩形面积。", "weight": 15},
            {"dimension": "step4", "title": "代码第 4 步：宽度公式 w = i - stack[top] - 1 精准算宽", "detail": "细扣：弹出后新栈顶是左界，当前 i 是右界，开区间算宽准确无误。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：maxArea = Math.max(maxArea, h * w) 刷新极值", "detail": "细扣：高宽相乘计算当前矩形面积并滚动更新全局最大值。", "weight": 15},
            {"dimension": "step6", "title": "代码第 6 步：单次线性扫描严格 O(N) 复杂度证明", "detail": "细扣：每个柱子下标进栈一次出栈一次，时间复杂度严格 O(N)。", "weight": 15}
        ]
    },

    215: {
        "title_cn": "数组中的第 K 个最大元素",
        "title_en": "Kth Largest Element in an Array",
        "slug": "kth-largest-element-in-an-array",
        "difficulty": "Medium",
        "description": """给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

提示：
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4""",
        "plain_explanation": "找数组中第 k 大的数。虽然 sort((a,b)=>b-a) 取 nums[k-1] 也能过，但面试官要看的是'快速选择算法 (Quick Select)'！大白话：找第 k 大，也就是找升序排列后下标为 targetIdx = nums.length - k 的那个数。类似快速排序切分，我们随机挑选一个基准数 pivot，把小于等于它的丢左边，大于它的丢右边，最后基准数落在一个确定位置 i。此时见分晓：如果 i 刚好等于 targetIdx，直接命中收工！如果 i 太小（i < targetIdx），说明目标在右半边，左半边彻底抛弃，只去右半边找；如果 i 太大，只去左半边找！快排两边都走 (O(N log N))，快选每次扔掉一半只走一边 (N + N/2 + N/4 + ... <= 2N)，数学期望总耗时只要惊人的 O(N)！特别注意：必须使用随机主元防止极端用例退化！",
        "js_helpers": [
            {
                "name": "targetIdx = nums.length - k 转化目标",
                "what_it_does": "将找'第 k 大'转换为找升序排列后下标为 'nums.length - k' 的元素。",
                "junior_tip": "正向升序思维更加符合快排切分的下标比较直觉。"
            },
            {
                "name": "Math.floor(Math.random() * (right - left + 1)) + left 随机主元",
                "what_it_does": "在 [left, right] 区间内随机挑选一个索引作为 pivot 并与末位交换。",
                "junior_tip": "【必防死穴】遇到完全升序/降序用例，固定选端点会退化成 O(N^2) 超时，随机化可使期望稳定在 O(N)！"
            },
            {
                "name": "[nums[i], nums[j]] = [nums[j], nums[i]]",
                "what_it_does": "ES6 解构单行交换数组元素。",
                "junior_tip": "不需要声明 temp 变量，Lomuto 分区写起来极其利落。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    // 第 1 步：将“第 k 大”转换为“升序排序后下标为 targetIdx 的元素”
    const targetIdx = nums.length - k;

    // 快速选择辅助函数：在 [left, right] 区间内寻找 targetIdx
    const quickSelect = (left, right) => {
        // 递归触底
        if (left >= right) return nums[left];

        // 第 2 步：随机选取 pivot 下标并交换到区间末尾，防止极端用例退化至 O(N^2)
        const randIdx = left + Math.floor(Math.random() * (right - left + 1));
        [nums[randIdx], nums[right]] = [nums[right], nums[randIdx]];
        const pivot = nums[right];

        // 第 3 步：Lomuto 分区操作，将小于等于 pivot 的元素集中到左侧
        let i = left;
        for (let j = left; j < right; j++) {
            if (nums[j] <= pivot) {
                [nums[i], nums[j]] = [nums[j], nums[i]];
                i++;
            }
        }
        // 将 pivot 放置到最终正确的分界点 i 上
        [nums[i], nums[right]] = [nums[right], nums[i]];

        // 第 4 步：单侧分治，判断 targetIdx 与分界点 i 的相对位置
        if (i === targetIdx) {
            return nums[i]; // 恰好命中目标
        } else if (i < targetIdx) {
            return quickSelect(i + 1, right); // 目标在右半区，仅递归右侧
        } else {
            return quickSelect(left, i - 1);  // 目标在左半区，仅递归左侧
        }
    };

    return quickSelect(0, nums.length - 1);
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：targetIdx = nums.length - k 转化目标", "detail": "细扣：将第 k 大转为升序第 n-k 位索引查找，确立基准位置。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：随机选取 pivot 主元防退化", "detail": "细扣：Math.random 打散极端单调用例，防 O(N^2) 耗时击穿。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：Lomuto 原地切分分区划分区间", "detail": "细扣：双指针在区间内将 <= pivot 的数字沉到左边，pivot 归位。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：命中 targetIdx 当场返回", "detail": "细扣：i === targetIdx 命中即直接 return nums[i] 早停。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：单侧分治砍半与均摊 O(N) 复杂度推导", "detail": "细扣：快选只深入包含 target 的单边区间，等比数列求和证明均摊 O(N)。", "weight": 20}
        ]
    },

    347: {
        "title_cn": "前 K 个高频元素",
        "title_en": "Top K Frequent Elements",
        "slug": "top-k-frequent-elements",
        "difficulty": "Medium",
        "description": """给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
- 1 <= nums.length <= 10^5
- k 的取值范围是 [1, 数组中不相同的元素的个数]
- 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。""",
        "plain_explanation": "找出现频次最高的前 k 个元素。大白话'频次抽屉（桶排序）倒序收割'：1. 先用 Map 统计每个数字出现的频次（比如数字 3 出现了 5 次）；2. 建一组'频次桶 buckets'（数组下标代表出现的次数，桶里放具有该频次的数字列表）。因为数组长度是 n，一个数字最多也就能出现 n 次，所以桶的长度就是 n + 1！3. 从最大的频次 n 倒着往回扫描抽屉，把抽屉里的数字捞出来放进答案数组，捞满 k 个立刻收工！整个过程只有哈希计数 O(N)、入桶 O(N) 和倒序提取 O(N)，时间严格 O(N)，比手写堆排序还要快得多！",
        "js_helpers": [
            {
                "name": "map.set(num, (map.get(num) || 0) + 1)",
                "what_it_does": "使用 Map 统计每个元素出现的次数。",
                "junior_tip": "|| 0 是小白必须掌握的兜底技巧，首次出现默认频次从 0 累加。"
            },
            {
                "name": "Array.from({ length: n + 1 }, () => [])",
                "what_it_does": "创建 n + 1 个独立的空数组桶。",
                "junior_tip": "【小白必防浅拷贝坑】绝对不能写 new Array(n+1).fill([])，这样所有的桶共享同一个数组引用，改一个全变了！必须用 Array.from() 独立生成！"
            },
            {
                "name": "for (let freq = buckets.length - 1; freq > 0; freq--)",
                "what_it_does": "从最大可能频次从后向前倒序扫描桶。",
                "junior_tip": "天然保证高频数字优先出桶，达到收集数量 k 即可提前返回。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    // 第 1 步：使用 Map 统计每个数字出现的频率
    const freqMap = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }

    // 第 2 步：构建桶数组，下标代表出现的频次，内容为该频次对应的数字列表
    // 频次最大不会超过 nums.length，因此桶的长度为 nums.length + 1
    // 注意：必须使用 Array.from 独立初始化每个子数组，绝不能用 fill([])（会导致引用共享）
    const buckets = Array.from({ length: nums.length + 1 }, () => []);

    for (const [num, freq] of freqMap.entries()) {
        buckets[freq].push(num);
    }

    // 第 3 步：从最高频次（buckets.length - 1）向后倒序遍历桶，提取前 k 个高频元素
    const res = [];
    for (let freq = buckets.length - 1; freq > 0; freq--) {
        for (const num of buckets[freq]) {
            res.push(num);
            // 收集齐 k 个元素立即提前返回
            if (res.length === k) {
                return res;
            }
        }
    }

    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：Map 统计数字出现频次", "detail": "细扣：freqMap.set(num, (freqMap.get(num) || 0) + 1) 线性统计频次。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：Array.from 建立独立桶数组", "detail": "细扣：以频次为下标，桶中存元素数组，防 fill([]) 共享引用严重 Bug。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：遍历哈希表将元素按频次分发入桶", "detail": "细扣：for (const [num, freq] of freqMap.entries()) 对应入桶。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：倒序扫描桶优先收割高频者", "detail": "细扣：从最大可能频次从后向前遍历桶，先摘取频率最高的数字。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：res.length === k 立即早停与 O(N) 交付", "detail": "细扣：捞满 k 个当场交付，时间严格 O(N) 性能超越堆排序。", "weight": 20}
        ]
    },

    295: {
        "title_cn": "数据流的中位数",
        "title_en": "Find Median from Data Stream",
        "slug": "find-median-from-data-stream",
        "difficulty": "Hard",
        "description": """中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。

实现 MedianFinder 类:
- MedianFinder() 初始化 MedianFinder 对象。
- void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
- double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10^-5 以内的机率将被接受。

示例 1:
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

示例 2:
输入
["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"]
[[], [2], [], [3], []]
输出
[null, null, 2.0, null, 2.5]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(2);    // arr = [2]
medianFinder.findMedian(); // 返回 2.0
medianFinder.addNum(3);    // arr = [2, 3]
medianFinder.findMedian(); // 返回 2.5 ((2 + 3) / 2)

提示:
- -10^5 <= num <= 10^5
- 在调用 findMedian 之前，数据结构中至少有一个元素
- 最多 5 * 10^4 次调用 addNum 和 findMedian""",
        "plain_explanation": "不断有新数字流进来，随时以 O(1) 速度返回中位数。大白话：'二分插入法维持有序数组，中间一刀切'。在 JS 没有内置堆的情况下，最优雅且面试官极度认可的高性能方案是维护一个严格有序的数组 this.arr。每次 addNum 进来新数时，用二分查找（Binary Search）在 O(log N) 速度下精准找到它应该插入的正确位置 left，然后调用 splice(left, 0, num) 插进去，维持数组始终单调递增有序！求中位数时直接看正中间：如果总数是奇数，中位数就是正中间那个（arr[mid]）；如果总数是偶数，就是正中间两个数字的平均值（(arr[mid-1] + arr[mid]) / 2）！查询纯 O(1)，代码极度简洁坚固！",
        "js_helpers": [
            {
                "name": "二分查找定位插入索引 left",
                "what_it_does": "在有序数组中以 O(log N) 复杂度找到新数的位置。",
                "junior_tip": "while (left <= right) 逼近边界，当循环结束时 left 恰好是首个大于等于 num 的位置。"
            },
            {
                "name": "arr.splice(idx, 0, item)",
                "what_it_does": "在数组指定索引处插入新元素，保持数组有序。",
                "junior_tip": "第二个参数为 0 表示不删除任何旧元素，纯插入操作。"
            },
            {
                "name": "奇偶区分取中位数",
                "what_it_does": "n % 2 === 1 取单个中位数，否则取相邻双数求平均值。",
                "junior_tip": "利用 Math.floor(n / 2) 精确计算中点下标。"
            }
        ],
        "code_js": '''var MedianFinder = function() {
    // 维护一个始终保持升序排列的数组
    this.arr = [];
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    // 第 1 步：使用二分查找在 O(log N) 时间内寻找 num 应当插入的位置
    let left = 0;
    let right = this.arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (this.arr[mid] >= num) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    // 第 2 步：left 即为新数字在有序数组中的正确插入位置，将其插入保持有序
    this.arr.splice(left, 0, num);
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    const n = this.arr.length;
    const mid = Math.floor(n / 2);

    // 第 3 步：若总数为奇数，正中间的数即为中位数
    if (n % 2 === 1) {
        return this.arr[mid];
    } else {
        // 第 4 步：若总数为偶数，取中间两个数的算术平均值
        return (this.arr[mid - 1] + this.arr[mid]) / 2;
    }
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：有序数组 this.arr 容器初始化", "detail": "细扣：保持数据流内元素升序排列，奠定中位数快速提取基础。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：二分定位插入点 left", "detail": "细扣：O(log N) 速度确定新元素插入位置，left 最终收敛于正确插入点。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：splice(left, 0, num) 就地插入", "detail": "细扣：动态维护数组严格单调递增性。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：findMedian 奇数长度正中单数提取", "detail": "细扣：n % 2 === 1 时直接返回 arr[mid]，瞬时 O(1)。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：findMedian 偶数长度中间双数均值计算", "detail": "细扣：(arr[mid - 1] + arr[mid]) / 2，严格遵循中位数数学定义。", "weight": 20}
        ]
    },

    121: {
        "title_cn": "买卖股票的最佳时机",
        "title_en": "Best Time to Buy and Sell Stock",
        "slug": "best-time-to-buy-and-sell-stock",
        "difficulty": "Easy",
        "description": """给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4""",
        "plain_explanation": "只能买卖一次股票，求最大利润。大白话单次遍历记录最低价：你坐着单向时光列车从第一天走到最后一天（股票不能穿梭回过去）。心里随时记着一个值：'我在这之前见过的历史上最低的买入价格 minPrice'。每天你都做两件事：如果今天的股价刷新了历史最低，更新 minPrice（低谷抄底）；如果今天的股价比 minPrice 高，心算一下'如果我今天卖出，能赚多少钱（price - minPrice）'，刷新历史最大利润 maxProfit！只要一次遍历，时间 O(N) 空间 O(1) 秒杀！",
        "js_helpers": [
            {
                "name": "let minPrice = Infinity",
                "what_it_does": "将历史最低价格初始化为无穷大。",
                "junior_tip": "保证第一天的股票价格无论多大，都能顺利成为首个历史最低价格记录。"
            },
            {
                "name": "price - minPrice",
                "what_it_does": "计算假定今天卖出所能获取的差价利润。",
                "junior_tip": "买入必然发生在卖出之前，单向时序天然保证交易合法性。"
            },
            {
                "name": "maxProfit 默认置 0",
                "what_it_does": "若股票一路狂跌，默认不进行任何买卖交易。",
                "junior_tip": "题目要求无法获利时输出 0，保底机制防止负数亏损。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // 维护遍历过程中见过的历史最低买入价格，初始设为正无穷
    let minPrice = Infinity;
    // 维护遍历过程中能够获取的最大利润，初始为 0
    let maxProfit = 0;

    // 单次遍历股价数组
    for (const price of prices) {
        if (price < minPrice) {
            // 第 1 步：遇到更低的股价，刷新历史最低成本买入点
            minPrice = price;
        } else if (price - minPrice > maxProfit) {
            // 第 2 步：若在历史最低点买入并在今天卖出利润更高，刷新最大利润
            maxProfit = price - minPrice;
        }
    }

    return maxProfit;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：minPrice = Infinity 奠基买入点", "detail": "细扣：单变量滚动记录历史前缀最低价，初始设为无穷大。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：单层 for...of 循环推进日期", "detail": "细扣：单次扫描严格 O(N)，无需双重嵌套循环，杜绝 O(N^2) 超时。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：遇低点刷新 minPrice", "detail": "细扣：持续吸纳历史最低进价，锁定买入成本底线。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：遇高点测算差值刷新 maxProfit", "detail": "细扣：price - minPrice 与当前 maxProfit 比较，贪心锁定峰值利润。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：单调下跌保底返回 0 及 O(1) 空间验证", "detail": "细扣：单调下跌自然输出 0 不亏钱，时间 O(N) 额外空间仅为 O(1)。", "weight": 20}
        ]
    },

    55: {
        "title_cn": "跳跃游戏",
        "title_en": "Jump Game",
        "slug": "jump-game",
        "difficulty": "Medium",
        "description": """给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5""",
        "plain_explanation": "每个格子里的数字代表你能跳的最远距离，问能不能跳到最后一个格子。大白话贪心：'贪心雷达——最远火力覆盖范围 (maxReach) 滚雪球'。你根本不要去纠结每一步具体跳到哪一格。只要我们当前能覆盖到的最远右边界能够包罗万象，里面的任何落脚点我们都有办法走到！我们顺着步子一格一格往前走：只要当前位置 i 已经超过了你能到达的最远距离（i > maxReach），说明前面全是 0 陷阱，你根本走不到这里，直接断路返回 false！如果能走到，更新你的最远火力覆盖范围（maxReach = Math.max(maxReach, i + nums[i])）。一旦覆盖范围达到了或者超过了最后一个下标（maxReach >= n - 1），直接提前通关返回 true！",
        "js_helpers": [
            {
                "name": "i + nums[i] 算最远落脚点",
                "what_it_does": "当前坐标加上最大跳跃步数，得出从当前格起跳的最远射程。",
                "junior_tip": "维护连续覆盖范围，不需要回溯或 DP 数组！"
            },
            {
                "name": "if (i > maxReach) return false 断路拦截",
                "what_it_does": "检测当前指针是否走到了不可达的禁区。",
                "junior_tip": "若掉入全 0 陷阱导致无法前进，在此处被精准拦截并判假。"
            },
            {
                "name": "maxReach >= nums.length - 1 提前剪枝",
                "what_it_does": "若覆盖范围已经包含数组终点，提前宣布成功。",
                "junior_tip": "不需要遍历完后续所有元素，大幅缩减实际执行时间。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    // 维护当前能够到达的最远下标位置
    let maxReach = 0;

    for (let i = 0; i < nums.length; i++) {
        // 第 1 步：如果当前位置已经超越了最远可达范围，说明前面遇到了断层（0 陷阱），无法前进
        if (i > maxReach) {
            return false;
        }

        // 第 2 步：在当前格，更新最远能覆盖到的位置
        maxReach = Math.max(maxReach, i + nums[i]);

        // 第 3 步：如果最远可达范围已经覆盖或超越了最后一个下标，提前成功返回
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }

    return true;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：定义 maxReach = 0 最远覆盖线", "detail": "细扣：贪心维护当前可到达的最远闭区间边界。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：if (i > maxReach) return false 拦截断路", "detail": "细扣：掉进 0 的陷阱无法前进时安全判假，阻断无效遍历。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：Math.max(maxReach, i + nums[i]) 延展边界", "detail": "细扣：每步探测最大前进潜能，不断将最远覆盖线向右推移。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：maxReach >= n - 1 提前成功早停", "detail": "细扣：包含终点直接返回 true，剪除末端无用循环。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：单趟 O(N) 空间 O(1) 贪心无后效性验证", "detail": "细扣：只要更远的范围能被覆盖，其内部所有点皆必定可达，贪心逻辑闭环。", "weight": 20}
        ]
    },

    45: {
        "title_cn": "跳跃游戏 II",
        "title_en": "Jump Game II",
        "slug": "jump-game-ii",
        "difficulty": "Medium",
        "description": """给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
- 0 <= j <= nums[i] 
- i + j < n

返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

示例 1:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2

提示:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- 题目保证可以到达 nums[n-1]""",
        "plain_explanation": "一定能跳到终点，求跳到终点的最少跳跃次数。大白话：'火炬接力，波次推进（类似 BFS 按层展开）'。维护三个变量：steps（跳了几次）、end（当前这一步能跳到的最远边界）、maxPos（下一步能达到的极限边界）。我们一格格往前走，不断探测下一步能达到的最远位置（maxPos = Math.max(maxPos, i + nums[i])）。当我们走到了当前步数的极限 end 时，没办法了，这一步的能量耗尽了，必须正式起跳多耗费一步跳跃（steps++），并把边界更新为刚才物色好的潜力极限（end = maxPos）！【必防大坑】：循环只需要跑到倒数第二个格子（nums.length - 2）！因为到达终点后就不需要再跳了，如果跑到了最后一个格子，i === end 会错误地多算一次跳跃！",
        "js_helpers": [
            {
                "name": "for 循环只到 nums.length - 2",
                "what_it_does": "for (let i = 0; i < nums.length - 1; i++)。",
                "junior_tip": "【必须防多跳一步】如果遍历到了最后一个格子，触发 i === end 会错误地多算一次跳跃！"
            },
            {
                "name": "maxPos = Math.max(maxPos, i + nums[i])",
                "what_it_does": "动态搜寻当前波次内所有起跳点能达到的最远外推潜能。",
                "junior_tip": "不急于做决定，在当前步数耗尽前充分物色最好的落脚点。"
            },
            {
                "name": "if (i === end) 波次交接",
                "what_it_does": "当走到当前步数的边界，强制更新 end = maxPos 并将 steps++。",
                "junior_tip": "类似 BFS 层序遍历，当前层结束时步数加 1 进入下一层。"
            }
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let steps = 0;   // 记录跳跃次数
    let end = 0;     // 当前这一步跳跃所能覆盖的最远右边界
    let maxPos = 0;  // 在当前这一步区间内能够探测到的下一步最远潜力位置

    // 注意：只遍历到倒数第二个元素 (nums.length - 2)！
    // 因为到达终点时无需再起跳；若遍历到终点且恰好 i === end，会错误地多算一次 steps++
    for (let i = 0; i < nums.length - 1; i++) {
        // 第 1 步：探测当前区间内各点起跳能达到的最远位置
        maxPos = Math.max(maxPos, i + nums[i]);

        // 第 2 步：到达了当前步数的极限边界，必须起跳进入下一波次
        if (i === end) {
            end = maxPos; // 更新下一跳的覆盖终点
            steps++;      // 跳跃次数累加 1
        }
    }

    return steps;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：steps, end, maxPos 三变量协同语义确立", "detail": "细扣：分别记录步数、当前步边界与下一步潜能，构筑波次推进模型。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：for 循环上界设定为 n - 2 防多跳特判", "detail": "细扣：严格防止到达终点时多触发一次起跳计数，避免低级 Bug。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：maxPos 持续刷新最远潜能", "detail": "细扣：探查当前区间内所有跳跃点的最大外推力，选出最优接棒人。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：i === end 耗尽当前边界结算步数 steps++", "detail": "细扣：当前步能量耗尽必须起跳，步数自增进入下一波次。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：波次交接 end = maxPos 与 O(N) 贪心推导", "detail": "细扣：将下一波次终点设为最远潜力，单趟扫描 O(N) 空间 O(1)。", "weight": 20}
        ]
    },

    763: {
        "title_cn": "划分字母区间",
        "title_en": "Partition Labels",
        "slug": "partition-labels",
        "difficulty": "Medium",
        "description": """给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

例如，字符串 "ababcc" 能够被分成 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是无效的。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 

示例 2：
输入：s = "eccbbbbdec"
输出：[10]

提示：
- 1 <= s.length <= 500
- s 仅由小写英文字母组成""",
        "plain_explanation": "把字符串分成尽可能多的片段，保证同一个字母只出现在同一个片段中。大白话：'责任底线与橡皮筋撑大——段内的每个字母都拉着一根橡皮筋，直到所有人最后的尾巴都在圈内才能切断！' 先巡视一趟字符串，在哈希表 last 里记下每个字母'最后一次露面的下标'（比如字母 'a' 最后出现在第 8 格，那只要这个段里有 'a'，这个段的长度就必须至少延展到第 8 格才能切断！）。二次遍历字符串，段的右边界 end 必须包容当前段内所有字母的最后出现位置（end = Math.max(end, last[s[i]])）。当我们正好走到 i === end 时，说明段内所有字母在后面都绝不会再出现了，大功告成，咔嚓一刀切断（收集长度 end - start + 1），开启下一段！",
        "js_helpers": [
            {
                "name": "last[s[i]] = i 预存字符最后下标",
                "what_it_does": "单次遍历记录每个字符在整个字符串中最后一次出现的索引。",
                "junior_tip": "只需记录最后一次坐标，前序坐标自然被覆盖，逻辑极简！"
            },
            {
                "name": "end = Math.max(end, last[s[i]])",
                "what_it_does": "动态撑大当前片段的右边界。",
                "junior_tip": "橡皮筋机制：只要段内发现新字母，它的最后落脚点就可能将右边界向右拉得更长。"
            },
            {
                "name": "i === end 判定闭环切分",
                "what_it_does": "当指针抵达当前段的最远右边界时，触发切断收割。",
                "junior_tip": "此时段内所有字符在后续绝对不再出现，段长为 end - start + 1。"
            }
        ],
        "code_js": '''/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    // 第 1 步：预处理每个字符最后一次出现的下标位置
    const last = {};
    for (let i = 0; i < s.length; i++) {
        last[s[i]] = i;
    }

    const res = [];
    let start = 0; // 当前片段的起始索引
    let end = 0;   // 当前片段能够容纳所有字母的最远右边界

    // 第 2 步：遍历字符串，贪心确定切分点
    for (let i = 0; i < s.length; i++) {
        // 当前段必须延伸到包含当前字符最后一次出现的下标
        end = Math.max(end, last[s[i]]);

        // 第 3 步：当遍历指针到达了当前片段的最远右边界时，
        // 说明当前片段内的所有字符在后续都不会再出现，可以果断切断
        if (i === end) {
            res.push(end - start + 1); // 收集当前片段的长度
            start = i + 1;             // 开启下一个片段的起点
        }
    }

    return res;
};''',
        "checkpoints": [
            {"dimension": "step1", "title": "代码第 1 步：预处理每个字符最后出现的下标", "detail": "细扣：last[s[i]] = i 一次遍历确立各字符生死线与最后责任界限。", "weight": 20},
            {"dimension": "step2", "title": "代码第 2 步：start 与 end 双指针维护当前独立片段区间", "detail": "细扣：定义片段开合范围，初始双指针均指向 0。", "weight": 20},
            {"dimension": "step3", "title": "代码第 3 步：end = Math.max(end, last[s[i]]) 动态撑大右边界", "detail": "细扣：段内任意字符的滞后性推迟切断时间，橡皮筋向右延伸。", "weight": 20},
            {"dimension": "step4", "title": "代码第 4 步：i === end 命中切分点收割长度", "detail": "细扣：res.push(end - start + 1) 安全收尾，保证片段不漏任何字符。", "weight": 20},
            {"dimension": "step5", "title": "代码第 5 步：start = i + 1 切换下一段与 O(N) 线性时间证明", "detail": "细扣：无缝衔接下一片段，两趟遍历时间 O(N) 空间 O(Σ) 仅 26 个字母。", "weight": 20}
        ]
    }
}
