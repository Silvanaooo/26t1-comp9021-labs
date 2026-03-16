def f_1(*L) -> None :
    """
    Draw a (2n+1)×(2n+1) grid representing an axis-aligned closed polyline
    defined by a permutation of 1..n (n is even, n ≥ 4). The sequence alternates
    x and y, starting with x, and wraps around to close the path.
    :param *L: int. A permutation of 1..n in some order (n even, n ≥ 4).
    :return: This function prints the grid to stdout; it does not return a value.
    """
    black_square = '\N{Black Large Square}'
    white_square = '\N{White Large Square}'

    # Extend the input by repeating the first element at the end to make
    # "wrap-around" access safe when we look at L[i+1].
    L_add = list(L) + [L[0]]

    # Build the list of geometric points as (x, y) pairs.
    points = []
    for i in range(1, len(L_add), 2):
        xn = L_add[i - 1]  # x on the left of y
        xm = L_add[i + 1]  # x on the right of y (wrap-around already handled)
        y = L_add[i]  # current y
        points.append((xn, y))
        points.append((xm, y))

    # Close the polygonal chain by appending the first point again as the last point.
    points_adjust = points + [points[0]]

    # Map each geometric point (x, y) to a "thickened" grid coordinate:
    points_adjust_again = [(2 * y - 1, 2 * x - 1) for x, y in points_adjust]

    # Prepare a boolean grid (visited) of size (2n+1)×(2n+1).
    # visited[row][col] == True means "this cell should be black".
    visited = [[False for _ in range(2 * len(L) + 1)] for _ in range(2 * len(L) + 1)]

    # Draw each segment between consecutive mapped points.
    # NOTE: Although variables are named x1,y1 etc., after mapping the first
    # component is "row" and the second component is "col".
    for points_index in range(len(points_adjust_again) - 1):
        x1, y1 = points_adjust_again[points_index]  # actually (row1, col1)
        x2, y2 = points_adjust_again[points_index + 1]  # actually (row2, col2)
        if x1 == x2:
            # Horizontal move on the grid: same row, varying columns.
            # Fill all columns between the two endpoints (inclusive).
            for y in range(min(y1, y2), max(y1, y2) + 1):
                visited[x1][y] = True
        if y1 == y2:
            # Vertical move on the grid: same column, varying rows.
            # Fill all rows between the two endpoints (inclusive).
            for x in range(min(x1, x2), max(x1, x2) + 1):
                visited[x][y1] = True

    # Convert the boolean visited grid into a character grid ("⬛"/"⬜").
    # (This creates a separate grid so the printing loop stays simple and readable.)
    grid = [[False for _ in range(2 * len(L) + 1)] for _ in range(2 * len(L) + 1)]
    for row in range(2 * len(L) + 1):
        for col in range(2 * len(L) + 1):
            if visited[row][col]:
                grid[row][col] = "⬛"  # or use black_square
            else:
                grid[row][col] = "⬜"  # or use white_square

    # Print the grid row by row as a single string per line.
    for line in grid:
        print("".join(line))


def closed_path(*x_y_coordinates) -> None:
    """
    Draw a (2n+1)×(2n+1) grid representing an axis-aligned closed polyline
    defined by a permutation of 1..n (n is even, n ≥ 4). The sequence alternates
    x and y, starting with x, and wraps around to close the path.
    :param *L: int. A permutation of 1..n in some order (n even, n ≥ 4).
    :return: This function prints the grid to stdout; it does not return a value.
    """
    black_points = set()  # set of (row, col) that should be drawn black

    # --- First pass: horizontal segments ---
    # i runs over all odd indices (y positions).
    for i in range(1, len(x_y_coordinates), 2):
        y = x_y_coordinates[i]
        # Left and right x-values: previous and next entries, with wrap-around.
        x_1, x_2 = sorted((x_y_coordinates[i - 1],
                           x_y_coordinates[(i + 1) % len(x_y_coordinates)]
                          )
                         )
        # Fill black points along the horizontal line.
        for x in range(x_1, x_2):
            black_points.add((2 * y - 1, 2 * x - 1))
            black_points.add((2 * y - 1, 2 * x))
        # Add the endpoint (last column on the right).
        black_points.add((2 * y - 1, 2 * x + 1))

    # --- Second pass: vertical segments ---
    # i runs over all even indices (x positions).
    for i in range(0, len(x_y_coordinates), 2):
        x = x_y_coordinates[i]
        # Below and above y-values: previous and next entries, with wrap-around.
        y_1, y_2 = sorted((x_y_coordinates[(i - 1) % len(x_y_coordinates)],
                           x_y_coordinates[i + 1]
                          )
                         )
        # Fill black points along the vertical line.
        for y in range(y_1, y_2):
            black_points.add((2 * y - 1, 2 * x - 1))
            black_points.add((2 * y, 2 * x - 1))
        # Add the endpoint (last row at the bottom).
        black_points.add((2 * y + 1, 2 * x - 1))

    # --- Printing phase ---
    # Grid size is (2n+1) × (2n+1), where n = len(x_y_coordinates).
    for y in range(2 * len(x_y_coordinates) + 1):
        for x in range(2 * len(x_y_coordinates) + 1):
            # Print black if (y, x) is in black_points, else white.
            print('\N{Black Large Square}', end='')\
                    if (y, x) in black_points\
                    else print('\N{White Large Square}', end='')
        print()