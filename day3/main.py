import re


def multiply(values: tuple[int, int]) -> int:
    first, second = values
    return int(first) * int(second)


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = "".join(file.read().strip().split("\n"))
    
    reg_exp = r'(?<=mul\()\d+,\d+(?=\))'
    values_list = [
        (int(x), int(y))
        for (x,y) in (value.split(",") for value in re.findall(reg_exp, text))
    ]
    print(sum(tuple(map(multiply, values_list))))

