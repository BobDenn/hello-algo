class MyList:
    """列表类简易实现"""
    def __init__(self) -> None:
        """构造方法"""
        # 列表容量
        self._capacity: int = 10
        # 具体数组
        self._arr: list[int] = [0] * self._capacity
        # 列表长度
        self._size: int = 0
        # 每次列表扩容的倍数
        self._extend_ratio: int = 2

    def size(self) -> int:
        """获取列表长度"""
        return self._size

    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity

    def get(self, index: int) -> int:
        """获取元素"""
        if index < 0 or index > self._size:
            raise IndexError("索引越界")
        return self._arr[index]

    def update(self, index: int, num: int):
        """更新元素"""
        if index < 0 or index > self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def extend_capacity(self):
        """列表扩容"""
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio -1)
        # 更新列表容量
        self._capacity = len(self._arr)
        
    def add(self, num: int):
        """添加元素"""
        if self._size == self._capacity: # 增加判断 实现扩容机制
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, index: int, num: int):
        """插入元素"""
        if index < 0 or index > self._size:
            raise IndexError("索引越界")
        if self._size == self._capacity:
            self.extend_capacity()
        for i in range(self._size -1, index-1, -1):
            self._arr[i+1] = self._arr[i]
        # 把 num 插在 index 处
        self._arr[index] = num
        self._size += 1
    
    def remove(self, index) -> int:
        """删除元素"""
        if index < 0 or index > self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        for i in range(index, self._size -1):
            self._arr[i] = self._arr[i+1]
        # 更新元素数量
        self._size -= 1
        # 返回被删除的元素
        return num
      
    def see_arr(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]
    