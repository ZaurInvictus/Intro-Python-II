# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = []
        self.exits = []
        self.items = []

    def __str__(self):
        output = f"{self.name}\n{self.description}"
        # for exit in self.exits:
        #     output += f'\nExit to the {exit}'
        return output

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    exits = []
    linked_rooms = []
