class ListNode:
    """双向列表节点"""
    def __init__(self, val: int) -> None:
        self.prev: ListNode | None = None # previous node
        self.val: int = val
        self.next: ListNode | None = None # next node
        

class LinkedListDeque:
    """base on double linked_list"""
    def __init__(self) -> None:
        self._front: ListNode | None = None # head node
        self._rear: ListNode | None = None # rear node
        self._size: int = 0 # queue's length
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def peek_front(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._front.val
    
    def peek_rear(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._rear.val
    
    def push(self, val: int, is_front: bool):
        """in deque"""
        node = ListNode(val)
        # 若链表为空 头节点和尾节点 都指向 node
        if self.is_empty():
            self._front = self._rear = node
        elif is_front:
            self._front.prev = node
            node.next = self._front
            self._front = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, val: int):
        """队首入队"""
        self.push(val, True)
    
    def push_last(self, val: int):
        """队尾入队"""
        self.push(val, False)

    def pop(self, is_front: bool):
        """出队"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        if is_front:
            # 暂存头节点
            val: int = self._front.val
            fnext: ListNode | None = self._front.next
            if fnext != None:
                fnext.prev = None
                self._front.next = None
            self._front = fnext
        else:
            val: int = self._rear.val
            rprev: ListNode | None = self._rear.prev
            if rprev != None:
                rprev.next = None
                self._rear.prev = None
            self._rear = rprev
        self._size -= 1
        return val

    def pop_first(self) -> int:
        """队首出队"""
        return self.pop(True)

    def pop_last(self) -> int:
        """队尾出队"""
        return self.pop(False)
    
    def to_list(self) -> list[int]:
        res = [0] * self.size()
        node = self._front
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res
