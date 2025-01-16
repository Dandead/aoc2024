import re


def multiply(values: tuple[int, int]) -> int:
    first, second = values
    return int(first) * int(second)



if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = "".join(file.read().strip().split("\n"))

    separators = r"(do\(\)|don't\(\))"
    list_of_pairs = ["do()"]
    # Separates text to blocks like: ["do()", "string_to_use", "don't()", "string_to_ignore"]
    list_of_pairs.extend(re.split(separators, text))
        
    reg_exp = r'(?<=mul\()\d+,\d+(?=\))'
    list_of_numbers = []
    for condition, text in zip(list_of_pairs[::2], list_of_pairs[1::2]):
        if condition == "do()":
            list_of_numbers.extend([
                (int(x), int(y))
                for (x,y) in (value.split(",") for value in re.findall(reg_exp, text))
            ])
        else:
            continue

    print(sum(map(multiply, list_of_numbers)))

