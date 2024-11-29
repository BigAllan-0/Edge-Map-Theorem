def print_grid(grid):
    """Prints the grid in a readable format."""
    for row in grid:
        print(" ".join(row))
    print()

def create_empty_grid(size):
    """Creates an empty grid of given size filled with '*'."""
    return [['*' for _ in range(size)] for _ in range(size)]