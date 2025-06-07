import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # 行と列のチェック
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # 対角線のチェック
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        if current_player == "X":
            try:
                row = int(input(f"プレイヤー {current_player} の行 (0, 1, 2): "))
                col = int(input(f"プレイヤー {current_player} の列 (0, 1, 2): "))
            except ValueError:
                print("無効な入力です。0, 1, 2 のいずれかを入力してください。")
                continue
        else:
            row, col = get_computer_move(board)
            print(f"コンピュータ {current_player} の行: {row}, 列: {col}")
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"プレイヤー {current_player} の勝ち!")
                break
            elif is_full(board):
                print_board(board)
                print("引き分け!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("その場所は既に埋まっています。もう一度試してください。")

if __name__ == "__main__":
    main()
