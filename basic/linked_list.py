class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None

class LinkList:
    """链表实例"""
    def __init__(self) -> None:
        self.head = None
        return ListNode
       
    def insert_head(n: ListNode, val: int) -> ListNode:
        new_head = ListNode(val)
        new_head.next = n
        return new_head
    
    def insert_tail(n: ListNode, val: int) -> ListNode:
        if n.next == None:
            new_tail = ListNode(val)
            n.next = new_tail
        return new_tail

    def insert_middle(n: ListNode, val: int) -> ListNode:
        """插在后面"""
        nx = ListNode(val)
        nx.next = n.next
        n.next = nx    
        return nx

    def remove(n: ListNode):
        n.next = None
        n2.next = n3
        

def findN(n: ListNode, target: int) -> int:
    """在链表中查找数值"""
    index = 0
    while n:
        if n.val == target:
            print(f"被查找元素的索引为{index}")
        n = n.next
        index += 1

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
new_head = LinkList.insert_head(n0, 0)
nx = LinkList.insert_middle(n2,7)
new_tail = LinkList.insert_tail(n4, 9)
# 删除节点
LinkList.remove(n2)
# 查找节点
findN(new_head, 9)
# 遍历链表
current_node = new_head
values = []
while current_node is not None:
    values.append(current_node.val)
    current_node = current_node.next
print(f"链表中有{values}")
# 链表中有[0, 1, 3, 2, 7, 5, 4, 9]
