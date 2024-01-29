for row in range(11):
    for col in range(11):
        if ((col == 0 and row < 5) or (col == 5) or (row == 5 and col != 5) or (row == 0 and col > 5) or
                (col == 10 and row > 5) or (row == 10 and col < 5)):
            print("*", end=" ")
        else:
            print(end="  ")

    print()
