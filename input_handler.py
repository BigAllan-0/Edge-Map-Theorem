def get_dot_location(dot_label, grid_size):
    """
    Asks the user for the (X, Y) location of a dot and validates the input.
    Args:
        dot_label: A string representing the dot label (e.g., "A1", "B2").
        grid_size: Size of the grid printed on command line.
    Returns:
        A tuple (x, y) representing the dot's location.
    """
    while True:
        try:
            location = input(f"Where is Dot {dot_label}? Enter as (X,Y): ").strip()
            x, y = map(int, location.strip("()").split(","))
            if 0 <= x < grid_size and 0 <= y < grid_size:
                return (x, y)
            else:
                print(f"Invalid location! Please enter values between 0 and {grid_size - 1}.")
        except ValueError:
            print("Invalid format! Please enter the location in the format (X,Y).")

from grid_utils import print_grid

def place_dots_on_grid(grid, dot_pairs):
    """
    Places dots on the grid based on user-provided locations.
    Args:
        grid: The grid to update printed on command line.
        dot_pairs: A list of tuples representing dot labels (e.g., ['A1', 'A2']).
    """
    for dot_label in dot_pairs:
        x, y = get_dot_location(dot_label, len(grid))
        grid[x][y] = dot_label[0]  # Use the first letter of the dot label as the color
        print(f"Placed Dot {dot_label} at ({x}, {y}). Current Grid:")
        print_grid(grid)
