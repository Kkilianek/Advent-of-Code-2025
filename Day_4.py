from collections import deque
from pathlib import Path

OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def load_grid(path: str = "Day_4.txt") -> list[str]:
    return Path(path).read_text().splitlines()


def neighbors(r: int, c: int, rows: int, cols: int):
    for dr, dc in OFFSETS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc


def count_accessible_rolls(path: str = "Day_4.txt", grid: list[str] | None = None) -> int:
    if grid is None:
        grid = load_grid(path)
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            neighbor_count = sum(
                1 for nr, nc in neighbors(r, c, rows, cols) if grid[nr][nc] == "@"
            )
            if neighbor_count < 4:
                accessible += 1
    return accessible


def count_removable_rolls(path: str = "Day_4.txt", grid: list[str] | None = None) -> int:
    if grid is None:
        grid = load_grid(path)
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    rolls = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "@"}
    neighbor_counts: dict[tuple[int, int], int] = {
        (r, c): sum(1 for nr, nc in neighbors(r, c, rows, cols) if (nr, nc) in rolls)
        for r, c in rolls
    }
    queue = deque([pos for pos, cnt in neighbor_counts.items() if cnt < 4])
    removed = 0

    while queue:
        pos = queue.popleft()
        if pos not in rolls:
            continue
        rolls.remove(pos)
        neighbor_counts.pop(pos, None)
        removed += 1
        r, c = pos
        for nr, nc in neighbors(r, c, rows, cols):
            npos = (nr, nc)
            if npos not in rolls:
                continue
            neighbor_counts[npos] -= 1
            if neighbor_counts[npos] < 4:
                queue.append(npos)
    return removed


if __name__ == "__main__":
    grid_data = load_grid()
    part1 = count_accessible_rolls(grid=grid_data)
    part2 = count_removable_rolls(grid=grid_data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
