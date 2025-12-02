from pathlib import Path

# --- Part 1: Count Zero Hits in Rotations --- #
def count_zero_hits(rotations: list[str], size: int = 100, start: int = 50) -> int:
    position = start
    zero_hits = 0
    for rotation in rotations:
        direction = rotation[0]
        value = int(rotation[1:])
        if direction == "L":
            position = (position - value) % size
        else:
            position = (position + value) % size
        if position == 0:
            zero_hits += 1
    return zero_hits

# --- Part 2: Every zero hit count --- #

def ceil_div(a: int, b: int) -> int:
    return -(-a // b)

def left_zero_hits(position: int, steps: int, size: int) -> int:
    upper = position - 1
    lower = position - steps
    k_max = upper // size
    k_min = ceil_div(lower, size)
    count = k_max - k_min + 1
    return count if count > 0 else 0

def count_zero_hits_method_0x434C49434B(rotations: list[str], size: int = 100, start: int = 50) -> int:
    position = start
    zero_hits = 0
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == "R":
            zero_hits += (position + steps) // size
            position = (position + steps) % size
        else:
            zero_hits += left_zero_hits(position, steps, size)
            position = (position - steps) % size
    return zero_hits


if __name__ == "__main__":
    rotations = [line.strip() for line in Path("Day_1.txt").read_text().splitlines() if line.strip()]
    print("Part 1:", count_zero_hits(rotations))
    print("Part 2 (0x434C49434B):", count_zero_hits_method_0x434C49434B(rotations))
