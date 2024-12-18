# Define safe check function
def safe_check(data: list[int]) -> bool:
    increase = data[0] < data[1]
    for i in range(len(data)-1): # Takes all elements except last
        if (data[i] < data[i+1]) != increase:
            return False
        if abs(data[i] - data[i+1]) > 3 or abs(data[i] - data[i+1]) < 1:
            return False
    return True

# Set up data
with open("data.txt", "r") as file:
    checks_list = [safe_check(list(map(int, x.split()))) for x in file]
#print(checks_list)
print(checks_list.count(True))
