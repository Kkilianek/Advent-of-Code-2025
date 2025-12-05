from bisect import bisect_right
from pathlib import Path


def parse_input(path: str) -> tuple[list[tuple[int, ...]], list[int]]:
    content = Path(path).read_text().strip()
    ranges_block, ids_block = content.split('\n\n', 1)
    ranges = [
        tuple(map(int, line.split('-')))
        for line in ranges_block.splitlines()
        if line.strip()
    ]
    ids = [
        int(line)
        for line in ids_block.splitlines()
        if line.strip()
    ]
    return ranges, ids


def merge_ranges(ranges: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
            continue
        if start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def count_fresh(ids: list[int], merged_ranges: list[tuple[int, ...]]) -> int:
    starts = [start for start, _ in merged_ranges]
    count = 0
    for value in ids:
        idx = bisect_right(starts, value) - 1
        if idx >= 0 and merged_ranges[idx][0] <= value <= merged_ranges[idx][1]:
            count += 1
    return count


def count_total_fresh(merged_ranges: list[tuple[int, ...]]) -> int:
    return sum(end - start + 1 for start, end in merged_ranges)


def main():
    ranges, ids = parse_input('Day_5.txt')
    merged = merge_ranges(ranges)
    part1 = count_fresh(ids, merged)
    part2 = count_total_fresh(merged)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    main()
