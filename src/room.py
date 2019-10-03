# Implement a class to hold room information. This should have name and
# description attributes.
# add ability  to add items to room
# items will be a list
# add loop that displays all items that are in the current room

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

        if items is None:
            self.items = []

    def __str__(self):
        item_name = ''
        for item in self.items:
            item_name += f"{item.name}  "
        return f"\n Room name: {self.name}  Room Description: {self.description}, \n items in this room: {item_name} \n"

    def on_take(self, item_name):
        selected_item = ''
        unselected_item = []
        for item in self.items:
            if item_name == item.name:
                selected_item = item_name
            else:
                unselected_item.append(item)
            self.items = unselected_item

        if selected_item == '':
            return 'item does not exist'
        else:
            return f'You have picked up {item_name}'
