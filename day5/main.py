from functools import cmp_to_key
from typing import List, Tuple
from math import floor


class Printer:
    def __init__(self, raw_rules: List[str], raw_instructions: List[str]) -> None:

        # Converts rules list from ["3|2", "5|1"] to [(3,2), (5,1)]
        self.rules: List[Tuple[int, int]] = [
            (int(x), int(y)) 
            for (x,y) in (s.split("|") for s in raw_rules)
        ]
        # Converts pages list from ["3,4,6,8", "1,3,2,5"] to [[3,4,6,8], [1,3,2,5]]
        self.instructions: List[List[int]] = [
            list(map(int, x.split(","))) 
            for x in raw_instructions
        ]

    def _check_instruction(self, instruction: List[int]) -> bool:
        for left, right in self.rules:
            if left in instruction and right in instruction:
                if instruction.index(left) > instruction.index(right):
                    return False
        return True

    def _get_middle_pages_sum(self, instructions) -> int:
        return sum([x[floor(len(x)/2)] for x in instructions])

    def get_good_instructions(self) -> List[List[int]]:
        return [
            instruction 
            for instruction in self.instructions
            if self._check_instruction(instruction)
        ]

    def get_bad_instructions(self) -> List[List[int]]:
        return [
            instruction 
            for instruction in self.instructions
            if not self._check_instruction(instruction)
        ]

    def convert_bad_to_good_instructions(self) -> List[List[int]]:
        bad_instructions = self.get_bad_instructions()
        output = []
        def comapare_pages(page1: int, page2: int) -> int:
            for left, right in self.rules:
                if left == page1 and right == page2:
                    return -1
                if left == page2 and right == page1:
                    return 1
            return 0

        for instruction in bad_instructions:
            instruction.sort(key=cmp_to_key(comapare_pages))
            output.append(instruction)

        return output

    def get_mid_good_pages_sum(self) -> int:
        return self._get_middle_pages_sum(self.get_good_instructions())

    def get_mid_bad_converted_pages_sum(self) -> int:
        return self._get_middle_pages_sum(self.convert_bad_to_good_instructions())

if __name__ == "__main__":
    with open("/home/dandead/Projects/aoc2024/day5/data.txt", "r") as file:
        text = file.read()
        list_of_rules, list_of_pages = text.split('\n\n')
        list_of_rules = list_of_rules.split("\n")
        list_of_instructions = list_of_pages.split("\n")
    printer = Printer(list_of_rules, list_of_instructions)
    print(printer.get_mid_good_pages_sum())
    print(printer.get_mid_bad_converted_pages_sum())