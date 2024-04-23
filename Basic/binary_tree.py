import collections as col


class TreeNode:
    """二叉树类节点"""
    def __init__(self, val) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    # 初始化队列, 加入根节点
    queue: col.deque[TreeNode] = col.deque()
    queue.append(root)
    # 保存结果
    res = []
    while queue:
        node: TreeNode = queue.popleft() # 队列出队
        res.append(node.val) # 保存节点值
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right) # 从左往右节点入队
    return res # 返回结果


if __name__ == "__main__":
    # 初始化二叉树
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(level_order(n1))
