class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None
    
    
    def insert_head(self, val: int):
        pass
    
    
    def insert_tail(self, val: int):
        pass
    
    
    def insert_middle(self, val: int):
        pass
    

# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建引用指向
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
# 插入节点

# 遍历链表
# current_node = n0
# while current_node is not None:
#     print(current_node.val, end=' ')
#     current_node = current_node.next

