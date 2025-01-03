import re


def expression_counter(text: str) -> int:
    regex = r'XMAS'
    matches_xmas = re.findall(regex, text)
    return len(matches_xmas)


def horizontal_search(matrix: list) -> int:
    # Searching in horizontal lines through matrix
    hor_count = 0
    for line in matrix:
        hor_count += expression_counter(line)
    return hor_count


def vertical_search(matrix: list) -> int:
    # Searching in vertical lines through matrix
    vert_count = 0
    matrix_len = len(matrix)
    for i in range(matrix_len):
        string = "".join([matrix[x][i] for x in range(matrix_len)])
        vert_count += expression_counter(string)
    return vert_count


def diagonal_search(matrix: list) -> int:
    # Searching in diagonal lines through matrix
    diag_count = 0
    matrix_len = len(matrix)
    diagonals = 2*matrix_len-1 # Amount of diagonals - (2*matrix_len)-1
    
    # Diagonal from top right to bottom left, start pos - left top
    for i in range(diagonals):
        letters = []
        if i < matrix_len:
            line, letter = 0, i
            letters.extend(matrix[line][letter])
            while letter != 0:
                line += 1
                letter -= 1
                letters.extend(matrix[line][letter])
        else:
            line = i - matrix_len + 1
            letter = matrix_len - 1
            letters.extend(matrix[line][letter])
            while letter != (i - matrix_len + 1):
                line += 1
                letter -= 1
                letters.extend(matrix[line][letter])
        diag_count += expression_counter("".join(letters))
    
    # Diagonal from top left to bottom right, start pos - right top
    for i in range(diagonals):
        if i < matrix_len:
            letters = []
            line, letter = 0, matrix_len - 1 - i
            letters.extend(matrix[line][letter])
            while letter != (matrix_len - 1):
                line += 1
                letter += 1
                letters.extend(matrix[line][letter])
            diag_count += expression_counter("".join(letters))
        else:
            letters = []
            line, letter = i - matrix_len + 1, 0
            letters.extend(matrix[line][letter])
            while line != (matrix_len - 1):
                line += 1
                letter += 1
                letters.extend(matrix[line][letter])
            diag_count += expression_counter("".join(letters))
    return diag_count


if __name__ == "__main__":

    with open("data.txt", "r") as file:
        text = file.read().strip()
        data = text.split("\n")
        reversed_data = text[::-1].split("\n")
    
    print(horizontal_search(data)
          +horizontal_search(reversed_data)
          +vertical_search(data)
          +vertical_search(reversed_data)
          +diagonal_search(data)
          +diagonal_search(reversed_data)
    )
