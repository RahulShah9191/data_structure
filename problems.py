# def combine_all(input):
#     check1 = False
#     check2 = False
#     check3 = False
#     if len(input) > 0:
#         if input[0] == 'a':
#             check1 = True
#
#     main_s = []
#     tmp_dict = {}
#     for item in input:
#         tmp_dict[item] = "0"
#         if item not in ['a', 'b']:
#             return False
#
#         if item == "a":
#             main_s.append(item)
#         elif item == "b":
#             try:
#                 main_s.pop()
#             except:
#                 return False
#
#     if len(tmp_dict.keys()) == 2:
#         check2 = True
#     if len(main_s) == 0:
#         check3 = True
#     if check1 and check2 and check3:
#         return True
#
#     return False


def longest_palidrom_substr(input_str):
    l = 0
    r = len(input_str)
    counter = 0
    while counter < r:
        #print(input_str[counter:r])
        if input_str[counter:r] == input_str[counter:r][::-1]:
            return input_str[counter:r]
        counter = counter + 1
    counter = len(input_str)
    while counter > l:
        #print(input_str[l:counter])
        if input_str[l:counter] == input_str[l:counter][::-1]:
            return input_str[l:counter]
        counter = counter - 1
    return None

def get_sum_position(nums, target):
    tmp_dict = {}
    for i, item in enumerate(nums):
        tmp_dict[item] = i
    for i, item in enumerate(nums):
        op = tmp_dict.get(target-item, None)
        if op and op != i:
            return [i, op]
    return None



def findMedianSortedArrays(nums1, nums2):
    p1 = 0
    p2 = 0
    op = []
    while (p1 < len(nums1) and p2 < len(nums2)):
        if nums1[p1] < nums2[p2]:
            op.append(nums1[p1])
            p1 += 1
        else:
            op.append(nums2[p2])
            p2 += 1
    op = op + nums1[p1:]
    op = op + nums2[p2:]
    print(op)
    mid = (len(nums1) + len(nums2)) // 2
    if (len(nums1) + len(nums2)) % 2 != 0:
        return op[mid]
    else:
        return (op[mid-1] + op[mid]) / 2

def mergeTwoLists(l1, l2):
    p1 = 0
    p2 = 0
    op = []
    while (p1 < len(l1) and p2 < len(l2)):
        if l1[p1] < l2[p2]:
            op.append(l1[p1])
            p1 += 1
        else:
            op.append(l2[p2])
            p2 += 1
    op = op + l1[p1:]
    op = op + l2[p2:]
    return op

def reverse(x):
    if -2**31 <= x <= 2**31 -1 :
        if x > 0:
            return int(str(x)[::-1])
        else:
            return int(str(x*-1)[::-1])*-1
    return 0

def shift_all_0_left(input_str):
    input_str = list(input_str)
    l = 0
    r = len(input_str) - 1
    while l < r:
        if input_str[l] == '0':
            l = l + 1
            continue
        if input_str[r] == '1':
            r = r - 1
            continue
        input_str[l], input_str[r] = input_str[r], input_str[l]
        l = l + 1
        r = r - 1
    return "".join(input_str)


def myAtoi(s):
    s1 = s.rstrip()
    s2 = s1.lstrip()
    int_s = int(s2)
    if -2147483648 <= int_s <= 2147483647:
        return int_s
    return 0


def threeSum(nums):
    op = set()
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            for k in range(j,len(nums)):
                if i !=j and i != k and j != k and (nums[i] + nums[j] + nums[k] == 0):
                    op.add((nums[i], nums[j], nums[k]))
    return list(op)


def letterCombinations(digits):

    chars_mapping = {
        2 : ['a', 'b', 'c'],
        3 : ['d','e','f'],
        4 : ['g','h','i'],
        5 : ['j','k','l'],
        6 : ['m','n','o'],
        7 : ['p','q','r','s'],
        8 : ['t','u','v'],
        9 : ['w','x','y','z']
    }

    if len(str(digits)) > 4 or len(str(digits)) <=0:
        return None
    else:
        l_of_l = []
        for c in str(digits):
            l_of_l.append(chars_mapping.get(int(c)))
        print(l_of_l)

def strStr(haystack, needle):
    needle_len = len(needle)
    i = 0
    k = 0
    while i < (len(haystack) - len(needle)):
        if haystack[i] == needle[k]:
            print()
        i += 1


