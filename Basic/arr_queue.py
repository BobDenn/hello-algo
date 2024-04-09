class ArrQueue:
    """基于环形数组实现的队列"""
    def __init__(self, size: int) -> None:
        """构造方法"""
        self._nums: list[int] = [0] * size
        # 队首索引
        self._front: int = 0
        self._size: int = 0
    
    def capacity(self) -> int:
        """获取容量信息"""
        return len(self._nums)
    
    def size(self) -> int:
        """获取长度信息"""
        return self._size
    
    def peak(self) -> int:
        """查询队首元素"""
        if self._size == 0:
            raise IndexError("队列为空")
        return self._nums[self._front]
    
    def push(self, val: int):
        """入队"""
        if self._size == self.capacity():
            raise IndexError("队列已满")
        rear: int = (self._front + self._size) % self.capacity()
        # 将 val 插入队尾
        self._nums[rear] = val
        self._size += 1
        
    def pop(self):
        """出队"""
        num = self.peak()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    def to_list(self) -> list[int]:
        """遍历"""
        res = [0] * self._size
        j: int = self._front
        for i in range(self._size):
            res[i] = self._nums[j % self.capacity()]
            j += 1
        return res
