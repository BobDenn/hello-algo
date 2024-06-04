def binary_search(nums: list[int], target: int) -> int:
    """二分查找(闭区间)"""
    i, j = 0, len(nums) - 1
    while i < j :
        m = ( i + j ) // 2 # mid
        if target > nums[m]:
            i = m + 1
        elif target < nums[m]:
            j = m - 1
        else:
            return m
    return -1 # 未找到目标 返回-1
        