from pathlib import Path


def max_bank_joltage_part1(line: str) -> int:
    digits = [int(ch) for ch in line.strip() if ch.isdigit()]
    n = len(digits)
    if n < 2:
        return 0

    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = max(digits[i], suffix[i + 1])

    best = 0
    for i in range(n - 1):
        candidate = digits[i] * 10 + suffix[i + 1]
        if candidate > best:
            best = candidate
            if best == 99:
                break
    return best


def max_bank_joltage_part2(line: str, pick: int = 12) -> int:
    digits = [int(ch) for ch in line.strip() if ch.isdigit()]
    n = len(digits)
    if n < pick:
        return 0

    remove = n - pick
    stack: list[int] = []
    for idx, digit in enumerate(digits):
        remaining = n - idx - 1
        while (
            stack
            and remove > 0
            and stack[-1] < digit
            and len(stack) + remaining >= pick
        ):
            stack.pop()
            remove -= 1
        stack.append(digit)

    if remove > 0:
        stack = stack[:-remove]
    elif len(stack) > pick:
        stack = stack[:pick]

    return int("".join(str(d) for d in stack))


def main() -> None:
    lines = [
        line.strip()
        for line in Path('Day_3.txt').read_text().splitlines()
        if line.strip()
    ]

    part1 = sum(max_bank_joltage_part1(line) for line in lines)
    part2 = sum(max_bank_joltage_part2(line) for line in lines)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
