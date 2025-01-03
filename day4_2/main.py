def mas_search(matrix: list) -> int:
    pos_variations = (["M","A","S"], ["S","A","M"])
    matrix_len = len(matrix)
    count = 0
    for line in range(1, matrix_len - 1): # Parsing all lines, except first and last
        for letter in range(1, matrix_len - 1): # Parsing all letters, except first and last
            if matrix[line][letter] == "A":
                l_r_cross = [matrix[line][letter]]
                l_r_cross.insert(0, matrix[line-1][letter-1])
                l_r_cross.append(matrix[line+1][letter+1])
                r_l_cross = [matrix[line][letter]]
                r_l_cross.insert(0, matrix[line-1][letter+1])
                r_l_cross.append(matrix[line+1][letter-1])
                if l_r_cross in pos_variations and r_l_cross in pos_variations:
                    count += 1
            else:
                continue
    return count

if __name__ == "__main__":

    with open("data.txt", "r") as file:
        data = [line for line in file]
    
    print(mas_search(data))

