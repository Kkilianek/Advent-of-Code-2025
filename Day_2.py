def generate_invalid_ids(start: int, end: int, min_repetitions: int = 2,
                         max_repetitions: int | None = None) -> set[int]:

    invalid_ids = set()

    pattern = 1
    while True:
        pattern_str = str(pattern)

        repetitions = min_repetitions
        if max_repetitions:
            max_reps = max_repetitions
        else:
            max_reps = len(str(end)) // len(pattern_str) + 1

        while repetitions <= max_reps:
            repeated = int(pattern_str * repetitions)

            if repeated > end:
                break

            if repeated >= start:
                invalid_ids.add(repeated)

            repetitions += 1

        if int(pattern_str * min_repetitions) > end:
            break

        pattern += 1

    return invalid_ids


def solve_range(ranges_str: str, min_repetitions: int = 2,
                max_repetitions: int | None = None) -> int:
    total = 0
    for range_part in ranges_str.split(','):
        start, end = map(int, range_part.split('-'))
        invalid_ids = generate_invalid_ids(start, end, min_repetitions, max_repetitions)
        total += sum(invalid_ids)
    return total


def solve_part1(ranges_str: str) -> int:
    return solve_range(ranges_str, min_repetitions=2, max_repetitions=2)



def solve_part2(ranges_str: str) -> int:
    return solve_range(ranges_str, min_repetitions=2, max_repetitions=None)


if __name__ == '__main__':
    with open('Day_2.txt') as f:
        ranges_str = f.read().strip()

    result_part1 = solve_part1(ranges_str)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(ranges_str)
    print(f"Part 2: {result_part2}")
