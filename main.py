def put_move(board, move, player):
    positions = {
        "A1": (0, 0),
        "A2": (1, 0),
        "A3": (2, 0),
        "B1": (0, 1),
        "B2": (1, 1),
        "B3": (2, 1),
        "C1": (0, 2),
        "C2": (1, 2),
        "C3": (2, 2),
    }
    move_row, move_col = positions[move]
    if player == 1:
        board[move_row][move_col] = "X"
    elif player == 2:
        board[move_row][move_col] = "O"
    return board, player


def is_valid_move(board, move):
    positions = {
        "A1": (0, 0),
        "A2": (1, 0),
        "A3": (2, 0),
        "B1": (0, 1),
        "B2": (1, 1),
        "B3": (2, 1),
        "C1": (0, 2),
        "C2": (1, 2),
        "C3": (2, 2),
    }
    move_row, move_col = positions[move]
    if board[move_row][move_col] == " ":
        return True
    else:
        print("I'm sorry, but this place is taken. Choose somewhere else")
    return False


def is_tie(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    print("it's a tie")
    return True


def has_won(board, player):
    # check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] != " ":
                print(f"Player {player} has won")
                return True
    # check for horizontal wins
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] != " ":
                print(f"Player {player} has won")
                return True
    # check for diagonal win
    if (
        board[0][0] == board[1][1] == board[2][2]
        or board[0][2] == board[1][1] == board[2]
    ):
        if board[1][1] != " ":
            print(f"Player {player} has won")
            return True

    return False


def print_board(board):
    print(
        f"__A___B___C__\n|   |   |   |\n| {board[0][0]} | {board[0][1]} | {board[0][2]} |1\n|___|___|___|\n|   |   |   |\n| {board[1][0]} | {board[1][1]} | {board[1][2]} |2\n|___|___|___|\n|   |   |   |\n| {board[2][0]} | {board[2][1]} | {board[2][2]} |3\n|___|___|___|"
    )


def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Player 1 you are X, Player 2 you are O.")
    while True:
        player = 1
        print_board(board)
        move = input("Player 1, pick a place to put your letter (e.g. A1, B2, C3)")
        while is_valid_move(board, move) == False:
            move = input("Player 1, pick a place to put your letter (e.g. A1, B2, C3)")
        board, player = put_move(board, move, player)
        print_board(board)
        if has_won(board, player) == True or is_tie(board) == True:
            print("GAME OVER")
            break
        player = 2
        move_2 = input("Player 2, pick a place to put your letter (e.g. A1, B2, C3)")
        while is_valid_move(board, move_2) == False:
            move_2 = input(
                "Player 2, pick a place to put your letter (e.g. A1, B2, C3)"
            )
        board, player = put_move(board, move_2, player)
        if has_won(board, player) == True or is_tie(board) == True:
            print("GAME OVER")
            break


play_game()
