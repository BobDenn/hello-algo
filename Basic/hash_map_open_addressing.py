import array_hash_map as kv


class HashMapOpenAddressing:
    """开放寻址哈希表"""
    def __init__(self):
        """构造方法"""
        self.size = 0 # 键值对数量
        self.capacity = 4 # 表容量
        self.load_thres = 2.0 / 3.0 # 扩容阈值
        self.extend_ratio = 2 # 扩容倍数
        self.buckets: list[kv.Pair | None] = [None] * self.capacity # 桶数组
        self.TOMBSTONE = kv.Pair(-1,'-1') # 懒删除机制的删除标记
        
    def hash_f(self, key: int) -> int:
        """哈希函数"""
        index = key % self.capacity
        return index
    
    def load_factor(self) -> float:
        """负载因子"""
        return self.size / self.capacity
    
    def extend(self):
        """扩容机制"""
        buckets_tmp = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        for pair in buckets_tmp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)
    
    def find_bucket(self, key: int) -> int:
        """查找key对应的桶索引"""
        index = self.hash_f(key)
        first_tombstone = -1
        # 线性检测 每当遇到空桶时跳出
        while self.buckets[index] is not None:
            # 如果遇到 key 就返回对应的桶索引
            if self.buckets[index].key == key:
                # 如果之前遇到了删除标记, 则将键值对移至该索引处
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[first_tombstone] = self.TOMBSTONE
                    return first_tombstone # 返回移动后的桶索引
                # 返回对应的桶索引
                return index 
            # 记录遇到的首个删除标记
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            # 计算桶索引 越过尾部返回头部
            index = (index + 1) % self.capacity
        # 若 key 不存在，则返回添加点的索引
        return index if first_tombstone == -1 else first_tombstone
    
    def get(self, key: int) -> str:
        """查找"""
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        return None
                
    def put(self, key: int, val: str):
        """添加元素"""
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.find_bucket(key)
        # 若找到键值对 则覆盖 val 返回
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        # 若键值对不存在 则添加键值对
        self.buckets[index] = kv.Pair(key, val)
        self.size += 1

    def remove(self, key):
        index = self.find_bucket(key)
        # 若找到键值对  用删除标记覆盖
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1
        
    def print(self):
        for pair in self.buckets:
            if pair is None:
                print('None')    
            elif pair is self.TOMBSTONE:
                print('TOMBSTONE')
            else:
                print(pair.key, "->", pair.val)

    