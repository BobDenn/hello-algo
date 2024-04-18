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
        self.EMPTY = kv.Pair(-1,'-1') # 懒删除机制的删除标记
        
    
    