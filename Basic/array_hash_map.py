class key_val:
    """键值对"""
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class ArrHashMap:
    """基于数组实现的哈希表"""
    def __init__(self) -> None:
        # 初始化桶的容量
        self.buckets: list[key_val | None] = [None] * 100

    def hash_f(self, key: int) -> int:
        """通过key获取index索引"""
        index = key % len(self.buckets)
        return index

    def get(self, key: int) -> str:
        """获取值"""
        index: int = self.hash_f(key)
        # 变量couple 存储键值对
        couple: key_val = self.buckets[index]
        if couple is None:
            print("该值为空")
        return couple.val
    
    def put(self, key: int, val: str):
        """添加键值对"""
        couple = key_val(key, val)
        index = self.hash_f(key)
        self.buckets[index] = couple
        
    def remove(self, key):
        """删除操作"""
        index = self.hash_f(key)
        # 置为None, 表示删除
        self.buckets[index] = None
    
    def all_key_val(self) -> list[key_val]:
        """获取所有的键值对"""
        res = []
        for key_val in self.buckets:
            if key_val is not None:
                res.append(key_val)
        return res
    
    def all_key(self) -> list[int]:
        """获取所有的键"""
        res: list[int] = []
        for key_val in self.buckets:
            if key_val is not None:
                res.append(key_val.key)
        return res
    
    def all_value(self) -> list[str]:
        """"获取所有的值"""    
        res: list[str] = []
        for key_val in self.buckets:
            if key_val is not None:
                res.append(key_val.val)
        return res
    
    def print_h(self):
        """打印哈希表"""
        for key_val in self.buckets:
            if key_val is not None:
                print(key_val.key, "->", key_val.val)


if __name__ == '__main__':
    myhash = ArrHashMap()
    myhash.put(12836, "小哈")
    myhash.put(15937, "小啰")
    myhash.put(16750, "小算")
    myhash.put(13276, "小法")
    myhash.put(10583, "小鸭")
    myhash.print_h()
