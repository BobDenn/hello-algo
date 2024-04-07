class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None

class LinkList:
    """链表实例"""
    def __init__(self) -> None:
        self.head = None

    def insert_head(n: ListNode, val: int) -> ListNode:
        new_node = ListNode(val)
        new_node.next = n
        return new_node
    
    def insert_tail(self) -> ListNode:
        pass
    
    def insert_middle(self) -> ListNode:
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
new_n0 = LinkList.insert_head(n0, 9)
# 遍历链表
current_node = new_n0
values = []
while current_node is not None:
    values.append(current_node.val)
    current_node = current_node.next
print(f"链表中有{values}")
