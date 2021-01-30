import re

str1 = "rahul is my name shah. I born in 09-01-1991, I am living in pune since 12-13-2012."
rx = "[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"

op = re.findall(rx,str1)
uniq_year = set()

for item in op:
    uniq_year.add(item.split("-")[-1])

print(uniq_year)
