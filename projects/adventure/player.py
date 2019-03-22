# player class to create player object
# accepts name and starting room as parameters


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    # travel function, accepts direction as parameter, show rooms is set to false
    def travel(self, direction, showRooms=False):
        # invoke getRoomInDirection from currentroom pass in direction, assign to nextRoom
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        # if condition as long as nextRoom is not None
        if nextRoom is not None:
            # update current room to next room
            self.currentRoom = nextRoom
            # if showroom exists, print description, (not doing this)
            if (showRooms):
                nextRoom.printRoomDescription(self)
        # if next room is none, print error
        else:
            print("You cannot move in that direction.")
