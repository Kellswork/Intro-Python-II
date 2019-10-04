# Write a class to hold player information, e.g. what room they are in
# currently.
# Player class should have an inventory
# add functionality that adds item to the player inventory
# invertory should be a list in player

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return (f"player name: {self.name}\n "
                f"your current room: {self.current_room}")

    # def on_take(self, item_name):
    #     if item_name in self.current_room['items']:
    #         print('here')
    #     else:
    #         print('not here')
        # for item in self.current_room.items:
        #     print('item.name: ', item.name)
        #     if item_name == item.name:
        #         print('item_name: ', item_name)
        #         print('here')
        #     else:
        #         print('not here')

        # return f"You have picked up {item_name}"