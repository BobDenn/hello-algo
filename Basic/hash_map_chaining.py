import array_hash_map as Kv


class HashMapChaining:
    """
    链式地址哈希表
    「链式地址separate chaining」将单个元素转换为链表, 将
    键值对作为链表节点，将所有发生冲突的键值对都存储在同一链表中
    """
    def __init__(self):
        """自身属性"""
        self.size = 0 # 键值对数量
        self.capcity = 4 # 哈希表容量
        self.load_thres = 2.0 / 3.0 # 触发扩容机制的阈值
        self.extend_ratio = 2 # 扩容倍数
        self.buckets = [[] for _ in range(self.capcity)] # 桶数组
    
    def hash_f(self, key: int) -> int:
        """计算索引"""
        return key % self.capcity
        
    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capcity # 键值对 / 总容量
    
    def get(self, key: int) -> str:
        """查找元素"""
        index = self.hash_f(key)
        bucket = self.buckets[index]
        for Pair in bucket:
            if Pair.key == key:
                return Pair.val
        return None
    
    def extend(self):
        """扩容哈希表"""
        # 暂存目前的桶
        buckets = self.buckets
        # 初始化扩容后的表
        self.capcity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capcity)]
        # 重置键值对数量
        self.size = 0
        for bucket in buckets:
            for Pair in bucket:
                self.put(Pair.key, Pair.val)

    def put(self, key: int, val: str):
        """插入"""
        if self.load_factor() > self.load_thres:
            self.extend()
        # 正常插入
        index = self.hash_f(key)
        bucket = self.buckets[index]
        for Pair in range(bucket):
            if Pair.key == key:
                Pair.val = val
                return
        # 如果没有对应的 key
        pair = Kv.Pair(key, val)
        bucket.append(pair)
        self.size += 1
        
    def remove(self, key: int):
        """删除操作"""
        index = self.hash_f(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break
    
    def print(self):
        """打印"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + "->" + pair.val)
            print(res) 

if __name__ == "__main__":
    print("finish")          
