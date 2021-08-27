from collections import Counter


def convert_to_sort_string(input_str="aaabbcddd"):
    d = Counter(input_str)
    op = [f"{k}{v}" for k,v in d.items()]
    return "".join(op)


def most_common(input_str, n):
    c = Counter(input_str)
    return c.most_common(n)




print(most_common("abracadabra", 5))



