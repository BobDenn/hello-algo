import linked_list


class Linkedlist_Queue:
    """基于链表实现队列"""
    def __init__(self) -> None:
        """构造方法"""
        self._front: linked_list.ListNode | None = None
        self._rear: linked_list.ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        """获取队列的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return not self._front
    
    def push(self, val: int):
        """入队"""
        node = linked_list.ListNode(val)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
    
    def peak(self) -> int:
        """访问队头元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
    
    def pop(self):
        """出队"""
        num = self.peak()
        # 删除头节点
        self._front = self._front.next
        self._size -= 1
        return num
    
    def to_list(self) -> list[int]:
        """通过列表查询队列"""
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue
