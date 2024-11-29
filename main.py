from grid_utils import create_empty_grid, print_grid
from input_handler import place_dots_on_grid

def main():
    grid_size = 5
    grid = create_empty_grid(grid_size)
    print("Initial Grid:")
    print_grid(grid)

    # Define the dot pairs
    dot_labels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']

    print("Place the dots on the grid.")
    place_dots_on_grid(grid, dot_labels)

    print("Final Grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()