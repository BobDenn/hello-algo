import linked_list


class LinkedListStack:
    """基于链表实现的栈"""
    def __init__(self) -> None:
        self._peak: linked_list.ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        """获取栈的长度"""
        return self._size
    
    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return not self._peak
    
    def push(self, val: int):
        """入栈"""
        node = linked_list.ListNode(val)
        # 栈顶的next指向当前栈顶
        node.next = self._peak
        self._peak = node
        self._size += 1
    
    def peak_val(self) -> int:
        """返回栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peak.val
    
    def pop(self) -> int:
        """出栈"""
        num = self.peak_val()
        self._peak = self._peak.next
        return num
    
    def seeinlist(self) -> list[int]:
        """在列表中查看栈"""
        arr = []
        node = self._peak
        while node:
            arr.append(node.val)
            node = node.next
        # arr.reverse()
        print(arr)

if __name__ == '__main__':
    stack = LinkedListStack()
    # print(stack.is_empty())
    stack.push(5)
    stack.push(8)
    stack.push(9)
    stack.push(1)
    stack.push(1)
    stack.push(2)
    # stack.seeinlist()  [2, 1, 1, 9, 8, 5]
    print(stack.pop())
    stack.seeinlist()
    print(stack.peak_val())
