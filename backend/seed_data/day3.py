DAY_3_PROBLEMS = [
    {
        "frontend_id": 94,
        "title_cn": "二叉树的中序遍历",
        "title_en": "Binary Tree Inorder Traversal",
        "slug": "binary-tree-inorder-traversal",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "显式栈模拟迭代：指针 curr 一路向左将左孩子全部压栈；当 curr 为空时，从栈中弹出节点访问其值，并将 curr 指向右孩子。",
            "traps": "循环条件必须是 `while curr or stack:`，两者满足其一即可继续。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "显式栈模拟中序遍历", "detail": "破题眼：一路向左入栈，触底回溯弹栈输出，转向右子树重复过程。", "weight": 25},
            {"dimension": "corner_case", "title": "双退出条件 while curr or stack", "detail": "防守点：区分 curr 为空但栈不为空（回溯阶段）与 curr 非空栈为空（初始阶段）。", "weight": 25},
            {"dimension": "solution", "title": "经典迭代非递归手写", "detail": "手写点：彻底摒弃递归，12 行内写出标准显式辅助栈中序遍历。", "weight": 25},
            {"dimension": "complexity", "title": "Morris 遍历 O(1) 空间口述", "detail": "演练点：口述利用二叉树空闲右孩子线索构建 Morris 遍历的进阶答法。", "weight": 25}
        ]
    },
    {
        "frontend_id": 104,
        "title_cn": "二叉树的最大深度",
        "title_en": "Maximum Depth of Binary Tree",
        "slug": "maximum-depth-of-binary-tree",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "后序递归分治：当前树的最大深度 = max(左子树深度, 右子树深度) + 1。Base case 为空节点深度为 0。",
            "traps": "也可以用 BFS 层序遍历统计层数，但递归后序一行搞定，极其优雅。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H) 树高",
            "code_python": '''class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "自底向上后序聚合", "detail": "破题眼：子树向上汇报深度，当前节点统领左右取最大值加一。", "weight": 25},
            {"dimension": "corner_case", "title": "叶子节点与空节点基底", "detail": "防守点：if not root: return 0 递归奠基石，单链倾斜树退化考量。", "weight": 25},
            {"dimension": "solution", "title": "单行递归极速手写", "detail": "手写点：3 行代码写出最纯粹的后序递归分解。", "weight": 25},
            {"dimension": "complexity", "title": "最坏与平衡树栈空间分析", "detail": "演练点：口述平衡树栈空间 O(log N)，完全倾斜链退化至 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 226,
        "title_cn": "翻转二叉树",
        "title_en": "Invert Binary Tree",
        "slug": "invert-binary-tree",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "前序或后序遍历：先交换当前节点的左孩子与右孩子，然后递归对左子树与右子树执行翻转。",
            "traps": "若采用中序遍历翻转，递归完左子树并交换后，原左子树变到了右边，右子树递归会再次翻转原左子树！故中序不推荐。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "左右镜像递归互换", "detail": "破题眼：树的递归本质，父节点交换左右分支，子节点各自镜像展开。", "weight": 25},
            {"dimension": "corner_case", "title": "叶子节点交换自闭环", "detail": "防守点：左右皆为 None 时交换无副作用，安全递归返回。", "weight": 25},
            {"dimension": "solution", "title": "Python 平行赋值手写", "detail": "手写点：使用 root.left, root.right = root.right, root.left 无需中间临时变量。", "weight": 25},
            {"dimension": "complexity", "title": "Max Howell 经典梗与工程健壮性", "detail": "演练点：熟知该题历史梗，口述 BFS 队列迭代翻转的广度优先替代方案。", "weight": 25}
        ]
    },
    {
        "frontend_id": 101,
        "title_cn": "对称二叉树",
        "title_en": "Symmetric Tree",
        "slug": "symmetric-tree",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "外内镜像双指针递归：比较两棵树是否对称，需满足：1. 根节点值相等；2. t1 的左子树与 t2 的右子树对称；3. t1 的右子树与 t2 的左子树对称。",
            "traps": "单棵树无法直接递归，必须构造辅助函数 `check(p, q)` 传入两个节点同时比对。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)
        return check(root.left, root.right)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "双树镜像同步下降", "detail": "破题眼：单树无法自省，裂变成两棵镜像树同时比对外侧与内侧。", "weight": 25},
            {"dimension": "corner_case", "title": "单空与全空分支三元判定", "detail": "防守点：严格区分双 None 返回 True，单 None 或值不等返回 False。", "weight": 25},
            {"dimension": "solution", "title": "check 辅助函数外内比对手写", "detail": "手写点：清晰写出 check(p.left, q.right) and check(p.right, q.left)。", "weight": 25},
            {"dimension": "complexity", "title": "队列双入双出迭代口述", "detail": "演练点：口述如何用队列成对入队出队实现非递归广度优先镜像检测。", "weight": 25}
        ]
    },
    {
        "frontend_id": 543,
        "title_cn": "二叉树的直径",
        "title_en": "Diameter of Binary Tree",
        "slug": "diameter-of-binary-tree",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "后序遍历动态维护全局最大值：对于任意节点，穿过该节点的最长路径 = 左子树深度 + 右子树深度。递归函数返回该节点的最大深度供父节点使用。",
            "traps": "直径不一定会经过根节点！所以必须在每个节点处更新全局变量 `ans = max(ans, L + R)`，而递归函数本身只返回单边深度 `max(L, R) + 1`。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def depth(node):
            if not node:
                return 0
            left_d = depth(node.left)
            right_d = depth(node.right)
            self.max_diameter = max(self.max_diameter, left_d + right_d)
            return max(left_d, right_d) + 1
        depth(root)
        return self.max_diameter
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "后序返回值与全局变量分离", "detail": "破题眼：函数返回单侧深度，中间过程用双侧深度之和更新全局直径。", "weight": 25},
            {"dimension": "corner_case", "title": "最大路径不经过 Root 树根", "detail": "防守点：深度偏斜在某一子树内部形成倒U型拐弯，全局 max_diameter 实时捕获。", "weight": 25},
            {"dimension": "solution", "title": "经典两用递归模板手写", "detail": "手写点：明确区分返回值 max(L, R)+1 与更新值 L+R，一气呵成。", "weight": 25},
            {"dimension": "complexity", "title": "点数与边数对应关系", "detail": "演练点：口述题目求的是路径边数，故左右深度直接相加即为边数，无需多余加减。", "weight": 25}
        ]
    },
    {
        "frontend_id": 102,
        "title_cn": "二叉树的层序遍历",
        "title_en": "Binary Tree Level Order Traversal",
        "slug": "binary-tree-level-order-traversal",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "BFS 队列：每层开始时记录 `level_size = len(queue)`，一次性将这批当前层的节点弹出并收集，同时将它们的左右孩子推入队列。",
            "traps": "必须先抓取固定长度 `len(q)`，不能边出队边动态根据当前队列长度循环，否则层与层会混杂。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "定长快照分层出队", "detail": "破题眼：range(len(q)) 快照当前层节点总数，内层循环严格剥离层级。", "weight": 25},
            {"dimension": "corner_case", "title": "空根节点直接防御", "detail": "防守点：if not root: return [] 防止把 None 放进 deque 抛空指针。", "weight": 25},
            {"dimension": "solution", "title": "deque 模板无死角手写", "detail": "手写点：Python 熟练应用 collections.deque 的 popleft 与 append。", "weight": 25},
            {"dimension": "complexity", "title": "最大层宽度与空间复杂度分析", "detail": "演练点：口述满二叉树最后一层拥有 N/2 个节点，队列最大空间消耗为 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 108,
        "title_cn": "将有序数组转换为二叉搜索树",
        "title_en": "Convert Sorted Array to Binary Search Tree",
        "slug": "convert-sorted-array-to-binary-search-tree",
        "difficulty": "Easy",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "分治构造平衡二叉树：选取有序数组的正中元素作为根节点，左半部分递归构造左子树，右半部分递归构造右子树。高度差天然 <= 1。",
            "traps": "区间定义推荐左闭右闭 `[left, right]`，中点取 `(left + right) // 2`。",
            "time_complexity": "O(N)",
            "space_complexity": "O(log N)",
            "code_python": '''class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums) - 1)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "中点二分分治构造", "detail": "破题眼：有序数组中点是 BST 根，两半元素数量差不超过 1，严格平衡。", "weight": 25},
            {"dimension": "corner_case", "title": "空区间递归终止基底", "detail": "防守点：left > right 时返回 None，完美对应叶子节点的左右空孩子。", "weight": 25},
            {"dimension": "solution", "title": "双闭区间二分手写", "detail": "手写点：辅助函数传索引代替数组切片，杜绝额外内存拷贝开销。", "weight": 25},
            {"dimension": "complexity", "title": "主定理 T(N)=2T(N/2)+O(1) 口述", "detail": "演练点：用主定理口述时间复杂度为 O(N)，栈深为 O(log N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 98,
        "title_cn": "验证二叉搜索树",
        "title_en": "Validate Binary Search Tree",
        "slug": "validate-binary-search-tree",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "上下界传递法：每个节点必须满足 `low < val < high`。递归左子树时更新上限 high = val；递归右子树时更新下限 low = val。或者中序遍历严格递增。",
            "traps": "不能只比较当前节点与左右孩子！必须是左子树中所有节点都小于当前节点，右子树全部大于当前节点。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, float('-inf'), float('inf'))
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "动态约束区间向下传递", "detail": "破题眼：突破局部孩子的局限，祖先节点向子孙节点注入 (low, high) 开区间约束。", "weight": 25},
            {"dimension": "corner_case", "title": "相等值非 BST 与数值溢出", "detail": "防守点：BST 要求严格小于和大于，等于即判定非法；初始边界设为无穷大。", "weight": 25},
            {"dimension": "solution", "title": "区间判定清晰手写", "detail": "手写点：10 行以内手写 validate 递归闭包，左右界更新精准。", "weight": 25},
            {"dimension": "complexity", "title": "中序遍历前驱比较法对比", "detail": "演练点：口述基于中序遍历维护 prev 值的第二种解法，证明严格递增等价性。", "weight": 25}
        ]
    },
    {
        "frontend_id": 230,
        "title_cn": "二叉搜索树中第 K 小的元素",
        "title_en": "Kth Smallest Element in a BST",
        "slug": "kth-smallest-element-in-a-bst",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "BST 的中序遍历是严格单调递增序列。使用栈显式中序遍历，每弹出一个元素 k 减 1，当 k == 0 时该元素即为第 k 小，立即提前返回剪枝。",
            "traps": "不要遍历完整棵树存进数组再取 nums[k-1]，面试官考察的是能否在找到第 k 个时提前终止。",
            "time_complexity": "O(H + K)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "中序有序性与提前终止", "detail": "破题眼：BST 中序递增，计数到 k 时立刻 return，将遍历时间锁死在 O(H+K)。", "weight": 25},
            {"dimension": "corner_case", "title": "k=1 最小值极速返回", "detail": "防守点：最左下角叶子首次弹栈即可命中 k=1，极佳响应。", "weight": 25},
            {"dimension": "solution", "title": "显式栈计数中序手写", "detail": "手写点：结合 94 题显式栈架构，弹栈后插入 k -= 1 触发早停。", "weight": 25},
            {"dimension": "complexity", "title": "频繁查询的高级数据结构拓展", "detail": "演练点：口述若 BST 频繁插入删除并查第 k 小，如何在节点中维护 node_count 改造树结构。", "weight": 25}
        ]
    },
    {
        "frontend_id": 199,
        "title_cn": "二叉树的右视图",
        "title_en": "Binary Tree Right Side View",
        "slug": "binary-tree-right-side-view",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "BFS 层序遍历：每层遍历时，最后一个节点（`i == len(q) - 1`）就是该层最右侧暴露的节点，收录到结果列表中。",
            "traps": "右视图不等于纯右孩子链！如果右子树深度浅，左子树更深的分支在下层依然会暴露在右视图中。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "广度优先分层末端捕获", "detail": "破题眼：每层 BFS 的最右侧节点（下标 n-1）天然构成右视图视角投影。", "weight": 25},
            {"dimension": "corner_case", "title": "左深右浅穿透露脸", "detail": "防守点：牢记右子树较短时左子树底层节点会被看到，BFS 层次遍历自然防御此坑。", "weight": 25},
            {"dimension": "solution", "title": "BFS 尾部采样子集手写", "detail": "手写点：在标准 levelOrder 循环内仅对 i == n - 1 进行收集，极其干练。", "weight": 25},
            {"dimension": "complexity", "title": "根-右-左 DFS 递归替代口述", "detail": "演练点：口述若用 DFS 先右后左递归，当 len(res) == depth 时添加该节点。", "weight": 25}
        ]
    },
    {
        "frontend_id": 114,
        "title_cn": "二叉树展开为链表",
        "title_en": "Flatten Binary Tree to Linked List",
        "slug": "flatten-binary-tree-to-linked-list",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "寻找左子树的最右前驱节点（Morris 思想）：当前节点若有左子树，找到其左子树的最右节点 pre；将当前节点的右子树挂到 pre 的右边；然后将左子树移到右边，左边置 None；curr 移向下一个右孩子。",
            "traps": "无需开辟额外空间，纯指针原地嫁接即可做到 O(1) 空间复杂度。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "左子树最右节点前驱缝合", "detail": "破题眼：前序遍历中右子树接在左子树最右侧后方，就地嫁接实现展开。", "weight": 25},
            {"dimension": "corner_case", "title": "左孩子清空与无左孩子下移", "detail": "防守点：curr.left 必须显式设为 None 保持单向单链，curr 无左子树时直接右走。", "weight": 25},
            {"dimension": "solution", "title": "极致 O(1) 空间移花接木手写", "detail": "手写点：双重 while 循环，原地移接右子树，无需递归与栈。", "weight": 25},
            {"dimension": "complexity", "title": "每条边访问次数证明", "detail": "演练点：口述每条边最多被访问两次，整体时间依然为严格 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 105,
        "title_cn": "从前序与中序遍历序列构造二叉树",
        "title_en": "Construct Binary Tree from Preorder and Inorder Traversal",
        "slug": "construct-binary-tree-from-preorder-and-inorder-traversal",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "前序首元素为根节点。在中序中定位该根节点，其左边全为左子树，右边全为右子树。统计左子树节点个数，递归拆分两序列的前序与中序区间。用哈希表预存中序索引达到 O(1) 查询。",
            "traps": "递归时务必精准计算前序与中序的起止索引，切忌在函数内频繁调用 list.index()，否则退化为 O(N^2)。",
            "time_complexity": "O(N)",
            "space_complexity": "O(N)",
            "code_python": '''class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            in_root = idx_map[root_val]
            left_size = in_root - in_left
            
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, in_root + 1, in_right)
            return root
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "前序定根 + 中序分左右", "detail": "破题眼：前序首节点是 root，中序 root 左侧是左子树，由此推得子树大小并递归切分。", "weight": 25},
            {"dimension": "corner_case", "title": "区间索引边界对齐", "detail": "防守点：利用 left_size = in_root - in_left 精准偏移 preorder 索引，杜绝 off-by-one。", "weight": 25},
            {"dimension": "solution", "title": "哈希加速与纯索引手写", "detail": "手写点：字典预处理 inorder 索引，helper 递归只传整数边界，杜绝数组切片。", "weight": 25},
            {"dimension": "complexity", "title": "后序+中序异曲同工辨析", "detail": "演练点：口述如何推导后序+中序（后序末尾为根），阐述前序+后序为何在非真二叉树下无法唯一定树。", "weight": 25}
        ]
    },
    {
        "frontend_id": 437,
        "title_cn": "路径总和 III",
        "title_en": "Path Sum III",
        "slug": "path-sum-iii",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "树上前缀和 + 哈希表回溯：沿 DFS 路径维护前缀和 curr_sum。在哈希表中查 `curr_sum - targetSum` 出现的次数。在子树递归返回时必须将当前 curr_sum 的计数减 1（回溯）。",
            "traps": "必须回溯哈希表！因为一条路径只能严格向下，不能横跨到兄弟节点的子树中去。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix[curr_sum - targetSum]
            prefix[curr_sum] += 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # 回溯：撤销当前节点前缀和
            prefix[curr_sum] -= 1
            return count
            
        return dfs(root, 0)
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "树上前缀和与分支回溯", "detail": "破题眼：将 560 题和为 K 的子数组无缝移植到二叉树上，单向路径做差值查询。", "weight": 25},
            {"dimension": "corner_case", "title": "回溯清理防跨分支污染", "detail": "防守点：离开当前节点时必须 prefix[curr_sum] -= 1，防止右子树查到左子树残留前缀。", "weight": 25},
            {"dimension": "solution", "title": "优雅递归带清理手写", "detail": "手写点：基底 prefix[0]=1 处理整条从根到当前点完全匹配的情况。", "weight": 25},
            {"dimension": "complexity", "title": "暴力双重递归 vs 前缀和时空对比", "detail": "演练点：口述暴力双重递归 O(N^2) 与哈希前缀和 O(N) 性能质的飞跃。", "weight": 25}
        ]
    },
    {
        "frontend_id": 236,
        "title_cn": "二叉树的最近公共祖先",
        "title_en": "Lowest Common Ancestor of a Binary Tree",
        "slug": "lowest-common-ancestor-of-a-binary-tree",
        "difficulty": "Medium",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "后序递归汇聚：若当前节点为空或等于 p 或 q，直接返回当前节点。递归寻找左右子树的返回值 left 和 right。若左右均非空，当前节点即为分叉祖先；若只有一边非空，返回非空的那一边。",
            "traps": "若左右均非空，说明 p 和 q 分布在当前节点的两侧，当前节点必为 LCA。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "后序自底向上信号汇合", "detail": "破题眼：子树往上报发现 p/q 的信号，两路信号在哪个节点首次撞车，该节点就是 LCA。", "weight": 25},
            {"dimension": "corner_case", "title": "自身作为另一节点的祖先", "detail": "防守点：若 p 是 q 的父节点，首次命中 p 直接返回，另一节点自然在 p 的子树中无需深挖。", "weight": 25},
            {"dimension": "solution", "title": "8 行传世经典代码手写", "detail": "手写点：大厂面试出镜率最高的二叉树代码，8 行纯逻辑绝不涂改。", "weight": 25},
            {"dimension": "complexity", "title": "二叉搜索树 LCA 简化版拓展", "detail": "演练点：口述如果在 BST 中，如何利用值大小快速单向二分判断走左还是走右。", "weight": 25}
        ]
    },
    {
        "frontend_id": 124,
        "title_cn": "二叉树中的最大路径和",
        "title_en": "Binary Tree Maximum Path Sum",
        "slug": "binary-tree-maximum-path-sum",
        "difficulty": "Hard",
        "category": "二叉树",
        "day": 3,
        "solution": {
            "core_insight": "后序遍历 + 动态更新全局最大值：每个节点向父节点贡献的最大单边贡献为 `node.val + max(0, left_gain, right_gain)`。若子树贡献为负，果断舍弃（取 0）。而在当前节点拐弯的最大路径和为 `node.val + left_gain + right_gain`，用于更新全局答案。",
            "traps": "子树贡献必须与 0 取 max！如果是负数坚决不往上加；更新全局值时是加上左右两边，返回给父节点时只能选左右其中一条边加自身。",
            "time_complexity": "O(N)",
            "space_complexity": "O(H)",
            "code_python": '''class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 当前节点作为拐点的路径和
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            
            # 返回给父节点的单边最大收益
            return node.val + max(left_gain, right_gain)
            
        max_gain(root)
        return max_sum
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "树上拐点路径与单边贡献分离", "detail": "破题眼：区分向上返回的单分支价值与就地成拱门的双分支价值，负增益断舍离取 0。", "weight": 25},
            {"dimension": "corner_case", "title": "全负数树全局初始值", "detail": "防守点：全局 max_sum 初始化为负无穷，防止树节点全为负数时被 0 错误覆盖。", "weight": 25},
            {"dimension": "solution", "title": "Hard 级递归极品手写", "detail": "手写点：清晰写出 max(gain, 0) 与 nonlocal 全局变量维护，一气呵成。", "weight": 25},
            {"dimension": "complexity", "title": "与 543 题直径问题架构复盘", "detail": "演练点：口述该题就是 543 题直径在带权值且有负数条件下的高级泛化形态。", "weight": 25}
        ]
    },
    {
        "frontend_id": 200,
        "title_cn": "岛屿数量",
        "title_en": "Number of Islands",
        "slug": "number-of-islands",
        "difficulty": "Medium",
        "category": "图论",
        "day": 3,
        "solution": {
            "core_insight": "网格图 DFS/BFS 连通分量：双重循环遍历网格。当遇到 '1' 时，岛屿数 +1，同时以此为起点进行 DFS 扩散，将连通的所有 '1' 原地沉没标记为 '0'（避免使用 visited 数组）。",
            "traps": "网格输入是字符串 '1' 和 '0'，不是整数 1 和 0；原地沉没可省去 O(MN) 的 visited 集合空间。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(M * N) 最坏递归栈",
            "code_python": '''class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # 沉没岛屿
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "沉岛策略与连通块标记", "detail": "破题眼：遇到 1 即启动连通洪泛，把访问过的 1 踩沉成 0，彻底省去额外 visited 表。", "weight": 25},
            {"dimension": "corner_case", "title": "越界与非陆地守门员条件", "detail": "防守点：dfs 首行做边界检查 r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1'。", "weight": 25},
            {"dimension": "solution", "title": "经典网格图 DFS 手写", "detail": "手写点：清晰的四方向递归扩散，5 分钟内稳健写出零 Bug 实现。", "weight": 25},
            {"dimension": "complexity", "title": "并查集并查分治口述", "detail": "演练点：口述如何用并查集（Union-Find）解决动态加点或并行切片岛屿合并场景。", "weight": 25}
        ]
    },
    {
        "frontend_id": 994,
        "title_cn": "腐烂的橘子",
        "title_en": "Rotting Oranges",
        "slug": "rotting-oranges",
        "difficulty": "Medium",
        "category": "图论",
        "day": 3,
        "solution": {
            "core_insight": "多源 BFS：首先将所有初始腐烂的橘子 (val == 2) 同时入队，并统计新鲜橘子总数 fresh。按层扩散，每分钟一轮扩散将四周的新鲜橘子腐烂并入队。若最终 fresh 为 0 返回分钟数，否则返回 -1。",
            "traps": "若初始没有新鲜橘子，直接返回 0；分钟数只在有新鲜橘子被成功腐烂时才自增。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(M * N)",
            "code_python": '''from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
        return minutes if fresh == 0 else -1
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "多源 BFS 齐头并进扩散", "detail": "破题眼：不能单个橘子单独 DFS，所有毒源同时入队，保证按分钟统一同步波浪式推进。", "weight": 25},
            {"dimension": "corner_case", "title": "零新鲜橘子与孤岛死角", "detail": "防守点：初始 fresh == 0 返回 0；队列空后 fresh > 0 返回 -1 说明有橘子永不接触。", "weight": 25},
            {"dimension": "solution", "title": "while q and fresh > 0 刹车手写", "detail": "手写点：循环条件加入 fresh > 0 避免最后一批已无感染却多加一分钟的经典 off-by-one。", "weight": 25},
            {"dimension": "complexity", "title": "时空复杂度严格验证", "detail": "演练点：每个格子最多入队出队一次，时间 O(MN)，空间最多存储全量格坐标 O(MN)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 207,
        "title_cn": "课程表",
        "title_en": "Course Schedule",
        "slug": "course-schedule",
        "difficulty": "Medium",
        "category": "图论",
        "day": 3,
        "solution": {
            "core_insight": "有向图拓扑排序（Kahn 算法 / 入度表）：统计每门课程的入度与邻接表。将所有入度为 0 的节点入队。弹出节点时，已修课程数 +1，并将后续邻接课程的入度减 1，若减为 0 则入队。最终比对修完课程数是否等于 numCourses。",
            "traps": "若有环，环上所有节点的入度永远不可能减为 0，因而不会被遍历到。",
            "time_complexity": "O(V + E)",
            "space_complexity": "O(V + E)",
            "code_python": '''from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = defaultdict(list)
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            in_degree[cur] += 1
            
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_count = 0
        while q:
            course = q.popleft()
            visited_count += 1
            for nxt in adj[course]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        return visited_count == numCourses
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "Kahn 算法入度削减破除死锁", "detail": "破题眼：DAG 拓扑排序基石，从无依赖的 0 入度节点层层剥笋消除边。", "weight": 25},
            {"dimension": "corner_case", "title": "自环与互相依赖死锁", "detail": "防守点：有环节点入度恒无法归零，visited_count < numCourses 精准拦截死锁。", "weight": 25},
            {"dimension": "solution", "title": "标准拓扑排序队列手写", "detail": "手写点：清晰构建 in_degree 数组与 adj 字典，队列出队驱动拓扑排序。", "weight": 25},
            {"dimension": "complexity", "title": "三色标记法 DFS 检测环口述", "detail": "演练点：口述三色标记（0未访、1正在访递归栈中、2已回溯完毕）的 DFS 判环方案。", "weight": 25}
        ]
    },
    {
        "frontend_id": 208,
        "title_cn": "实现 Trie (前缀树)",
        "title_en": "Implement Trie (Prefix Tree)",
        "slug": "implement-trie-prefix-tree",
        "difficulty": "Medium",
        "category": "前缀树",
        "day": 3,
        "solution": {
            "core_insight": "26 叉树或嵌套字典树：每个节点包含 `children` 字典（或长 26 数组）与 `is_end` 标志。插入遍历字符建节点；搜索时全匹配且 `is_end` 为 True；前缀匹配只需前缀字符全部存在即可。",
            "traps": "search 和 startsWith 的唯一区别在于：search 必须要求最后一个节点的 `is_end == True`。",
            "time_complexity": "操作均为 O(L) 字符串长度",
            "space_complexity": "O(Total Chars * Σ)",
            "code_python": '''class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self._find(word)
        return curr is not None and curr.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> Optional[TrieNode]:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "字符前缀共享空间字典树", "detail": "破题眼：多单词公共前缀折叠，每个节点代表一个字符状态，尾节点打标 is_end。", "weight": 25},
            {"dimension": "corner_case", "title": "完整单词与前缀区分", "detail": "防守点：search 必须验 is_end，startsWith 只要节点存在即可，抽出 _find 复用。", "weight": 25},
            {"dimension": "solution", "title": "TrieNode 封装手撕前缀树", "detail": "手写点：提取 _find 辅助方法，使 search 和 startsWith 极简复用，架构优良。", "weight": 25},
            {"dimension": "complexity", "title": "工业级应用与时空论证", "detail": "演练点：口述搜索引擎自动补全、敏感词过滤场景，分析检索耗时严格只与词长 L 相关。", "weight": 25}
        ]
    }
]
