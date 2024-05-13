class Avl_tree:
    """平衡二叉树"""
    class node:
        """AVL 树节点类""" 
        def __init__(self, val: int) -> None:
            self.val = val
            self.height = 0
            self.left = None
            self.right = None
    
    def height(node: "Avl_tree.node") -> int:
        """获取节点高度"""
        # 增加判断是否为空
        if node is not None:
            return node.height
        else:
            return -1

    def update_height(self, node: "Avl_tree.node" | None):
        """更新节点高度"""
        # 节点高度 = 最高子树 + 1
        node.height = max([self.height(self.node.left)],
                          [self.height(self.node.right)]) + 1
        
    def balance_factor(self, node: "Avl_tree.node" | None) -> int:
        """获取平衡因子"""
        # 空节点就是 0
        if node is None:
            return 0
        # 节点平衡因子 = 左子树 - 右子树
        return self.height(node.left) - self.height(node.right)
        
    def right_rotate(self, node: "Avl_tree.node" | None) -> node | None:
        """node中存放失衡节点, 右旋操作"""
        child = node.left
        grand_child = child.right
        # 以child为原点, 将node向右旋转
        child.right = node
        node.left = grand_child
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)
        return child

    def left_rotate(self, node: "Avl_tree.node" | None) -> node | None:
        """node中存放失衡节点, 左旋操作"""
        child = node.right
        grand_child = child.left
        # 以child为原点, 将node旋转
        child.left = node
        node.right = grand_child
        # 更新节点高度
        self.update_height(node)
        self.update_height(child)
        return child

