# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location='outside'):
        self.name = name
        self.location = location
        self.items = []

    def __str__(self):
        output = f"{self.name}."
        return output

    def getLocation(self):
        return self.location

    def getItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)
