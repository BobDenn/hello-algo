import heapq


min_heap, flag = [], 1
max_heap, flag = [], -1
# heapq模块默认实现小顶堆
# 用户输入数字
input_nums = input("请输入数字并使用空格分隔:")
# To number list
nums = list(map(int, input_nums.split()))
# pushing
i = 0
while i < len(nums):
    heapq.heappush(max_heap, flag * nums[i])
    i += 1
# Get the maximum value of heap
peek: int = flag * max_heap[0]
# poping
while max_heap:
    val = flag * heapq.heappop(max_heap)
    print(val, end=" ")
# get size of heap
size: int = len(max_heap)
print()
print("Heap's size", size)
is_empty = not max_heap
print("Is heap empty?", is_empty)
# use heapify function
min_heap: list[int] = [1, 3, 2, 4, 5]
heapq.heapify(min_heap)
while min_heap:
    val = flag * heapq.heappop(min_heap)
    print(val, end=" ")
    