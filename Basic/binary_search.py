def binary_search(nums: list[int], target: int) -> int:
    """二分查找[闭区间]"""
    i, j = 0, len(nums) - 1
    while i <= j :
        m = ( i + j ) // 2 # mid
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            return m
    return -1 # 未找到目标 返回-1


def binary_search_insertion(nums: list[int], target: int) -> int:
    """二分查找 (包含重复元素)"""
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            # 如果 nums[m] == target, 则继续向左查找
            j = m - 1
    # 如果找到了target，则返回其索引
    if i < len(nums) and nums[i] == target:
        return i
    # 如果没有找到target，则返回应该插入的位置
    return i        


if __name__ == "__main__":    
    nums = [7, 6, 3, 1, 0, 1, 3, 9, 8]
    nums_st = sorted(nums)
    print(nums_st)
    print(binary_search_insertion(nums=nums_st, target=3))
