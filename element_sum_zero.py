from itertools import combinations 
a = [1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6]
combination_list = list(combinations(a, 3)) 
for member in combination_list:
    if sum(member) == 0:
        print(member)
