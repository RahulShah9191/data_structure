def merge_2_sorted_list(data1, data2):
    i1 = 0
    i2 = 0
    p1 = len(data1)
    p2 = len(data2)
    data3 = []
    while i1 < len(data1) and i2 < len(data2):
        if data1[i1] < data2[i2]:
            data3.append(data1[i1])
            i1 = i1 + 1
        else:
            data3.append(data2[i2])
            i2 = i2 + 1
    data3 = data3 + data1[i1:]
    data3 = data3 + data2[i2:]
    return data3
