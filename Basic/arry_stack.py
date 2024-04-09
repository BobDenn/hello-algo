class arrystack:
    """基于动态数组实现栈"""
    def __init__(self) -> None:
        self._stack: list[int] = []
    
    def is_empty(self) -> bool:
        return self._stack == []
    
    def stacksize(self) -> int:
        return len(self._stack)
    
    def push(self, val: int):
        self._stack.append(val)
    
    def pop(self) -> int:
        if self.is_empty():
            # 报错
            raise IndexError("栈为空")
        return self._stack.pop()
    
    def peak(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    
    def to_list(self) -> list[int]:
        return self._stack
