class TreeNode:
    """二叉树类节点"""
    def __init__(self, val) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self, root) -> None:
        self._root: TreeNode = root


def search(self, num: int) -> TreeNode | None:
    """查找节点"""
    cur = BinarySearchTree._root
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

