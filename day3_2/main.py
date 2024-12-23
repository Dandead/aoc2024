import re


def multiply(obj: str) -> int:
    splited = obj.split(",")
    return int(splited[0]) * int(splited[1])


with open("data.txt", "r") as file:
    text = "".join(file)
    separators = r"(do\(\)|don't\(\))"
    list_of_pairs = ["do()"]
    list_of_pairs.extend(re.split(separators, text))
    

reg_exp = r'(?<=mul\()\d+,\d+(?=\))'
list_of_numbers = []
for condition, text in zip(list_of_pairs[::2], list_of_pairs[1::2]):
    if condition == "do()":
        list_of_numbers.extend(re.findall(reg_exp, text))
    else:
        continue

print(sum(map(multiply, list_of_numbers)))

