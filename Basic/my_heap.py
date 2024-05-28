class my_heap:
    """自己实现一个大顶堆的类"""
    def __init__(self, max_heap: list[int]) -> None:
        self.max_heap = max_heap
        self.size: int = len(max_heap)
        self.is_empty = not max_heap
        for i in range(self.father(self.size - 1), -1, -1):
            self.sift_down(i)
    
    def left_son(self, i: int) -> int:
        return 2 * i + 1
    
    def right_son(self, i: int) -> int:
        return 2 * i + 2
    
    def father(self, i: int) -> int:
        return (i - 1) // 2

    def peek(self) -> int:
        return self.max_heap[0]
    
    def push(self, val: int):
        """元素入堆"""
        self.max_heap.append(val)
        self.sift_up(self.size - 1)
        
    def swap(self, i: int, j: int):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]
        
    def sift_up(self, i: int):
        """从节点i开始, 从底至顶堆化"""
        while i > 0:
            # 获取节点i的父节点
            p = self.father(i)
            if self.max_heap[i] <= self.max_heap[p]:
                break
            # 否则交换两节点
            self.swap(i, p)
            # 循环向上堆化
            i = p
    
    def sift_down(self, i: int):
        """从节点i开始, 从顶至底堆化"""
        while True:
            # 判断节点 i,l,r中最大的节点, 记为ma
            l, r, ma = self.left_son(i), self.right_son(i), i
            if l < self.size and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            if ma == i:
                break
            # 交换两节点
            self.swap(i, ma)
            # 循环向下堆化
            i = ma
    
    def pop(self) -> int:
        """元素出堆"""
        if self.is_empty:
            raise IndexError("堆为空")
        self.swap(0, self.size - 1)
        # 删除节点
        val = self.max_heap.pop()
        self.size -= 1
        self.sift_down(0)
        return val    
    