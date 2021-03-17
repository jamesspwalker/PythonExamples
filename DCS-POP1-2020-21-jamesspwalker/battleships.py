#see the readme.md file for description and data
import random
import re

def is_sunk(ship):
    if len(ship[4]) == ship[3]:
        return True
    else:
        return False

def ship_type(ship):
    if ship[3] == 1:
        return "submarine"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"
    else:
        return "error"

def is_open_sea(row, column, fleet):
    open_sea = True
    dx = [1,1,1,0,0,0,-1,-1,-1]
    dy = [1,0,-1,1,0,-1,1,0,-1]
    for ship in fleet:
        for i in range(ship[3]):
            for j in range(9):
                if ship[2]:
                    if (row, column) == (ship[0] + dx[j], ship[1] + dy[j] + i):
                        open_sea = False
                elif not ship[2]:
                    if (row, column) == (ship[0] + dx[j] + i, ship[1] + dy[j]):
                        open_sea = False
    return open_sea

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    ok = True
    for i in range(length):
        if horizontal:
            if not is_open_sea(row, column + i, fleet):
                ok = False
            if column + i > 9:
                ok = False
        elif not horizontal:
            if not is_open_sea(row + i, column, fleet):
                ok = False
            if row + i > 9:
                ok = False

    return ok


def place_ship_at(row, column, horizontal, length, fleet):
    if ok_to_place_ship_at(row, column, horizontal, length, fleet):
        newShip = (row, column, horizontal, length, set())
        fleet.append(newShip)
    else:
        print("Error: Unable to place ship")

def randomly_place_all_ships():
    fleet = []
    while len(fleet) < 1:
        row = random.randint(0,9)
        column = random.randint(0,9)
        horizontal = random.randint(0,1)
        length = 4
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
    while len(fleet) < 3:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        horizontal = random.randint(0, 1)
        length = 3
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
    while len(fleet) < 6:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        horizontal = random.randint(0, 1)
        length = 2
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
    while len(fleet) < 10:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        horizontal = random.randint(0, 1)
        length = 1
        if ok_to_place_ship_at(row, column, horizontal, length, fleet):
            place_ship_at(row, column, horizontal, length, fleet)
    return fleet

def check_if_hits(row, column, fleet):
    hit = False
    for ship in fleet:
        for i in range(ship[3]):
            if (row, column) not in ship[4]:
                if ship[2]:
                    if (row, column) == (ship[0], ship[1] + i):
                        hit = True
                elif not ship[2]:
                    if (row, column) == (ship[0] + i, ship[1]):
                        hit = True
    return hit

def hit(row, column, fleet):
    if check_if_hits(row, column, fleet):
       for ship in fleet:
           for i in range(ship[3]):
               if ship[2]:
                   if (row, column) == (ship[0], ship[1] + i):
                       ship[4].add((row, column))
                       hit_ship = ship
               elif not ship[2]:
                   if (row, column) == (ship[0] + i, ship[1]):
                       ship[4].add((row, column))
                       hit_ship = ship
    return sorted(fleet), hit_ship

def are_unsunk_ships_left(fleet):
    ships_left = False
    for ship in fleet:
        if not is_sunk(ship):
            ships_left = True
    return ships_left

def main():
    current_fleet = randomly_place_all_ships()
    print(current_fleet)
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
                print("You have a hit!")
                (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                print(current_fleet)
                if is_sunk(ship_hit):
                    print("You sank a " + ship_type(ship_hit) + "!")
            else:
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


if __name__ == '__main__': #keep this in
   main()
