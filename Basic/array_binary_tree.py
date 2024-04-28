# 给定某节点, 获取它的值/左右子节点/父节点
# 获取前序遍历/中序遍历/后序遍历/层序遍历序列


class ArrayBinaryTree:
    """数组二叉树"""
    def __init__(self, arr: list[int | None]) -> None:
        self._tree = list(arr) # 转换成元组 ? A: 函数list()

    def size(self):
        """节点数量"""
        return len(self._tree)
    
    def val(self, i: int) -> int:
        """获取索引为 i 节点的值"""
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]
    
    def left(self, i: int) -> int | None:
        """ 获取索引为i节点的左子节点的索引 """
        return 2 * i + 1
    
    def right(self, i: int) -> int | None:
        """ 获取索引为 i 节点的右子节点的索引 """
        return 2 * i + 2
    
    def parent(self, i: int) -> int | None:
        """ 获取索引为 i 节点的父节点的索引 """
        return (i - 1) // 2 # 取整数部分
    
    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    
    def dfs(self, i: int, order: str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == 'pre':
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        if order == 'in':
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        if order == 'post':
            self.res.append(self.val(i))
    
    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []        
        self.dfs(0, order='pre')
        return self.res
    
    def in_order(self):
        """中序遍历"""
        self.res = []
        self.dfs(0, order="in")
        return self.res
    
    def post_order(self):
        self.res = []
        self.dfs(0, order="post")
        return self.res
