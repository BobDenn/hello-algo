# 给定某节点, 获取它的值/左右子节点/父节点
# 获取前序遍历/中序遍历/后序遍历/层序遍历序列


class ArryBinaryTree:
    """数组二叉树"""
    def __init__(self, arr: list[int | None]) -> None:
        self._tree = list(arr) # 转换成元组 ?

    
