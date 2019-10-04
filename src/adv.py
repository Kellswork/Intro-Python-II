from room import Room
from player import Player
from item import Item

# Declare all the rooms
from src.item import Item

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# create a dictionary of items and append the key to some rooms

item = {
    'outside': [Item("bones", "the bones of those who have walked this path be with you"),
                Item("stones", "cast your stones wisely, it might save you")],
    'foyer': [Item("torch", "may the light guide your direction"),
              Item("mask", "protection for the dusty path ahead")],
    'overlook': [Item("rope", "climb down this slippy slope"),
                 Item("axe", "chop doen a tree to build your bridge")],
    'treasure': [Item("tears", "free your heart of the pain of your loss"),
                 Item("sandals", "the journey out of here might be a long one")],
}

room['outside'].items = item['outside']
room['foyer'].items = item['foyer']
room['overlook'].items = item['overlook']
room['treasure'].items = item['treasure']

# when user wants to see their inventory, write if statement to check if it is empty or not

# Make a new player object that is currently in the 'outside' room.
player = Player('kelechi', room['outside'])


# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# code for player movement

def move_player(move, current_room):
    attrib = move + '_to'
    if hasattr(current_room, attrib):
        return getattr(current_room, attrib)

    print('you cannot go that direction')

    return current_room


done = False

while not done:
    print(player.current_room)
    direction = input("choose a direction:'n', 's', 'e', 'w' 'q' to quit: ").lower().strip().split()
    if direction == 'q':
        print('Later')
        done = True

    elif direction in ['n', 's', 'e', 'w']:
        player.current_room = move_player(direction, player.current_room)

    elif direction[0] == 'get' or 'take':
        print(player.current_room.on_take(direction[1]))

    else:
        print('invalid input, please try again')
# add item list to the Room class
# add a loop that will display all the items in each room
