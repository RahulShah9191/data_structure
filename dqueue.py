from collections import deque


def print_patternn(input_str):
    d = deque(input_str)
    print(input_str)
    for i in range(len(input_str)):
        if i % 2 == 0:
            d.pop()
            print("".join(list(d)))
        else:
            d.popleft()
            print("".join(list(d)))


def rotate_str(inpput_str, position):
    d = deque(inpput_str)
    d.rotate(position)
    return "".join(d)


def reverse_list(nums):
    d = deque()
    for item in nums:
        d.appendleft(item)
    return list(d)


def shift_all_0_left(input_str):
    d = deque()
    for c in input_str:
        if c == '0':
            d.appendleft(c)
        else:
            d.append(c)
    return "".join(d)


def print_last_n_line(file, n):
    with open(file) as f:
        return "".join(list(deque(f,n)))


def del_n_position(nums, n):
    d = deque(nums)
    d.rotate(-1 * n)
    d.popleft()
    d.rotate(n)
    return list(d)


print(del_n_position([1,2,3,4,5,6,7], 2))
