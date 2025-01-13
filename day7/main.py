def calculate(data):
    def sum_multiply(tup, dest_num):
        result = set()
        for num in tup:
            result.add(num+dest_num)
            result.add(num*dest_num)
        return result

    def sum_multiply_concat(tup, dest_num):
        result = set()
        for num in tup:
            result.add(num+dest_num)
            result.add(num*dest_num)
            result.add(int(str(num)+str(dest_num)))
        return result

    first_final_sum = 0
    second_final_sum = 0
    for row in data:
        result, values = row
        first_part_set = {values[0]}
        second_part_set = {values[0]}
        try:
            for id, num in enumerate(values):
                first_part_set = sum_multiply(first_part_set, values[id+1])
                second_part_set = sum_multiply_concat(second_part_set, values[id+1])
        except IndexError:
            if result in first_part_set:
                first_final_sum += result
            if result in second_part_set:
                second_final_sum += result

    print(f'First answer: {first_final_sum}\nSecond answer: {second_final_sum}')
            



if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = file.read().strip()
    data: tuple[tuple[int, tuple[int, ...]], ...] = tuple([
        (int(line.split(":")[0]), tuple(map(int, line.split(":")[1].strip().split(" "))))
        for line in text.split("\n")
    ]) # converts text to tuple: ((result, (int, ...)), (result, (int, ...)))
    calculate(data)
    