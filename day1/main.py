# Defining merge sorting algorithm

def merge(left: list, right: list) -> list:
    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

# Set up lists of data

first_list = []
second_list = []

with open("data.txt", "r") as data:
    for line in data:
        first, second = line.split()
        first_list.append(first)
        second_list.append(second)

first_sorted = merge_sort(first_list)
second_sorted = merge_sort(second_list)

result = 0
for i in range(0, len(first_sorted)):
    result += abs(int(first_sorted[i])-int(second_sorted[i]))

print(result)
