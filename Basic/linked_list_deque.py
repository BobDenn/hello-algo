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
    
    
