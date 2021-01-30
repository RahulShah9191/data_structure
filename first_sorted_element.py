'''
Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.
'''


def check_left_sequence(arr, num):
    b = sorted(arr)
    return True if b[-1] <= num else False

def check_right_sequence(arr, num):
    b = sorted(arr)
    return True if b[0] >= num else False

def first_sorted_element(arr):
    for i in range(1, len(arr) -1):
        if check_left_sequence(arr[:i], arr[i]) and check_right_sequence(arr[i+1:], arr[i]):
            return arr[i]
    return -1

if __name__ == "__main__":
    testcase = input()
    for tc in range(int(testcase)):
        length = int(input())
        arr = input().split(' ')
        print(first_sorted_element(arr))
