def safe_check(data: list[int], editable: bool=True) -> bool:

    increase = data[0] < data[len(data)-1]

    for i in range(len(data)-1): # Takes all elements except last
        if (data[i] < data[i+1]) != increase:
            if not editable:
                return False
            else:
                pop_first = data.copy()
                pop_first.pop(i)
                pop_second = data.copy()
                pop_second.pop(i+1)
                return safe_check(pop_first, editable=False) or safe_check(pop_second, editable=False)
        if abs(data[i] - data[i+1]) > 3 or abs(data[i] - data[i+1]) < 1:
            if not editable:
                return False
            else:
                pop_first = data.copy()
                pop_first.pop(i)
                pop_second = data.copy()
                pop_second.pop(i+1)
                return safe_check(pop_first, editable=False) or safe_check(pop_second, editable=False)
    return True


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = file.read().strip().split("\n")
    checks_list = [safe_check(list(map(int, x.split()))) for x in text]
    print(checks_list.count(True))
