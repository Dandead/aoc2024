Coord = tuple[int, int]


def get_trailheads(matrix: list[list[int]]) -> set[Coord]:
    trailheads = set()
    for y, line in enumerate(matrix):
        for x, num in enumerate(line):
            if num == 0:
                trailheads.add((x,y))
    return trailheads


def in_bounds(coord: Coord, bounds: Coord) -> bool:
    return 0 <= coord[0] <= bounds[0] and 0 <= coord[1] <= bounds[1]


def get_trailheads_scores(matrix: list[list[int]], trailheads: set[Coord]) -> tuple[int, int]:
    bounds = (len(matrix[0])-1, len(matrix)-1)
    p1_score = 0
    p2_score = 0

    def find_path(pos: Coord, matrix: list[list[int]], bounds: Coord) -> list[Coord]:
        if matrix[pos[1]][pos[0]] == 9:
            return [pos]
        endings = []
        ways = ((0, -1), (1, 0), (0, 1), (-1, 0))
        for way in ways:
            next_pos: Coord = (pos[0]+way[0], pos[1]+way[1])
            if (
                in_bounds(next_pos, bounds) and
                matrix[next_pos[1]][next_pos[0]] == matrix[pos[1]][pos[0]] + 1
            ):
                endings.extend(find_path(next_pos, matrix, bounds))
        return endings

    for trailhead in trailheads:
        score = find_path(trailhead, matrix, bounds)
        p1_score += len(set(score))
        p2_score += len(score)
    return (p1_score, p2_score)
    


if __name__ == "__main__":
    with open("data.txt", "r") as file:
        text = file.read().strip()
    island_map = [list(map(int, line.strip())) for line in text.split("\n")]
    trailheads = get_trailheads(island_map)
    p1, p2 = get_trailheads_scores(island_map, trailheads)
    print(f'First answer: {p1}\nSecond answer: {p2}')
