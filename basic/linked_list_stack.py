import linked_list


class LinkedListStack:
    """基于链表实现的栈"""
    def __init__(self) -> None:
        self._peak: linked_list.ListNode | None = None
        self._size: int = 0
    
    def size(self):
        """获取栈的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return not self._peak
    
    def push(self, val: int):
        """入栈"""
        node = linked_list.ListNode(val)
        node.next = self._peak
        # 栈顶的next指向当前栈顶
        self._peak = node
        self._size += 1
    
    def peak(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peak.val
    
    def pop(self) -> int:
        """出栈"""
        num = self._peak()
        self._peak = self._peak.next
        return num
