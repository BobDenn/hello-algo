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
  print(nums)
  
  
def remove(nums: list[int], index: int):
  """删除index处的num"""
  for i in range(index, len(nums)-1):
    nums[index] = nums[index+1]
  print(nums)
  
  
def traverse(nums: list[int]):
  """遍历数组"""
  count = 0
  for i in range(len(nums)):
    count += 1
  for num in nums:
    count += 1
  for i,num in enumerate(nums):
    count += 1
  print(nums)
  
arr: list[int] = [0] * 5
# print(arr)
nums: list[int] = [1, 3, 2, 5, 4]
# print(nums)
print(random_access(nums))
insert(nums, 4, 8)
traverse(nums)
