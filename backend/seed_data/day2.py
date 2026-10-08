DAY_2_PROBLEMS = [
    {
        "frontend_id": 73,
        "title_cn": "矩阵置零",
        "title_en": "Set Matrix Zeroes",
        "slug": "set-matrix-zeroes",
        "difficulty": "Medium",
        "category": "矩阵",
        "day": 2,
        "solution": {
            "core_insight": "O(1) 额外空间：用矩阵的第 0 行和第 0 列来记录其他行列是否有零。先用两个标记变量记录第 0 行和第 0 列本身是否包含零，再逆序或避开首行列填零。",
            "traps": "更新首行首列的状态会污染尚未读取的标记，因此必须先标记内部，最后处理第 0 行和第 0 列。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "首行首列复用为标记位", "detail": "破题眼：将第 0 行第 0 列作为现成哈希桶，用两个 bool 变量维护首行首列自身命运。", "weight": 25},
            {"dimension": "corner_case", "title": "首行首列状态被提前覆盖", "detail": "防守点：处理内部矩阵后再处理首行首列，防止连环置零扩散导致全盘置零。", "weight": 25},
            {"dimension": "solution", "title": "O(1) 空间三步走手写", "detail": "手写点：先验首行首列、打标内矩阵、依标置零、最后处理首行首列四步曲。", "weight": 25},
            {"dimension": "complexity", "title": "空间降维过程说明", "detail": "演练点：口述从 O(M+N) 辅助数组优化到 O(1) 的逻辑推理。", "weight": 25}
        ]
    },
    {
        "frontend_id": 54,
        "title_cn": "螺旋矩阵",
        "title_en": "Spiral Matrix",
        "slug": "spiral-matrix",
        "difficulty": "Medium",
        "category": "矩阵",
        "day": 2,
        "solution": {
            "core_insight": "设定四个边界：top, bottom, left, right。顺时针按 右->下->左->上 循环遍历，每走完一条边收缩相应边界。当上下或左右越界时终止。",
            "traps": "向左和向上遍历前必须重新检查 top <= bottom 和 left <= right，否则单行或单列矩阵会出现重复读取。",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(1)（返回数组除外）",
            "code_python": '''class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "四边界动态收缩模型", "detail": "破题眼：top/bottom/left/right 四向约束，每完成一行或一列收缩边界。", "weight": 25},
            {"dimension": "corner_case", "title": "单行/单列防止倒行重复", "detail": "防守点：向左走和向上走前显式判断 top <= bottom 与 left <= right，防重复打印。", "weight": 25},
            {"dimension": "solution", "title": "四方向循环经典结构", "detail": "手写点：结构清晰对称，边界加减一毫不含糊。", "weight": 25},
            {"dimension": "complexity", "title": "严格一趟遍历口述", "detail": "演练点：说明所有元素仅访问一次，总时间严格 O(M*N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 48,
        "title_cn": "旋转图像",
        "title_en": "Rotate Image",
        "slug": "rotate-image",
        "difficulty": "Medium",
        "category": "矩阵",
        "day": 2,
        "solution": {
            "core_insight": "顺时针旋转 90 度 = 主对角线翻转 (转置) + 逐行左右对称反转。两步均可直接原地就地完成，极难写错。",
            "traps": "对角线转置时 j 的范围必须是 range(i, n)，若写成 range(n) 会翻两次导致复原。",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # 1. 沿主对角线转置
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 2. 左右镜像反转每一行
        for i in range(n):
            matrix[i].reverse()
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "转置加反转代替四角循环", "detail": "破题眼：几何矩阵分解定理，顺时针 90° = 转置 + 左右镜像，代码极简。", "weight": 25},
            {"dimension": "corner_case", "title": "转置遍历范围防二次翻转", "detail": "防守点：内层循环严控 j >= i，防止元素交换两次抵消回到原点。", "weight": 25},
            {"dimension": "solution", "title": "原地操作纯净手写", "detail": "手写点：不到 10 行的原地变换代码，无需推导复杂的四角轮换下标公式。", "weight": 25},
            {"dimension": "complexity", "title": "几何变换推广说明", "detail": "演练点：口述如何通过类似组合实现逆时针旋转 90°（副对角线转置或水平翻转+转置）。", "weight": 25}
        ]
    },
    {
        "frontend_id": 240,
        "title_cn": "搜索二维矩阵 II",
        "title_en": "Search a 2D Matrix II",
        "slug": "search-a-2d-matrix-ii",
        "difficulty": "Medium",
        "category": "矩阵",
        "day": 2,
        "solution": {
            "core_insight": "从右上角 (0, n-1) 出发视为二叉搜索树根节点：当前值 > target 则向左移动 (col -= 1)；当前值 < target 则向下移动 (row += 1)。",
            "traps": "不能从左上角或右下角出发，因为左上角往右和往下都是增大，没有确定单调方向。",
            "time_complexity": "O(M + N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "右上角 BST 决策树模型", "detail": "破题眼：立足右上角，左小下大，具备完美二分单调决策性。", "weight": 25},
            {"dimension": "corner_case", "title": "越界退出判定", "detail": "防守点：row < m and col >= 0 边界守门员，处理 target 小于全矩阵或大于全矩阵。", "weight": 25},
            {"dimension": "solution", "title": "O(M+N) 线性爬楼梯手写", "detail": "手写点：10 行内写出精简 while 循环，三分支比对。", "weight": 25},
            {"dimension": "complexity", "title": "为何左上角不行", "detail": "演练点：清晰向面试官解释为什么必须选右上角或左下角作为起点（分支单调性）。", "weight": 25}
        ]
    },
    {
        "frontend_id": 160,
        "title_cn": "相交链表",
        "title_en": "Intersection of Two Linked Lists",
        "slug": "intersection-of-two-linked-lists",
        "difficulty": "Easy",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "浪漫双指针：指针 pA 走完 A 转去走 B，pB 走完 B 转去走 A。两者总路程都为 a + c + b，若有交点必在交点相遇；若无交点同时停在 None。",
            "traps": "循环退出条件是 pA == pB，不需要额外统计链表长度。",
            "time_complexity": "O(M + N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "消除长度差双指针走两趟", "detail": "破题眼：A+B 路径对等原理，两指针走过相同总步数必在交点或尾部 None 相逢。", "weight": 25},
            {"dimension": "corner_case", "title": "不相交情况安全退出", "detail": "防守点：两链表无交点时，各走完两轮后 pA == pB == None，自然退出并返回 None。", "weight": 25},
            {"dimension": "solution", "title": "4 行核心循环手写", "detail": "手写点：极为精巧优雅，不用预先扫描链表长度与差值对齐。", "weight": 25},
            {"dimension": "complexity", "title": "时空严格论证", "detail": "演练点：口述每个指针最多走 M+N 步，空间消耗恒为 O(1)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 206,
        "title_cn": "反转链表",
        "title_en": "Reverse Linked List",
        "slug": "reverse-linked-list",
        "difficulty": "Easy",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "双指针迭代：prev 初始化为 None，curr 为 head。循环中先暂存 nxt = curr.next，再让 curr.next = prev，随后将 prev 与 curr 齐步前移。",
            "traps": "先存后断！不要先改指针导致后面的链表丢失。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "链表断链与双指针后移", "detail": "破题眼：经典 prev/curr/nxt 三元指针推进，单向指针原地反转。", "weight": 25},
            {"dimension": "corner_case", "title": "空节点与单节点安全", "detail": "防守点：head 为 None 或单节点时正确返回 prev，不产生 NullPointer 异常。", "weight": 25},
            {"dimension": "solution", "title": "迭代解法无缝手写", "detail": "手写点：1 分钟内闭着眼睛 Bug-free 默写，这是大厂一面必考基本功。", "weight": 25},
            {"dimension": "complexity", "title": "递归反转深度与栈溢出口述", "detail": "演练点：口述递归反转的逻辑，并指出递归有 O(N) 栈深，工程中推荐迭代。", "weight": 25}
        ]
    },
    {
        "frontend_id": 234,
        "title_cn": "回文链表",
        "title_en": "Palindrome Linked List",
        "slug": "palindrome-linked-list",
        "difficulty": "Easy",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "1. 快慢指针找链表中点；2. 反转后半段链表；3. 双指针从两端向中间同步比对；4. （可选）恢复链表。空间复杂度 O(1)。",
            "traps": "奇偶长度对齐：fast.next 和 fast.next.next 的终止判定；比较时只认后半段结束即可。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 反转后半部分
        prev = None
        curr = slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 比对前后两半
        p1, p2 = head, prev
        res = True
        while res and p2:
            if p1.val != p2.val:
                res = False
            p1 = p1.next
            p2 = p2.next
        return res
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "快慢指针中点 + 链表反转组合拳", "detail": "破题眼：将链表题三大基本操作（快慢找中、就地反转、双向比对）完美串联。", "weight": 25},
            {"dimension": "corner_case", "title": "奇偶长度平分界限", "detail": "防守点：使用 fast.next and fast.next.next 准确定位前半分段末尾。", "weight": 25},
            {"dimension": "solution", "title": "严格 O(1) 空间就地校验手写", "detail": "手写点：不转化为数组/列表，纯指针操作完成回文校验。", "weight": 25},
            {"dimension": "complexity", "title": "还原链表的工程素养说明", "detail": "演练点：主动向面试官提及在工业界并发场景下，应把后半段反转回去以保护输入数据结构。", "weight": 25}
        ]
    },
    {
        "frontend_id": 141,
        "title_cn": "环形链表",
        "title_en": "Linked List Cycle",
        "slug": "linked-list-cycle",
        "difficulty": "Easy",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "快慢指针（Floyd 判圈算法）：slow 每次走 1 步，fast 每次走 2 步。若链表有环，快指针一定会在环内套圈追上慢指针。",
            "traps": "while 循环条件必须同时判断 fast 和 fast.next 是否存在。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "Floyd 龟兔赛跑判圈", "detail": "破题眼：利用相对速度为 1 的快慢指针在封闭环内必定追及相遇。", "weight": 25},
            {"dimension": "corner_case", "title": "空链表与单节点无环", "detail": "防守点：fast and fast.next 双保险防止对 None 取 next 抛异常。", "weight": 25},
            {"dimension": "solution", "title": "6 行标准模板默写", "detail": "手写点：快慢指针经典起手式，干净利落。", "weight": 25},
            {"dimension": "complexity", "title": "追及步数数学论证", "detail": "演练点：口述慢指针入环后，快指针在 1 圈之内必定追上，时间必为 O(N)。", "weight": 25}
        ]
    },
    {
        "frontend_id": 142,
        "title_cn": "环形链表 II",
        "title_en": "Linked List Cycle II",
        "slug": "linked-list-cycle-ii",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "数学推导：设头到入环点距离 a，入环点到相遇点 b，环剩余长 c。快指针路程 a + n(b+c) + b = 2(a+b)，得 a = c + (n-1)(b+c)。相遇后让一个指针回到 head，两指针每次各走 1 步，再次相遇点即为入环点。",
            "traps": "找到相遇点后切忌直接返回相遇点，必须让一指针重回 head 单步走。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "相遇点重置单步推演", "detail": "破题眼：数学公式推导 a = (n-1)L + c，从头走与从相遇点走必然在环入口碰头。", "weight": 25},
            {"dimension": "corner_case", "title": "无环场景早退", "detail": "防守点：如果 fast 走到尽头则无环，安全返回 None。", "weight": 25},
            {"dimension": "solution", "title": "双阶段循环结构手写", "detail": "手写点：先找到相遇点，再起第二重单步同步移动循环，逻辑层次清晰。", "weight": 25},
            {"dimension": "complexity", "title": "白板推导公式演示", "detail": "演练点：能熟练在白板上画出 a, b, c 并写出等式 2(a+b) = a+b+k*L 给面试官看。", "weight": 25}
        ]
    },
    {
        "frontend_id": 21,
        "title_cn": "合并两个有序链表",
        "title_en": "Merge Two Sorted Lists",
        "slug": "merge-two-sorted-lists",
        "difficulty": "Easy",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "哑节点（Dummy Head）：创建 dummy 节点，比较 l1 与 l2 的当前值，较小的接在 curr 后面，然后指针推进。循环结束后将剩余未空的链表直接挂到末尾。",
            "traps": "剩余部分只需一行 `curr.next = l1 or l2`，无需再写 while 循环遍历。",
            "time_complexity": "O(M + N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "哨兵哑节点规范头节点", "detail": "破题眼：使用 dummy = ListNode(-1) 避免对空头节点的繁琐特判。", "weight": 25},
            {"dimension": "corner_case", "title": "某链表率先耗尽", "detail": "防守点：curr.next = list1 or list2 一行完成非空剩余链表的挂载。", "weight": 25},
            {"dimension": "solution", "title": "标准双指针归并链表手写", "detail": "手写点：清晰易读，变量更新无缝隙，10 行搞定。", "weight": 25},
            {"dimension": "complexity", "title": "迭代 vs 递归开销分析", "detail": "演练点：口述迭代 O(1) 空间相比递归版本避免了栈溢出，在生产环境中更稳定。", "weight": 25}
        ]
    },
    {
        "frontend_id": 2,
        "title_cn": "两数相加",
        "title_en": "Add Two Numbers",
        "slug": "add-two-numbers",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "链表逆序排列刚好对应低位到高位。用 dummy 节点维护新链表，维护 carry 进位值。循环条件为 l1 或 l2 或 carry 不为 0。",
            "traps": "最高位产生的进位容易被遗忘，循环条件加上 `or carry` 即可完美统一处理。",
            "time_complexity": "O(max(M, N))",
            "space_complexity": "O(1)（返回链表除外）",
            "code_python": '''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "大数高精度逐位加法模拟", "detail": "破题眼：逆序存储天然契合竖式加法，carry 充当跨位连接器。", "weight": 25},
            {"dimension": "corner_case", "title": "最高位余数进位节点补充", "detail": "防守点：while l1 or l2 or carry 确保最高位进位 1 能正确生成新节点。", "weight": 25},
            {"dimension": "solution", "title": "优雅处理长度不一链表", "detail": "手写点：使用 val = l.val if l else 0 规避多次 if 判断，代码高度对称。", "weight": 25},
            {"dimension": "complexity", "title": "若链表正序存储如何处理", "detail": "演练点：扩展口述如果题目改成正序存储，如何使用双栈或先反转再相加。", "weight": 25}
        ]
    },
    {
        "frontend_id": 19,
        "title_cn": "删除链表的倒数第 N 个结点",
        "title_en": "Remove Nth Node From End of List",
        "slug": "remove-nth-node-from-end-of-list",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "前驱节点与定距双指针：dummy 节点指向 head。fast 指针先走 n 步，然后 fast 和 slow 同时前移，当 fast 到达最后一个节点时，slow 刚好停在待删节点的前驱。",
            "traps": "删除头节点的场景很多新手会漏掉，通过引入 dummy 节点让头节点与普通节点逻辑完全一致。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "尺子双指针保持 n 步间距", "detail": "破题眼：先走 n 步固定窗宽，同步移动定位待删节点的前一个节点。", "weight": 25},
            {"dimension": "corner_case", "title": "删除第一个头结点特判", "detail": "防守点：dummy 节点的引入使得删除头节点操作退化为普通删除，无任何特判。", "weight": 25},
            {"dimension": "solution", "title": "fast.next 停在链尾手写", "detail": "手写点：利用 while fast.next 使 slow 停在前驱节点，直接 slow.next = slow.next.next。", "weight": 25},
            {"dimension": "complexity", "title": "一趟扫描严格性验证", "detail": "演练点：口述仅需一趟扫描完成删除，时间 O(N)，无需先扫长度再扫二遍。", "weight": 25}
        ]
    },
    {
        "frontend_id": 24,
        "title_cn": "两两交换链表中的节点",
        "title_en": "Swap Nodes in Pairs",
        "slug": "swap-nodes-in-pairs",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "哨兵节点 dummy。每次迭代考虑 dummy/prev 之后的两个节点 node1 和 node2。交换步骤：prev.next = node2; node1.next = node2.next; node2.next = node1; prev = node1。",
            "traps": "指针断链顺序必须严格注意，先让 node1 指向 node2.next，防止后序链表失联。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            curr.next = node2
            node1.next = node2.next
            node2.next = node1
            curr = node1
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "局部两两交换微观拓扑", "detail": "破题眼：锁定 curr.next 与 curr.next.next，四条指针重连闭环。", "weight": 25},
            {"dimension": "corner_case", "title": "奇数个节点末尾不交换", "detail": "防守点：while curr.next and curr.next.next 确保偶数对才进循环，奇数末尾安然不动。", "weight": 25},
            {"dimension": "solution", "title": "顺序无死角手写", "detail": "手写点：明确 node1/node2 临时变量命名，交换后 curr 移动到 node1。", "weight": 25},
            {"dimension": "complexity", "title": "与 K 个一组翻转的共性口述", "detail": "演练点：指出两两交换实质上就是 k=2 时的 Reverse Nodes in k-Group 特例。", "weight": 25}
        ]
    },
    {
        "frontend_id": 25,
        "title_cn": "K 个一组翻转链表",
        "title_en": "Reverse Nodes in k-Group",
        "slug": "reverse-nodes-in-k-group",
        "difficulty": "Hard",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "分段探测与局部反转：dummy 节点。用 group_end 向前探查 k 步，若不足 k 步直接结束。若足 k 步，切断后序连接，翻转这一段子链表，拼接首尾，推进 group_prev。",
            "traps": "翻转后原先的 group_start 变成了这一段的尾巴，它的 next 需要连接到下一组的开头。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "code_python": '''class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        def reverse(start: ListNode, end: ListNode):
            prev = None
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            start = group_prev.next
            # 翻转 [start, group_next)
            new_head = reverse(start, group_next)
            group_prev.next = new_head
            start.next = group_next
            group_prev = start
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "区间探查与分块反转", "detail": "破题眼：先走 k 步探路，不足则保留，足额则局部反转，重新缝合首尾。", "weight": 25},
            {"dimension": "corner_case", "title": "尾部不足 k 个节点保持原序", "detail": "防守点：探路时 if not kth: return dummy.next 精准刹车。", "weight": 25},
            {"dimension": "solution", "title": "开闭区间反转辅助函数手写", "detail": "手写点：写出左闭右开区间反转模板，缝合逻辑干净无死循环。", "weight": 25},
            {"dimension": "complexity", "title": "大厂面试常客白板推演", "detail": "演练点：口述每组遍历两遍（探路+反转），时间仍为 O(2N) = O(N)，原地 O(1) 空间。", "weight": 25}
        ]
    },
    {
        "frontend_id": 138,
        "title_cn": "随机链表的复制",
        "title_en": "Copy List with Random Pointer",
        "slug": "copy-list-with-random-pointer",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "原地拆分穿插法（O(1) 空间）：1. 在每个原节点后复制一个新节点；2. 设置新节点的 random：curr.next.random = curr.random.next；3. 将交织的链表拆分成原链表与新链表。",
            "traps": "设置 random 时必须判断 curr.random 是否为空；拆分链表时必须将原链表的 next 完整还原，否则原结构被破坏报错。",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)（哈希表法为 O(N)）",
            "code_python": '''class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 1. 复制每个节点并插入原节点后
        curr = head
        while curr:
            copy = Node(curr.val, curr.next, None)
            curr.next = copy
            curr = copy.next
            
        # 2. 设置 copy 节点的 random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # 3. 拆分链表
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "节点克隆就地穿插", "detail": "破题眼：A -> A' -> B -> B'，利用新旧节点相邻关系免去 O(N) 哈希映射表。", "weight": 25},
            {"dimension": "corner_case", "title": "random 为 None 与链表解绑", "detail": "防守点：curr.random 为空防空指针；拆分时必须还原原链表，不破坏原有数据结构。", "weight": 25},
            {"dimension": "solution", "title": "三遍遍历穿插手写", "detail": "手写点：构建克隆、连接 random、解绑分离三个 while 循环层次分明。", "weight": 25},
            {"dimension": "complexity", "title": "哈希法 vs 原地穿插法对比", "detail": "演练点：口述哈希字典法 O(N) 空间与原地穿插法 O(1) 空间在面试中的进阶回答。", "weight": 25}
        ]
    },
    {
        "frontend_id": 148,
        "title_cn": "排序链表",
        "title_en": "Sort List",
        "slug": "sort-list",
        "difficulty": "Medium",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "自顶向下归并排序：1. 快慢指针找中点（截断链表为两截）；2. 递归排序左半段与右半段；3. 双指针合并两个有序链表。",
            "traps": "找中点时必须将前半段末尾的 next 断开（slow.next = None），否则递归永不终止死循环。",
            "time_complexity": "O(N log N)",
            "space_complexity": "O(log N) 递归栈",
            "code_python": '''class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 快慢指针找中点前驱
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None  # 彻底断开
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并两个有序链表
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "链表分治与归并排序", "detail": "破题眼：链表天然适合归并排序，合并仅需修改指针，无需额外搬运数组。", "weight": 25},
            {"dimension": "corner_case", "title": "快慢指针切断链表中点", "detail": "防守点：fast = head.next 保证偶数长度停在前半段末尾，显式 slow.next = None。", "weight": 25},
            {"dimension": "solution", "title": "分治归并模板集成手写", "detail": "手写点：二分切断、递归下降、有序合并三合一，逻辑严密。", "weight": 25},
            {"dimension": "complexity", "title": "自底向上自适应步长扩展", "detail": "演练点：口述如何通过自底向上步长翻倍（step=1,2,4...）做到极致 O(1) 空间复杂度。", "weight": 25}
        ]
    },
    {
        "frontend_id": 23,
        "title_cn": "合并 K 个升序链表",
        "title_en": "Merge k Sorted Lists",
        "slug": "merge-k-sorted-lists",
        "difficulty": "Hard",
        "category": "链表",
        "day": 2,
        "solution": {
            "core_insight": "最小堆（优先队列）：将 k 个链表的头节点压入小顶堆。每次取出堆顶最小节点接入新链表，再将该节点的 next 节点入堆。堆大小始终不超过 k。",
            "traps": "Python heapq 比较时若 val 相等会比较 ListNode，导致 TypeError。可存入三元组 `(node.val, i, node)` 避免比较 ListNode。",
            "time_complexity": "O(N log K)",
            "space_complexity": "O(K)",
            "code_python": '''import heapq

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "多路归并与容量 K 最小堆", "detail": "破题眼：维持大小为 k 的小顶堆，每次弹出全局最小值，弹一个补一个。", "weight": 25},
            {"dimension": "corner_case", "title": "元组唯一性破除比较冲突", "detail": "防守点：存 (node.val, i, node) 用下标 i 作为二级比较项，防止 Python 对象抛错。", "weight": 25},
            {"dimension": "solution", "title": "heapq 极简多路归并手写", "detail": "手写点：15 行内写出标准优先队列多路归并解，熟练无死角。", "weight": 25},
            {"dimension": "complexity", "title": "分治两两合并法对比", "detail": "演练点：口述两两分治合并（类似归并排序树）同样为 O(N log K) 且 O(1) 空间开销。", "weight": 25}
        ]
    },
    {
        "frontend_id": 146,
        "title_cn": "LRU 缓存",
        "title_en": "LRU Cache",
        "slug": "lru-cache",
        "difficulty": "Medium",
        "category": "哈希表",
        "day": 2,
        "solution": {
            "core_insight": "哈希表 + 双向链表（带伪头和伪尾节点）。哈希表实现 O(1) 查找；双向链表实现 O(1) 节点删除并移至头部。容量超出时淘汰伪尾前驱节点。",
            "traps": "更新 key 时不仅要更新 value，还要将其移到表头（标记为最近使用）；从双向链表中移除节点时两端指针都要修好。",
            "time_complexity": "get 和 put 均为 O(1)",
            "space_complexity": "O(capacity)",
            "code_python": '''class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            if len(self.cache) > self.capacity:
                removed = self.tail.prev
                self._remove_node(removed)
                del self.cache[removed.key]
'''
        },
        "checkpoints": [
            {"dimension": "pattern", "title": "哈希定位与双向链表 O(1) 移位", "detail": "破题眼：字典解决寻找，双向链表解决 O(1) 任意位置删除与插入。", "weight": 25},
            {"dimension": "corner_case", "title": "伪头伪尾哨兵节点保护", "detail": "防守点：使用 head/tail 哑节点消除头尾变动时的判空边界代码。", "weight": 25},
            {"dimension": "solution", "title": "手撕完整双向链表类", "detail": "手写点：不依赖 OrderedDict，从零手写 _remove_node 和 _add_to_head 核心原子操作。", "weight": 25},
            {"dimension": "complexity", "title": "大厂架构与高并发并发拓展", "detail": "演练点：口述若要在多线程环境下实现 LRU，如何使用读写锁或分段锁减小锁粒度。", "weight": 25}
        ]
    }
]
