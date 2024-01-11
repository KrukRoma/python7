def board_and_coordinates():
    board = [[-1 for _ in range(8)] for _ in range(8)]

    x = int(input("Введіть рядок від 0 до 7 : "))
    y = int(input("Введіть стовбчик від 0 до 7 : "))

    coordinates = 0
    board[x][y] = coordinates
    return board, x, y, coordinates

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2,1), (-2,-1)]

def is_move(board, new_x, new_y):
    return 0 <= new_x < 8 and 0 <= new_y < 8 and board[new_x][new_y] == -1

def horse_recurse(board, x, y, coordinates, moves):
    if coordinates == 63:
        return True

    for move in moves:
        new_x, new_y = x + move[0], y + move[1]

        if is_move(board, new_x, new_y):
            board[new_x][new_y] = coordinates + 1

            if horse_recurse(board, new_x, new_y, coordinates + 1, moves):
                return True
            
            board[new_x][new_y] = -1

    return False


board, x, y, coordinates = board_and_coordinates()
success = horse_recurse(board, x, y, coordinates, moves)

if success:
    print("Шлях коня : ")
    for row in board:
        print(row)
else:
    print("Шлях коня не існує")

