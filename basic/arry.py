import random


def random_access(nums: list[int]) -> int:
  """获取一个数组的随机数"""
  random_index = random.randint(0, len(nums)-1)
  random_num = nums[random_index]
  return random_num


def insert(nums: list[int], index: int, num: int):
  """在数组的 index 处插入元素num"""
  # index 处的数字往后挤
  for i in range(len(nums)-1, index, -1):
    nums[i] = nums[i - 1]
  nums[index] = num


def remove(nums: list[int], index: int):
  """删除index处的num"""
  for i in range(index, len(nums)-1):
    nums[index] = nums[index+1]


def traverse(nums: list[int]):
  """遍历数组"""
  count = 0
  for i in range(len(nums)):
    count += 1
  for num in nums:
    count += 1
  for i,num in enumerate(nums):
    # enumerate 同时列出数据和数据下标
    count += 1
  return nums


def find(nums: list[int], target: int) -> int:
  """find target"""
  for i, num in enumerate(nums):
    if nums[i] == target:
      return i, num
  return -1


def extend(nums: list[int], large: int) -> list[int]:
  """扩展数组"""
  res = [0] * (len(nums) + large)
  for i in range(len(nums)):
    res[i] = nums[i]
  return res


arr: list[int] = [0] * 5
# print(arr)
nums: list[int] = [1, 3, 2, 5, 4]
# print(nums)
print(f"返回随机数: {random_access(nums)}")
insert(nums, 4, 8)
print(f"遍历数组: {traverse(nums)}")
Index, Value = find(nums, 8)
if Index != -1 :
  print(f"在{Index}处的值为{Value}")
else:
  print("没有找到目标值")
# 扩展数组
print(f"扩展后的数组为: {extend(nums, 3)}")
#今天浪费一天