class Avl_tree:
    """平衡二叉树"""
    class Treenode:
        """AVL 树节点类""" 
        def __init__(self, val: int) -> None:
            self.val = val
            self.height = 0
            self.left = None
            self.right = None
    
    @staticmethod
    def height(node: Treenode | None) -> int:
        """获取节点高度"""
        # 增加判断是否为空
        if node is not None:
            return node.height
        return -1

    def update_height(self, node: Treenode | None):
        """更新节点高度"""
        # 节点高度 = 最高子树 + 1
        node.height = max([self.height(self.left)],
                          [self.height(self.right)]) + 1
        
    def balance_factor(self, node) -> int:
        """获取平衡因子"""
        # 空节点就是 0
        if node is None:
            return 0
        # 节点平衡因子 = 左子树 - 右子树
        return self.height(node.left) - self.height(node.right)
        
