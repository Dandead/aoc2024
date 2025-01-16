class Guard:
    """
    pos - starting position
        (x, y)
    direction - direction of view
        ^ - top, > - right, v - bottom, < - left
    """
    def __init__(self, pos: tuple[int, int], direction: str) -> None:
        self.x_pos, self.y_pos = pos
        self.direction = direction
        self.unique_cells = {(self.x_pos, self.y_pos)}
        self.visited_obstacles = set()
        self.has_looped = False

    def move(self) -> None:
        match self.direction:
            case "^":
                self.y_pos -= 1
            case ">":
                self.x_pos += 1
            case "v":
                self.y_pos += 1
            case "<":
                self.x_pos -= 1
        self.unique_cells.add((self.x_pos, self.y_pos))

    def rotate(self) -> None:
        match self.direction:
            case "^":
                self.direction = ">"
            case ">":
                self.direction = "v"
            case "v":
                self.direction = "<"
            case "<":
                self.direction = "^"
    
    def count_visited_cells(self) -> int:
        return len(self.unique_cells)

    def get_coords(self):
        return (self.x_pos, self.y_pos)

    def get_next_step(self) -> tuple[int, int]:
        match self.direction:
            case "^":
                return (self.x_pos, self.y_pos - 1)
            case ">":
                return (self.x_pos + 1, self.y_pos)
            case "v":
                return (self.x_pos, self.y_pos + 1)
            case "<":
                return (self.x_pos - 1, self.y_pos)
            case _:
                return (self.x_pos, self.y_pos)


def parse_map(text: str) -> tuple[list[list[str]], set[tuple[int, int]], tuple[int, int]]:
    """Returns the matrix view of map, obstacles set and start position"""
    matrix = [list(row) for row in text.split("\n")]
    obstacles = set()
    start_pos = tuple()
    for y_id, row in enumerate(matrix):
        for x_id, char in enumerate(row):
            if char == "#":
                obstacles.add((x_id, y_id))
            if char == "^":
                start_pos = (x_id, y_id)
    matrix[start_pos[1]][start_pos[0]] = "."
    return matrix, obstacles, start_pos


def search_loops(matrix, obstacles, start_pos, direction):
    escaped_guard = simulate_walking(matrix, obstacles, start_pos, direction)
    print(f'1st answer: {escaped_guard.count_visited_cells()}')
    unique_cells = escaped_guard.unique_cells
    loops = 0
    for cell in unique_cells:
        mapp = matrix.copy()
        mapp[cell[1]][cell[0]] = "#"
        obs = obstacles.copy()
        obs.add(cell)
        if simulate_walking(mapp, obs, start_pos, direction).has_looped:
            loops += 1
    print(f'2nd answer: {loops}')


def simulate_walking(matrix, obstacles, start_pos, direction):
    border = len(matrix)
    guard = Guard(start_pos, direction)
    x, y = start_pos
    while True:
        try:
            next_x, next_y = guard.get_next_step()
            if border <= next_x or next_x < 0 or border <= next_y or next_y < 0:
                raise IndexError("Out of map")
            elif (next_x, next_y) not in obstacles:
                guard.move()
                x, y = next_x, next_y
            else:
                if ((next_x, next_y), (x, y)) in guard.visited_obstacles:
                    guard.has_looped = True
                    return guard
                else:
                    guard.visited_obstacles.add(
                        ((next_x, next_y),(x, y))
                    )
                guard.rotate()
        except IndexError:
            return guard


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = file.read()

    matrix, obstacles, start_pos = parse_map(text)
    search_loops(matrix, obstacles, start_pos, "^")
