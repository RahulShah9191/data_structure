from itertools import  combinations

def perfect_sum(nums, target):
    target_nums = []
    for i in range(1, len(nums)+1):
        target_nums = target_nums + list(combinations(nums, i))
    return [x for x in target_nums if sum(x) == target]

if __name__ == "__main__":
    print(perfect_sum([1,2,3,4,5], 10))
