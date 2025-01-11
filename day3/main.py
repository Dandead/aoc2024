import re


def multiply(obj: str) -> int:
    splited = obj.split(",")
    return int(splited[0]) * int(splited[1])

reg_exp = r'(?<=mul\()\d+,\d+(?=\))'
values_list = []

with open("data.txt", "r") as file:
    for line in file:
        values_list.extend(re.findall(reg_exp, line))
print(sum(list(map(multiply, values_list))))

