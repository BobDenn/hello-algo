class ListNode:
    """双向列表节点"""
    def __init__(self, val: int) -> None:
        self.prev: ListNode | None = None # previous node
        self.val: int = val
        self.next: ListNode | None = None # next node
        

class LinkedListDeque:
    """base on double linked_list"""
    pass
