from battleships import *

# generates base board
def generate_board():
   board = []
   for i in range(10):
      board.append(['.']*10)
   return board

# updates board whether hit or miss
def update_board(board, row, column, fleet):
   if check_if_hits(row, column, fleet):
      board[row][column] = "X"
   else:
      board[row][column] = "-"
   return board

# updates board if a ship is sunk
def update_board_sunk_ship(board, ship):
   for i in range(ship[3]):
      if ship_type(ship) == "submarine":
         board[list(ship[4])[i][0]][list(ship[4])[i][1]] = "S"
      if ship_type(ship) == "destroyer":
         board[list(ship[4])[i][0]][list(ship[4])[i][1]] = "D"
      if ship_type(ship) == "cruiser":
         board[list(ship[4])[i][0]][list(ship[4])[i][1]] = "C"
      if ship_type(ship) == "battleship":
         board[list(ship[4])[i][0]][list(ship[4])[i][1]] = "B"
   return board

# formats and prints out board
def print_board(board):
   print("   ", " ".join("0123456789"))
   print("   ", " ".join("__________"))
   for num, line, row in zip("0123456789", "||||||||||", board):
      print(num, line, " ".join(row))

def extension():
   print("extension")
   board = generate_board()
   print_board(board)
   current_fleet = randomly_place_all_ships()
   game_over = False
   shots = 0
   win = False
   while not game_over:
      str = input("Enter row and column to shoot (separated by a space): ")
      if str == "quit":
         game_over = True
      elif re.match("[0-9] [0-9]", str):
         loc_str = str.split()
         current_row = int(loc_str[0])
         current_column = int(loc_str[1])
         shots += 1
         already_hit = False
         for ship in current_fleet:
            if (current_row, current_column) in ship[4]:
               already_hit = True
         if not already_hit and check_if_hits(current_row, current_column, current_fleet):
            board = update_board(board, current_row, current_column, current_fleet)
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
               update_board_sunk_ship(board, ship_hit)
               print("You sank a " + ship_type(ship_hit) + "!")
            print_board(board)
         else:
            board = update_board(board, current_row, current_column, current_fleet)
            print_board(board)
            print("You missed!")

         if not are_unsunk_ships_left(current_fleet):
            win = True
            game_over = True
      else:
         print("please input valid input")
   if win:
      print("You win! You required", shots, "shots.")
   else:
      print("You quit, loser")

if __name__ == '__main__':
   extension()
