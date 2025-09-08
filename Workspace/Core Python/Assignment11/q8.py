def snakes_ladder():
    board = []  # Final 2D list to hold rows

    # Create numbers from 1 to 100
    numbers = list(range(100, 0,-1))

    # Break into 10 rows of 10 numbers each
    for i in range(0, 100, 10):
        row = numbers[i:i+10]  # slicing
        if (i // 10) % 2 == 1:
            row.reverse()  # reverse every second row
        board.append(row)  # append to board

    # Print the board
    for row in board:
        print(" ".join(f"{num:3}" for num in row))

snakes_ladder()