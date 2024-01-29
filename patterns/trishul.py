for row in range(12):
    for col in range(11):
        if (row == 5 and (1 < col < 9) or (col == 5 and row != 5) or ((col == 1 or col == 9) and (1 < row < 5)) or (
                row == 1 and (col == 0 or col == 10))):
            print("*", end=" ")
        else:
            print(end="  ")

    print()
