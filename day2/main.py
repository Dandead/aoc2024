def safe_check(data: list[int]) -> bool:
    increase = data[0] < data[1]
    for i in range(len(data)-1): # Takes all elements except last
        if (data[i] < data[i+1]) != increase:
            return False
        if abs(data[i] - data[i+1]) > 3 or abs(data[i] - data[i+1]) < 1:
            return False
    return True


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = file.read().strip().split("\n")
    checks_list = [safe_check(list(map(int, x.split()))) for x in text]
    print(checks_list.count(True))
