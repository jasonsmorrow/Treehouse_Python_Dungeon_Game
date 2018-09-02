import random
from os import system, name

# DONE - draw grid
# DONE - pick random location for player
# DONE - pick random location for exit door
# DONE - pick random location for monster
# DONE - draw player in the grid
# DONE - take input for movement
# DONE - move player unless invalid move (past edge of grid)
# DONE - check for win/loss
# DONE - clear screen and redraw grid

CELLS = [
  (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
  (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
  (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
  (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
  (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_map(player, icon='@'):
    # if player at location, draw player
    cell_border = "-" * 11
    game_map = [cell_border]
    for y in range(5):
        current_row = "|"
        for x in range(5):
            if player[0] == x and player[1] == y:
                current_row += '{}|'.format(icon)
            else:
                current_row += ' |'
        game_map.append(current_row)
        game_map.append(cell_border)
    
    clear()
    for item in game_map:
        print(item)


def get_locations():

    return random.sample(CELLS, 3)


def move_player(player, this_move):
    # get the player's location
    # if move == LEFT, x-1
    if this_move == 'LEFT':
        player = (player[0] - 1, player[1])
    # if move == RIGHT, x+1
    if this_move == 'RIGHT':
        player = (player[0] + 1, player[1])
    # if move == UP, y-1
    if this_move == 'UP':
        player = (player[0], player[1] - 1)
    # if move == DOWN, y-1
    if this_move == 'DOWN':
        player = (player[0], player[1] + 1)
    return player


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player's y == 0, they can't move up
    if player[1] == 0:
        moves.remove('UP')
    # if player's y == 4, they can't move down
    if player[1] == 4:
        moves.remove('DOWN')
    # if player's x == 0, they can't move left
    if player[0] == 0:
        moves.remove('LEFT')
    # if player's x == 4, they can't move right
    if player[0] == 4:
        moves.remove('RIGHT')
    return moves


# Initial setup - choose player, door, and monster location
player_one, door, monster = get_locations()
print("Welcome to the dungeon!")
print_map(player_one)

while True:
    print("You're currently in room {}".format(player_one))  # fill with player position
    print("You can move {}".format(get_moves(player_one))) # fill with available moves
    print("Enter QUIT to quit")
  
    move = input("> ")
    move = move.upper()
  
    if move == 'QUIT':
        break
    elif move in get_moves(player_one):
        player_one = move_player(player_one, move)
        if player_one == door:
            print_map(player_one, '#')
            print('You escaped the dungeon!')
            break
        elif player_one == monster:
            print_map(player_one, '%')
            print('You have been eaten by a grue!')
            break
        else:
            print_map(player_one)
    else:
        print("You can't move {}.  Please try again.".format(move))
  
    # DONE - Good move?  Change position
    # DONE - Bad move? Dont' change anything
    # DONE - On the door? They win!
    # DONE - On the monster? They lose!
    # DONE - Otherwise, loop back around
