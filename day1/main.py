def merge(left: list[int], right: list[int]) -> list[int]:
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

def merge_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])  # Splits list, until merge_sort -
    right = merge_sort(array[mid:]) # - returns a list with lenght 1
    return merge(left, right)       # and then merge them


if __name__ == "__main__":
    first_list = []
    second_list = []

    with open("data.txt", "r") as data:
        for line in data:
            first, second = line.strip().split()
            first_list.append(int(first))
            second_list.append(int(second))

    first_sorted = merge_sort(first_list)
    second_sorted = merge_sort(second_list)

    diff_result = 0
    sim_result = 0
    sim_control_set = set()
    for index, value in enumerate(first_sorted):
        diff_result += abs(first_sorted[index]-second_sorted[index])
        if value not in sim_control_set:
            sim_result += value * second_list.count(value)
        else:
            sim_control_set.add(value)

    print(f'First answer:{diff_result}')
    print(f'Second answer: {sim_result}')