import time


def disk_map_to_blocks(line: str) -> list[str]:
    list_input: list[int] = [int(char) for char in line]
    list_output: list[str] = []

    for id, block in enumerate(list_input):
        if id % 2 == 0:                         # File
            list_output.extend([str(id//2)] * block)
        else:                                   # Empty space
            list_output.extend(["."] * block)
    
    return list_output


def fragment_disk_data(inp: list[str]) -> list[str]:
    blocks_map = inp.copy()
    start_pointer = 0
    end_pointer = len(blocks_map) - 1

    while start_pointer < end_pointer:
        if blocks_map[start_pointer] == "." and blocks_map[end_pointer] != ".":
            blocks_map[start_pointer] = blocks_map[end_pointer]
            blocks_map[end_pointer] = "."
        else:
            if blocks_map[start_pointer] != ".":
                start_pointer += 1
            if blocks_map[end_pointer] == ".":
                end_pointer -= 1
    return blocks_map


def compress_disk_data(inp: list[str]) -> list[str]:
    blocks_map = inp.copy()
    end_pointer = len(blocks_map) - 1
    start_pointer = 0
    last_id = None
    block_start = 0
    block_end = 0
    space_start = 0
    space_end = 0

    while end_pointer > 0:
        if (
            blocks_map[end_pointer] == "." or
            (last_id is not None and int(blocks_map[end_pointer])>last_id)
        ):  # Skip element if it's "." or if ID > then latest inspected
            end_pointer -= 1
            continue
        
        last_id = int(blocks_map[end_pointer])
        block_end = end_pointer
        while True: # Collecting all same blocks
            end_pointer -= 1
            if blocks_map[end_pointer] == str(last_id):
                continue
            else:
                block_start = end_pointer + 1
                break

        start_pointer = 0
        while start_pointer < end_pointer:  # Searching availible free space
            if blocks_map[start_pointer] != ".":    # Skip if not "."
                start_pointer += 1
                continue
            space_start = start_pointer
            while True:         # Collecting all near empty blocks
                start_pointer += 1
                if blocks_map[start_pointer] == ".":
                    continue
                else:
                    space_end = start_pointer - 1
                    break
            if (space_end - space_start) < (block_end - block_start):
                # Skips if file lenght > empty space
                continue
            else:
                for i in range(block_start, block_end+1):
                    blocks_map[space_start] = blocks_map[i]
                    blocks_map[i] = "."
                    space_start += 1
                break
    return blocks_map


def get_filesystem_checksum(line: list[str]) -> int:
    output: int = 0
    for id, num in enumerate(line):
        if num != ".":
            output += id * int(num)
    return output


if __name__ == "__main__":
    start = time.time()
    with open("data.txt", "r") as file:
        text = file.read().strip()
    disk = disk_map_to_blocks(text)
    fragmented_disk = fragment_disk_data(disk)
    compressed_disk = compress_disk_data(disk)
    frag_checksum = get_filesystem_checksum(fragmented_disk)
    comp_checksum = get_filesystem_checksum(compressed_disk)
    print(f'1st answer: {frag_checksum}')
    print(f'2st answer: {comp_checksum}')
    end = time.time()
    print(end-start)