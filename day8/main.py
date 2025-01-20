from itertools import permutations


Coord = tuple[int,int]


def parse_map(map_list: list[str]) -> dict[str, list[Coord]]:
    coord_dict: dict[str, list[Coord]] = {}
    for y, row in enumerate(map_list):
        for x, char in enumerate(row):
            if char == ".":
                pass
            else:
                if char in coord_dict:
                    coord_dict[char].append((x, y))
                else:
                    coord_dict[char] = [(x, y)]
    return coord_dict


def in_bounds(coord: Coord, limits: Coord) -> bool:
    return 0 <= coord[0] <= limits[0] and 0 <= coord[1] <= limits[1]


def get_antinodes(coords_dict: dict[str, list[Coord]], limits: tuple[int,int]) -> set[Coord]:
    antinodes: set[Coord] = set()
    for coordinates in coords_dict.values():
        for f_coord, s_coord in permutations(coordinates, 2):
            antinode = (
                f_coord[0] - (s_coord[0] - f_coord[0]),
                f_coord[1] - (s_coord[1] - f_coord[1]),
            )
            if in_bounds(antinode, limits):
                antinodes.add(antinode)
    return antinodes


def get_replicating_antonides(coords_dict: dict[str, list[Coord]], limits: tuple[int,int]) -> set[Coord]:
    antinodes: set[Coord] = set()
    for coordinates in coords_dict.values():
        for f_coord, s_coord in permutations(coordinates, 2):
            for replica in range(max(limits)):
                antinode = (
                    f_coord[0] - ((s_coord[0] - f_coord[0]) * replica),
                    f_coord[1] - ((s_coord[1] - f_coord[1]) * replica),
                )
                if in_bounds(antinode, limits):
                    antinodes.add(antinode)
                else:
                    break
    return antinodes


def print_map_with_antinodes(map_list: list[str], coords: set[Coord]):
    matrix = [list(x) for x in map_list]
    for (x, y) in coords:
        matrix[y][x] = "#"
    text = ["".join(x) for x in matrix]
    print("\n".join(map_list))
    print("\n\n")
    print("\n".join(text))
    print("\n")



if __name__ == "__main__":

    with open("data.txt", "r") as file:
        text = file.read().strip()

    map_list = text.split("\n")
    limits = len(map_list)-1, len(map_list[0])-1
    antenas = parse_map(map_list)

    first_part = get_antinodes(antenas, limits)
    second_part = get_replicating_antonides(antenas, limits)

    # print_map_with_antinodes(map_list, first_part)
    # print_map_with_antinodes(map_list, second_part)
    print(f'First answer: {len(first_part)}')
    print(f'Second answer: {len(second_part)}')
