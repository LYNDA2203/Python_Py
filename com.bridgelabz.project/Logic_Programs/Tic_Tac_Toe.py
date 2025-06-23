import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print("\nBoard:")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def is_winner(self, mark):
        # Check rows, columns and diagonals
        for i in range(3):
            if all(self.board[i][j] == mark for j in range(3)) or \
               all(self.board[j][i] == mark for j in range(3)):
                return True

        if all(self.board[i][i] == mark for i in range(3)) or \
           all(self.board[i][2 - i] == mark for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col, mark):
        if self.is_valid_move(row, col):
            self.board[row][col] = mark
            return True
        return False

    def computer_move(self):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.make_move(row, col, 'O'):
                print(f"Computer placed 'O' at ({row}, {col})")
                break

    def user_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if self.make_move(row, col, 'X'):
                    print(f"You placed 'X' at ({row}, {col})")
                    break
                else:
                    print("Invalid move. Cell already occupied or out of bounds.")
            except ValueError:
                print("Invalid input. Please enter numeric values between 0 and 2.")

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while True:
            self.computer_move()
            self.print_board()
            if self.is_winner('O'):
                print("Computer wins!")
                break
            if self.is_full():
                print("It's a draw!")
                break

            self.user_move()
            self.print_board()
            if self.is_winner('X'):
                print("You win!")
                break
            if self.is_full():
                print("It's a draw!")
                break


# ----------- Start Game -------------
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
