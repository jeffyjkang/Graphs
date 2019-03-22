# Implement a class to hold room information. This should have name and
# description attributes.

# room class, holds id, name, descript, potential paths, and coordinates (x,y)


class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"
    # created repr so when invoke name, returns name of room, which should be number

    def __repr__(self):
        return self.name

    # prints room description
    def printRoomDescription(self, player):
        print(str(self))
    # function that appends exits to list if room has exits to n,s,w,e

    def getExits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    # returns string of all exits available for room
    def getExitsString(self):
        return f"Exits: [{', '.join(self.getExits())}]"
    # function to connect the room, if passed in direction, and passed in
    # connectingRoom exists, assign room _to current room

    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.n_to = connectingRoom
            connectingRoom.s_to = self
        elif direction == "s":
            self.s_to = connectingRoom
            connectingRoom.n_to = self
        elif direction == "e":
            self.e_to = connectingRoom
            connectingRoom.w_to = self
        elif direction == "w":
            self.w_to = connectingRoom
            connectingRoom.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    # function returns room that exists in direction of passed in argument
    # if direction is not valid returns none
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    # function that returns x and y coordinates of room
    def getCoords(self):
        return [self.x, self.y]

    # def printRooms(self):
    #     rotatedRoomGrid = []
    #     for i in range(0, len(self.roomGrid)):
    #         rotatedRoomGrid.append([None] * len(self.roomGrid))
    #     for i in range(len(self.roomGrid)):
    #         for j in range(len(self.roomGrid[0])):
    #             rotatedRoomGrid[len(self.roomGrid[0]) -
    #                             j - 1][i] = self.roomGrid[i][j]
    #     roomGrid = rotatedRoomGrid
    #     map_str = ""
    #     for row in roomGrid:
    #         map_str += "#"
    #         for room in row:
    #             if room is not None and room.n_to is not None:
    #                 map_str += "  |  "
    #             else:
    #                 map_str += "     "
    #         map_str += "#\n"
    #         # Print room row
    #         map_str += "#"
    #         for room in row:
    #             if room is not None and room.w_to is not None:
    #                 map_str += "-"
    #             else:
    #                 map_str += " "
    #             if room is not None:
    #                 map_str += f"{room.id}".zfill(3)
    #             else:
    #                 map_str += "   "
    #             if room is not None and room.e_to is not None:
    #                 map_str += "-"
    #             else:
    #                 map_str += " "
    #         map_str += "#\n"
    #         map_str += "#"
    #         for room in row:
    #             if room is not None and room.s_to is not None:
    #                 map_str += "  |  "
    #             else:
    #                 map_str += "     "
    #         map_str += "#\n"
    #     print(map_str)
