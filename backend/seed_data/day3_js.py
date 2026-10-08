"""Day 3 JavaScript Solutions with Junior-level explanations, JS helpers, code-aligned checkpoints, and complete problem descriptions."""
DAY_3_JS_DATA = {
    94: {
        "title_cn": '二叉树的中序遍历',
        "title_en": 'Binary Tree Inorder Traversal',
        "slug": 'binary-tree-inorder-traversal',
        "difficulty": 'Easy',
        "description": '''给定一个二叉树的根节点 root ，返回它的 中序 遍历结果。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

提示：
- 树中节点数目在范围 [0, 100] 内
- -100 <= Node.val <= 100
- 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
''',
        "plain_explanation": '''中序遍历的次序规定为：【左子树 -> 根节点 -> 右子树】。
虽然递归写法只有寥寥数行，但在高频大厂面试中，面试官往往要求手写非递归的显式辅助栈迭代版本，考察对计算机调用栈底层的理解。
保姆级大白话模拟：
想象你背着一个登山背包（JavaScript 数组 stack），站在树根面前：
1. 【一路向左扎到底】：只要当前节点指针 curr 还没撞南墙（curr !== null），你就把当前节点当作途经的驿站压入背包（stack.push(curr)），然后义无反顾地迈向它的左孩子（curr = curr.left）。这一步是在把所有左侧祖先按顺序保存起来。
2. 【触底回溯弹栈】：当左边走到尽头（curr === null）时，说明最左下角已经没有更小的左子树了。此时从背包顶部弹出一个最新存入的节点（curr = stack.pop()）。这正是当前局部子树的“根”！按照“左-根-右”的契约，现在是访问根节点的绝佳时机，把它的值收集进结果清单（res.push(curr.val)）。
3. 【右转开辟新天地】：访问完这个根节点后，它的左子树和自身都已处理完毕，下一步自然是一脚迈入它的右孩子（curr = curr.right）。如果右孩子存在，它会再次触发“一路向左扎到底”；如果右孩子是 null，下一轮循环会直接从背包里弹出更上层的祖先节点。
4. 【双哨兵守护循环】：循环条件设计为 while (curr !== null || stack.length > 0)。当前指针不为空表示还在探路下行，栈不为空表示还有回溯待办事项。当两者同时为空时，遍历完美落幕！
''',
        "js_helpers": [
            {
                "name": 'const stack = [] 与 stack.push() / stack.pop()',
                "what_it_does": '使用 JS 动态数组模拟计算机执行栈（LIFO，后进先出）。',
                "junior_tip": 'pop() 会移除并返回数组末尾元素，耗时 O(1)。模拟递归回溯的利器。'
            },
            {
                "name": 'while (curr !== null || stack.length > 0)',
                "what_it_does": '双退出哨兵循环控制条件。',
                "junior_tip": '【小白常错】绝对不能只写 stack.length > 0，因为在刚出发时栈是空的，必须依靠 curr !== null 启动第一次压栈。'
            },
            {
                "name": 'curr = curr.right 驱动分支转移',
                "what_it_does": '完成当前根节点访问后转向右子树。',
                "junior_tip": '若右子树为空，下一轮外层循环将直接跳过内层压栈 while，连续弹栈回溯到更高级别的父节点。'
            },
        ],
        "code_js": '''/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    const res = [];
    const stack = [];
    let curr = root;

    // 第 1 步：只要还有节点未处理，或栈中还有存货待回溯，就持续推进
    while (curr !== null || stack.length > 0) {
        // 第 2 步：一路向左扎到底，把沿途节点全部压入背包
        while (curr !== null) {
            stack.push(curr);
            curr = curr.left;
        }

        // 第 3 步：触底回溯，弹出栈顶节点（最深未访问的左节点或当前根节点）
        curr = stack.pop();
        res.push(curr.val); // 访问根节点数值

        // 第 4 步：转向右子树，开启右分支的中序遍历
        curr = curr.right;
    }

    return res;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：显式辅助栈 stack 初始化与双退出哨兵',
                "detail": '细扣：while (curr !== null || stack.length > 0) 保证探路与回溯阶段无缝衔接。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：内层 while 一路向左扎到底压栈',
                "detail": '细扣：stack.push(curr); curr = curr.left 保证所有左子孙先于根节点被暂存等待。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：弹栈并收获中间根节点值',
                "detail": '细扣：curr = stack.pop(); res.push(curr.val) 严格践行“左-根-右”访问规约。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：转向右分支 curr = curr.right',
                "detail": '细扣：右孩子继续走同样循环，为空则下一轮继续弹栈回溯上层祖先。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：复杂度评估与 Morris 进阶口述',
                "detail": '细扣：时间 O(N)，栈深平均 O(log N) 最坏 O(N)；口述线索二叉树 Morris 遍历 O(1) 空间解法。',
                "weight": 20
            },
        ]
    },
    104: {
        "title_cn": '二叉树的最大深度',
        "title_en": 'Maximum Depth of Binary Tree',
        "slug": 'maximum-depth-of-binary-tree',
        "difficulty": 'Easy',
        "description": '''给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2

提示：
- 树中节点的数量在 [0, 10^4] 区间内。
- -100 <= Node.val <= 100
''',
        "plain_explanation": '''求一棵树的最大深度，是理解“递归自底向上分治汇总”思想的最佳范例。
保姆级大白话比喻：
想象你是公司的董事长（root），你想知道整个公司从顶到底一共跨越了多少个管理层级。
作为最高层，你不需要亲自拿尺子去丈量每一个基层岗位。你只需要做一件事情——“向两位副总裁下达汇报指令”：
1. 问左副总裁：“你分管的左半边体系，最大深度是多少？”（maxDepth(root.left)）
2. 问右副总裁：“你分管的右半边体系，最大深度是多少？”（maxDepth(root.right)）
3. 两位副总裁再把同样的问题一级级向下安排。当问到底层空指针（root === null）时，意味着到了基层边界，没有员工了，直接向上汇报深度为 0（递归奠基石）。
4. 任何一位管理层收到左右两个方向汇报上来的深度数字后，挑出其中层级更深的那一个（Math.max(左深度, 右深度)），再加上自己这一级（+ 1），作为自己的总深度向上层汇报。
5. 最终自底向上汇总到董事长手中，最大深度便水落石出！整段逻辑只需优雅的 3 行代码。
''',
        "js_helpers": [
            {
                "name": 'if (root === null) return 0;',
                "what_it_does": '递归基石守卫条件。',
                "junior_tip": '遇空直接回溯返回深度 0，避免访问 null.left 引发 TypeError 运行时崩溃。'
            },
            {
                "name": 'Math.max(leftDepth, rightDepth) + 1',
                "what_it_does": '后序遍历自底向上聚合计算。',
                "junior_tip": '左右子树高度取较大者，再 +1 加上当前节点自身的 1 层高度。'
            },
            {
                "name": '递归调用栈 Call Stack 空间分析',
                "what_it_does": 'JS 引擎内部为每一层递归开辟执行上下文。',
                "junior_tip": '空间复杂度取决于树高 H。平衡树时 H = log N，极度倾斜退化为链表时 H = N。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    // 第 1 步：递归终点基底——空节点深度为 0
    if (root === null) return 0;

    // 第 2 步：自底向上分治，递归求左子树最大深度
    const leftDepth = maxDepth(root.left);
    // 第 3 步：递归求右子树最大深度
    const rightDepth = maxDepth(root.right);

    // 第 4 步：后序汇总，取左右较深者加上自身当前层（+1）返回上级
    return Math.max(leftDepth, rightDepth) + 1;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：递归基底 if (root === null) return 0',
                "detail": '细扣：空节点深度奠基石为 0，防止空指针异常。',
                "weight": 25
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：分治下探左子树最大深度',
                "detail": '细扣：const leftDepth = maxDepth(root.left) 深入左子树。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：分治下探右子树最大深度',
                "detail": '细扣：const rightDepth = maxDepth(root.right) 深入右子树。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：后序聚合 Math.max(L, R) + 1 向上返回',
                "detail": '细扣：自底向上汇总，时间严格 O(N)，栈空间平衡树 O(log N) 最坏 O(N)。',
                "weight": 25
            },
        ]
    },
    226: {
        "title_cn": '翻转二叉树',
        "title_en": 'Invert Binary Tree',
        "slug": 'invert-binary-tree',
        "difficulty": 'Easy',
        "description": '''给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

示例 2：
输入：root = [2,1,3]
输出：[2,3,1]

示例 3：
输入：root = []
输出：[]

提示：
- 树中节点数目范围在 [0, 100] 内
- -100 <= Node.val <= 100
''',
        "plain_explanation": '''著名的 Homebrew 作者 Max Howell 曾在推特调侃：“Google 面试官因为我没能在白板上手写翻转二叉树而挂了我。”
其实这道题的思想极其纯粹直观——“照镜子（左右镜像互搏）”。
保姆级大白话：
1. 站在每一个二叉树节点面前，你只需要做一件极其粗暴的事：把它的左臂和右臂对调一下（左孩子和右孩子交换指针引用）。
2. 调换之后，原本的左孩子现在来到了右边，原本的右孩子来到了左边。
3. 接着，你给左孩子下达指令：“去把你自己的整棵子树翻转一下”；给右孩子下达指令：“去把你自己的整棵子树翻转一下”。
4. 走到空节点（root === null）时，什么都不用做，直接原路返回 null。
5. 为什么说前序遍历和后序遍历都可以？
   - 前序遍历：先交换当前节点的左右子节点，再分别递归进入左、右子树。
   - 后序遍历：先分别翻转好左、右子树，再把翻转后的左右子节点交换挂在当前节点上。
   - 【反面教材】：千万不要在中序遍历中直接照搬！如果在中序遍历中先翻转了左树，再交换左右，此时原左树被调到了右边，接着递归进入右树时，实际上是在对刚才已经翻转好的左树进行二次翻转，而原本的右树一次都没被翻转！
''',
        "js_helpers": [
            {
                "name": '[root.left, root.right] = [root.right, root.left]',
                "what_it_does": 'ES6 解构赋值语法，原子地单行交换两个变量引用。',
                "junior_tip": '无需引入冗余的中间临时变量 temp，代码极具现代 JS 风格与可读性。'
            },
            {
                "name": 'if (root === null) return null;',
                "what_it_does": '空节点守卫与递归终止。',
                "junior_tip": '叶子节点的左右子节点交换后均为 null，递归天然收敛闭环。'
            },
            {
                "name": '广度优先遍历 BFS 迭代方案对比',
                "what_it_does": '使用普通队列 queue = [root] 逐层弹出节点并交换左右子树。',
                "junior_tip": '面试官若要求非递归解法，层序队列出队解构交换左右指针即可，时间 O(N) 空间 O(N)。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    // 第 1 步：递归基底——空节点直接返回 null
    if (root === null) return null;

    // 第 2 步：ES6 解构赋值，原子交换当前节点的左右子节点引用
    [root.left, root.right] = [root.right, root.left];

    // 第 3 步：递归对新的左子树执行翻转
    invertTree(root.left);
    // 第 4 步：递归对新的右子树执行翻转
    invertTree(root.right);

    // 第 5 步：返回翻转完成后的树根节点
    return root;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：判空安全拦截 if (root === null) return null',
                "detail": '细扣：空指针边界安全防护，叶子节点左右空指针交换自闭环。',
                "weight": 25
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：ES6 解构单行互换左右子节点引用',
                "detail": '细扣：[root.left, root.right] = [root.right, root.left] 优雅原子交换。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：递归进入左子树与右子树展开翻转',
                "detail": '细扣：前序或后序遍历自顶向下镜像，严防中序遍历的逻辑陷阱。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：返回根节点 root 与时空复杂度分析',
                "detail": '细扣：每个节点访问一次，时间严格 O(N)，调用栈空间 O(H)。',
                "weight": 25
            },
        ]
    },
    101: {
        "title_cn": '对称二叉树',
        "title_en": 'Symmetric Tree',
        "slug": 'symmetric-tree',
        "difficulty": 'Easy',
        "description": '''给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

提示：
- 树中节点数目在范围 [1, 1000] 内
- -100 <= Node.val <= 100
- 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
''',
        "plain_explanation": '''判断一棵树是否轴对称，关键在于理解“镜像对齐”的概念。
一棵树自己无法直接跟自己比对对称性，必须把它拆分成两个并行的实体——左半树 p 和右半树 q。
保姆级大白话：
想象两个人站在镜子两边面对面做动作，要保持完全镜像对称，必须严格遵守以下三条铁律：
1. 【自身模样完全一致】：两个对应位置的节点值必须严格相等（p.val === q.val）。如果一个长得像张三一个长得像李四，直接判不对称！
2. 【外侧动作同步照镜】：p 的左臂（最外侧）必须与 q 的右臂（最外侧）完全一致（check(p.left, q.right)）。
3. 【内侧动作同步照镜】：p 的右臂（内侧）必须与 q 的左臂（内侧）完全一致（check(p.right, q.left)）。
4. 【空节点守卫法则】：
   - 如果两个人面前都是空的（!p && !q），说明两边都到头了，完全对称，返回 true；
   - 如果只有一个人面前是空的，另一个人面前有东西（!p || !q），说明一边多出一根树枝，形态不对称，返回 false。
从树根开始，同时派遣指针走向 root.left 和 root.right，交叉递归比对，答案便迎刃而解！
''',
        "js_helpers": [
            {
                "name": 'const check = (p, q) => { ... } 双节点递归辅助函数',
                "what_it_does": '将单树轴对称问题升维成双树镜像比对问题。',
                "junior_tip": '树的对称性无法在单节点下探中解决，构造双参数辅助函数是标准解法模式。'
            },
            {
                "name": 'if (!p && !q) return true; if (!p || !q) return false;',
                "what_it_does": '双空与单空的互斥卫语句检查。',
                "junior_tip": '先排查双空（合法结束），再排查单空（形态不对称），顺序不能颠倒。'
            },
            {
                "name": 'check(p.left, q.right) && check(p.right, q.left)',
                "what_it_does": '外侧与内侧交叉镜像比对。',
                "junior_tip": '充分利用 JS 的逻辑与（&&）短路特性，一旦外侧不匹配立即早停，提高效率。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    if (!root) return true;

    // 辅助函数：深度比对两棵子树 p 和 q 是否互为镜像
    const check = (p, q) => {
        // 1. 两者皆为空节点，天然对称
        if (!p && !q) return true;
        // 2. 仅有一方为空，结构不对称
        if (!p || !q) return false;
        // 3. 双方数值不相等，内容不对称
        if (p.val !== q.val) return false;

        // 4. 外侧与内侧交叉递归比对：p.left 对应 q.right，p.right 对应 q.left
        return check(p.left, q.right) && check(p.right, q.left);
    };

    // 从根节点的左孩子与右孩子开始比对
    return check(root.left, root.right);
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：根节点防御与构建 check(p, q) 双节点比对体系',
                "detail": '细扣：将单树对称拆解为左右两棵子树的同步下降检验。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：空节点双向互斥判定',
                "detail": '细扣：双空为 true，单空为 false，拦截树结构非对称形态。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：当前节点数值相等比对 p.val !== q.val',
                "detail": '细扣：数值不等立即短路失败退出。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：外侧与内侧交叉镜像递归比对',
                "detail": '细扣：check(p.left, q.right) && check(p.right, q.left) 外外相对、内内相对。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：迭代法（双端入队队列）思路与复杂度',
                "detail": '细扣：可用队列成对存入节点迭代比对，时间严格 O(N)，空间 O(H)。',
                "weight": 20
            },
        ]
    },
    543: {
        "title_cn": '二叉树的直径',
        "title_en": 'Diameter of Binary Tree',
        "slug": 'diameter-of-binary-tree',
        "difficulty": 'Easy',
        "description": '''给你一棵二叉树的根节点 root ，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能穿过也可能不穿过根节点。
两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1

提示：
- 树中节点数目在范围 [1, 10^4] 内
- -100 <= Node.val <= 100
''',
        "plain_explanation": '''二叉树的直径是指树中任意两个节点之间的最长路径（包含的边数）。
初学者极其容易踩入一个巨大思维陷阱：“最长路径不就是从根节点出发，左子树最大深度 + 右子树最大深度 吗？”
错！最长的路径完全有可能“偏居一隅”，在左子树内部极深的地方横向拐了一个大弯，根本不经过树根！
破题关键：“拱门最高点（拐弯处）的一箭双雕思想”。
大白话模型：
1. 观察任何一条穿过节点 node 的局部最长路径：它一定是从 node 的左子树最深叶子爬上来，经过 node 本身，再一路滑到 node 的右子树最深叶子。
2. 因此，以 node 为最高拱顶的连通路径边数，恰好等于：【左子树深度 + 右子树深度】！
3. 我们在用后序遍历计算深度的过程中，可以顺带做两件事：
   - 【暗度陈仓（更新全局纪录）】：算出了左深度 left 和右深度 right 之后，立刻计算穿过当前节点的拱门边数 left + right，并用它刷新全局最大纪录 maxDiameter = Math.max(maxDiameter, left + right)；
   - 【明修栈道（向上汇报单边）】：当前节点在向父节点汇报自己的深度时，只能汇报自己的单侧延伸最大深度（Math.max(left, right) + 1），因为父节点如果要把你串进更上层的路径里，绝对不能让你在脚底下分叉！
4. 整棵树只需跑一次优雅的后序遍历，所有可能作为拐弯最高点的节点都被考量了一遍，全局最大直径自然浮出水面。
''',
        "js_helpers": [
            {
                "name": 'let maxDiameter = 0 全局闭包变量',
                "what_it_does": '在外层作用域声明标尺，捕获遍历过程中出现过的历史最大拐弯跨度。',
                "junior_tip": '解决脱离根节点、隐藏在子树极深处的局部最优拐弯问题。'
            },
            {
                "name": '边数 vs 节点数换算',
                "what_it_does": '路径长度定义为两节点间的边数。',
                "junior_tip": '左深度代表左臂节点数，右深度代表右臂节点数，穿过当前节点的边数刚好就是 left + right，无需 + 1。'
            },
            {
                "name": 'return Math.max(left, right) + 1 向上单边延伸',
                "what_it_does": '向父节点汇报单侧最大延伸深度。',
                "junior_tip": '【高频经典套路】返回值用于向上递归拼装，全局变量用于捕获最优子结构拐弯！'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    let maxDiameter = 0;

    // 辅助函数：自底向上后序遍历计算 node 的单侧最大深度
    const getDepth = (node) => {
        // 空节点深度为 0
        if (!node) return 0;

        // 递归获取左右子树深度
        const left = getDepth(node.left);
        const right = getDepth(node.right);

        // 核心：以当前 node 为最高拐点的拱门边数 = 左深度 + 右深度
        // 顺带刷新全局最大直径纪录
        maxDiameter = Math.max(maxDiameter, left + right);

        // 向上级父节点汇报自己的单侧最大深度（必须取较深的一条 + 自身 1 层）
        return Math.max(left, right) + 1;
    };

    getDepth(root);
    return maxDiameter;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：定义闭包变量 let maxDiameter = 0',
                "detail": '细扣：捕获不经过根节点、深藏于某棵子树内部的全局极大值。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：后序遍历自底向上汇报深度基底',
                "detail": '细扣：递归终止返回 0，确保叶子节点计算自底向上成立。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：以当前节点为拐点刷新 maxDiameter',
                "detail": '细扣：maxDiameter = Math.max(maxDiameter, left + right) 精确计算边数。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：向上级返回单边深度 Math.max(L, R) + 1',
                "detail": '细扣：不可分叉，向上只能送出单边最大深度供父级拼装。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：一次遍历 O(N) 时间与 O(H) 空间分析',
                "detail": '细扣：杜绝每个节点重复算深度的 O(N^2) 暴力解，整树一次后序搞定。',
                "weight": 20
            },
        ]
    },
    102: {
        "title_cn": '二叉树的层序遍历',
        "title_en": 'Binary Tree Level Order Traversal',
        "slug": 'binary-tree-level-order-traversal',
        "difficulty": 'Medium',
        "description": '''给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
- 树中节点数目在范围 [0, 2000] 内
- -1000 <= Node.val <= 1000
''',
        "plain_explanation": '''层序遍历要求我们从上到下、一层一层、从左到右打印出二叉树的所有节点。
这是广度优先搜索（BFS）最经典的教科书级范式！
保姆级大白话比喻：
想象学校军训排队检阅，要求每一排（层）的学生必须整整齐齐打印在同一个小名单里：
1. 【队伍集结】：准备一个排队等待检阅的队伍（队列 const queue = [root]）。先让总指挥（根节点）一个人站在队伍第一排。
2. 【拍照锁定当前排人数（核心大招）】：
   - 每一轮循环开始时，队列里站着的【所有人】，刚好就是当前这一排的全体成员！
   - 你必须立刻掏出相机给队伍拍一张快照：记录当前队伍的人数 const levelSize = queue.length！
   - 【小白最容易犯的致命错误】：千万不能直接写 for (let i = 0; i < queue.length; i++)！因为在循环内部，当前排的学生会不断把他们的下一代孩子 push 进队伍尾部，导致 queue.length 动态变长，把下一排的人和当前排的人混在了一起！必须用 const levelSize 提前锁死！
3. 【定量出队收缴数值】：
   - 循环固定执行 levelSize 次：
   - 每次把队伍最前面的一个人请出来（node = queue.shift()），把他的分数放进当前排的专属名单 level 里；
   - 同时，如果他有左孩子，让左孩子排到队伍末尾；如果他有右孩子，让右孩子排到队伍末尾。
4. 【交卷入库】：循环刚好跑完 levelSize 次时，当前这一排的人正好全部检阅完毕，下一排的人也整齐地在队尾候场。把本排名单存入总大榜 res.push(level)！
5. 重复上述操作，直至队列中空无一人，一张层级分明的二维成绩单便完美生成！
''',
        "js_helpers": [
            {
                "name": 'const levelSize = queue.length 定长快照',
                "what_it_does": '进入内层循环前先固定当前层的节点总数。',
                "junior_tip": '【核心避坑】循环内会持续向队尾 push 新孩子，必须预先拍照固定循环次数，杜绝层级混淆！'
            },
            {
                "name": 'queue.shift() 与 queue.push()',
                "what_it_does": '模拟先进先出（FIFO）队列。',
                "junior_tip": 'shift() 从队头弹出，push() 从队尾注入，严格保持从左到右的水平扫描次序。'
            },
            {
                "name": 'if (!root) return [] 边界判空',
                "what_it_does": '防御空树入参。',
                "junior_tip": '避免将 null 推入队列造成无谓的分支判断与额外开销。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    // 边界特判：空树直接返回空结果数组
    if (!root) return [];

    const res = [];
    // 初始化 BFS 队列，根节点入队
    const queue = [root];

    // 只要队伍里还有待处理的层级节点
    while (queue.length > 0) {
        const level = [];
        // 关键步骤：拍摄快照，固定当前层的总节点数量
        const levelSize = queue.length;

        // 严格循环 levelSize 次，保证只处理当前层的节点
        for (let i = 0; i < levelSize; i++) {
            // 从队头取出当前节点
            const node = queue.shift();
            level.push(node.val);

            // 将下一层的左右孩子节点依次推入队尾候场
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        // 当前层处理完毕，收录进二维总结果
        res.push(level);
    }

    return res;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：根节点防御判空与 BFS 队列初始化',
                "detail": '细扣：if (!root) return [] 与 const queue = [root] 安全启航。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：拍摄定长快照 const levelSize = queue.length',
                "detail": '细扣：剥离层级分水岭，防止新入队孩子干扰当前层计数。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：定长循环出队与本层数值收集',
                "detail": '细扣：for 循环 levelSize 次，node = queue.shift(); level.push(node.val)。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：左右子节点依次入队',
                "detail": '细扣：if (node.left/right) queue.push(...) 波浪式向下一层延展。',
                "weight": 15
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：二维层序归档与时空复杂度分析',
                "detail": '细扣：res.push(level)，时间严格 O(N)，队列空间最多 O(N/2) 即 O(N)。',
                "weight": 15
            },
        ]
    },
    108: {
        "title_cn": '将有序数组转换为二叉搜索树',
        "title_en": 'Convert Sorted Array to Binary Search Tree',
        "slug": 'convert-sorted-array-to-binary-search-tree',
        "difficulty": 'Easy',
        "description": '''给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足“每个节点的左右两个子树的高度差的绝对值不超过 1 ”的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案。

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 按 严格递增 顺序排列
''',
        "plain_explanation": '''题目要求把一个已经升序排好序的数组，转换成一棵“高度平衡的二叉搜索树（BST）”。
二叉搜索树的灵魂法则是：根节点的左边所有数都比它小，右边所有数都比它大。
如何保证左右子树高度差不超过 1？
保姆级大白话：
1. 【每次抓正中间的数当老大（二分分治）】：
   - 既然数组已经从小到大排好了，要想让树的两边重量完全均等，最完美的候选人是谁？必然是正中间的那个元素（mid）！
   - 我们把它挑出来作为当前子树的树根 root = new TreeNode(nums[mid])。
2. 【左右天然对称割裂】：
   - 挑出正中间之后，它左边的所有元素天然全部小于它，且数量正好占一半，刚好拿去递归组建左子树；
   - 它右边的所有元素天然全部大于它，且数量也正好占一半，刚好拿去递归组建右子树！
   - 左右两边的节点总数相差最多只有 1 个，整棵树天然就是绝对极致的高度平衡！
3. 【双指针索引 vs 数组切片】：
   - 递归时切记：千万不要写 nums.slice(0, mid)！频繁切片拷贝数组会在内存中产生巨大的垃圾回收压力，把空间复杂度拖垮到 O(N)。
   - 最优做法是：原数组不动，只传左右边界指针 build(left, right)！当 left > right 时说明区间空了，直接返回 null。
''',
        "js_helpers": [
            {
                "name": 'Math.floor((left + right) / 2)',
                "what_it_does": '计算区间中点索引并向下取整。',
                "junior_tip": '避免浮点数下标。在大数场景下也可写为 left + Math.floor((right - left) / 2) 防溢出。'
            },
            {
                "name": 'new TreeNode(nums[mid])',
                "what_it_does": '实例化当前平衡子树的根节点。',
                "junior_tip": '以中点数值构筑轴心，两翼节点数最多相差 1，天然保障高度平衡。'
            },
            {
                "name": '索引界限传参 vs nums.slice()',
                "what_it_does": '传左右索引界限 [left, right] 控制子数组范围。',
                "junior_tip": '切忌频繁调用 slice()，传索引零内存拷贝，递归栈空间只要优雅的 O(log N)。'
            },
        ],
        "code_js": '''/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    // 辅助函数：根据 [left, right] 闭区间递归构造高度平衡二叉搜索树
    const build = (left, right) => {
        // 递归基底：区间非法说明已经没有节点，返回 null
        if (left > right) return null;

        // 选择中点作为当前子树的根节点，保证左右节点数量大致均等
        const mid = Math.floor((left + right) / 2);
        const root = new TreeNode(nums[mid]);

        // 递归构建左半区间为左子树
        root.left = build(left, mid - 1);
        // 递归构建右半区间为右子树
        root.right = build(mid + 1, right);

        return root;
    };

    // 从全局完整数组区间 [0, nums.length - 1] 启动构建
    return build(0, nums.length - 1);
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：区间分治辅助函数 build(left, right) 架构',
                "detail": '细扣：传递双指针区间避免 slice 数组复制开销。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：递归基底 left > right 返回 null',
                "detail": '细扣：处理空子树与叶子节点左右指针收敛。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：二分中点取整作为平衡根节点',
                "detail": '细扣：Math.floor((left + right) / 2) 选出中位数保证两翼节点数均衡。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：递归左右两半划分区间构建子树',
                "detail": '细扣：root.left = build(left, mid-1); root.right = build(mid+1, right)。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：树高严格证明与时空复杂度',
                "detail": '细扣：树高恒为 O(log N)，时间严格 O(N)，调用栈空间严格 O(log N)。',
                "weight": 20
            },
        ]
    },
    98: {
        "title_cn": '验证二叉搜索树',
        "title_en": 'Validate Binary Search Tree',
        "slug": 'validate-binary-search-tree',
        "difficulty": 'Medium',
        "description": '''给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
- 节点的左子树只包含 小于 当前节点的数。
- 节点的右子树只包含 大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的节点值是 4 。

提示：
- 树中节点数目范围在 [1, 10^4] 内
- -2^31 <= Node.val <= 2^31 - 1
''',
        "plain_explanation": '''这道题是整个二叉树章节中最容易写出看似正确但隐藏严重 Bug 的经典题！
【小白最常犯的致命错误】：
只检查当前节点是不是比左孩子大、比右孩子小（比如只写 root.left.val < root.val && root.right.val > root.val）。
为什么错？举个反例：
根节点是 5，它的右孩子是 6，6 的左孩子是 4。
局部看 6 的左孩子 4 < 6 毫无问题，但在整棵树的大局看，4 出现在了 5 的右子树里，违反了“右子树的所有后代必须全大于 5”的核心法则！
保姆级大白话解法：“祖先下传的紧箍咒区间约束 (min, max)”。
1. 每个节点从诞生起，身上就被套上了一个合法取值范围 (min, max)。
2. 最顶层的树根无拘无束，取值范围是 (-Infinity, +Infinity)。
3. 当节点带着紧箍咒往左下探时：左孩子必须比自己小，所以上界 max 被瞬间收紧为当前节点的值（max = node.val），而下界 min 保持不变；
4. 当节点带着紧箍咒往右下探时：右孩子必须比自己大，所以下界 min 被瞬间收紧为当前节点的值（min = node.val），而上界 max 保持不变；
5. 沿途每一个节点只要发现自己的值越界了（node.val <= min || node.val >= max），立即判非法返回 false！
6. 这样，最深处的子孙节点依然时刻受制于顶层所有祖先施加的边界，全局秩序井然！
''',
        "js_helpers": [
            {
                "name": '-Infinity 与 Infinity',
                "what_it_does": 'JS 内置的负无穷大与正无穷大常量。',
                "junior_tip": '作为初始上下界限，完美覆盖题目给出的 [-2^31, 2^31 - 1] 数值范围。'
            },
            {
                "name": 'node.val <= min || node.val >= max 严格开区间校验',
                "what_it_does": 'BST 规则判定卫语句。',
                "junior_tip": 'BST 严格不允许出现重复相等值，带有等号的越界必须直接判定为 false。'
            },
            {
                "name": '中序遍历单调性对比思路',
                "what_it_does": 'BST 中序遍历所得序列必须严格单调递增。',
                "junior_tip": '若用中序遍历解法，需维护上一个访问的前驱节点值 prev，当前值 <= prev 即判非法。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    // 辅助函数：校验 node 是否严格落在开区间 (min, max) 内
    const validate = (node, min, max) => {
        // 空节点天然满足二叉搜索树定义
        if (!node) return true;

        // 若当前节点值突破了祖先约束的上下界，直接判为非法
        if (node.val <= min || node.val >= max) {
            return false;
        }

        // 深入左子树：上界收缩为当前节点值 node.val，下界不变
        // 深入右子树：下界收缩为当前节点值 node.val，上界不变
        // 左右两边必须同时合法
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    };

    // 根节点初始范围为全集 (-Infinity, Infinity)
    return validate(root, -Infinity, Infinity);
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：递归检验函数 validate(node, min, max) 架构',
                "detail": '细扣：祖先自顶向下传递有效开区间，打破局部双节点比较的局限。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：严格开区间校验 node.val <= min || >= max',
                "detail": '细扣：BST 不允许重复节点，带等号拦截越界数值。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：走向左子树收紧上界 validate(node.left, min, node.val)',
                "detail": '细扣：左树所有节点必须严格小于当前节点数值。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：走向右子树收紧下界 validate(node.right, node.val, max)',
                "detail": '细扣：右树所有节点必须严格大于当前节点数值。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：正负无穷初始化与时空复杂度',
                "detail": '细扣：入口 validate(root, -Infinity, Infinity)，时间 O(N) 空间 O(H)。',
                "weight": 10
            },
        ]
    },
    230: {
        "title_cn": '二叉搜索树中第 K 小的元素',
        "title_en": 'Kth Smallest Element in a BST',
        "slug": 'kth-smallest-element-in-a-bst',
        "difficulty": 'Medium',
        "description": '''给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

提示：
- 树中的节点数为 n 。
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4
- 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁查找第 k 小的值，你将如何优化算法？
''',
        "plain_explanation": '''二叉搜索树（BST）拥有一个神级数学性质：
【对 BST 进行中序遍历（左 -> 根 -> 右），输出的节点数值序列是一个严格递增的有序数组！】
这意味着：“找第 k 小的元素”，本质上就是“找中序遍历访问到的第 k 个节点”！
新手最粗暴的做法：用递归把整棵树完整遍历一遍，存进数组 res，然后取 res[k - 1]。
但在真实技术面试中，这种做法会被大大扣分！因为树可能有成千上万个节点，如果 k = 1，你根本不需要遍历整棵树，这完全是内存和时间的浪费！
保姆级大白话最优解：“显式栈中序遍历 + 倒计时早停（Early Stopping）”。
1. 准备一个辅助栈 stack，用迭代法做中序遍历。
2. 指针 curr 一路向左扎到底，把沿途节点全压进栈中。此时栈顶就是整棵树全局最小的节点！
3. 弹出栈顶节点访问：此时我们见证了一个按从小到大排好的数字，倒计时器 k 减 1（k--）。
4. 【命中即刻刹车】：一旦 k 减到了 0（if (k === 0)），恭喜你！当前弹出的节点正是第 k 小的真命天子，立刻 return curr.val！后面剩下的成千上万个节点连碰都不用碰！
5. 如果 k 还没到 0，指针移向右子树（curr = curr.right），继续下一轮迭代。
''',
        "js_helpers": [
            {
                "name": '显式栈辅助迭代 const stack = []',
                "what_it_does": '使用数组模拟执行栈进行非递归中序遍历。',
                "junior_tip": '相比递归写法，显式栈支持在中途随时 return 早停中断，极大提升执行效率。'
            },
            {
                "name": 'k-- 倒计时计数器',
                "what_it_does": '每次弹出栈顶元素（访问一个有效节点）时将 k 减 1。',
                "junior_tip": '无需维护额外的 index 变量，直接递减入参 k，k === 0 时即为目标。'
            },
            {
                "name": '进阶频繁查询优化考点',
                "what_it_does": '在每个节点维护其子树节点总数 count。',
                "junior_tip": '若频繁增删并查第 k 小，类似 AVL 或红黑树维护 size，可在 O(log N) 时间内类似二分查找快速命中。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const stack = [];
    let curr = root;

    // 只要还有节点未探索或栈中还有存货
    while (curr !== null || stack.length > 0) {
        // 第 1 步：一路向左扎到底，定位当前最小节点
        while (curr !== null) {
            stack.push(curr);
            curr = curr.left;
        }

        // 第 2 步：弹出当前最小节点（符合中序遍历升序次序）
        curr = stack.pop();

        // 第 3 步：倒计时扣减
        k--;
        // 命中第 k 小的元素，立即早停返回，无需遍历整树
        if (k === 0) {
            return curr.val;
        }

        // 第 4 步：转向右分支继续探索
        curr = curr.right;
    }

    return -1;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：显式辅助栈中序遍历架构搭建',
                "detail": '细扣：双条件 while 控制迭代流，模拟系统调用栈。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：一路向左深入定位当前最小值',
                "detail": '细扣：while (curr !== null) 深入左下角叶子节点。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：弹栈升序访问与倒计时 k--',
                "detail": '细扣：curr = stack.pop(); k--; 严格保持升序计数。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：if (k === 0) 提前刹车早退',
                "detail": '细扣：命中即刻 return curr.val，将时间截断在 O(H + k)。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：右分支步进与频繁查询优化思路',
                "detail": '细扣：未达标继续 curr = curr.right；口述节点 size 优化设计。',
                "weight": 10
            },
        ]
    },
    199: {
        "title_cn": '二叉树的右视图',
        "title_en": 'Binary Tree Right Side View',
        "slug": 'binary-tree-right-side-view',
        "difficulty": 'Medium',
        "description": '''给定一个二叉树的根节点 root ，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]

示例 2：
输入：root = [1,null,3]
输出：[1,3]

示例 3：
输入：root = []
输出：[]

提示：
- 二叉树的节点大小在 [0, 100] 范围内。
- -100 <= Node.val <= 100
''',
        "plain_explanation": '''站在树的右侧看这棵树，能看到的节点到底是什么？
保姆级大白话：
答案其实就是：**每一层露在最右侧的那个守门员节点**！
【新手大坑】：
千万不要写成“一路往右走 root.right”！因为如果右子树很矮（比如只有 2 层），而左子树很深（有 5 层），在第 3、4、5 层时，右边是空荡荡的，左子树伸出来的节点由于没有任何遮挡，站在右侧依然清晰可见！
因此，这道题的本质依然是：**BFS 层序遍历**！
1. 用第 102 题的层序遍历模板，用队列按波浪式一层一层扫描。
2. 每一层开始前，拍快照锁定当前层总人数 const levelSize = queue.length。
3. 循环出队这批人（for let i = 0; i < levelSize; i++）：
   - 当数到这一层的最后一个成员时（i === levelSize - 1），它就是当前层最右侧露脸的唯一幸运儿！直接把它的值收集进结果 res.push(node.val)！
   - 本层前面的成员（i < levelSize - 1）全被它挡住了，直接忽略其数值；
   - 但是！所有人带来的左右孩子，依然一视同仁全部推入队尾候场，参与下一层的竞争！
4. 队列扫完，自上而下的右视图就整整齐齐地出炉了。
''',
        "js_helpers": [
            {
                "name": 'i === levelSize - 1 末尾守门员判定',
                "what_it_does": '精准锁定当前层最后出队的节点。',
                "junior_tip": '一层只录入这一个代表，其他前面的节点全部被其在水平视线上遮挡。'
            },
            {
                "name": 'const levelSize = queue.length',
                "what_it_does": '固定当前层的节点总容量。',
                "junior_tip": '标准 BFS 层序分水岭，保证每一层独立封闭处理。'
            },
            {
                "name": 'DFS 根-右-左优先遍历替代方案',
                "what_it_does": '采用先右后左的深度优先遍历。',
                "junior_tip": '若 res.length === depth 则说明该深度首次被访问（即最右节点），推入 res[depth] 亦可。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    if (!root) return [];

    const res = [];
    const queue = [root];

    // BFS 逐层推进
    while (queue.length > 0) {
        // 关键：快照锁定当前层的节点总数
        const levelSize = queue.length;

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();

            // 若当前节点是本层的最后一个节点，它就是右视图所见节点
            if (i === levelSize - 1) {
                res.push(node.val);
            }

            // 左右孩子节点按常规入队，参与下一层角逐
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }

    return res;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：判空防御与 BFS 队列初始化',
                "detail": '细扣：if (!root) return [] 排除空树，queue = [root] 启程。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：快照锁定层大小 const levelSize = queue.length',
                "detail": '细扣：定长出队，建立每一层严密的视线屏障。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：i === levelSize - 1 捕获末尾可视节点',
                "detail": '细扣：每层最后一个节点天然遮蔽该层左侧所有节点。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：左右子节点依次入队',
                "detail": '细扣：左深右浅场景自然被下层右视图捕获，鲁棒性极强。',
                "weight": 15
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：BFS 与 DFS 对比及复杂度评估',
                "detail": '细扣：时间严格 O(N)，队列空间最多 O(N/2) 即 O(N)。',
                "weight": 15
            },
        ]
    },
    114: {
        "title_cn": '二叉树展开为链表',
        "title_en": 'Flatten Binary Tree to Linked List',
        "slug": 'flatten-binary-tree-to-linked-list',
        "difficulty": 'Medium',
        "description": '''给你二叉树的根节点 root ，请你将它展开为一个单链表：
- 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个节点，而左子指针始终为 null 。
- 展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]

提示：
- 树中节点数在范围 [0, 2000] 内
- -100 <= Node.val <= 100
- 进阶：你可以使用 O(1) 额外空间展开这棵树吗？
''',
        "plain_explanation": '''展开成单链表，并且顺序必须严格符合先序遍历（根 -> 左 -> 右），同时进阶要求 O(1) 额外空间！
如果用递归或者用数组暂存，空间都是 O(N)。如何在 O(1) 空间下纯原地展开？
保姆级大白话：“移花接木嫁接法（Morris 遍历思想）”。
1. 思考先序遍历的根本次序：根 -> 左子树全体 -> 右子树全体。
2. 这意味着：当整棵左子树全部遍历完之后，紧接着遍历的第一个节点是谁？正是【原本的右子树】！
3. 那么整棵左子树在先序遍历里最后一个被访问的节点是谁？正是【左子树里最右下角的那片叶子节点（前驱节点 pre）】！
4. 于是，对于当前节点 curr：
   - 如果它有左孩子：我们先顺着它的左孩子一路向右走到底，找到左子树的最右节点 pre；
   - 然后实施【嫁接】：把 curr 原本的整棵右子树剪切下来，嫁接到 pre 的右边（pre.right = curr.right）！
   - 然后把左子树整体搬移到右边（curr.right = curr.left），并将左指针彻底剪断（curr.left = null）！
   - 此时，curr 的左边已经空了，右边是一条平整的先序链条；
5. curr 沿着右指针走一步（curr = curr.right），去处理下一个节点，重复上述动作。
6. 不开辟任何栈、不写任何递归，整棵树像拉链一样原地拉成了一条平滑的单链表！空间绝对 O(1)！
''',
        "js_helpers": [
            {
                "name": 'let pre = curr.left; while (pre.right !== null) pre = pre.right;',
                "what_it_does": '寻找左子树在先序遍历中的前驱归宿点（最右下叶子）。',
                "junior_tip": '先序遍历中，右子树将紧跟在前驱叶子节点之后被访问。'
            },
            {
                "name": '三步指针重组移花接木',
                "what_it_does": 'pre.right = curr.right; curr.right = curr.left; curr.left = null;',
                "junior_tip": '右树缝接至前驱右侧，左树平移至右侧，原左指针切断置 null。'
            },
            {
                "name": 'curr = curr.right 单向推进',
                "what_it_does": '沿着重构好的单链表顺延处理下一个节点。',
                "junior_tip": '纯原地指针修改，完全不需要显式栈或系统递归栈，空间复杂度压至极致的 O(1)。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {void} 原地修改，不要返回任何值
 */
var flatten = function(root) {
    let curr = root;

    // 沿单链表方向向下一步步处理
    while (curr !== null) {
        // 如果当前节点存在左子树，需要进行移花接木
        if (curr.left !== null) {
            // 第 1 步：找到左子树的最右叶子节点（前驱节点）
            let pre = curr.left;
            while (pre.right !== null) {
                pre = pre.right;
            }

            // 第 2 步：将原本的右子树嫁接到前驱节点的右边
            pre.right = curr.right;

            // 第 3 步：把左子树整体转移到右边，左侧指针断开置空
            curr.right = curr.left;
            curr.left = null;
        }

        // 第 4 步：向下一个右节点推进
        curr = curr.right;
    }
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：外层迭代推进 while (curr !== null)',
                "detail": '细扣：单指针沿展开链条向下巡查处理。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：内层循环定位左子树最右节点 pre',
                "detail": '细扣：while (pre.right !== null) pre = pre.right 锁定先序前驱。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：缝合嫁接右子树 pre.right = curr.right',
                "detail": '细扣：将原右子树无损缝合到左子树末尾。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：左树右移 curr.right = curr.left 与 curr.left = null',
                "detail": '细扣：将重组后的分支接在右边，左指针清空符合单链表定义。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：步进 curr = curr.right 与 O(1) 空间证明',
                "detail": '细扣：每条边最多被访问两次，时间 O(N)，额外空间绝对 O(1)。',
                "weight": 10
            },
        ]
    },
    105: {
        "title_cn": '从前序与中序遍历序列构造二叉树',
        "title_en": 'Construct Binary Tree from Preorder and Inorder Traversal',
        "slug": 'construct-binary-tree-from-preorder-and-inorder-traversal',
        "difficulty": 'Medium',
        "description": '''给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]

提示:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder 和 inorder 均 无重复 元素
- inorder 均出现在 preorder
- preorder 保证 为二叉树的前序遍历序列
- inorder 保证 为二叉树的中序遍历序列
''',
        "plain_explanation": '''如何仅凭两组一维数组复原出整棵立体的二叉树？
保姆级大白话三步走：
1. 【前序遍历的特权：第一位永远是当前的树根】：
   - 前序遍历是“根 -> 左 -> 右”，所以对于任意一段区间，它的第一个元素 preorder[pStart] 毋庸置疑就是当前的根节点 root！
2. 【中序遍历的特权：根节点是楚河汉界】：
   - 中序遍历是“左 -> 根 -> 右”。我们在中序数组里定位到这个根节点所在的下标 rootIdx。
   - 此时整个中序数组被一刀切为两半：
     - rootIdx 左边的所有元素，全部来自左子树！
     - rootIdx 右边的所有元素，全部来自右子树！
3. 【左右子树尺寸对齐，递归建树】：
   - 数一下左子树到底有几个节点：leftSize = rootIdx - iStart。
   - 那么在前序数组中，紧贴在根节点后面的 leftSize 个元素（pStart + 1 到 pStart + leftSize），就精确对应左子树的前序遍历！
   - 剩下的元素（pStart + leftSize + 1 到 pEnd），就精确对应右子树的前序遍历！
   - 左右两边拿到各自的前序和中序子区间，递归调用自己，树根的左右子树便瞬间接驳完成！
4. 【工程核心性能优化】：
   - 千万不要每次都在中序数组里调用 inorder.indexOf(rootVal)！这样每次都是 O(N) 线性查找，整道题会退化到 O(N^2) 导致严重超时！
   - 必须提前准备一个 Map，预先存下 { 节点值 => 中序下标 }，把查询压到 O(1)，建树全程 O(N) 极速完成！
''',
        "js_helpers": [
            {
                "name": 'const map = new Map() 预存中序索引',
                "what_it_does": 'inorder.forEach((v, i) => map.set(v, i)) 预存映射关系。',
                "junior_tip": '彻底消灭内层重复 indexOf()，将查找根节点从 O(N) 降为 O(1)。'
            },
            {
                "name": 'const leftSize = rootIdx - iStart',
                "what_it_does": '根据中序下标计算左子树节点总数。',
                "junior_tip": '关键尺寸转换器！在前序序列中向前偏移 leftSize 个身位即可切出左子树前序。'
            },
            {
                "name": '区间指针 helper(pStart, pEnd, iStart, iEnd)',
                "what_it_does": '传递四个边界下标控制子树区间。',
                "junior_tip": '零数组切片（slice）拷贝开销，代码纯净且极具工程健壮性。'
            },
        ],
        "code_js": '''/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    // 第 1 步：Map 预存中序序列的 { 节点值 => 下标 }，将查找根节点从 O(N) 优化至 O(1)
    const map = new Map();
    for (let i = 0; i < inorder.length; i++) {
        map.set(inorder[i], i);
    }

    // 辅助递归函数：根据前序与中序的索引闭区间构建子树
    const helper = (pStart, pEnd, iStart, iEnd) => {
        // 递归基底：区间非法返回 null
        if (pStart > pEnd) return null;

        // 前序遍历区间的第一个元素必为根节点
        const rootVal = preorder[pStart];
        const root = new TreeNode(rootVal);

        // 获取根在中序中的索引及左子树大小
        const rootIdx = map.get(rootVal);
        const leftSize = rootIdx - iStart;

        // 递归构造左子树：前序取 [pStart + 1, pStart + leftSize]，中序取 [iStart, rootIdx - 1]
        root.left = helper(pStart + 1, pStart + leftSize, iStart, rootIdx - 1);
        // 递归构造右子树：前序取 [pStart + leftSize + 1, pEnd]，中序取 [rootIdx + 1, iEnd]
        root.right = helper(pStart + leftSize + 1, pEnd, rootIdx + 1, iEnd);

        return root;
    };

    return helper(0, preorder.length - 1, 0, inorder.length - 1);
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：Map 记录 inorder 索引位置',
                "detail": '细扣：以值映射下标，避免内层 indexOf() 导致 O(N^2) 退化超时。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：前序首节点定根 rootVal = preorder[pStart]',
                "detail": '细扣：中序划分左右两半，推导 leftSize = rootIdx - iStart。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：精确计算子区间递归左子树',
                "detail": '细扣：pStart + 1 到 pStart + leftSize 完美对齐左子树前序。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：精确计算子区间递归右子树',
                "detail": '细扣：pStart + leftSize + 1 到 pEnd 对应右子树前序。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：递归基底判定与时间 O(N) 空间 O(N) 证明',
                "detail": '细扣：if (pStart > pEnd) return null 防守；传指针无额外数组开销。',
                "weight": 20
            },
        ]
    },
    437: {
        "title_cn": '路径总和 III',
        "title_en": 'Path Sum III',
        "slug": 'path-sum-iii',
        "difficulty": 'Medium',
        "description": '''给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条：
5 -> 3
5 -> 2 -> 1
-3 -> 11

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3

提示:
- 二叉树的节点数在 [0, 1000] 的范围内。
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000
''',
        "plain_explanation": '''统计满足路径和为 targetSum 的所有向下路径数量。
如果用两重递归暴力搜索（对每个节点都跑一次 DFS 向下累加），会有大量重复计算，时间复杂度高达 O(N^2)。
保姆级大白话高阶优化：“把第 560 题和为 K 的子数组搬到树上（树上前缀和 + 回溯销账）”。
1. 【前缀和的核心数学逻辑】：
   - 假设从根节点一路走到当前节点，沿途累加的总和是 currSum。
   - 如果在这条路径上，存在某个上游祖先节点，它的前缀和刚好是 currSum - targetSum；
   - 那么从那个祖先节点的子节点开始到当前节点，这一截子路径的和就刚好等于 targetSum！
2. 【哈希表记录频次】：
   - 我们准备一个 Map，记录沿途祖先们出现过的各种前缀和频次。
   - 走到当前节点，立刻翻看 Map：map.get(currSum - targetSum) 出现过几次，就说明当前节点可以和几位祖先配对，产生了几条合法路径！
3. 【关键一步：回溯销账（离开现场抹去痕迹）】：
   - 当左子树全部探索完毕，递归准备返回父节点、转向探索右子树时：
   - 【核心必防】：右子树和左子树是平级的兄弟分支，右子树绝不能把左子树走过的前缀和当作自己的祖先！
   - 所以离开当前节点前，必须把当前前缀和在 Map 里的计数减 1（map.set(currSum, count - 1)）！
4. 初始时别忘了塞入哨兵 map.set(0, 1)，代表前缀和为 0 出现过 1 次，用于捕获直接从根节点出发就刚好等于 targetSum 的整条路径。
''',
        "js_helpers": [
            {
                "name": 'map.set(0, 1) 初始前缀和哨兵',
                "what_it_does": '空路径前缀和为 0 记为出现 1 次。',
                "junior_tip": '支持从根节点直接出发且自身正好等于 targetSum 的完整路径被命中。'
            },
            {
                "name": 'map.get(currSum - targetSum) || 0',
                "what_it_does": 'O(1) 速度差值查表。',
                "junior_tip": '将双重遍历的 O(N^2) 复杂度直降至 O(N)，利用哈希表空间换时间。'
            },
            {
                "name": 'map.set(currSum, map.get(currSum) - 1) 回溯销账',
                "what_it_does": '离开当前节点返回父级前撤销频次。',
                "junior_tip": '【核心必防】不回溯的话，左子树的前缀和会污染右子树，导致横跨兄弟分支算错！'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    // 准备前缀和哈希表：{ 前缀和 => 出现次数 }
    const map = new Map();
    // 关键哨兵：空路径的前缀和为 0 出现 1 次
    map.set(0, 1);

    // 辅助深度优先遍历函数
    const dfs = (node, currSum) => {
        if (!node) return 0;

        // 累加当前节点的值到路径前缀和
        currSum += node.val;

        // 查表：寻找是否存在祖先前缀和满足 currSum - targetSum
        let count = map.get(currSum - targetSum) || 0;

        // 将当前前缀和记入哈希表
        map.set(currSum, (map.get(currSum) || 0) + 1);

        // 递归进入左右子树，累加子树中满足条件的路径数
        count += dfs(node.left, currSum);
        count += dfs(node.right, currSum);

        // 核心回溯：离开当前节点时，将当前前缀和频次减 1，防止跨分支污染
        map.set(currSum, map.get(currSum) - 1);

        return count;
    };

    return dfs(root, 0);
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：map.set(0, 1) 初始空前缀哨兵',
                "detail": '细扣：前缀和哈希表初始化，支持从根节点直接出发命中。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：累加 currSum 并查表统计 count',
                "detail": '细扣：count = map.get(currSum - targetSum) || 0 差值检索合法前驱。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：当前前缀和入表并在左右子树递归',
                "detail": '细扣：深度遍历收集左右分支子路径总和并累加返回。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：回溯撤销 map.set(currSum, get - 1)',
                "detail": '细扣：撤销当前分支前缀频次，彻底防范兄弟分支数据污染。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：前缀和优化与时空复杂度分析',
                "detail": '细扣：将 O(N^2) 双重递归降至严格 O(N) 时间，空间 O(H) 栈深。',
                "weight": 20
            },
        ]
    },
    236: {
        "title_cn": '二叉树的最近公共祖先',
        "title_en": 'Lowest Common Ancestor of a Binary Tree',
        "slug": 'lowest-common-ancestor-of-a-binary-tree',
        "difficulty": 'Medium',
        "description": '''给定一个二叉树, 找到该树中两个指定节点的最近公共祖先（LCA）。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
- 树中节点数目在范围 [2, 10^5] 内。
- -10^9 <= Node.val <= 10^9
- 所有 Node.val 互不相同 。
- p != q
- p 和 q 均存在于给定的二叉树中。
''',
        "plain_explanation": '''找最近公共祖先（Lowest Common Ancestor，简称 LCA），这是无数面试官最钟爱的考察题之一。
代码虽然不到十行，但其递归哲理极为深刻。
保姆级大白话：“左右密探上山汇报，分岔路口即是祖先”。
1. 【密探下山探路】：
   - 我们派密探进入当前节点 root：
   - 如果密探走到了绝壁（root === null），或者恰好撞见了我们要找的嫌疑人之一（root === p || root === q）；
   - 密探立刻停下脚步，向上面汇报自己的当前节点（return root）。
2. 【自底向上聚合密报】：
   - 左子树派出的密探带回的情报是 left，右子树派出的密探带回的情报是 right。
   - 此时当前节点 root 综合分析两份情报：
     - **情况 1：双路撞车（left && right 都不为空）**
       左密探说“我在左边抓到了一个人！”，右密探说“我在右边也抓到了一个人！”
       这说明什么？说明 p 和 q 正好分居在当前节点的左右两侧！当前节点就是他们分道扬镳的相交点，当前节点百分之百就是最近公共祖先（return root）！
     - **情况 2：只有单侧有消息（left 为空或 right 为空）**
       说明两个嫌疑人都在同一侧子树里（或者一个人本身就是另一个人的祖先）。那就把抓到成果的那一侧密报原封不动往上呈报（return left ? left : right）。
     - **情况 3：两边都空**
       直接返回 null。
''',
        "js_helpers": [
            {
                "name": 'if (!root || root === p || root === q) return root;',
                "what_it_does": '递归基底与目标早停捕获。',
                "junior_tip": '撞见 p 或 q 立即向上返回，若其中一个是另一个的祖先，该节点会一路被透传至最终结果。'
            },
            {
                "name": 'if (left && right) return root;',
                "what_it_does": '分叉汇聚核心判据。',
                "junior_tip": '左右两路搜索均有收获，当前节点即为分歧汇合的最近公共祖先。'
            },
            {
                "name": 'return left ? left : right;',
                "what_it_does": '单边透传三元表达式。',
                "junior_tip": '若仅有一侧发现目标，将发现结果继续无损向上传递。'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    // 第 1 步：递归基底——若走到底为 null，或者当前节点就是目标 p 或 q，直接返回当前节点
    if (!root || root === p || root === q) {
        return root;
    }

    // 第 2 步：递归下探左子树与右子树寻找目标
    const left = lowestCommonAncestor(root.left, p, q);
    const right = lowestCommonAncestor(root.right, p, q);

    // 第 3 步：如果左右两边各找到了一个目标，说明 p 和 q 分布在当前节点两侧，当前节点必为 LCA
    if (left && right) {
        return root;
    }

    // 第 4 步：如果只有一边找到了目标，将找到的结果继续向上级汇报传递
    return left ? left : right;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：root === p || root === q 早停汇报',
                "detail": '细扣：命中目标或遇空立即返回自身，向上透传信号。',
                "weight": 25
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：递归探测左子树与右子树',
                "detail": '细扣：分别获取 left 和 right 左右子树搜索成果。',
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：left && right 双路撞车锁定 LCA',
                "detail": '细扣：两边各找到一个，当前节点必为分叉公共祖先，直接 return root。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：单边透传 return left ? left : right',
                "detail": '细扣：若分布在同侧则祖先自然透传，时间严格 O(N)，栈深 O(H)。',
                "weight": 25
            },
        ]
    },
    124: {
        "title_cn": '二叉树中的最大路径和',
        "title_en": 'Binary Tree Maximum Path Sum',
        "slug": 'binary-tree-maximum-path-sum',
        "difficulty": 'Hard',
        "description": '''二叉树中的 路径 被定义成一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
- 树中节点数目范围是 [1, 3 * 10^4]
- -1000 <= Node.val <= 1000
''',
        "plain_explanation": '''Hard 级别的神题！二叉树中的最大路径和，允许路径从任意节点出发、在任意节点结束、甚至在某个节点处向上再向下拐弯！
核心难点：节点数值可能为负数！
保姆级大白话破题法则：“负收益果断断舍离 + 拱桥拐弯全局留痕”。
1. 【负利润果断断舍离（截断取 0）】：
   - 想象你在经营连锁店，一个子树向你汇报它的最大利润。
   - 如果左子树算出来的最大利润居然是个负数（比如亏损了 -10），那你何必带上它？直接一脚踢开，把它贡献的利润截断为 0（Math.max(0, leftGain)）！不选也是一种智慧！
2. 【区分“局部拐弯拱桥”与“向上单边汇报”】：
   - 站在任何一个节点面前，以它为最高拐弯点的完整拱桥路径总和是：
     拱桥和 = node.val + leftGain + rightGain（从左爬上来，穿过自己，滑向右边）。
     我们拿这个完整的拱桥和去刷新全局历史最高分 maxSum = Math.max(maxSum, 拱桥和)！
   - 但是！函数向上级父节点汇报时，能汇报这条拱桥吗？**绝对不能！因为一条路径不能分叉**！
   - 如果父节点还要把你连进更上层的路径里，你只能伸出一只胳膊！所以函数只能向上级汇报：
     单边最大贡献 = node.val + Math.max(leftGain, rightGain)！
3. 全局最高分 maxSum 初始化为 -Infinity，防止整棵树都是负数（比如树只有单个节点 [-3]）时被 0 错误覆盖。
''',
        "js_helpers": [
            {
                "name": 'let maxSum = -Infinity 全局初始化',
                "what_it_does": '将全局最大路径和初始化为负无穷大。',
                "junior_tip": '防守整棵树节点全部为负数（例如 [-3]）的边界，若初始化为 0 会得出错误答案。'
            },
            {
                "name": 'Math.max(0, maxGain(node.left)) 负收益截断',
                "what_it_does": '子树如果贡献负利润，果断截断取 0。',
                "junior_tip": '取 0 代表不走该子分支，避免负收益拉低总路径和。'
            },
            {
                "name": '拱桥拐弯和 vs 单边延伸贡献',
                "what_it_does": '拐弯和更新全局 maxSum；单边和返回给父节点递归。',
                "junior_tip": '【核心避坑】向上汇报只能选左右单边中较长的一条，因为路径绝不可在父级分叉！'
            },
        ],
        "code_js": '''/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
    let maxSum = -Infinity;

    // 辅助函数：自底向上后序遍历，计算当前 node 能为父级贡献的最大单边增益
    const maxGain = (node) => {
        // 空节点贡献为 0
        if (!node) return 0;

        // 递归求左右子树的最大单边贡献；如果贡献为负数，果断取 0 舍弃
        const leftGain = Math.max(0, maxGain(node.left));
        const rightGain = Math.max(0, maxGain(node.right));

        // 核心：以当前 node 为拐弯顶点的拱桥路径总和
        const currentPathSum = node.val + leftGain + rightGain;

        // 刷新全局最大路径和纪录
        maxSum = Math.max(maxSum, currentPathSum);

        // 向上层父节点汇报：只能挑选左右单边中收益较大的一条，加上当前节点自身
        return node.val + Math.max(leftGain, rightGain);
    };

    maxGain(root);
    return maxSum;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：maxSum 初始化为 -Infinity',
                "detail": '细扣：全负数树边界防守，杜绝被 0 错误覆盖。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：Math.max(0, gain) 负收益截断',
                "detail": '细扣：如果子分支和为负数果断弃选取 0，不连累整体。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：刷新拐点路径 node.val + left + right',
                "detail": '细扣：当前节点做山峰拱门，更新全局历史最优 maxSum。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：返回 node.val + Math.max(L, R) 单边',
                "detail": '细扣：不可分叉，向上只能送出单边最大收益供父级拼装。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：后序遍历一次完成与复杂度证明',
                "detail": '细扣：整树遍历一次，时间严格 O(N)，调用栈空间严格 O(H)。',
                "weight": 20
            },
        ]
    },
    200: {
        "title_cn": '岛屿数量',
        "title_en": 'Number of Islands',
        "slug": 'number-of-islands',
        "difficulty": 'Medium',
        "description": '''给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] 的值为 '0' 或 '1'
''',
        "plain_explanation": '''连通块计数的绝佳入门题。
保姆级大白话：“巡航侦察 + 击沉陆地（原地洪水填充 DFS）”。
1. 【网格巡航】：
   - 我们用双层 for 循环，像雷达扫描一样逐行逐列扫描网格 grid[i][j]。
   - 一旦雷达扫描到了没有被沉没的陆地 '1'：
   - 恭喜！这代表我们发现了一座全新的独立岛屿，岛屿总计数 count++！
2. 【启动空投轰炸，原地沉岛】：
   - 发现新岛后，我们绝对不能拍屁股就走。因为整座岛是一大片连通的陆地，如果我们不管它，后续循环扫描到该岛的其他相连地块时，会把它们错误地重复算成新岛！
   - 所以，我们必须立即启动 DFS 深度优先搜索，执行【沉岛战术】：
     - 从当前坐标出发，向上下左右四个方向扩散蔓延；
     - 只要踩到了连着的陆地 '1'，当场把它炸沉变成水 '0'（grid[r][c] = '0'）；
     - 顺藤摸瓜，直到把整座相连的岛屿全部击沉入海！
3. 【原地标记零额外内存】：
   - 直接把陆地原地修改为 '0'，完全不需要额外声明庞大的 visited 二维数组，空间极其节省！
4. 雷达全部扫描完毕后，统计到的 count 就是精准的岛屿总数！
''',
        "js_helpers": [
            {
                "name": "grid[r][c] = '0' 原地击沉标记",
                "what_it_does": "将已访问过的陆地原地修改为海水 '0'。",
                "junior_tip": '免除开辟 O(M*N) 大小 visited 数组的高昂内存开销，原地沉岛极为高效。'
            },
            {
                "name": '网格边界与海水统一拦截卫语句',
                "what_it_does": "if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] !== '1') return;",
                "junior_tip": '一行代码覆盖四个方向出界判定以及海水/已沉没判定，优雅整洁。'
            },
            {
                "name": '四方向深度优先扩散',
                "what_it_does": 'dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1);',
                "junior_tip": '经典的网格图四连通模型，按序递归探索连通陆地。'
            },
        ],
        "code_js": '''/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (!grid || grid.length === 0) return 0;

    const m = grid.length;
    const n = grid[0].length;
    let count = 0;

    // 辅助深度优先搜索函数：原地击沉连通的整座岛屿
    const dfs = (r, c) => {
        // 边界检查：越界或者当前格子是水 '0'（包括已沉没的陆地），直接停止
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] !== '1') {
            return;
        }

        // 原地击沉：将陆地置为 '0'，防止后续循环重复计数
        grid[r][c] = '0';

        // 向上下左右四个方向递归蔓延击沉相连陆地
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };

    // 双层循环遍历网格中的每一个格子
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            // 只要发现一处陆地，说明探得一座新岛
            if (grid[i][j] === '1') {
                count++;
                // 深度优先遍历把整座岛屿全部击沉
                dfs(i, j);
            }
        }
    }

    return count;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：双层 for 循环巡视网格',
                "detail": "细扣：遇到 '1' 触发新岛屿 count++，启动沉岛流程。",
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：DFS 边界与海水守门员检查',
                "detail": "细扣：r<0||r>=m||c<0||c>=n||grid[r][c]!=='1' 统一防护拦截越界与水域。",
                "weight": 25
            },
            {
                "dimension": 'step3',
                "title": "代码第 3 步：grid[r][c] = '0' 原地击沉标记",
                "detail": '细扣：击沉陆地避免重复计数，省去 O(MN) 的 visited 数组空间开销。',
                "weight": 25
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：四方向递归蔓延击沉',
                "detail": '细扣：上下左右深度优先填充连通块，保证整座岛无遗漏沉没。',
                "weight": 15
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：复杂度评估与返回 count',
                "detail": '细扣：每个格子最多被访问 5 次，总时间严格 O(M*N)，栈空间最多 O(M*N)。',
                "weight": 15
            },
        ]
    },
    994: {
        "title_cn": '腐烂的橘子',
        "title_en": 'Rotting Oranges',
        "slug": 'rotting-oranges',
        "difficulty": 'Medium',
        "description": '''在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
- 值 0 代表空单元格；
- 值 1 代表新鲜橘子；
- 值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的 最小分钟数。如果不可能使所有新鲜橘子都腐烂，则返回 -1 。

示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。

示例 3：
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

提示：
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] 仅为 0、1 或 2
''',
        "plain_explanation": '''求所有新鲜橘子全部变烂的最短时间。
