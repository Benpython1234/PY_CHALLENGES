#TIC TAC TOE
def Board_maker(board):
    for row in board:
         print(" | ".join(row))
         print("-"*9)

def check_winner(board):
     for i in range(3):
          if board[i][0]== board[i][1] == board[i][2] != " ":
               return board[i][0]
          if board[0][i]== board[1][i] == board[2][i] != " ":
               return board[0][i]
          
     if board[0][0]== board[1][1] == board[2][2] != " ":
               return board[0][0]
     if board[0][2]== board[1][1] == board[2][0] != " ":
               return board[0][2]
     return None

def full_board(board):
      return all(cell != " " for row in board for cell in row)
def main_board(board):
      board = [[" " for _ in range(3)]for _ in range(3)]
      current_player = "X"
      while True:
        Board_maker(board)
        try:
            row = int(input(f"Player {current_player}, enter the row (0-2): "))
            col = int(input(f"Player {current_player}, enter the column (0-2): "))

            if board[row][col] == " ":
                board[row][col] = current_player
                winner = check_winner(board)

                if winner:
                    Board_maker(board)
                    print(f"Player {winner} wins!")
                    break
                elif full_board(board):
                    print("It's a draw!")
                    break

                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")


if __name__ == "__main__":
    main_board()