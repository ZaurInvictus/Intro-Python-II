from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].exits = ['n']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].exits = ['n', 's', 'e']

room['overlook'].s_to = room['foyer']
room['overlook'].exits = ['s']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].exits = ['w', 'n']

room['treasure'].s_to = room['narrow']
room['treasure'].exits = ['s']

#
# Main
#

# Items
item = {
    'torch': Item('a torch', 'A stick that has been wrapped in oiled cloth, the cloth is aflame.')
}
room['outside'].addItem(item['torch'])

#
# Player
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(input('Enter your name, adventurer.\n'))
location = player1.getLocation()
currentRoom = room[player1.getLocation()]
choice = ''

# print(room[location].n_to)
# print(f'{player1.name} is at {room[location]}')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("""Welcome to the game!\n""")

while choice != 'q':
    print(f'Your Location:\n{currentRoom}')
    exits = currentRoom.exits
    items = currentRoom.items
    if len(items) > 0:
        print(f'On the ground lies:')
        for item in items:
            print(item.name)
    choice = input(
        f'Choose your path, {player1.name}.\nThere are exits to the {exits[:]}:\nEnter q to Quit.')
    if len(choice) == 1:
        if choice == 'n' or choice == 'north' or choice == 'North' and dir(currentRoom).count('n_to') > 0:
            newRoom = currentRoom.n_to
            currentRoom = newRoom
            continue
        elif choice == 's' and dir(currentRoom).count('s_to') > 0:
            newRoom = currentRoom.s_to
            currentRoom = newRoom
            continue
        elif choice == 'e' and dir(currentRoom).count('e_to') > 0:
            newRoom = currentRoom.e_to
            currentRoom = newRoom
            continue
        elif choice == 'w' and dir(currentRoom).count('w_to') > 0:
            newRoom = currentRoom.w_to
            currentRoom = newRoom
            continue
        elif choice == 'q' or choice == 'quit' or choice == 'qq' or choice == 'QQ' or choice == 'Q':
            print('Farewell,', player1.name)
            exit
        else:
            print(f'{room[location]}')
            exits = room[location].exits
            choice = input(
                f'Your last choice was invalid.\nChoose your path, {player1.name}.\nThere are exits to the {exits[:]}:\nEnter q to Quit.')
    else:
        choice = input('Incorrect')












