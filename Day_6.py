from pathlib import Path
from math import prod


def parse_grid(path: str) -> list[str]:
    lines = Path(path).read_text().splitlines()
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]


def column_ranges(grid: list[str]) -> list[tuple[int, int]]:
    height = len(grid)
    width = len(grid[0])
    ranges: list[tuple[int, int]] = []
    start = None
    for col in range(width):
        if all(grid[row][col] == ' ' for row in range(height)):
            if start is not None:
                ranges.append((start, col))
                start = None
        else:
            if start is None:
                start = col
    if start is not None:
        ranges.append((start, width))
    return ranges


def extract_operator(grid: list[str], left: int, right: int) -> str:
    op = grid[-1][left:right].strip()
    if op not in {'+', '*'}:
        raise ValueError(f'Unknown operator: {op!r}')
    return op


def solve_part1(grid: list[str]) -> int:
    total = 0
    for left, right in column_ranges(grid):
        operands = [
            int(row[left:right].strip())
            for row in grid[:-1]
            if row[left:right].strip()
        ]
        op = extract_operator(grid, left, right)
        total += sum(operands) if op == '+' else prod(operands)
    return total


def column_numbers(grid: list[str], left: int, right: int) -> list[int]:
    height = len(grid) - 1
    numbers: list[int] = []
    for col in range(right - 1, left - 1, -1):
        digits = ''.join(
            grid[row][col]
            for row in range(height)
            if grid[row][col].isdigit()
        )
        if digits:
            numbers.append(int(digits))
    return numbers


def solve_part2(grid: list[str]) -> int:
    total = 0
    for left, right in column_ranges(grid):
        operands = column_numbers(grid, left, right)
        op = extract_operator(grid, left, right)
        total += sum(operands) if op == '+' else prod(operands)
    return total


def solve(path: str) -> tuple[int, int]:
    grid = parse_grid(path)
    return solve_part1(grid), solve_part2(grid)


if __name__ == '__main__':
    part1, part2 = solve('Day_6.txt')
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
