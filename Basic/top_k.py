import heapq


def top_k_heap(nums: list[int], k: int) -> list[int]:
    """基于堆查找数组中最大的k个元素"""
    heap = [] # 初始化
    # 入堆
    for i in range(k):
        heapq.heappush(heap, nums[i])
    # 从第 k+1 个元素开始, 保持堆的长度为 k
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


if __name__ == '__main__':
    nums = [1, 1, 3, 7, 0, 0, 5, 6, 7, 3]
    print(top_k_heap(nums, 5))
    addnums = [24, 36, 48, 60, 72]
    nums.extend(addnums)
    print(top_k_heap(nums, 5))
