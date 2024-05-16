class Avl_tree:
    """平衡二叉树"""
    class node:
        """AVL 树节点类""" 
        def __init__(self, val: int) -> None:
            self.val = val
            self.height = 0
            self.left = None
            self.right = None
            
    def __init__(self) -> None:
        self._root = None
    
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
        node.height = max(self.height(self.node.left),
                          self.height(self.node.right)) + 1
        
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

    def rotate(self, node: "Avl_tree.node" | None):
        """针对不同情况, 进行旋转操作, 使该子树重新恢复平衡"""
        factor = self.balance_factor(node)
        # 左偏树
        if factor > 1:
            if self.balance_factor(node.left) >= 0:
                # 右旋 
                return self.right_rotate(node)
            else:
                # 先左旋后右旋
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 右偏树        
        elif factor < -1:
            if self.balance_factor(node.right) <= 0:
                # 左旋
                return self.left_rotate(node)
            else:
                # 先右旋后左旋
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        # 平衡树, 无需旋转, 直接返回
        return node

    def insert(self, val):
        """插入节点"""
        self._root = self.insert_helper(self._root, val)
    
    def insert_helper(self, node: "Avl_tree.node", val: int):
        """辅助插入"""
        if node is None:
            return Avl_tree.node(val)
        # 查找位置, 插入节点
        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)    
        else:
            # 重复节点不插入 直接返回
            return node
        # 别忘了更新节点高度
        self.update_height(node)
        return self.rotate(node)

    def remove(self, val: int):
        """删除节点"""
        self._root = self.remove_helper(self._root, val)
    
    def remove_helper(self, node: "Avl_tree.node" | None, val:int) -> "Avl_tree.node" | None:
        """辅助删除"""
        if node is None:
            return None
        # 开始递归删除并更新
        if val < node.val:
            node.left = self.remove_helper(node.left, val)         
        elif val > node.val:
            node.right = self.remove_helper(node.right, val)
        else:
            if node.left is None or node.right is None:
                child = node.left or node.right
                if child is None:
                    return None
                else:
                    node = child
            else:
                # 子节点数量
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.right = self.remove_helper(node.right, temp.val)
                node.val = temp.val
        # 更新节点高度
        self.update_height(node)
        # 2. 执行旋转操作，使该子树重新恢复平衡
        return self.rotate(node)     
                       