
def sumr_rec(list):
    if len(list) ==1 :
        return list[0]
    else:
        return list[0] + sum(list[1:])
    