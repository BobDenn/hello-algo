class TreeNode:
    """二叉树类节点"""
    def __init__(self, val) -> None:
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        
    

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
    