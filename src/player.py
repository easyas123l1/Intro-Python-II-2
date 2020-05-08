# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    def move_to(self, direction, current_loc):
        # try to move in the specified direction
        attribute = direction + '_to'

        # if can move in specified direction from current location
        if hasattr(current_loc, attribute):
            return getattr(current_loc, attribute)

        print("You can't go that way\n")

        return current_loc

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.pop(item)