为什么绝对不能对每个烂橘子分别算时间？
因为全场所有的初始烂橘子是【在第 0 分钟同时、齐头并进地向四周放毒传染】！
保姆级大白话：“多源毒源同步波浪扩散（多源 BFS）”。
1. 【第 0 分钟普查人口】：
   - 全盘扫描一遍矩阵。
   - 把场上所有的初始烂橘子（值为 2）的坐标统统推进初始队列 queue。它们是第一批同时爆发的毒源！
   - 同时，数一下全场一共有多少个新鲜橘子（freshCount）。
2. 【特殊情况秒退】：
   - 如果场上原本一个新鲜橘子都没有（freshCount === 0），直接返回 0 分钟！
3. 【按分钟一波一波传染】：
   - 只要队列里还有毒源，并且场上还有未感染的新鲜橘子（while (queue.length > 0 && freshCount > 0)）：
   - 时间增加 1 分钟（minutes++）。
   - 拍摄快照锁定当前这一分钟里所有的毒源数量 const size = queue.length。
   - 循环出队这批毒源，沿着上下左右四个方向伸出触手：
     - 如果邻居是新鲜橘子（grid[nr][nc] === 1）：
     - 当场把它感染变烂（grid[nr][nc] = 2）；
     - 新鲜橘子总数减 1（freshCount--）；
     - 并把这个新鲜出炉的二级毒源推入队列，等待下一分钟去祸害更远的邻居！
