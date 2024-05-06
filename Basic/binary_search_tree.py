class TreeNode:
    """二叉树类节点"""
    def __init__(self, val) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self, root: TreeNode) -> None:
        self._root: TreeNode = root

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur = self._root
        # 循环查找, 越过叶节点跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            # 目标节点在 cur 的左子树中
            elif cur.val > num:
                cur = cur.left
            # 找到就跳出循环
            else:
                break
        # 返回搜索到的值
        return cur

    def insert(self, num:int):
        """插入节点"""
        # 若树为空, 则初始化根节点
        if self._root is None:
            self._root = TreeNode(num)
            return
        # 循环查找, 越过叶节点后跳出
        cur, pre = self._root, None
        while cur is not None:
            # 如果找到重复节点, 直接返回
            if num == cur.val:
                return
            pre = cur
            # 插入位置在cur的右子树中
            if num > cur.val:
                cur = cur.right
            # 插入位置在cur的左子树中
            else:
                cur = cur.left
        # 插入节点
        node = TreeNode(num)
        if num < pre.val:
            pre.left = node
        else:
            pre.right = node
            
    def remove(self, num: int):
        """ 删除节点 """
        # 若树为空, 直接提前返回
        if self._root is None:
            return
        # 循环查找, 越过叶节点后跳出
        cur, Pre = self._root, None
        while cur is not None:
            # 找到待删除节点, 跳出循环
            if cur.val == num:
                break
            pre = cur
            # 待删除节点在cur的右子树中
            if cur.val < num:
                cur = cur.right
            # 待删除节点在cur的左子树中
            else:
                cur = cur.left
        # 若无待删除节点, 则直接返回
        if cur is None:
            return
        # 子节点数量 = 0 / 1
        if cur.left is None or cur.right is None:
            # 当子节点数量

