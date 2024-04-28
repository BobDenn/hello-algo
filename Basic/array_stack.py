class ArrayStack:
    """基于动态数组实现栈"""
    def __init__(self) -> None:
        """initial"""
        self._stack: list[int] = []
    
    def is_empty(self) -> bool:
        """是否为空"""
        return self._stack == []
    
    def stacksize(self) -> int:
        """size of stack"""
        return len(self._stack)
    
    def push(self, val: int):
        """put in value"""
        self._stack.append(val)
    
    def pop(self) -> int:
        """delete last value"""
        if self.is_empty():
            # 报错
            raise IndexError("栈为空")
        return self._stack.pop()
    
    def peak(self) -> int:
        """read top value"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    
    def to_list(self) -> list[int]:
        """Look at the stack through the list"""
        return self._stack


if __name__ == "__main__":
    pass