4. 【大结局验伤】：
   - 波浪平息后，如果还有幸存的新鲜橘子（freshCount > 0，比如被四面海水隔绝的孤岛橘子），说明毒源永远无法触达，返回 -1！
   - 否则返回耗费的总分钟数 minutes！
''',
        "js_helpers": [
            {
                "name": '多源毒源同时入队',
                "what_it_does": '首轮扫描将所有值为 2 的坐标同步塞入 BFS 队列。',
                "junior_tip": '多源 BFS 的灵魂！所有初始点拥有相同的时间起点（第 0 分钟），保证最短时间。'
            },
            {
                "name": 'const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]',
                "what_it_does": '定义上下左右四个方向的偏移量。',
                "junior_tip": '优雅遍历邻居的标准写法，避免冗长的四个 if 分支代码。'
            },
            {
                "name": 'while (queue.length > 0 && freshCount > 0)',
                "what_it_does": '双条件控时循环哨兵。',
                "junior_tip": '【核心必防】必须判 freshCount > 0，避免最后一批橘子出队时四周无新鲜橘子却多计 1 分钟！'
            },
        ],
        "code_js": '''/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const queue = [];
    let freshCount = 0;

    // 第 1 步：全盘扫描，收集所有初始腐烂橘子（多毒源）并统计新鲜橘子总数
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 2) {
                queue.push([i, j]);
            } else if (grid[i][j] === 1) {
                freshCount++;
            }
        }
    }

    // 若原本就没有新鲜橘子，直接 0 分钟完事
    if (freshCount === 0) return 0;

    let minutes = 0;
    // 四方向偏移量数组
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    // 第 2 步：按分钟多源 BFS 波浪式向外扩散
    while (queue.length > 0 && freshCount > 0) {
        minutes++;
        const size = queue.length; // 快照锁定当前分钟内的全部毒源

        for (let k = 0; k < size; k++) {
            const [r, c] = queue.shift();

            // 检查上下左右四个邻居
            for (const [dr, dc] of dirs) {
                const nr = r + dr;
                const nc = c + dc;

                // 遇到未感染的新鲜橘子，立即传染变烂
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 1) {
                    grid[nr][nc] = 2; // 标记为腐烂
                    freshCount--;     // 新鲜橘子减少
                    queue.push([nr, nc]); // 新毒源加入下一轮队列
                }
            }
        }
    }

    // 第 3 步：若仍有幸存的新鲜橘子返回 -1，否则返回耗费分钟数
    return freshCount === 0 ? minutes : -1;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：初始收集所有 2 号毒源与 freshCount',
                "detail": '细扣：所有毒源同步入队，freshCount === 0 直接早退 0 分钟。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：while (q.length && freshCount > 0) 控时',
                "detail": '细扣：必须判 freshCount > 0 避免最后一步无感染多加一分钟。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：拍摄当前分钟毒源容量 const size = queue.length',
                "detail": '细扣：分层 BFS 按分钟计时的核心，精确隔离每分钟毒源。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：四方向扩散感染并推入新毒源',
                "detail": '细扣：grid[nr][nc] = 2; freshCount-- 实时同步减扣与入队。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：freshCount === 0 ? minutes : -1 终局检测',
                "detail": '细扣：检测孤立不可达新鲜橘子，时间严格 O(M*N) 空间 O(M*N)。',
                "weight": 20
            },
        ]
    },
    207: {
        "title_cn": '课程表',
        "title_en": 'Course Schedule',
        "slug": 'course-schedule',
        "difficulty": 'Medium',
        "description": '''你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程 bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共 2 门课程。学习课程 1 之前，你需要完成课程 0。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共 2 门课程。学习课程 1 之前，你需要先完成课程 0；并且学习课程 0 之前，你还应先完成课程 1。这导致了死锁循环。

提示：
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- prerequisites[i] 中的所有课程对 互不相同
''',
        "plain_explanation": '''判断是否存在一种拓扑序列能修完所有课程，本质就是：**判断有向图中是否存在环（循环依赖死锁）**！
保姆级大白话高阶模型：“Kahn 拓扑排序算法——剥洋葱与技能树解锁”。
1. 【概念拆解：入度与出度邻接表】：
   - **入度（In-degree）**：一门课身上挂着几把锁（需要先修几门课）。如果入度是 0，说明它是新手村免费技能，完全不需要前置门槛，进场就能学！
   - **邻接表（Adjacency list）**：记录每一门先修课学完后，能够顺带给哪些后续课程当跳板（解除依赖）。
2. 【小心依赖方向的大坑】：
   - prerequisites[i] = [cur, pre]：要想学 cur，必须先学 pre！
   - 这意味着：有向边的方向是从 pre 指向 cur（pre -> cur）！
   - 所以是 cur 身上挂了一把锁（inDegree[cur]++），而 pre 记下了后续小弟（adj[pre].push(cur)）！
3. 【剥洋葱拓扑排序过程】：
   - 第一轮：把所有完全不需要先修课的自由课程（入度为 0）通统推入队列 queue。
   - 只要队列不为空，出队一门课进行学习，修完的课程总数 count++；
   - 顺着这门课的邻接表，通知它所有的后续课程小弟：“你们的前置要求少了一个，锁减少一把”（inDegree[next]--）；
   - 一旦某个小弟身上的所有锁全被解开（inDegree[next] === 0），说明它也自由了，立刻推入队列等待学习！
4. 【大结局：死锁检测】：
   - 队列空了之后，比对一下：修完的课程总数 count 是否等于总课程数 numCourses？
   - 如果有循环依赖（比如 A 依赖 B，B 依赖 A），环上的课程因为彼此死锁，入度永远不可能降到 0，永远无法入队！
   - 所以只要 count === numCourses 就说明无环成功（true），否则存在环死锁（false）！
''',
        "js_helpers": [
            {
                "name": 'const inDegree = new Array(numCourses).fill(0)',
                "what_it_does": '初始化入度数组，记录每门课的前置依赖门锁数。',
                "junior_tip": 'new Array(len).fill(0) 快速填零，方便后续进行 inDegree[cur]++ 累加。'
            },
            {
                "name": 'const adj = Array.from({ length: numCourses }, () => [])',
                "what_it_does": '安全构建邻接表二维数组。',
                "junior_tip": '【小白致命错误】绝对不能写 new Array(numCourses).fill([])，否则所有位置引用同一个空数组！必须用 Array.from()。'
            },
            {
                "name": '有向图边方向辨析：pre -> cur',
                "what_it_does": '[cur, pre] 代表先学 pre 才能学 cur。',
                "junior_tip": '正确对应 inDegree[cur]++（当前课添锁）与 adj[pre].push(cur)（先修课引出后继）。'
            },
        ],
        "code_js": '''/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    // 统计每门课的入度（需要多少门先修课）
    const inDegree = new Array(numCourses).fill(0);
    // 邻接表：adj[pre] 存储所有依赖于 pre 的后续课程
    const adj = Array.from({ length: numCourses }, () => []);

    // 第 1 步：建图，根据 [cur, pre] 填充入度与邻接表
    for (const [cur, pre] of prerequisites) {
        inDegree[cur]++;
        adj[pre].push(cur);
    }

    // 第 2 步：将所有无需先修课（入度为 0）的课程推入 BFS 队列
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }

    let count = 0; // 记录成功修完的课程门数

    // 第 3 步：拓扑排序剥洋葱
    while (queue.length > 0) {
        const course = queue.shift();
        count++;

        // 遍历所有依赖当前课程的后续课程
        for (const next of adj[course]) {
            inDegree[next]--; // 后续课程的依赖锁减少一把
            // 若所有先修课均已完成，解锁入队
            if (inDegree[next] === 0) {
                queue.push(next);
            }
        }
    }

    // 第 4 步：若修完的课程数等于总课程数，说明无环成功；否则存在死锁环
    return count === numCourses;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：构建 inDegree 数组与 adj 邻接表',
                "detail": '细扣：inDegree[cur]++ 记录先修锁，adj[pre].push(cur) 登记后继。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：入度为 0 课程入队启航',
                "detail": '细扣：无先修门槛的自由节点推入队列驱动 Kahn 拓扑展开。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：出队并削减后继节点入度',
                "detail": '细扣：inDegree[next]--，若归零代表全部前置解锁，立即入队。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：count 累计修完课程数',
                "detail": '细扣：每出队一门课 count++，拓扑有序推进遍历流。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：比对 count === numCourses 锁定死锁环',
                "detail": '细扣：环上节点入度无法清零无法入队，count < numCourses 拦截，时间 O(V+E) 空间 O(V+E)。',
                "weight": 20
            },
        ]
    },
    208: {
        "title_cn": '实现 Trie (前缀树)',
        "title_en": 'Implement Trie (Prefix Tree)',
        "slug": 'implement-trie-prefix-tree',
        "difficulty": 'Medium',
        "description": '''Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
请你实现 Trie 类：
- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word 。
- boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例 1：
输入：
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出：
[null, null, true, false, true, null, true]
解释：
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

示例 2：
输入：
["Trie", "insert", "search", "startsWith"]
[[], ["hot"], ["h"], ["h"]]
输出：
[null, null, false, true]
解释：
插入 "hot"，查询完整单词 "h" 尚不存在返回 False，查询前缀 "h" 存在返回 True。

提示：
- 1 <= word.length, prefix.length <= 2000
- word 和 prefix 仅由小写英文字母组成
- insert、search 和 startsWith 调用次数总计至多为 3 * 10^4 次
''',
        "plain_explanation": '''前缀树（Trie 树，字典树），是搜索引擎自动补全、输入法联想和拼写检查的幕后功臣。
为什么不用普通的哈希表 Set？
因为哈希表查完整单词是 O(1)，但它根本无法在 O(L) 时间内告诉你“有没有以 app 开头的单词”；而 Trie 让拥有公共前缀的单词共享前面的分支！
保姆级大白话：“推门进小木屋与挂完结标牌”。
1. 【节点结构（小木屋）】：
   - 树上的每个节点就是一个小木屋 TrieNode。
   - 屋里有若干扇门通向其他房间：this.children = {}（用字母作为门牌号，比如 'a' 到 'z'）。
   - 屋里还有一个布尔旗帜：this.isEnd = false，用来标记“到我这间木屋为止，算不算一个完整单词的终点”。
2. 【插入单词 insert(word)】：
   - 顺着单词的字母推门前行：
   - 如果当前房间里有这个字母对应的门，直接推门走进去；
   - 如果没有这扇门，当场建一间新房间（new TrieNode()）并走进去；
   - 走到最后一个字母所在的房间，把那间房的牌子翻过来挂上：isEnd = true！
3. 【优雅抽象：公共探路助手 _searchNode(str)】：
   - 无论是查完整单词 search 还是查前缀 startsWith，核心动作都是一样的：“顺着字符一路推门”。
   - 我们提取一个公共辅助函数 _searchNode(str)：
     - 顺着 str 逐个字符推门，只要中途发现哪扇门不存在，立刻返回 null；
     - 如果顺畅推完全部字符，返回最后到达的那间木屋节点。
4. 【精准区分查词与查前缀】：
   - **startsWith(prefix)**：只要路通了就行，完全不关心是不是单词结尾，直接判断 `node !== null`！
   - **search(word)**：不仅路要通，而且最后到达的房间必须挂着完结牌，必须满足 `node !== null && node.isEnd === true`！
''',
        "js_helpers": [
            {
                "name": 'class TrieNode { constructor() { this.children = {}; this.isEnd = false; } }',
                "what_it_does": '字典树节点封装。',
                "junior_tip": '用普通对象 {} 作为字符映射表最简单优雅，isEnd 记录单词终止状态。'
            },
            {
                "name": 'Trie.prototype._searchNode(str) 公共探路方法',
                "what_it_does": '沿字符路径下探，返回到达的末端节点或 null。',
                "junior_tip": '将 search 与 startsWith 的公共遍历逻辑抽离，代码简洁且绝无重复冗余。'
            },
            {
                "name": '区分 search (验 isEnd) 与 startsWith (只验非空)',
                "what_it_does": 'search 检查完整单词，startsWith 检查前缀是否存在。',
                "junior_tip": "深刻理解为什么 search('app') 在只存入 'apple' 时返回 false，而 startsWith 返回 true。"
            },
        ],
        "code_js": '''/**
 * 字典树节点类
 */
class TrieNode {
    constructor() {
        // 子字符映射表：例如 { 'a': TrieNode, 'b': TrieNode }
        this.children = {};
        // 标记是否为某个完整单词的结尾
        this.isEnd = false;
    }
}

/**
 * 初始化前缀树
 */
var Trie = function() {
    this.root = new TrieNode();
};

/** 
 * 向前缀树中插入一个单词
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let curr = this.root;

    for (const ch of word) {
        // 若当前字符对应的分支不存在，新建节点
        if (!curr.children[ch]) {
            curr.children[ch] = new TrieNode();
        }
        // 步入子节点
        curr = curr.children[ch];
    }

    // 单词末尾节点打上完结标记
    curr.isEnd = true;
};

/**
 * 内部公共辅助函数：沿着字符串路径下探查找最终节点
 * @param {string} str
 * @return {TrieNode|null}
 */
Trie.prototype._searchNode = function(str) {
    let curr = this.root;

    for (const ch of str) {
        if (!curr.children[ch]) {
            return null; // 路径中断，不存在
        }
        curr = curr.children[ch];
    }

    return curr; // 返回路径终点节点
};

/** 
 * 检索前缀树中是否存在完整单词 word
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    const node = this._searchNode(word);
    // 节点必须存在且打上了 isEnd 完结标记
    return node !== null && node.isEnd === true;
};

/** 
 * 检索前缀树中是否存在以 prefix 为前缀的单词
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    const node = this._searchNode(prefix);
    // 只要路径存在即代表前缀命中
    return node !== null;
};
''',
        "checkpoints": [
            {
                "dimension": 'step1',
                "title": '代码第 1 步：TrieNode 封装 children 与 isEnd',
                "detail": '细扣：节点维护字符字典映射与完整词终结标志位。',
                "weight": 20
            },
            {
                "dimension": 'step2',
                "title": '代码第 2 步：insert 沿字母串建树并在末尾挂牌',
                "detail": '细扣：缺节点补建，尾节点标 isEnd = true。',
                "weight": 20
            },
            {
                "dimension": 'step3',
                "title": '代码第 3 步：提取公共探路方法 _searchNode(str)',
                "detail": '细扣：抽取公共探路方法，search 与 startsWith 极简复用，消除代码重复。',
                "weight": 20
            },
            {
                "dimension": 'step4',
                "title": '代码第 4 步：区别 search (node.isEnd === true) 与 startsWith',
                "detail": '细扣：词查询必须验证 isEnd，前缀查询节点存在即可。',
                "weight": 20
            },
            {
                "dimension": 'step5',
                "title": '代码第 5 步：各操作时间 O(L) 与空间 O(L) 复杂度分析',
                "detail": '细扣：L 为字符串长度，每个字符推门一次，查询与插入皆为高效 O(L)。',
                "weight": 20
            },
        ]
    },
}
