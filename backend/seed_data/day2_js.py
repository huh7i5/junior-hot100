"""Day 2 JavaScript Solutions with Junior-level explanations, JS helpers, and code-aligned checkpoints.
Auto-generated and deeply refactored to production standard.
"""

DAY_2_JS_DATA = {
    73: {
        "title_cn": '矩阵置零',
        "title_en": 'Set Matrix Zeroes',
        "slug": 'set-matrix-zeroes',
        "difficulty": 'Medium',
        "description": '给定一个 `m x n` 的矩阵，如果一个元素为 `0` ，则将其所在行和列的所有元素都设为 `0` 。请使用 **原地** 算法。\n\n### 示例 1:\n- 输入: matrix = [[1,1,1],[1,0,1],[1,1,1]]\n- 输出: [[1,0,1],[0,0,0],[1,0,1]]\n- 解释: 坐标 (1,1) 为 0，因此第 1 行和第 1 列的所有元素均被置为 0。\n\n### 示例 2:\n- 输入: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n- 输出: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]\n- 解释: 第 0 行存在两个 0，导致第 0 行、第 0 列、第 3 列被全置为 0。\n\n### 提示与约束:\n- m == matrix.length\n- n == matrix[0].length\n- 1 <= m, n <= 200\n- -2^31 <= matrix[i][j] <= 2^31 - 1\n\n### 进阶要求:\n- 一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。\n- 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。\n- 你能想出一个仅使用常量 O(1) 额外空间的解决方案吗？',
        "plain_explanation": '想象一个考场座位表，如果某个考生被判定作弊（值为 0），整排和整列的考生都必须取消成绩（全置为 0）。\n初学者常犯的冲动错误是：一看到 0，就抄起橡皮擦立刻把整行整列全改成 0。这样一来，后面本来没作弊的正常考生也被你改成了 0，等监考老师巡查到后面时，就会误以为他们也作弊了，从而引发滚雪球式的连环误伤，导致整个考场全变成 0！\n\n题目要求额外空间必须是 O(1)，这意味着不能重新拿一张新的大白纸画座位表。\n大白话神仙解法：【借用矩阵最外层的第 0 行和第 0 列，作为现成的小黑板来打勾】！\n当我们在内部发现 matrix[i][j] 是 0 时，就跑到它正上方的黑板 matrix[0][j] 和正左方的黑板 matrix[i][0] 各写一个 0。\n但是等等！第 0 行和第 0 列自己本身也是考生的座位啊！如果它们自己本来就有人是 0 呢？\n所以动工前，先用两个独立的布尔哨兵变量 row0HasZero 和 col0HasZero，把第 0 行和第 0 列原本有没有 0 单独记下来。\n然后严格按部就班：\n1. 查内层，并在边缘黑板打勾；\n2. 依据黑板标记，把内层该置零的格子刷成 0；\n3. 最后看两个哨兵，决定是否把黑板自己整行整列刷成 0。\n层次分明，绝不误伤！',
        "js_helpers": [
            {
                "name": 'matrix.length 与 matrix[0].length',
                "what_it_does": '获取二维数组的行数 m 与列数 n。',
                "junior_tip": '在 JavaScript 中二维数组本质是‘数组里面装数组’。读取 matrix[0].length 之前，最好防御检查 matrix.length > 0，防止空指针异常。'
            },
            {
                "name": '布尔哨兵变量 (let row0HasZero = false)',
                "what_it_does": '用简单的布尔状态记录第一行/列的初始命运。',
                "junior_tip": '算法中的‘分治保护’思想：先把边缘特殊情况用常数变量锁存起来，后续就能放心大胆地把边缘当临时草稿纸复用。'
            },
            {
                "name": '原地打标 (In-place Tagging)',
                "what_it_does": '将已有的数据边界复用为哈希查找表，避免额外开辟内存。',
                "junior_tip": '很多初学者以为 O(1) 空间就是不能做任何标记，其实只要利用输入矩阵已有的位置存放标记，就是工程与面试中最推崇的原地技巧。'
            },
        ],
        "code_js": '/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar setZeroes = function(matrix) {\n    const m = matrix.length;\n    const n = matrix[0].length;\n\n    // 第 1 步：用两个布尔哨兵分别记录第 0 行和第 0 列本身是否原本就含有 0\n    let row0HasZero = false;\n    let col0HasZero = false;\n\n    // 检查第 0 行是否有 0\n    for (let j = 0; j < n; j++) {\n        if (matrix[0][j] === 0) {\n            row0HasZero = true;\n            break;\n        }\n    }\n\n    // 检查第 0 列是否有 0\n    for (let i = 0; i < m; i++) {\n        if (matrix[i][0] === 0) {\n            col0HasZero = true;\n            break;\n        }\n    }\n\n    // 第 2 步：借用第 0 行和第 0 列作为现成打标黑板\n    // 遍历内部子矩阵 (i >= 1, j >= 1)，若当前格子为 0，则在其行首和列首打标记\n    for (let i = 1; i < m; i++) {\n        for (let j = 1; j < n; j++) {\n            if (matrix[i][j] === 0) {\n                matrix[i][0] = 0; // 标记第 i 行需要置零\n                matrix[0][j] = 0; // 标记第 j 列需要置零\n            }\n        }\n    }\n\n    // 第 3 步：根据第 0 行和第 0 列记录的标记，将内部对应的格子置零\n    for (let i = 1; i < m; i++) {\n        for (let j = 1; j < n; j++) {\n            if (matrix[i][0] === 0 || matrix[0][j] === 0) {\n                matrix[i][j] = 0;\n            }\n        }\n    }\n\n    // 第 4 步：最后根据最初保存的哨兵状态，处理第 0 行自身\n    if (row0HasZero) {\n        for (let j = 0; j < n; j++) {\n            matrix[0][j] = 0;\n        }\n    }\n\n    // 第 5 步：最后根据最初保存的哨兵状态，处理第 0 列自身\n    if (col0HasZero) {\n        for (let i = 0; i < m; i++) {\n            matrix[i][0] = 0;\n        }\n    }\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '布尔哨兵预检首行首列命运',
                "detail": '提前扫描第 0 行和第 0 列是否存在原始 0，用独立布尔值锁定，杜绝后续复用空间时自身状态被冲刷覆盖。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '原地打标利用矩阵边缘作为哈希表',
                "detail": '遍历子矩阵 (1..m-1, 1..n-1)，遇到 0 即将 matrix[i][0] 和 matrix[0][j] 刷为 0，将空间复杂度压缩至严格 O(1)。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '内部优先依据标尺覆写数据',
                "detail": '仅依据行首和列首的值决定内部格子是否置零，此时不影响首行首列标记的持续有效性。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '首行自身整行按需归零',
                "detail": '若 row0HasZero 为 true，整行赋 0，独立于内部矩阵逻辑完成收尾。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": '首列自身整列按需归零',
                "detail": '若 col0HasZero 为 true，整列赋 0，规避与首行逻辑交叉导致的冲突。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '时空复杂度与无额外空间论证',
                "detail": '双重遍历耗时 O(M*N)，仅使用 2 个布尔标记变量，完全符合原地算法约束。',
                "weight": 15
            },
        ],
    },
    54: {
        "title_cn": '螺旋矩阵',
        "title_en": 'Spiral Matrix',
        "slug": 'spiral-matrix',
        "difficulty": 'Medium',
        "description": '给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。\n\n### 示例 1:\n- 输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]\n- 输出: [1,2,3,6,9,8,7,4,5]\n- 解释: 按照顺时针路径依次走过顶行 (1,2,3)，右列 (6,9)，底行 (8,7)，左列 (4)，中心 (5)。\n\n### 示例 2:\n- 输入: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n- 输出: [1,2,3,4,8,12,11,10,9,5,6,7]\n- 解释: 矩阵顺时针环绕一圈后进入内层核心。\n\n### 提示与约束:\n- m == matrix.length\n- n == matrix[i].length\n- 1 <= m, n <= 10\n- -100 <= matrix[i][j] <= 100',
        "plain_explanation": '想象你在吃一个四四方方的洋葱，或者玩贪吃蛇顺时针一圈圈往肚子里钻。\n解决这个问题的最直观大白话：【给矩阵立四面可以移动的围栏】！\n- 天花板：top = 0\n- 地板：bottom = m - 1\n- 左墙壁：left = 0\n- 右墙壁：right = n - 1\n\n每一圈永远只做四件事，像口诀一样顺口：\n1. 【向右走】：在 top 那一行从 left 走到 right，走完之后天花板往下压一格（top++）；\n2. 【向下走】：在 right 那一列从 top 走到 bottom，走完之后右墙壁往左缩一格（right--）；\n3. 【向左走】：在地板 bottom 这一行从 right 倒着走到 left，走完之后地板往上抬一格（bottom--）；\n4. 【向上走】：在左墙 left 这一列从 bottom 倒着走到 top，走完之后左墙壁往右推一格（left++）。\n\n最容易踩坑翻车的盲点：\n如果矩阵不是正方形，而是长条形（比如 1 行 4 列，或者 3 行 1 列）。\n向右走完后 top 增加了，此时天花板可能已经穿过了地板（top > bottom）！\n如果你不加检查就直接盲目执行“向左走”和“向上走”，贪吃蛇就会倒车撞墙，把已经走过的格子重复塞进结果数组里！\n所以，只要在第 3 步和第 4 步前，各加一个安全防撞检查（top <= bottom 和 left <= right），代码就稳如泰山！',
        "js_helpers": [
            {
                "name": 'res.push(...)',
                "what_it_does": '将当前访问到的矩阵元素按顺序追加到结果数组中。',
                "junior_tip": 'JavaScript 中 push() 是往数组末尾追加元素的高效方法，平均时间复杂度为 O(1)。'
            },
            {
                "name": '四边界动态收缩模型 (top, bottom, left, right)',
                "what_it_does": '用 4 个整数指针圈定当前尚未被访问的子矩阵范围。',
                "junior_tip": '循环的终止条件就是两道围墙撞车：while (top <= bottom && left <= right)，非常形象且无需借助 visited 访问标记数组。'
            },
            {
                "name": '递减循环 for (let j = right; j >= left; j--)',
                "what_it_does": '从右往左或者从下往上倒序遍历坐标。',
                "junior_tip": '新手写倒序遍历时容易把终止条件写成 j > left 从而漏掉最左侧元素，牢记必须是 j >= left 包含端点。'
            },
        ],
        "code_js": '/**\n * @param {number[][]} matrix\n * @return {number[]}\n */\nvar spiralOrder = function(matrix) {\n    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return [];\n    \n    const res = [];\n    let top = 0;\n    let bottom = matrix.length - 1;\n    let left = 0;\n    let right = matrix[0].length - 1;\n\n    // 当上下或左右边界未交叉撞车时持续旋转收缩\n    while (top <= bottom && left <= right) {\n        // 1. 从左到右遍历当前 top 行\n        for (let j = left; j <= right; j++) {\n            res.push(matrix[top][j]);\n        }\n        top++; // 天花板下压一格\n\n        // 2. 从上到下遍历当前 right 列\n        for (let i = top; i <= bottom; i++) {\n            res.push(matrix[i][right]);\n        }\n        right--; // 右墙壁向左收缩一格\n\n        // 3. 向左走前必须防翻车：确保 top 依然 <= bottom\n        if (top <= bottom) {\n            for (let j = right; j >= left; j--) {\n                res.push(matrix[bottom][j]);\n            }\n            bottom--; // 地板向上抬升一格\n        }\n\n        // 4. 向上走前必须防翻车：确保 left 依然 <= right\n        if (left <= right) {\n            for (let i = bottom; i >= top; i--) {\n                res.push(matrix[i][left]);\n            }\n            left++; // 左墙壁向右推进一格\n        }\n    }\n\n    return res;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '四界限活动围栏初始化',
                "detail": '声明 top=0, bottom=m-1, left=0, right=n-1，建立动态四边界收缩模型。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '向右遍历与上边界收缩',
                "detail": '顺时针第一步遍历 top 行，遍历完毕执行 top++ 下压围栏。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '向下遍历与右边界收缩',
                "detail": '顺时针第二步遍历 right 列，遍历完毕执行 right-- 内缩围栏。',
                "weight": 15
            },
            {
                "dimension": 'point4',
                "title": '向左遍历前置条件校验防单行重复',
                "detail": '显式判断 top <= bottom 后再执行递减循环，避免扁平单行矩阵折返重复读取。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '向上遍历前置条件校验防单列重复',
                "detail": '显式判断 left <= right 后再执行向上循环，left++ 封闭该层螺旋圈。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '全图一趟遍历与时间复杂度 O(MN)',
                "detail": '每个元素被恰好访问一次并 push 入结果数组，时间 O(M*N)，辅助空间 O(1)。',
                "weight": 15
            },
        ],
    },
    48: {
        "title_cn": '旋转图像',
        "title_en": 'Rotate Image',
        "slug": 'rotate-image',
        "difficulty": 'Medium',
        "description": '给定一个 `n × n` 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。\n\n你必须在 **原地** 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。\n\n### 示例 1:\n- 输入: matrix = [[1,2,3],[4,5,6],[7,8,9]]\n- 输出: [[7,4,1],[8,5,2],[9,6,3]]\n- 解释: 第一行 [1,2,3] 旋转后变成了最后一列从上到下 [1,2,3]。\n\n### 示例 2:\n- 输入: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n- 输出: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]\n\n### 提示与约束:\n- n == matrix.length == matrix[i].length\n- 1 <= n <= 20\n- -1000 <= matrix[i][j] <= 1000',
        "plain_explanation": '想象你在桌上旋转一张正方形的手帕或者折纸。\n如果你试图硬算每个格子的新坐标并直接四方轮换，公式极易写错下标（比如 i 变 j, j 变 n-1-i，脑子直接宕机）。\n在几何数学里，有一个让人拍案叫绝的两次翻折等价技巧：\n【顺时针旋转 90 度 = 沿主对角线对折翻转 + 水平左右对折翻转】！\n\n第一步：沿主对角线对折（也叫矩阵转置）。\n把对角线两边的元素互换：matrix[i][j] 和 matrix[j][i] 交换。\n注意：只需要遍历严格的上半部分三角形（j 从 i + 1 开始），不然你把左下角和右上角换过去，下一轮循环又傻傻换回来了！\n\n第二步：水平左右对折（把每一行像照镜子一样反过来）。\n对每一行使用简单的双指针，最左边的数和最右边的数互换，向中间收拢。\n\n只要这两步简单干净的小学折纸操作，矩阵就神奇且完美地顺时针转了整整 90 度！代码零思考负担，原地 O(1) 额外内存！',
        "js_helpers": [
            {
                "name": '[matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]',
                "what_it_does": '利用 ES6 解构赋值语法，原地互换两个变量的值。',
                "junior_tip": '无需声明临时中间变量 let temp = a; a = b; b = temp;，一行解构交换在 JavaScript 现代引擎中有深度优化，清晰优雅。'
            },
            {
                "name": '严格上三角遍历 for (let j = i + 1; j < n; j++)',
                "what_it_does": '只遍历主对角线右上方的元素。',
                "junior_tip": '对角线上的元素 matrix[i][i] 不需要自己跟自己换；j 从 i + 1 开始能严格保证每对对称元素只被交换一次。'
            },
            {
                "name": '双指针水平镜像 while (left < right)',
                "what_it_does": '对每一行数组进行左右对调逆序。',
                "junior_tip": '虽然也可以写 matrix[i].reverse()，但在面试中手写双指针不仅更体现基础功底，而且跨语言通用性极强。'
            },
        ],
        "code_js": '/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar rotate = function(matrix) {\n    const n = matrix.length;\n\n    // 第 1 步：沿主对角线对折翻转（转置矩阵）\n    // 注意内层循环从 i + 1 开始，只遍历严格上三角，避免换过去又换回来\n    for (let i = 0; i < n; i++) {\n        for (let j = i + 1; j < n; j++) {\n            // 利用 ES6 解构赋值原地交换\n            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];\n        }\n    }\n\n    // 第 2 步：将每一行进行左右对称翻转（水平镜像）\n    for (let i = 0; i < n; i++) {\n        let left = 0;\n        let right = n - 1;\n        while (left < right) {\n            [matrix[i][left], matrix[i][right]] = [matrix[i][right], matrix[i][left]];\n            left++;\n            right--;\n        }\n    }\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '几何变换等价分解法',
                "detail": '识别顺时针旋转 90 度等价于先转置（沿对角线翻转）再加上逐行左右翻转。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '严格上三角遍历转置',
                "detail": '内层循环设置 j = i + 1，精准互换 matrix[i][j] 与 matrix[j][i]，杜绝偶数次反转复原。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": 'ES6 解构赋值原地安全交换',
                "detail": '使用 [a, b] = [b, a] 实现零额外变量原地对调，代码具备极佳可读性。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '双指针单行镜像对称反转',
                "detail": '遍历每一行采用 left 与 right 对撞双指针，直到收敛完成行逆序。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '原地修改与空间 O(1) 约束',
                "detail": '不申请任何辅助矩阵，空间严格 O(1)，时间严格 O(N^2)。',
                "weight": 20
            },
        ],
    },
    240: {
        "title_cn": '搜索二维矩阵 II',
        "title_en": 'Search a 2D Matrix II',
        "slug": 'search-a-2d-matrix-ii',
        "difficulty": 'Medium',
        "description": '编写一个高效的算法来搜索 `m x n` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：\n- 每行的元素从左到右升序排列。\n- 每列的元素从上到下升序排列。\n\n### 示例 1:\n- 输入: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5\n- 输出: true\n- 解释: 矩阵中存在值为 5 的元素，位于坐标 (1, 1)。\n\n### 示例 2:\n- 输入: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20\n- 输出: false\n- 解释: 20 不在矩阵中。\n\n### 提示与约束:\n- m == matrix.length\n- n == matrix[i].length\n- 1 <= n, m <= 300\n- -10^9 <= matrix[i][j] <= 10^9\n- 每行的所有元素从左到右升序排列\n- 每列的所有元素从上到下升序排列\n- -10^9 <= target <= 10^9',
        "plain_explanation": '想象你在十字路口做排查。\n如果你站在左上角（最小的数），往右走变大，往下走也变大，如果 target 比当前值大，你根本不知道该往右走还是往下走（选择困难症，二分无法进行）。\n同理，如果站在右下角（最大的数），往左变小，往上变小，也是双向同变。\n\n但是，如果你站在【右上角（第 0 行，最后一列）】：\n奇迹发生了！\n- 往左走，数字一定变小；\n- 往下走，数字一定变大！\n这不就是一颗天然的【二叉搜索树（BST）】的根节点吗？！\n\n我们把搜索指针立在右上角 (row = 0, col = n - 1)：\n1. 如果当前格子 === target：大功告成，直接返回 true！\n2. 如果当前格子 > target：说明当前格太大了。而当前列它下面的数比它还要大，因此【这一整列都不可能存在 target】，我们可以果断把这一列全部淘汰，向左走（col--）！\n3. 如果当前格子 < target：说明当前格太小了。而当前行它左边的数比它还要小，因此【这一整行都不可能存在 target】，我们可以果断把这一行全部淘汰，向下走（row++）！\n\n每次比对，都能像切西瓜一样直接切掉整整一行或整整一列！最多走 m + n 步就能搜完，时间复杂度从 O(mn) 直接降维打击到 O(m + n)！',
        "js_helpers": [
            {
                "name": '右上角顶点初始化 let row = 0, col = n - 1',
                "what_it_does": '选定具备‘向左变小、向下变大’正交特性的战略立足点。',
                "junior_tip": '也可以选择左下角 (row = m - 1, col = 0)，效果完全对称；但切记绝对不能选左上角或右下角。'
            },
            {
                "name": '边界保护 while (row < m && col >= 0)',
                "what_it_does": '确保搜索指针在矩阵有效坐标内行进，不发生数组下标越界。',
                "junior_tip": 'row 从 0 往下递增，上界是 m；col 从 n - 1 往左递减，下界是 0。'
            },
            {
                "name": 'Z 字形剪枝淘汰 (col-- 与 row++)',
                "what_it_does": '单步排除一整列或一整行。',
                "junior_tip": '这是利用有序矩阵特性的最经典 O(M+N) 算法，也被称为‘鞍点搜索’或‘阶梯搜索’。'
            },
        ],
        "code_js": '/**\n * @param {number[][]} matrix\n * @param {number} target\n * @return {boolean}\n */\nvar searchMatrix = function(matrix, target) {\n    if (!matrix || matrix.length === 0 || matrix[0].length === 0) return false;\n\n    const m = matrix.length;\n    const n = matrix[0].length;\n\n    // 从矩阵的右上角顶点出发 (0, n - 1)\n    let row = 0;\n    let col = n - 1;\n\n    // 只要没有走出矩阵边界就持续移动排查\n    while (row < m && col >= 0) {\n        const val = matrix[row][col];\n        if (val === target) {\n            // 抓到目标值，立刻返回\n            return true;\n        } else if (val > target) {\n            // 当前值比 target 大，该列下方所有元素都更大，整列淘汰\n            col--;\n        } else {\n            // 当前值比 target 小，该行左侧所有元素都更小，整行淘汰\n            row++;\n        }\n    }\n\n    // 走出边界仍未找到，说明 target 不存在\n    return false;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '抽象二叉搜索树根节点选择',
                "detail": '洞察右上角（或左下角）元素的双向分流特性：向左必小，向下必大。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '右上角初始指针定位',
                "detail": '初始化 row = 0, col = n - 1，建立精准单向决策起点。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '根据比对结果执行整行整列剪枝',
                "detail": 'val > target 时 col-- 淘汰当前列；val < target 时 row++ 淘汰当前行。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '边界越界判定与快速收敛',
                "detail": 'while (row < m && col >= 0) 保证每一次循环都排除一行或一列，绝无无效循环。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '时空复杂度优化跨越',
                "detail": '最多移动 M + N 步，复杂度从普通暴力的 O(MN) 骤降至 O(M+N)，空间 O(1)。',
                "weight": 20
            },
        ],
    },
    160: {
        "title_cn": '相交链表',
        "title_en": 'Intersection of Two Linked Lists',
        "slug": 'intersection-of-two-linked-lists',
        "difficulty": 'Easy',
        "description": "给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。\n\n题目数据 **保证** 整个链式结构中不存在环。\n注意，函数返回结果后，链表必须 **保持其原始结构** 。\n\n### 示例 1:\n- 输入: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3\n- 输出: Intersected at '8'\n- 解释: 相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。\n\n### 示例 2:\n- 输入: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1\n- 输出: Intersected at '2'\n- 解释: 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。\n\n### 示例 3:\n- 输入: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2\n- 输出: null\n- 解释: 两条链表不相交，返回 null。\n\n### 提示与约束:\n- listA 中节点数目为 m\n- listB 中节点数目为 n\n- 1 <= m, n <= 3 * 10^4\n- 1 <= Node.val <= 10^5\n- 0 <= skipA <= m\n- 0 <= skipB <= n\n- 如果 listA 和 listB 没有交点，intersectVal 为 0\n- 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]\n\n### 进阶要求:\n- 你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？",
        "plain_explanation": '这道题有一个计算机算法界最浪漫的别名：【走过你来时的路，我们终将相遇】。\n\n如果两个链表相交，就像两条支流汇入同一条主江。\n假设链表 A 独有的路程长度是 a，链表 B 独有的路程长度是 b，公共相交的那段路长是 c。\n两个人（指针 pA 和 指针 pB）以相同的速度奔跑：\n- pA 从 A 出发，跑完自己的路程（a + c）到达终点 null 后，立刻转身跳到 B 的起点重新跑；\n- pB 从 B 出发，跑完自己的路程（b + c）到达终点 null 后，立刻转身跳到 A 的起点重新跑。\n\n算一算他们第二趟在交点碰头时各自跑过的总路程：\npA 跑了：a + c + b\npB 跑了：b + c + a\n看到了吗？(a + c + b) 和 (b + c + a) 在数学上完全相等！\n这意味着两人在这一刻跑的步数完全一致，必然会同时到达相交的那个第一个节点！\n\n如果不相交呢（即 c = 0）？\npA 跑了 a 之后去跑 B，总路程 a + b 到达 null；\npB 跑了 b 之后去跑 A，总路程 b + a 到达 null；\n两人也会在同一时刻双双走到 null，循环终止并返回 null。\n全程一行额外数组/哈希表都不需要开辟，纯靠双指针同步收敛，达到空间严格 O(1) 的极致艺术！',
        "js_helpers": [
            {
                "name": '严格对象引用比对 pA === pB',
                "what_it_does": '判断两个指针变量是否指向堆内存中的同一个节点对象。',
                "junior_tip": '链表相交比的是‘节点内存地址是否相同’，而不是比节点的数值 val 是否相等！千万不要写成 pA.val === pB.val。'
            },
            {
                "name": '三元运算符平滑换道 pA = pA === null ? headB : pA.next',
                "what_it_does": '当指针抵达末尾 null 时无缝切换到另一条链表的头部继续前进。',
                "junior_tip": '必须允许指针先走到 null，然后再切到对方头部；不能在 pA.next === null 时就提前切换，否则若两链表长度相等且不相交，会导致死循环。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val) {\n *     this.val = val;\n *     this.next = null;\n * }\n */\n\n/**\n * @param {ListNode} headA\n * @param {ListNode} headB\n * @return {ListNode}\n */\nvar getIntersectionNode = function(headA, headB) {\n    if (!headA || !headB) return null;\n\n    // 准备双指针分别从两条链表的起点出发\n    let pA = headA;\n    let pB = headB;\n\n    // 只要两个指针没有指向同一个节点对象，就继续向前\n    while (pA !== pB) {\n        // 如果 pA 到达末尾 null，则换轨到 headB 继续走，否则走下一步\n        pA = pA === null ? headB : pA.next;\n        // 如果 pB 到达末尾 null，则换轨到 headA 继续走，否则走下一步\n        pB = pB === null ? headA : pB.next;\n    }\n\n    // 相遇时可能是公共交点节点，也可能是不相交时双双到达的 null\n    return pA;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '浪漫双指针路程等长对齐原理',
                "detail": '领会 pA 走 a+c+b 与 pB 走 b+c+a 步数恒等原理，利用步数差抹平长度差。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '空链表边界拦截',
                "detail": '开头防御 if (!headA || !headB) return null，确保初始状态指针安全有效。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '指针换轨逻辑与三元运算符',
                "detail": '严格使用 pA === null ? headB : pA.next，注意必须到达 null 后再切轨，不能跳过 null。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '引用严格相等判定而非数值比较',
                "detail": '用 pA !== pB 比较内存节点对象地址，杜绝值相同而节点不同的假相交逻辑错误。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '不相交自然收敛至双 null 跳出',
                "detail": '若无交点，各走 a+b 步后均同时到达 null，满足 pA === pB 正常优雅终止并返回 null。',
                "weight": 20
            },
        ],
    },
    206: {
        "title_cn": '反转链表',
        "title_en": 'Reverse Linked List',
        "slug": 'reverse-linked-list',
        "difficulty": 'Easy',
        "description": '给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。\n\n### 示例 1:\n- 输入: head = [1,2,3,4,5]\n- 输出: [5,4,3,2,1]\n\n### 示例 2:\n- 输入: head = [1,2]\n- 输出: [2,1]\n\n### 示例 3:\n- 输入: head = []\n- 输出: []\n\n### 提示与约束:\n- 链表中节点的数目范围是 [0, 5000]\n- -5000 <= Node.val <= 5000\n\n### 进阶要求:\n- 链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？',
        "plain_explanation": '想象一列开往远方的绿皮火车，每节车厢的挂钩都单向扣向后一节：\n1 号 -> 2 号 -> 3 号 -> null。\n现在我们要把火车的行驶方向完全倒过来，挂钩反向连接：\nnull <- 1 号 <- 2 号 <- 3 号。\n\n反转的核心是【穿针引线三剑客】：\n- prev：上一节车厢，初始为 null（因为原先的 1 号车厢翻转后就是尾巴，尾巴后面必须连 null）；\n- curr：当前正准备掉头拆挂钩的车厢，初始就是 head；\n- nextTemp：暂存变量。\n\n【最关键的救命操作】：\n当你把当前车厢 curr 的挂钩强行掰向 prev（执行 curr.next = prev）的一瞬间，curr 和原本后一节车厢之间的链条就被你硬生生扯断了！\n如果不提前拉住后面的车厢，整列火车后半截就会在内存中直接飘走失联（变成无法访问的孤儿节点）！\n所以每一步必须牢记口诀：\n1. 先抓牢后继：const nextTemp = curr.next;\n2. 再调转挂钩：curr.next = prev;\n3. 前驱往前挪：prev = curr;\n4. 游标往前挪：curr = nextTemp;\n\n当 curr 走完最后一节车厢变成 null 时，prev 刚好稳稳停在原来的末尾节点（也就是新火车的车头），直接返回 prev！',
        "js_helpers": [
            {
                "name": '指针重定向 curr.next = prev',
                "what_it_does": '改变单向链表节点的指向引用，完成局部掉头。',
                "junior_tip": '这是链表反转最核心的单步原子操作，会立即覆盖原有的 next 引用。'
            },
            {
                "name": '临存后继 const nextTemp = curr.next',
                "what_it_does": '在修改 curr.next 之前将原有的下一个节点地址用局部变量锁定。',
                "junior_tip": '切断旧指针前必须先保存新方向，这是所有链表重构题目的第一军规。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val) {\n *     this.val = val;\n *     this.next = null;\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar reverseList = function(head) {\n    // prev 指向当前节点反转后的前驱节点，初始为 null（反转后原头节点的 next 指向 null）\n    let prev = null;\n    let curr = head;\n\n    while (curr !== null) {\n        // 第 1 步：必须先暂存原链表的下一个节点，防止掉链丢失\n        const nextTemp = curr.next;\n\n        // 第 2 步：将当前节点的 next 倒转指向 prev\n        curr.next = prev;\n\n        // 第 3 步：前驱指针前进到当前节点\n        prev = curr;\n\n        // 第 4 步：当前游标前移到刚才暂存的下一节点\n        curr = nextTemp;\n    }\n\n    // 当 curr 走到 null 时，prev 恰好停在新的头节点上\n    return prev;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '双指针状态维护 prev 与 curr',
                "detail": '初始令 prev = null, curr = head，为首节点反转后作为尾节点指向 null 做好铺垫。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '临时指针暂存防止断链',
                "detail": '关键操作 const nextTemp = curr.next 必须在修改指针前执行，防止后继节点在内存中游离丢失。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '核心指针掉头操作',
                "detail": '执行 curr.next = prev，完成单向引用的局部物理反转。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '指针同步交替前推',
                "detail": '顺序执行 prev = curr 与 curr = nextTemp，保持循环不变性推进。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '边界空链表处理与返回 prev',
                "detail": '当 curr === null 循环自然结束，返回停留在原链表尾部的 prev 作为新头。',
                "weight": 20
            },
        ],
    },
    234: {
        "title_cn": '回文链表',
        "title_en": 'Palindrome Linked List',
        "slug": 'palindrome-linked-list',
        "difficulty": 'Easy',
        "description": '给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。\n\n### 示例 1:\n- 输入: head = [1,2,2,1]\n- 输出: true\n- 解释: 正着读 1->2->2->1，倒着读 1->2->2->1，完全一致。\n\n### 示例 2:\n- 输入: head = [1,2]\n- 输出: false\n\n### 提示与约束:\n- 链表中节点数目在范围 [1, 10^5] 内\n- 0 <= Node.val <= 9\n\n### 进阶要求:\n- 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？',
        "plain_explanation": '回文就是像“上海自来水来自海上”一样，正着念和倒着念完全一样。\n如果把链表节点的值挨个掏出来塞进一个数组，再用双指针从两端向中间对对碰，虽然很简单，但需要 O(N) 的额外数组内存，无法通过进阶要求的 O(1) 空间限制。\n\n大白话三部曲教你纯指针 O(1) 原地通关：\n1. 【快慢指针找中点】：\n   乌龟走 1 步，兔子走 2 步。当兔子跑到终点时，乌龟刚好不偏不倚停在整条链表正中间！\n2. 【把后半段链表反转掉】：\n   就像把书的下半部分撕下来，倒着装订回去（直接复用 206 题的反转单链表模板！）。此时后半段的头节点变成了原本的链表尾部。\n3. 【两头同时向中点走，逐一查验】：\n   拿一个指针 p1 指着前半段的头部，另一个指针 p2 指着倒转后的后半段头部。\n   两人同时一步一步往前迈，每走一步就比对两人的 val 是不是一样。\n   只要有一个不一样，立刻判定不是回文！如果一直比到后半段结束都一样，那就是回文！\n\n（高段位工程素养补充）：做完检查后，把后半段再反转一次接回去，保证原链表完好如初不被破坏。面试官看到这步细节直接好感度拉满！',
        "js_helpers": [
            {
                "name": '快慢指针寻中 fast.next !== null && fast.next.next !== null',
                "what_it_does": '快指针一次前进两步，慢指针一次前进一步，精确捕获前半段末尾节点。',
                "junior_tip": '这种终止条件能确保：偶数长度链表（如 4 个节点）时 slow 停在第 2 个节点；奇数长度（如 5 个节点）时 slow 停在第 3 个正中节点。'
            },
            {
                "name": '封装子函数 reverse(node)',
                "what_it_does": '复用单链表反转逻辑，使主函数步骤条理极其清晰。',
                "junior_tip": '函数是一等公民，把通用逻辑就地封装成小箭头函数，代码模块化且不易写串变量。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val) {\n *     this.val = val;\n *     this.next = null;\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {boolean}\n */\nvar isPalindrome = function(head) {\n    if (!head || !head.next) return true;\n\n    // 辅助函数：反转单链表\n    const reverse = (node) => {\n        let prev = null;\n        let curr = node;\n        while (curr !== null) {\n            const nextTemp = curr.next;\n            curr.next = prev;\n            prev = curr;\n            curr = nextTemp;\n        }\n        return prev;\n    };\n\n    // 第 1 步：快慢指针寻找链表中点（让 slow 停在前半段末尾）\n    let slow = head;\n    let fast = head;\n    while (fast.next !== null && fast.next.next !== null) {\n        slow = slow.next;\n        fast = fast.next.next;\n    }\n\n    // 第 2 步：反转后半段链表（从 slow.next 开始）\n    let secondHalfStart = reverse(slow.next);\n\n    // 第 3 步：前半段与后半段逐节点比对 val\n    let p1 = head;\n    let p2 = secondHalfStart;\n    let result = true;\n\n    while (result && p2 !== null) {\n        if (p1.val !== p2.val) {\n            result = false;\n        }\n        p1 = p1.next;\n        p2 = p2.next;\n    }\n\n    // 第 4 步：还原后半段链表保持原数据结构完好（良好工程素养）\n    slow.next = reverse(secondHalfStart);\n\n    return result;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '空节点与单节点边界前置',
                "detail": '节点数 <= 1 时直接判定为 true，避免快慢指针寻中越界。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '快慢指针精准定位前半段尾部',
                "detail": 'fast 走 2 步 slow 走 1 步，终止条件 fast.next !== null && fast.next.next !== null 确保奇偶长度均分。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '后半段链表局部反转',
                "detail": '将 slow.next 作为头节点进行单链表反转，得到倒序的后半段指针。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '双指针对齐比对节点值',
                "detail": '同步遍历 p1 和 p2，只要出现 p1.val !== p2.val 即记录不匹配。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": '链表结构原样还原修补',
                "detail": '再次执行 reverse(secondHalfStart) 并挂回 slow.next，符合无破坏性算法规范。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '空间 O(1) 与时间 O(N) 分析',
                "detail": '无需辅助数组，全过程纯指针操作，空间严格常数级。',
                "weight": 15
            },
        ],
    },
    141: {
        "title_cn": '环形链表',
        "title_en": 'Linked List Cycle',
        "slug": 'linked-list-cycle',
        "difficulty": 'Easy',
        "description": '给你一个链表的头节点 `head` ，判断链表中是否有环。\n\n如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：`pos` 不作为参数进行传递 。仅仅是为了标识链表的实际情况。\n\n如果链表中存在环 ，则返回 `true` 。 否则，返回 `false` 。\n\n### 示例 1:\n- 输入: head = [3,2,0,-4], pos = 1\n- 输出: true\n- 解释: 链表中有一个环，其尾部连接到第二个节点 (索引 1)。\n\n### 示例 2:\n- 输入: head = [1,2], pos = 0\n- 输出: true\n- 解释: 链表中有一个环，其尾部连接到第一个节点 (索引 0)。\n\n### 示例 3:\n- 输入: head = [1], pos = -1\n- 输出: false\n- 解释: 链表中没有环。\n\n### 提示与约束:\n- 链表中节点的数目范围是 [0, 10^4]\n- -10^5 <= Node.val <= 10^5\n- pos 为 -1 或者链表中的一个有效索引。\n\n### 进阶要求:\n- 你能用 O(1)（即，常量）内存解决此问题吗？',
        "plain_explanation": "想象操场环形跑道上的经典寓言：【龟兔赛跑】（弗洛伊德判圈算法 Floyd's Cycle Detection）。\n\n如果是一条笔直的单行道：\n跑得快的兔子（每次走两步）会飞速冲到尽头（撞见 null）。只要兔子看到 null，就说明这条路有尽头，绝对没有环！\n\n如果是包含环形跑道的迷宫：\n乌龟（slow每次走一步）和兔子（fast每次走两步）都会一头扎进环里转圈圈。\n因为兔子每走一轮，相对于乌龟都多前进 1 步（两者的相对速度差为 1）。\n只要进入了环，在相对运动的视角下，就相当于乌龟静止站着，兔子每次以 1 步的距离逐渐缩短与乌龟的差距。\n兔子是绝对不可能“飞跃”乌龟而不被察觉的，它必定会在某一时刻从后面“追尾/套圈”撞上乌龟（slow === fast）！\n\n只要两只动物在同一个节点碰头了，铁证如山，必定有环！\n整个过程无需任何哈希表记录走过的足迹，空间复杂度严格为纯天然的 O(1)！",
        "js_helpers": [
            {
                "name": 'fast !== null && fast.next !== null 双重空指针防护',
                "what_it_does": '确保访问 fast.next.next 之前，前置节点都是有效存在的对象。',
                "junior_tip": "JS 新手最常犯的报错是 Cannot read properties of null (reading 'next')。由于 fast 每次跨两步，必须连验两层非空。"
            },
            {
                "name": 'slow === fast 碰头套圈校验',
                "what_it_does": '判断快慢指针是否引用了同一个节点对象。',
                "junior_tip": '严格利用 JS 对象的引用相等性，只要相遇立即 return true，耗时只有常数级判断。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val) {\n *     this.val = val;\n *     this.next = null;\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {boolean}\n */\nvar hasCycle = function(head) {\n    if (!head || !head.next) return false;\n\n    // 乌龟走 1 步，兔子走 2 步\n    let slow = head;\n    let fast = head;\n\n    // 只要兔子还没跑到尽头（即还有路可走）\n    while (fast !== null && fast.next !== null) {\n        slow = slow.next;\n        fast = fast.next.next;\n\n        // 如果快慢指针相遇，说明存在环，兔子套圈了乌龟\n        if (slow === fast) {\n            return true;\n        }\n    }\n\n    // 兔子跑到了 null，说明是无环直道\n    return false;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '弗洛伊德龟兔赛跑算法原理',
                "detail": '理解相对速度为 1 时，快指针若在闭环中必定能在有限步内追上并套圈慢指针。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '空链表与单节点无环快速特判',
                "detail": '防御 if (!head || !head.next) 直接返回 false，保证后续双指针能安全起跑。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '快指针深层访问空指针保护',
                "detail": 'while (fast !== null && fast.next !== null) 严格防御 TypeError 运行时异常。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '双速推进与碰头判定',
                "detail": 'slow = slow.next 与 fast = fast.next.next，并在碰头处 slow === fast 立即返回 true。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '自然出界与 O(1) 空间优势',
                "detail": '快指针遇 null 立即判定无环，完全避免哈希 Set 带来的 O(N) 空间开销。',
                "weight": 20
            },
        ],
    },
    142: {
        "title_cn": '环形链表 II',
        "title_en": 'Linked List Cycle II',
        "slug": 'linked-list-cycle-ii',
        "difficulty": 'Medium',
        "description": '给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 如果链表无环，则返回 `null`。\n\n如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：`pos` 不作为参数进行传递 。仅仅是为了标识链表的实际情况。\n\n**不允许修改** 链表。\n\n### 示例 1:\n- 输入: head = [3,2,0,-4], pos = 1\n- 输出: 返回索引为 1 的链表节点\n- 解释: 链表中有一个环，其尾部连接到第二个节点。\n\n### 示例 2:\n- 输入: head = [1,2], pos = 0\n- 输出: 返回索引为 0 的链表节点\n- 解释: 链表中有一个环，其尾部连接到第一个节点。\n\n### 示例 3:\n- 输入: head = [1], pos = -1\n- 输出: 返回 null\n- 解释: 链表中没有环。\n\n### 提示与约束:\n- 链表中节点的数目范围在范围 [0, 10^4] 内\n- -10^5 <= Node.val <= 10^5\n- pos 的值为 -1 或者链表中的一个有效索引\n\n### 进阶要求:\n- 你是否可以使用 O(1) 空间解决此题？',
        "plain_explanation": '141 题只问“有没有环”，而这道题更进了一步：“环的入口门牌号在哪个节点”？\n\n两阶段大白话拆解：\n第一阶段：【相遇】\n还是龟兔赛跑，兔子一步走 2 格，乌龟一步走 1 格。如果他们相遇了，证明有环。但注意：相遇的地点往往是在环里面的某个深处，而不是入环点！\n\n第二阶段：【数学魔法寻根】\n我们把路程拆成三段：\n- 起点到入环点的距离为 a；\n- 入环点到相遇点的距离为 b；\n- 相遇点继续往前走，绕回入环点的距离为 c。\n（整个环的周长就是 b + c）。\n在相遇时刻：\n乌龟跑了：a + b\n兔子跑了：a + b + k*(b + c)（k 代表兔子已经在环里多跑了 k 圈）。\n因为兔子速度是乌龟的两倍，兔子路程 = 2 * 乌龟路程：\na + b + k*(b + c) = 2 * (a + b)\n两边消去一个 (a + b)，得到极其震撼的数学等式：\na = k*(b + c) - b = (k - 1)*(b + c) + c！\n\n这意味着什么？！\n如果把兔子抓回链表起点 head，让乌龟留在原地的相遇点；\n然后两人改成【一模一样的龟速（每次各走 1 步）】同时起步！\n当兔子从起点走了 a 步到达入环点时，乌龟刚好绕了 (k-1) 圈又走了 c 步，也恰好抵达入环点！\n两人必定会在【入环节点】实现第二次碰头！直接把碰头节点返回即可！',
        "js_helpers": [
            {
                "name": '两阶段状态机切换',
                "what_it_does": '先用快慢指针验环并捕获相遇点，后用双指针单速测距汇聚到入环点。',
                "junior_tip": '通过一个布尔标记 hasCycle 或直接在相遇后 break，使算法进入第二阶段。'
            },
            {
                "name": 'ptr1 = head 与 ptr2 = slow 同速步进',
                "what_it_does": '一个指针从链表起点出发，另一个从相遇点出发，每次各前进一步。',
                "junior_tip": '利用严格推导出的步数恒等性，彻底告别 Set 记录内存地址的做法，将空间锁定在 O(1)。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val) {\n *     this.val = val;\n *     this.next = null;\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar detectCycle = function(head) {\n    if (!head || !head.next) return null;\n\n    let slow = head;\n    let fast = head;\n\n    // 阶段一：快慢指针寻找相遇点\n    let hasCycle = false;\n    while (fast !== null && fast.next !== null) {\n        slow = slow.next;\n        fast = fast.next.next;\n        if (slow === fast) {\n            hasCycle = true;\n            break;\n        }\n    }\n\n    // 如果快指针走到尽头，说明无环\n    if (!hasCycle) return null;\n\n    // 阶段二：数学定理寻入环点\n    // 将一个指针移回起点 head，另一个留在相遇点，两人同速各前进一步\n    let ptr1 = head;\n    let ptr2 = slow;\n\n    while (ptr1 !== ptr2) {\n        ptr1 = ptr1.next;\n        ptr2 = ptr2.next;\n    }\n\n    // 再次相遇点即为环入口节点\n    return ptr1;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '阶段一快慢指针探测相遇',
                "detail": '运用 fast 走 2 slow 走 1 在环中碰头，确定环的存在性。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '无环快速退出保护',
                "detail": 'fast 或 fast.next 达 null 时标志无环，直接返回 null。',
                "weight": 15
            },
            {
                "dimension": 'point3',
                "title": '数论推导步数守恒原理',
                "detail": '深刻理解 a = c + (k-1)(b+c)，即起点到环入口距离等于相遇点绕行到环入口距离。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '阶段二双指针单速协同汇聚',
                "detail": '令 ptr1 = head, ptr2 = slow，每次各前进一步同步巡航。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '相交碰撞点即为环入口节点',
                "detail": 'while (ptr1 !== ptr2) 终止点即为第一个入环节点。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '零额外空间与不修改原链表约束',
                "detail": '严格遵循 O(1) 空间要求，不修改任何 next 指针。',
                "weight": 15
            },
        ],
    },
    21: {
        "title_cn": '合并两个有序链表',
        "title_en": 'Merge Two Sorted Lists',
        "slug": 'merge-two-sorted-lists',
        "difficulty": 'Easy',
        "description": '将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。\n\n### 示例 1:\n- 输入: l1 = [1,2,4], l2 = [1,3,4]\n- 输出: [1,1,2,3,4,4]\n- 解释: 两个升序链表节点按大小交错穿插接驳。\n\n### 示例 2:\n- 输入: l1 = [], l2 = []\n- 输出: []\n\n### 示例 3:\n- 输入: l1 = [], l2 = [0]\n- 输出: [0]\n\n### 提示与约束:\n- 两个链表的节点数目范围是 [0, 50]\n- -100 <= Node.val <= 100\n- l1 和 l2 均按 非递减顺序 排列',
        "plain_explanation": '想象两排幼儿园小朋友，各自都已经按照身高从矮到高排好了队。\n老师的任务是把他们整编成一列新的、同样按照身高从矮到高排列的大长队。\n\n初学者的最大痛苦是：新队伍的第一个人到底是谁？\n如果先写一堆 if (l1.val < l2.val) 来决定谁当 head，不仅代码冗长，而且如果其中一个队伍一开始就是空的，还得写一大堆特判，极易漏判报空指针异常。\n\n【链表第一大杀器：虚拟假头节点（Dummy Head / 哨兵）】登场！\n老师自己先站在队头最前面当一面“假旗帜”：const dummy = new ListNode(-1)。\n然后拿一个游标指针 curr 指着这面旗帜。\n接着看两个队伍排头的两位小朋友：谁个子矮，curr 的手就牵住谁（curr.next = 较小的那个）；\n被牵走的小朋友出列前进一步，老师的游标 curr 也跟着迈一步。\n\n当其中一个队伍全部挑完出列后，另一个队伍剩下的小朋友因为本来就已经排好序了，根本不用一个一个挑！\n直接大手一挥：curr.next = list1 !== null ? list1 : list2;，把整条剩余队伍直接连在屁股后面！\n最后返回假旗帜后面的第一个小朋友 dummy.next，优雅收工，零边界特判！',
        "js_helpers": [
            {
                "name": 'new ListNode(-1) 虚拟哨兵节点',
                "what_it_does": '凭空创建一个前置辅助节点，使真实头节点也有前驱。',
                "junior_tip": '工程中最常用的链表设计模式。解决了‘新链表头节点尚未确定’时的鸡生蛋蛋生鸡问题，最后统一返回 dummy.next。'
            },
            {
                "name": '条件短路整段挂载 curr.next = list1 !== null ? list1 : list2',
                "what_it_does": '一次性将非空链表的剩余所有节点拼接到当前尾部。',
                "junior_tip": '单向链表的特性：只要接上了头，后面的所有节点都自动随之接入，时间复杂度仅为 O(1)。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} list1\n * @param {ListNode} list2\n * @return {ListNode}\n */\nvar mergeTwoLists = function(list1, list2) {\n    // 创建一个哑节点（哨兵节点），作为合并后链表的前驱护城河\n    const dummy = new ListNode(-1);\n    let curr = dummy;\n\n    // 当两个链表都还有节点时，比较大小并接在 curr 后面\n    while (list1 !== null && list2 !== null) {\n        if (list1.val <= list2.val) {\n            curr.next = list1;\n            list1 = list1.next;\n        } else {\n            curr.next = list2;\n            list2 = list2.next;\n        }\n        curr = curr.next;\n    }\n\n    // 拼接剩余未遍历完的非空链表段\n    curr.next = list1 !== null ? list1 : list2;\n\n    // 返回假头节点的下一个节点，即真正的合并后头节点\n    return dummy.next;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '哑节点 (Dummy Node) 哨兵模式',
                "detail": '用 const dummy = new ListNode(-1) 规避头节点初始化为 null 的特判逻辑。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '双指针值比对与游标挂载',
                "detail": 'while 循环内比较 list1.val 与 list2.val，较小者接入 curr.next。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '指针步进与状态更新',
                "detail": '接入节点后前移对应链表指针，并推进 curr = curr.next 维持游标始终在队尾。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '剩余非空链表直接拼接',
                "detail": 'curr.next = list1 !== null ? list1 : list2，常数时间完成整段挂载。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '返回 dummy.next 卸磨杀驴',
                "detail": '舍弃哨兵头，准确返回合并后链表真实起点，空间严格 O(1)。',
                "weight": 20
            },
        ],
    },
    2: {
        "title_cn": '两数相加',
        "title_en": 'Add Two Numbers',
        "slug": 'add-two-numbers',
        "difficulty": 'Medium',
        "description": '给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。\n\n请你将两个数相加，并以相同形式返回一个表示和的链表。\n\n你可以假设除了数字 0 之外，这两个数都不会以 0 开头。\n\n### 示例 1:\n- 输入: l1 = [2,4,3], l2 = [5,6,4]\n- 输出: [7,0,8]\n- 解释: 342 + 465 = 807。\n- 节点从个位开始：2+5=7，4+6=10(写0进1)，3+4+1=8。\n\n### 示例 2:\n- 输入: l1 = [0], l2 = [0]\n- 输出: [0]\n\n### 示例 3:\n- 输入: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]\n- 输出: [8,9,9,9,0,0,0,1]\n- 解释: 连续产生多轮进位，并在最高位额外扩展出一个新的节点 1。\n\n### 提示与约束:\n- 每个链表中的节点数在范围 [1, 100] 内\n- 0 <= Node.val <= 9\n- 题目数据保证列表表示的数字不含前导零',
        "plain_explanation": '想象我们在小学草稿纸上算竖式加法。\n为什么题目要把数字【逆序】存储（比如数字 342，链表头是 2，然后是 4，最后是 3）？\n这不仅不是为难我们，反而是天大的恩赐！\n因为我们做竖式加法，本来就是【从最低位的个位数开始加，逢十进一，一路往高位算】的！头节点正好是个位，完全吻合计算直觉！\n\n准备一个算盘小助手：\n- 进位变量 carry，初始为 0；\n- 哨兵假头 dummy，用于收录生成的新答案链表。\n\n计算每一位时的三把斧：\n1. 拿两个链表当前位的数（如果某个链表已经短小走完了，就自动补 0 对齐）：\n   sum = val1 + val2 + carry\n2. 计算新的进位：carry = Math.floor(sum / 10)（比如 13 / 10 取整是 1）；\n3. 计算当前位应该留下的数字：digit = sum % 10（比如 13 % 10 是 3）；\n4. 创建一个新节点 new ListNode(digit) 挂在结果链表尾部，指针往后挪。\n\n【初学者最容易死锁的边界惨案】：\n两个链表都走到底了（都变成 null 了），但如果最后一步的相加产生了进位（比如 99 + 1 = 100，最后的最高位进位 1）！\n所以 while 循环的条件必须是：\nl1 !== null || l2 !== null || carry !== 0\n哪怕链表空了，只要 carry 还是 1，就必须再循环一次生成最高位的那个 1 节点！',
        "js_helpers": [
            {
                "name": 'Math.floor(sum / 10)',
                "what_it_does": '获取除法向下取整后的整数结果，提取进位。',
                "junior_tip": 'JavaScript 中数字默认是 64 位浮点数，13 / 10 会得到 1.3！必须使用 Math.floor() 或 Math.trunc() 取整，否则会导致浮点节点数值。'
            },
            {
                "name": 'sum % 10 取模运算',
                "what_it_does": '获取当前数位的个位数数值（0 到 9 之间）。',
                "junior_tip": '模运算在处理大整数运算、循环移位、哈希映射时是出现频率最高的基础运算符。'
            },
            {
                "name": '补零对齐技巧 val1 = l1 ? l1.val : 0',
                "what_it_does": '优雅处理两条链表长度不一致的问题。',
                "junior_tip": '无需在外层先写个循环算长度，边走边通过三元表达式动态补 0，代码极简且不增加额外遍历开销。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} l1\n * @param {ListNode} l2\n * @return {ListNode}\n */\nvar addTwoNumbers = function(l1, l2) {\n    const dummy = new ListNode(0);\n    let curr = dummy;\n    let carry = 0; // 进位值（初始为 0）\n\n    // 只要两个链表有任意一个没走完，或者最后还有一个进位，就必须继续创建新节点\n    while (l1 !== null || l2 !== null || carry !== 0) {\n        // 短链表高位自动补 0 对齐\n        const val1 = l1 !== null ? l1.val : 0;\n        const val2 = l2 !== null ? l2.val : 0;\n\n        // 计算当前总和\n        const sum = val1 + val2 + carry;\n        carry = Math.floor(sum / 10); // 更新进位（向下的整数商）\n        const digit = sum % 10;       // 当前节点存储的余数数值\n\n        // 创建新节点并接入结果链表尾部\n        curr.next = new ListNode(digit);\n        curr = curr.next;\n\n        // 对应非空链表向后推进一步\n        if (l1 !== null) l1 = l1.next;\n        if (l2 !== null) l2 = l2.next;\n    }\n\n    return dummy.next;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '进位标志 carry 与假头节点',
                "detail": '声明 carry = 0 与 dummy 节点，统一头尾与进位逻辑。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '长短链表不对齐时补零对齐',
                "detail": '提取值时使用 l1 ? l1.val : 0，天然抹平位数差。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '十进制进位与个位数拆解计算',
                "detail": '计算 sum = val1 + val2 + carry，通过 Math.floor(sum / 10) 与 sum % 10 分离进位与本位。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '链表尾部新节点追加',
                "detail": 'curr.next = new ListNode(digit) 保持逆序存储特性。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": '最高位溢出额外进位处理',
                "detail": 'while 循环条件包含 carry !== 0，确保例如 99 + 1 = 100 最后的进位 1 能顺利成节点。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '单趟遍历时间 O(max(N,M))',
                "detail": '耗时与较长链表长度呈线性关系，空间为构建答案链表的必要开销。',
                "weight": 15
            },
        ],
    },
    19: {
        "title_cn": '删除链表的倒数第 N 个结点',
        "title_en": 'Remove Nth Node From End of List',
        "slug": 'remove-nth-node-from-end-of-list',
        "difficulty": 'Medium',
        "description": '给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。\n\n### 示例 1:\n- 输入: head = [1,2,3,4,5], n = 2\n- 输出: [1,2,3,5]\n- 解释: 倒数第 2 个节点是 4，删除后链表变为 1->2->3->5。\n\n### 示例 2:\n- 输入: head = [1], n = 1\n- 输出: []\n\n### 示例 3:\n- 输入: head = [1,2], n = 1\n- 输出: [1]\n\n### 提示与约束:\n- 链表中结点的数目为 sz\n- 1 <= sz <= 30\n- 0 <= Node.val <= 100\n- 1 <= n <= sz\n\n### 进阶要求:\n- 你能尝试使用一趟扫描实现吗？',
        "plain_explanation": '单向链表最讨厌的特性就是：【只能往前走，不能倒着看】。\n如果不走完一遍，你根本不知道整条链表到底有多长，怎么才能在只走一趟的情况下，精准揪出倒数第 n 个节点？\n\n大白话解法：【拉一把固定长度为 n 的皮尺】（双指针定距滑窗）。\n两个人在跑道上赛跑：快跑者 fast 和 慢跑者 slow。\n1. 让 fast 先从起点往前跑 n + 1 步，此时 fast 和 slow 之间硬生生拉开了一把长为 n + 1 的尺子。\n2. 然后，让 fast 和 slow 保持这个距离，以完全相同的速度一步一步往前走。\n3. 当 fast 终于跑到跑道尽头（走出链表变成 null）时，慢跑者 slow 因为始终落后这把尺子的距离，恰好稳稳停在【待删除节点的前一个节点（前驱节点）】！\n\n为什么我们要停在前一个节点？\n因为在单链表里，要想抹杀一个节点，我们必须站在它的前驱节点上，执行：\nslow.next = slow.next.next;（绕过它，直接连到它的孙子节点）。\n\n【避坑核心：dummy 护城河】：\n如果链表只有 1 个节点，或者我们要删除的就是原先的第 1 个节点（头节点），它前面根本没有前驱节点怎么办？\n提前在链表头前面挂一个哨兵假头 dummy（dummy.next = head）！\n让快慢指针都从 dummy 出发，这样哪怕删除的是原头节点，slow 也会安安稳稳停在 dummy 上，直接 dummy.next = dummy.next.next，万无一失！',
        "js_helpers": [
            {
                "name": 'new ListNode(0, head) 构造哨兵',
                "what_it_does": '直接在实例化 ListNode 时传入第二个参数作为 next，绑定原有头节点。',
                "junior_tip": 'LeetCode 提供的 ListNode 构造函数标准支持 new ListNode(val, next)，一步搞定假头挂接。'
            },
            {
                "name": '定长快慢指针滑窗',
                "what_it_does": '先单向推移 fast 指针拉开 n+1 间距，再同步步进锁定前驱位置。',
                "junior_tip": '注意是领先 n + 1 步而不是 n 步，因为删除操作的目标是停留在待删节点的‘前驱’，必须多留一格余量。'
            },
            {
                "name": '跳跃引用 slow.next = slow.next.next',
                "what_it_does": '单向链表中删除中间节点的标准物理操作。',
                "junior_tip": '被跳过的节点失去了从 head 可达的引用链条，在 JavaScript 引擎的垃圾回收机制（GC）中会被自动回收释放内存。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} head\n * @param {number} n\n * @return {ListNode}\n */\nvar removeNthFromEnd = function(head, n) {\n    // 建立虚拟头节点，防止删除的是原本的第一个节点（头节点）\n    const dummy = new ListNode(0, head);\n    let fast = dummy;\n    let slow = dummy;\n\n    // 第 1 步：让 fast 先向前走 n + 1 步\n    // 这样 fast 和 slow 之间始终保持 n + 1 个节点的间隔\n    for (let i = 0; i <= n; i++) {\n        fast = fast.next;\n    }\n\n    // 第 2 步：fast 与 slow 同步向前走，直到 fast 走出链表末尾（到达 null）\n    while (fast !== null) {\n        fast = fast.next;\n        slow = slow.next;\n    }\n\n    // 此时 slow 恰好停在待删除节点的前驱节点上！\n    // 第 3 步：跳过待删除节点完成删除\n    slow.next = slow.next.next;\n\n    return dummy.next;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": 'dummy 假头节点护城河',
                "detail": '令 dummy.next = head，彻底解决删除原 head 节点时需要返回新头的问题。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '快指针提前步进 n + 1 步',
                "detail": '从 dummy 出发走 n + 1 步，精确拉开两指针间的尺子距离。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '双指针同速巡航至末尾',
                "detail": 'while (fast !== null) 保持等距前行，当 fast 抵达 null，slow 恰达待删前驱。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '前驱断链与跳跃拼接',
                "detail": '执行 slow.next = slow.next.next，在单向链表中干净剔除目标节点。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '一趟扫描 O(L) 与常数空间',
                "detail": '仅需单次遍历完成定位与删除，完全符合进阶要求。',
                "weight": 20
            },
        ],
    },
    24: {
        "title_cn": '两两交换链表中的节点',
        "title_en": 'Swap Nodes in Pairs',
        "slug": 'swap-nodes-in-pairs',
        "difficulty": 'Medium',
        "description": '给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。\n\n### 示例 1:\n- 输入: head = [1,2,3,4]\n- 输出: [2,1,4,3]\n- 解释: 1 与 2 交换变成 2->1，3 与 4 交换变成 4->3，串联为 2->1->4->3。\n\n### 示例 2:\n- 输入: head = []\n- 输出: []\n\n### 示例 3:\n- 输入: head = [1]\n- 输出: [1]\n\n### 提示与约束:\n- 链表中节点的数目在范围 [0, 100] 内\n- 0 <= Node.val <= 100',
        "plain_explanation": '想象一队舞伴正在排队跳交戈舞，规则是每两个人一组，两两互换位置。\n题目明确规定：严禁投机取巧单纯把节点里面的数字 val 换掉，必须货真价实地把节点对象的指针连线重新接驳！\n\n我们看局部四个人的一小段链表：\nprev -> node1 -> node2 -> nextPair...\n交换之后，我们希望变成：\nprev -> node2 -> node1 -> nextPair...\n\n要想做到这一点，必须重新理顺三根引线（按顺序严格执行）：\n1. 【前驱牵住第 2 个人】：prev.next = node2;\n2. 【第 1 个人牵住下一组队头】：node1.next = node2.next;\n3. 【第 2 个人反手牵住第 1 个人】：node2.next = node1;\n\n连完之后，这一组交换就彻底大功告成！\n然后，把前驱指针往前跳跃两步，停在刚刚换完这一组的尾巴上（也就是 node1）：\nprev = node1;\n继续去处理后面的下一组舞伴！\n\n依然是老规矩，在最前面放一个 dummy 哨兵假头（dummy.next = head），让初始的 prev 站在 dummy 上，最后直接返回 dummy.next 即可！',
        "js_helpers": [
            {
                "name": '局部命名节点引用 const node1 = prev.next; const node2 = prev.next.next;',
                "what_it_does": '在修改任何 next 指针前，先把即将参与交换的两个节点用语义明确的变量名锁定。',
                "junior_tip": '新手最容易在连续连线时把自己绕晕（比如写成 prev.next.next = prev.next 导致死循环）。起一个清晰的局部变量名字，是防 Bug 的最高明策略。'
            },
            {
                "name": '循环终止条件 while (prev.next !== null && prev.next.next !== null)',
                "what_it_does": '确保后面还至少存在两个节点才启动交换。',
                "junior_tip": '如果链表长度是奇数，最后会剩下一个单独的节点；这个条件能保证当只剩 1 个或 0 个节点时自然退出，不发生越界。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar swapPairs = function(head) {\n    // 虚拟头节点，指向当前未交换对的前驱\n    const dummy = new ListNode(0, head);\n    let prev = dummy;\n\n    // 只要后面还有至少两个节点，就可以继续两两交换\n    while (prev.next !== null && prev.next.next !== null) {\n        const node1 = prev.next;\n        const node2 = prev.next.next;\n\n        // 重新接线三部曲：\n        // 1. 前驱指向第二个节点\n        prev.next = node2;\n        // 2. 第一个节点指向后面的链表\n        node1.next = node2.next;\n        // 3. 第二个节点反手指向第一个节点\n        node2.next = node1;\n\n        // 前驱游标推进两格，停在已经交换完的这一对的尾巴上（即 node1）\n        prev = node1;\n    }\n\n    return dummy.next;\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '哨兵节点 dummy 挂接原头',
                "detail": '初始设 prev = dummy，规避首对交换后新头节点丢失风险。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '偶数节点存在性循环守卫',
                "detail": 'while (prev.next !== null && prev.next.next !== null) 保证每次处理有效成对节点。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '明确命名局部节点引用',
                "detail": 'const node1 = prev.next 与 const node2 = prev.next.next，防止复杂嵌套 next 赋值产生死循环。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '重新穿针引线三步走',
                "detail": '顺次执行 prev.next=node2, node1.next=node2.next, node2.next=node1，严防环路断链。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '前驱游标前进至 node1',
                "detail": '正确将 prev 更新为 node1，准备处理下一组节点，空间复杂度 O(1)。',
                "weight": 20
            },
        ],
    },
    25: {
        "title_cn": 'K 个一组翻转链表',
        "title_en": 'Reverse Nodes in k-Group',
        "slug": 'reverse-nodes-in-k-group',
        "difficulty": 'Hard',
        "description": '给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。\n\n`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。\n\n你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。\n\n### 示例 1:\n- 输入: head = [1,2,3,4,5], k = 2\n- 输出: [2,1,4,3,5]\n- 解释: 前两个节点 1,2 翻转为 2,1；接着两个节点 3,4 翻转为 4,3；末尾剩余节点 5 不满 2 个，保持原样。\n\n### 示例 2:\n- 输入: head = [1,2,3,4,5], k = 3\n- 输出: [3,2,1,4,5]\n- 解释: 前三个节点 1,2,3 翻转为 3,2,1；末尾剩余节点 4,5 不满 3 个，保持原样。\n\n### 提示与约束:\n- 链表中的节点数目为 n\n- 1 <= k <= n <= 5000\n- 0 <= Node.val <= 1000\n- 1 <= k <= n\n\n### 进阶要求:\n- 你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？',
        "plain_explanation": '这道题是整个 LeetCode 链表题型里的【压轴大 BOSS】（Hard 题之王，也是大厂高频面试题）。\n只要掌握了清晰的结构拆分，它其实就是“206 题反转单链表”加上“组团巡检”的流水线作业！\n\n大白话全流程拆解：\n准备一个大管家 groupPrev（上一组翻转后的尾巴，最开始是 dummy 假头）。\n每一轮循环，管家只做三件事：\n\n1. 【数人头（探路）】：\n   从 groupPrev 出发，往前数 k 个人（groupEnd）。\n   如果在数到 k 之前就遇到了 null，说明后面剩下的人不够 k 个了！\n   题目说不够 k 个就保持原样，管家直接吹哨收工（return dummy.next）！\n\n2. 【局部手术（翻转这一组）】：\n   如果够 k 个人，我们记录下这组的头 groupStart 和这组的尾 groupEnd，以及下一组的开头 nextGroup = groupEnd.next。\n   把 [groupStart, groupEnd] 这一段单独拎出来局部反转（就像 206 题）。\n   翻转完成后，原来的尾巴变成了新头（newHead），原来的头变成了新尾巴（newTail）！\n\n3. 【缝合回主干并交接班】：\n   让上一组的尾巴牵住这一组的新头：groupPrev.next = newHead;\n   让这一组的新尾巴牵住下一组的开头：newTail.next = nextGroup;\n   最后管家交接班：groupPrev = newTail;，走向下一组！\n\n每一步逻辑独立封闭，没有复杂交织，空间严格 O(1)！',
        "js_helpers": [
            {
                "name": '区间局部反转辅助函数 reverse(headNode, tailNode)',
                "what_it_does": '反转从 headNode 到 tailNode 的封闭区间，返回 [newHead, newTail]。',
                "junior_tip": '将局部反转逻辑抽离成封闭函数，让主循环的‘探路 - 翻转 - 缝合’逻辑极其清爽，面试官一眼就能看出极高的工程素养。'
            },
            {
                "name": '前瞻探路循环 for (let i = 0; i < k; i++)',
                "what_it_does": '在真正修改任何指针前，先验证剩余链表长度是否满足 k 个节点。',
                "junior_tip": '‘先验证再修改’是防止链表破坏的最安全策略，一旦 groupEnd === null 立即安全撤退。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} head\n * @param {number} k\n * @return {ListNode}\n */\nvar reverseKGroup = function(head, k) {\n    if (!head || k <= 1) return head;\n\n    const dummy = new ListNode(0, head);\n    let groupPrev = dummy;\n\n    // 辅助函数：反转闭区间 [headNode, tailNode] 的链表\n    const reverse = (headNode, tailNode) => {\n        let prev = null;\n        let curr = headNode;\n        const stop = tailNode.next; // 反转的右边界哨兵\n        while (curr !== stop) {\n            const nextTemp = curr.next;\n            curr.next = prev;\n            prev = curr;\n            curr = nextTemp;\n        }\n        return [tailNode, headNode]; // 返回新的 [新头, 新尾]\n    };\n\n    while (true) {\n        // 第 1 步：探路，检查当前组是否至少有 k 个节点\n        let groupEnd = groupPrev;\n        for (let i = 0; i < k; i++) {\n            groupEnd = groupEnd.next;\n            if (groupEnd === null) {\n                // 不足 k 个节点，保持原有顺序直接返回\n                return dummy.next;\n            }\n        }\n\n        const groupStart = groupPrev.next;\n        const nextGroup = groupEnd.next;\n\n        // 第 2 步：局部翻转当前组的 k 个节点\n        const [newHead, newTail] = reverse(groupStart, groupEnd);\n\n        // 第 3 步：将翻转后的链表重新缝合回主干\n        groupPrev.next = newHead;\n        newTail.next = nextGroup;\n\n        // 第 4 步：推进 groupPrev 到当前组的新尾部，准备下一组\n        groupPrev = newTail;\n    }\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": 'dummy 哨兵与 groupPrev 指针',
                "detail": '记录上一组末尾，便于与新反转的组头无缝拼接。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '前向探索 k 个节点验证充足性',
                "detail": '循环 k 次检查 groupEnd 是否遇 null，不足 k 个节点立即终止并保持原序。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '锁定断点边界 groupStart 与 nextGroup',
                "detail": '精准切断并记录局部头尾与下一组开端，确保操作闭环。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '子区间原地反转算法',
                "detail": '局部翻转 [head, tail]，输出 [newHead, newTail]，逻辑高度内聚。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": '主干双向重新缝合',
                "detail": 'groupPrev.next = newHead 且 newTail.next = nextGroup，维持整条链表贯通。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '常数级 O(1) 空间硬指标',
                "detail": '不依赖任何外部数组存储节点，完全通过指针重定向完成，时间严格 O(N)。',
                "weight": 15
            },
        ],
    },
    138: {
        "title_cn": '随机链表的复制',
        "title_en": 'Copy List with Random Pointer',
        "slug": 'copy-list-with-random-pointer',
        "difficulty": 'Medium',
        "description": '给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。\n\n构造这个链表的 **深拷贝**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的节点都不应引用原链表中的节点。\n\n例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。\n\n返回复制链表的头节点。\n\n### 示例 1:\n- 输入: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]\n- 输出: [[7,null],[13,0],[11,4],[10,2],[1,0]]\n\n### 示例 2:\n- 输入: head = [[1,1],[2,1]]\n- 输出: [[1,1],[2,1]]\n\n### 示例 3:\n- 输入: head = [[3,null],[3,0],[3,null]]\n- 输出: [[3,null],[3,0],[3,null]]\n\n### 提示与约束:\n- 0 <= n <= 1000\n- -10^4 <= Node.val <= 10^4\n- Node.random 为 null 或指向链表中的节点。',
        "plain_explanation": '这道题的难点在哪里？\n普通的链表只有 next 指针，我们顺着一路向后 new ListNode() 就能轻松克隆。\n但这里多了一个随心所欲的 random 指针！\n比如第 1 个节点的 random 可能直接跨过千山万水指向第 100 个节点。\n但当我们克隆第 1 个节点时，第 100 个节点根本还没有被 new 出来呢！巧妇难为无米之炊！\n\n大白话解法：【影分身通讯录（Map 哈希映射法）】！\n我们分两趟走，彻底解决时序依赖问题：\n\n第一趟走：【只造人，不牵线】\n从头到尾遍历原链表，给每一个原节点克隆一个光溜溜的新节点 new _Node(curr.val)。\n然后在手机通讯录（Map）里登记好：\nmap.set(原节点对象, 新克隆出来的节点对象)。\n这一趟走完，所有的克隆人已经全部诞生并在通讯录里一一对应备案了！\n\n第二趟走：【顺藤摸瓜，给克隆人牵线】\n再次从头遍历原链表，对于每一个原节点 curr：\n它的克隆人是谁？map.get(curr)！\n原节点的 next 对应的克隆人是谁？map.get(curr.next)！\n原节点的 random 对应的克隆人是谁？map.get(curr.random)！\n直接牵线：\nclonedNode.next = curr.next ? map.get(curr.next) : null;\nclonedNode.random = curr.random ? map.get(curr.random) : null;\n\n两趟走完，所有的网状关系全部丝滑对齐，最后返回 map.get(head)！代码既安全又绝无脑力负担！',
        "js_helpers": [
            {
                "name": 'new Map() 以对象引用为 Key',
                "what_it_does": '建立 原节点对象 => 克隆节点对象 的强引用映射。',
                "junior_tip": 'JavaScript 普通对象的 key 只能是字符串或 Symbol；但 ES6 的 Map 允许任意对象直接充当 key，这是本题的绝佳数据结构！'
            },
            {
                "name": '安全取值 map.get(curr.next) || null',
                "what_it_does": '防止当 curr.next 为 null 时向 Map 传递 null 产生不可预期行为。',
                "junior_tip": '利用三元判断 curr.next ? map.get(curr.next) : null，代码具备极佳的防御性编程风格。'
            },
        ],
        "code_js": '/**\n * // Definition for a _Node.\n * function _Node(val, next, random) {\n *    this.val = val;\n *    this.next = next;\n *    this.random = random;\n * };\n */\n\n/**\n * @param {_Node} head\n * @return {_Node}\n */\nvar copyRandomList = function(head) {\n    if (!head) return null;\n\n    // 建立映射表：Map<原节点对象, 新克隆节点对象>\n    const map = new Map();\n\n    // 第 1 趟：遍历原链表，只克隆所有节点本身，并存入 Map\n    let curr = head;\n    while (curr !== null) {\n        map.set(curr, new _Node(curr.val, null, null));\n        curr = curr.next;\n    }\n\n    // 第 2 趟：再次遍历原链表，为每一个克隆节点的 next 和 random 连线\n    curr = head;\n    while (curr !== null) {\n        const clonedNode = map.get(curr);\n        // 新节点的 next 指向原节点 next 所映射的克隆节点\n        clonedNode.next = curr.next ? map.get(curr.next) : null;\n        // 新节点的 random 指向原节点 random 所映射的克隆节点\n        clonedNode.random = curr.random ? map.get(curr.random) : null;\n        curr = curr.next;\n    }\n\n    // 返回原头节点对应的新克隆头节点\n    return map.get(head);\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '哈希映射建立原节点与克隆节点关联',
                "detail": 'const map = new Map() 以原节点引用为 key，克隆节点为 value。',
                "weight": 20
            },
            {
                "dimension": 'point2',
                "title": '第一趟遍历纯节点实例化',
                "detail": '先仅根据 val 创建全新节点，存入哈希表，抹平 random 指针向后引用的时序依赖。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '第二趟遍历 next 连线映射',
                "detail": 'clonedNode.next = curr.next ? map.get(curr.next) : null，安全恢复主链骨架。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": 'random 随机指针通过 Map 寻址',
                "detail": 'clonedNode.random = curr.random ? map.get(curr.random) : null，瞬时完成网状引用深拷贝。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '深拷贝纯净性与返回 map.get(head)',
                "detail": '所有指针均指向新对象，无任何原节点内存残留，时间复杂度严格 O(N)。',
                "weight": 20
            },
        ],
    },
    148: {
        "title_cn": '排序链表',
        "title_en": 'Sort List',
        "slug": 'sort-list',
        "difficulty": 'Medium',
        "description": '给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。\n\n### 示例 1:\n- 输入: head = [4,2,1,3]\n- 输出: [1,2,3,4]\n\n### 示例 2:\n- 输入: head = [-1,5,3,4,0]\n- 输出: [-1,0,3,4,5]\n\n### 示例 3:\n- 输入: head = []\n- 输出: []\n\n### 提示与约束:\n- 链表中节点的数目在范围 [0, 5 * 10^4] 内\n- -10^5 <= Node.val <= 10^5\n\n### 进阶要求:\n- 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？',
        "plain_explanation": '数组做排序常常用快速排序，但对于【单向链表】来说，归并排序（Merge Sort）才是天造地设的绝配！\n为什么？\n因为数组做归并排序需要额外开辟一个 O(N) 的辅助数组来装合并结果；\n而链表合并只需要改变几个指针的指向（复用第 21 题合并两个有序链表），天然只需要 O(1) 的辅助指针内存！\n\n归并排序大白话三步走：\n1. 【分（找中点并断链）】：\n   用快慢指针寻找链表正中间。\n   【关键命门操作】：必须将前半段的尾巴强行切断（slow.next = null）！\n   硬生生把一条长链表劈成两条互不相关的独立短链表。如果不切断，两段链表黏在一起，递归就会进入无限死循环导致栈溢出！\n2. 【治（递归劈半）】：\n   递归对左半段执行 sortList(head)；\n   递归对右半段执行 sortList(mid)；\n   一路劈下去，直到链表只剩下 1 个节点（天然有序）时返回。\n3. 【合（拉链式缝合）】：\n   调用合并函数 merge(left, right)，用双指针像拉拉链一样把两个排好序的短链表整合成一个长升序链表！\n\n整棵递归树的高度是 log N，每一层的所有节点总共只被比对一遍（O(N)），总时间复杂度稳稳维持在 O(N log N)！',
        "js_helpers": [
            {
                "name": '快慢指针中点偏置技巧 let fast = head.next;',
                "what_it_does": '快指针从 head.next 出发，保证慢指针 slow 停在左半段的最后一个节点上。',
                "junior_tip": '如果只有 2 个节点时 fast 也从 head 出发，slow 会停在第 2 个节点上，导致劈半后左半段长度仍为 2，右半段为 0，陷入死递归！因此 fast 必须偏置起跑。'
            },
            {
                "name": '物理断链 slow.next = null',
                "what_it_does": '切断前后两段链表的链接，形成两个独立的单链表递归入参。',
                "junior_tip": '链表递归分治的核心操作，忘写这行是导致 Maximum call stack size exceeded 的第一大元凶。'
            },
            {
                "name": '递归基 if (!head || !head.next) return head;',
                "what_it_does": '当节点为 0 或 1 时无需排序，天然构成递归终止条件。',
                "junior_tip": '递归函数必须首先书写递归基，确保递归能够安全触底反弹。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar sortList = function(head) {\n    // 递归基：如果链表为空或只有一个节点，天然有序，直接返回\n    if (!head || !head.next) return head;\n\n    // 辅助函数：合并两个有序单链表（复用第 21 题经典逻辑）\n    const merge = (l1, l2) => {\n        const dummy = new ListNode(0);\n        let curr = dummy;\n        while (l1 !== null && l2 !== null) {\n            if (l1.val <= l2.val) {\n                curr.next = l1;\n                l1 = l1.next;\n            } else {\n                curr.next = l2;\n                l2 = l2.next;\n            }\n            curr = curr.next;\n        }\n        curr.next = l1 !== null ? l1 : l2;\n        return dummy.next;\n    };\n\n    // 第 1 步：使用快慢指针寻找链表中点并断链\n    let slow = head;\n    let fast = head.next; // fast 从 head.next 起步，保证 slow 停在左半段末尾\n    while (fast !== null && fast.next !== null) {\n        slow = slow.next;\n        fast = fast.next.next;\n    }\n\n    const mid = slow.next;\n    slow.next = null; // 必须物理断开！把一条链表劈成两半\n\n    // 第 2 步：递归对左右两半分别进行归并排序\n    const left = sortList(head);\n    const right = sortList(mid);\n\n    // 第 3 步：将两个有序子链表缝合归并\n    return merge(left, right);\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '递归基拦截与单节点有序性',
                "detail": 'if (!head || !head.next) return head，为递归终止提供严密基底。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '快慢指针偏置步进寻找中点',
                "detail": 'fast = head.next 偏置技巧使 slow 准确落在中点前驱，避免两节点时无限死递归。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": 'slow.next = null 物理断链切分',
                "detail": '劈断链表是归并排序链表切分的死命令，未断链将导致栈溢出死循环。',
                "weight": 20
            },
            {
                "dimension": 'point4',
                "title": '分治递归 divide 左右两段',
                "detail": '分别调用 sortList(head) 与 sortList(mid)，分治至原子层级。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": '拉链式有序合并 merge',
                "detail": '借助 dummy 节点在 O(1) 空间下高效缝合两条有序子链表。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '时间 O(N log N) 理论达标',
                "detail": '递归树高 log N，每层合并耗时 O(N)，完全符合进阶时间复杂度。',
                "weight": 15
            },
        ],
    },
    23: {
        "title_cn": '合并 K 个升序链表',
        "title_en": 'Merge k Sorted Lists',
        "slug": 'merge-k-sorted-lists',
        "difficulty": 'Hard',
        "description": '给你一个链表数组，每个链表都已经按升序排列。\n\n请你将所有链表合并到一个升序链表中，返回合并后的链表。\n\n### 示例 1:\n- 输入: lists = [[1,4,5],[1,3,4],[2,6]]\n- 输出: [1,1,2,3,4,4,5,6]\n- 解释: 链表数组如下：\n[\n  1->4->5,\n  1->3->4,\n  2->6\n]\n将它们合并为一个有序链表:\n1->1->2->3->4->4->5->6\n\n### 示例 2:\n- 输入: lists = []\n- 输出: []\n\n### 示例 3:\n- 输入: lists = [[]]\n- 输出: []\n\n### 提示与约束:\n- k == lists.length\n- 0 <= k <= 10^4\n- 0 <= lists[i].length <= 500\n- -10^4 <= lists[i][j] <= 10^4\n- lists[i] 按 升序 排列\n- lists[i].length 的总和不超过 10^4',
        "plain_explanation": '想象世界杯足球赛，有 k 支球队参加淘汰赛争夺总冠军。\n如果采用最笨的打法：\n让第 1 支队伍和第 2 支队伍合并；合并完的新长队再和第 3 支队伍合并；然后再和第 4 支合并……\n这就好比第 1 支队伍要连续踢 k 场比赛！前面的节点会被重复遍历 k 次，总时间复杂度高达 O(k^2 * N)，直接在 LeetCode 判超时（TLE）！\n\n高明的打法：【两两分组，锦标赛淘汰制（分治归并 Divide and Conquer）】！\n假设有 8 支队伍：\n- 第一轮：(1和2合), (3和4合), (5和6合), (7和8合) -> 剩下 4 支队伍；\n- 第二轮：(1-2和3-4合), (5-6和7-8合) -> 剩下 2 支队伍；\n- 决赛：两个半区的胜者做最后合并 -> 决出最终的一条完整长链表！\n\n看到妙处了吗？\n整个淘汰赛树的高度只有 log k 层！\n每一层中，所有的节点加起来依然只被处理了 1 次！\n总时间复杂度瞬间从 O(k^2 * N) 被压到 O(N log k)！\n每次两两合并的具体实现，直接无缝复用第 21 题“合并两个有序链表”的代码，干净优雅且威力无穷！',
        "js_helpers": [
            {
                "name": '区间二分分治 mergeRange(start, end)',
                "what_it_does": '将数组下标区间 [start, end] 折半为两半，自底向上合并。',
                "junior_tip": 'Math.floor((start + end) / 2) 计算中点 mid，分别递归 mergeRange(start, mid) 和 mergeRange(mid + 1, end)。'
            },
            {
                "name": '边界防御 lists.length === 0',
                "what_it_does": '处理空输入数组特殊情况。',
                "junior_tip": '如果 lists 是空数组 []，直接返回 null，防止访问 lists[0] 时越界报错。'
            },
        ],
        "code_js": '/**\n * Definition for singly-linked list.\n * function ListNode(val, next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next = (next===undefined ? null : next)\n * }\n */\n\n/**\n * @param {ListNode[]} lists\n * @return {ListNode}\n */\nvar mergeKLists = function(lists) {\n    if (!lists || lists.length === 0) return null;\n\n    // 辅助函数：合并两个有序链表（复用第 21 题）\n    const mergeTwo = (l1, l2) => {\n        const dummy = new ListNode(0);\n        let curr = dummy;\n        while (l1 !== null && l2 !== null) {\n            if (l1.val <= l2.val) {\n                curr.next = l1;\n                l1 = l1.next;\n            } else {\n                curr.next = l2;\n                l2 = l2.next;\n            }\n            curr = curr.next;\n        }\n        curr.next = l1 !== null ? l1 : l2;\n        return dummy.next;\n    };\n\n    // 分治合并函数：合并 lists 中从 start 到 end 范围的链表\n    const mergeRange = (start, end) => {\n        if (start === end) return lists[start];\n        if (start > end) return null;\n\n        const mid = Math.floor((start + end) / 2);\n        const left = mergeRange(start, mid);\n        const right = mergeRange(mid + 1, end);\n\n        return mergeTwo(left, right);\n    };\n\n    return mergeRange(0, lists.length - 1);\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '空数组与空链表输入边界处理',
                "detail": 'if (!lists || lists.length === 0) return null 快速防护。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '分治思想折半区间分解',
                "detail": 'mergeRange(start, end) 二分切分任务，形成平衡二叉合并树。',
                "weight": 20
            },
            {
                "dimension": 'point3',
                "title": '递归折半基底与 mid 计算',
                "detail": 'Math.floor((start + end) / 2) 与 start === end 快速返回单链表。',
                "weight": 15
            },
            {
                "dimension": 'point4',
                "title": '双指针有序合并底座复用',
                "detail": '提取 mergeTwo 高效合并左右两路归并结果。',
                "weight": 20
            },
            {
                "dimension": 'point5',
                "title": '树形合并降低时间复杂度',
                "detail": '将逐一累加的 O(K^2 N) 优化到严格 O(N log K)，彻底杜绝 LeetCode 超时。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '递归调用栈空间 O(log K)',
                "detail": '系统调用栈深度仅为 log K，内存消耗极低。',
                "weight": 15
            },
        ],
    },
    146: {
        "title_cn": 'LRU 缓存',
        "title_en": 'LRU Cache',
        "slug": 'lru-cache',
        "difficulty": 'Medium',
        "description": '请你设计并实现一个满足  **LRU (最近最少使用) 缓存** 约束的数据结构。\n\n实现 `LRUCache` 类：\n- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存\n- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。\n- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。\n\n函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。\n\n### 示例 1:\n- 输入:\n  ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]\n  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\n- 输出:\n  [null, null, null, 1, null, -1, null, -1, 3, 4]\n- 解释:\n  LRUCache lRUCache = new LRUCache(2);\n  lRUCache.put(1, 1); // 缓存是 {1=1}\n  lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}\n  lRUCache.get(1);    // 返回 1\n  lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}\n  lRUCache.get(2);    // 返回 -1 (未找到)\n  lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}\n  lRUCache.get(1);    // 返回 -1 (未找到)\n  lRUCache.get(3);    // 返回 3\n  lRUCache.get(4);    // 返回 4\n\n### 提示与约束:\n- 1 <= capacity <= 3000\n- 0 <= key <= 10000\n- 0 <= value <= 10^5\n- 最多调用 2 * 10^5 次 get 和 put',
        "plain_explanation": '想象你的办公桌面上堆放着经常要查阅的专业书（桌面面积有限，只能放 capacity 本书）。\n- 每次查阅一本书（get）：你把这本书抽出来翻看，看完后顺手把它放在桌面的最顶端（表示刚刚用过）；\n- 借阅一本新书（put）：你把新书放在最顶端。如果桌面上书放不下了，就把堆在最底下落灰最久的那本书（最久未使用的倒霉蛋）扔进垃圾桶！\n\n题目有极其严苛的硬性要求：get 和 put 都必须在 O(1) 常数时间内完成！\n为什么单用数组不行？因为数组中间删元素挪位置是 O(N)；\n为什么单用哈希表不行？因为哈希表没有顺序，找不出谁最久没用；\n为什么单用单链表不行？因为找到节点后要删除它，单链表找不到前驱指针，耗时 O(N)。\n\n【终极黄金搭档：哈希表 Map + 双向链表（带虚拟双哨兵）】！\n- 哈希表 Map<key, node>：负责 O(1) 速度瞬时定位书本在链表里的节点引用；\n- 双向链表（含 prev 和 next）：负责 O(1) 速度将任意节点从当前位置撕下来，并插入到最头部！\n\n【双哨兵的护城河神威】：\n我们设置一个虚头 head 和一个虚尾 tail，head.next 指向 tail，tail.prev 指向 head。\n所有真实的数据节点都夹在 head 和 tail 之间！\n- 插入头部：直接插在 head 后面；\n- 删除末尾：直接拔掉 tail.prev 指向的那个节点；\n永远不需要判断 node.prev 是否为 null，永远不需要判断 tail 是否为空，一行判空都没有，这就是教科书级别的工业级数据结构！',
        "js_helpers": [
            {
                "name": 'class DLinkedNode 双向链表节点',
                "what_it_does": '包含 key, value, prev, next 四个属性的独立节点对象。',
                "junior_tip": '为什么节点里还要存 key？因为当缓存超限淘汰 tail.prev 时，我们需要知道它的 key 是多少，才能同步从 Map 中把这个 key 给 delete 掉！'
            },
            {
                "name": '虚拟双哨兵 (this.head 与 this.tail)',
                "what_it_does": '固定头尾界标，使所有实际节点的增删均发生在中间位置。',
                "junior_tip": '彻底根除空链表、单节点链表在插入删除时频繁出现的‘找不到 next’或‘找不到 prev’报错。'
            },
            {
                "name": 'Map.prototype.delete(key)',
                "what_it_does": '在 O(1) 时间内从 Map 中移除指定的键值对。',
                "junior_tip": '在淘汰尾部节点时，必须执行 this.map.delete(removed.key)，保持 Map 长度与真实链表完全同步。'
            },
            {
                "name": 'ES6 Map 保持插入顺序的妙用科普',
                "what_it_does": 'JS 引擎保证 Map 遍历顺序与 set 的插入顺序严格一致。',
                "junior_tip": '在日常业务代码中，可以通过 map.delete(key) 再 map.set(key, val) 实现极其精简的内置 LRU，但面试时手写双向链表才是考察算法底蕴的硬核关键！'
            },
        ],
        "code_js": '// 双向链表节点定义\nclass DLinkedNode {\n    constructor(key = 0, value = 0) {\n        this.key = key;\n        this.value = value;\n        this.prev = null;\n        this.next = null;\n    }\n}\n\n/**\n * @param {number} capacity\n */\nvar LRUCache = function(capacity) {\n    this.capacity = capacity;\n    this.size = 0;\n    this.map = new Map(); // 哈希表：key => DLinkedNode\n\n    // 创建虚拟头节点和虚拟尾节点（哨兵节点）\n    this.head = new DLinkedNode();\n    this.tail = new DLinkedNode();\n    this.head.next = this.tail;\n    this.tail.prev = this.head;\n};\n\n// 辅助方法：将节点添加到双向链表头部（表示最新使用）\nLRUCache.prototype.addToHead = function(node) {\n    node.prev = this.head;\n    node.next = this.head.next;\n    this.head.next.prev = node;\n    this.head.next = node;\n};\n\n// 辅助方法：从双向链表中移除指定节点\nLRUCache.prototype.removeNode = function(node) {\n    node.prev.next = node.next;\n    node.next.prev = node.prev;\n};\n\n// 辅助方法：将已有节点移到链表头部（先移除，再加到头）\nLRUCache.prototype.moveToHead = function(node) {\n    this.removeNode(node);\n    this.addToHead(node);\n};\n\n// 辅助方法：删除链表尾部的真实节点（最久未使用）并返回它\nLRUCache.prototype.removeTail = function() {\n    const lastNode = this.tail.prev;\n    this.removeNode(lastNode);\n    return lastNode;\n};\n\n/** \n * @param {number} key\n * @return {number}\n */\nLRUCache.prototype.get = function(key) {\n    if (!this.map.has(key)) {\n        return -1;\n    }\n    const node = this.map.get(key);\n    // 命中缓存，更新热度移到头部\n    this.moveToHead(node);\n    return node.value;\n};\n\n/** \n * @param {number} key \n * @param {number} value\n * @return {void}\n */\nLRUCache.prototype.put = function(key, value) {\n    if (this.map.has(key)) {\n        // 如果 key 存在，更新值并移到头部\n        const node = this.map.get(key);\n        node.value = value;\n        this.moveToHead(node);\n    } else {\n        // 新建节点并插入头部\n        const newNode = new DLinkedNode(key, value);\n        this.map.set(key, newNode);\n        this.addToHead(newNode);\n        this.size++;\n\n        // 如果超出容量，逐出最久未使用的节点\n        if (this.size > this.capacity) {\n            const removed = this.removeTail();\n            this.map.delete(removed.key); // 同步从哈希表中删除对应 key\n            this.size--;\n        }\n    }\n};',
        "checkpoints": [
            {
                "dimension": 'point1',
                "title": '数据结构设计选型（哈希表 + 双向链表）',
                "detail": '阐明为什么单纯数组或单链表无法在 O(1) 内兼顾查找和任意位置节点挪动。',
                "weight": 15
            },
            {
                "dimension": 'point2',
                "title": '双虚拟哨兵节点 head 与 tail 护航',
                "detail": '建立相互指向的虚头虚尾，杜绝插入删除时对 null 边缘做繁琐分支判定。',
                "weight": 15
            },
            {
                "dimension": 'point3',
                "title": '双向链表核心四针穿引 (addToHead & removeNode)',
                "detail": '熟练手写节点拔除与头插逻辑，四根指针变动顺序无差错。',
                "weight": 15
            },
            {
                "dimension": 'point4',
                "title": 'get(key) 命中热度刷新机制',
                "detail": '读取到 node 后调用 moveToHead(node)，实现瞬时提升为最近使用。',
                "weight": 15
            },
            {
                "dimension": 'point5',
                "title": 'put 已有 key 覆盖与置顶',
                "detail": '覆盖 value 并移至头部，不增加 size。',
                "weight": 15
            },
            {
                "dimension": 'point6',
                "title": '容量超限触发淘汰与 Map 同步删除',
                "detail": '调用 removeTail() 斩断尾部节点，利用 removed.key 在 Map 中精准 delete。',
                "weight": 15
            },
            {
                "dimension": 'point7',
                "title": 'ES6 Map 迭代器替代方案延伸',
                "detail": '掌握 Map.prototype.keys().next().value 的顺序特性，展现工程全局视野。',
                "weight": 10
            },
        ],
    },
}
