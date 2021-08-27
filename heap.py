
import heapq


def heap_sort(nums):
    import time
    s = time.perf_counter()
    heapq.heapify(nums)
    op = []
    for _ in range(len(nums)):
        op.append(heapq.heappop(nums))
    print(f"{time.perf_counter() - s}  ns")
    return op


def bubble_sort(nums):
    import time
    s = time.perf_counter()
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(f"{time.perf_counter() - s}  ns")
    return nums


def n_largest_heap(n, nums):
    heapq.heapify(nums)
    return heapq.nlargest(n, nums)


def n_smallest_heap(n, nums):
    heapq.heapify(nums)
    return heapq.nsmallest(n, nums)

# element   heap - sort                 bubble - sort
# 10 -      1.195799995912239e-05       1.3329998182598501e-05
# 100 -     5.962100112810731e-05       0.0007358639995800331
# 1000 -    0.00041952099854825065      0.07986475900543155
# 10000 -   0.007111473998520523        5.287992757999746
# 1L -      0.050869570004579145        ??




print(bubble_sort([i for i in range(100000,0,-1)]))
