from room import Room
import random
import math

# world class which constructs a world object has properties of starting room
# rooms, which is dict that will contain all of the rooms that are assigned a number
# roomGrid which will be a two dimensional list containing the room objects
# grid size which will be updated to contain the size of grid of rooms


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.roomGrid = []
        self.gridSize = 0

    # function load graph takes the provided roomGraph and creates the graph
    def loadGraph(self, roomGraph):
        # numRooms is initialized to the length of the roomGraph which is a
        # dict that has the room number as the key and the coordinates as the value
        numRooms = len(roomGraph)
        # rooms is initialized to have empty or the None key for each room in the room graph
        rooms = [None] * numRooms
        # print(f"rooms:{rooms}")
        # grid size initialized to 1
        gridSize = 1
        # loop through the number of numRooms, or length of roomGraph
        for i in range(0, numRooms):
            # arbitrary x is assigned to roomGraph at key i and the zeroith index
            # and zeroith index again which would be the first value of the tuple
            # which is the x coordinate at the ith room
            x = roomGraph[i][0][0]
            # print(x)
            # increment the gridSize, by reassigning it to the max of either the
            # x or y coordinates
            gridSize = max(gridSize, roomGraph[i][0][0], roomGraph[i][0][1])
            # reassign the rooms dict at key of i to a string which will provide value of
            # Room at i and the x and y coordinates
            self.rooms[i] = Room(
                f"Room {i}", f"({roomGraph[i][0][0]},{roomGraph[i][0][1]})", i, roomGraph[i][0][0], roomGraph[i][0][1])
        # initialize the roomGrid to empty list
        self.roomGrid = []
        # increment gridsize by 1, to accommodate list size
        # print(f'gridsize before increment: {gridSize}')
        gridSize += 1
        # print(f'gridsize after increment: {gridSize}')
        # assign graph gridsize to adjusted gridsize
        self.gridSize = gridSize
        # loop through the gridsize
        for i in range(0, gridSize):
            # print(f'roomGrid before append: {self.roomGrid}')
            # per iteration of gridSize, append None by length of gridsize
            self.roomGrid.append([None] * gridSize)
            # print(f'roomGrid after append: {self.roomGrid}')
        # for each key in roomGraph
        for roomID in roomGraph:
            # print(f'roomID: {roomID}')
            # assign the rooms dict key to roomID or key in roomgraph, then assign to room
            room = self.rooms[roomID]
            # reassign the roomGrid coordinates to room, which is rooms dict key
            # which in turn is roomGraph key
            self.roomGrid[room.x][room.y] = room
            # if the 'n' string is in the room graph at specific room :
            if 'n' in roomGraph[roomID][1]:
                # if n exists invoke connectRooms for the rooms dict at the
                # key of roomGraph, pass it n for direction and key of
                # rooms at roomGraph at specific room , index 1
                # and the value of the 'n' key, or room number
                self.rooms[roomID].connectRooms(
                    'n', self.rooms[roomGraph[roomID][1]['n']])
            # if the 's' string is in the room graph at specific room :
            if 's' in roomGraph[roomID][1]:
                # if s exists invoke connectRooms for the rooms dict at the
                # key of roomGraph, pass it s for direction and key of
                # rooms at roomGraph at specific room , index 1
                # and the value of the 's' key, or room number
                self.rooms[roomID].connectRooms(
                    's', self.rooms[roomGraph[roomID][1]['s']])
            # if the 'e' string is in the room graph at specific room :
            if 'e' in roomGraph[roomID][1]:
                # if e exists invoke connectRooms for the rooms dict at the
                # key of roomGraph, pass it e for direction and key of
                # rooms at roomGraph at specific room , index 1
                # and the value of the 'e' key, or room number
                self.rooms[roomID].connectRooms(
                    'e', self.rooms[roomGraph[roomID][1]['e']])
            # if the 'w' string is in the room graph at specific room :
            if 'w' in roomGraph[roomID][1]:
                # if w exists invoke connectRooms for the rooms dict at the
                # key of roomGraph, pass it w for direction and key of
                # rooms at roomGraph at specific room , index 1
                # and the value of the 'w' key, or room number
                self.rooms[roomID].connectRooms(
                    'w', self.rooms[roomGraph[roomID][1]['w']])
        self.startingRoom = self.rooms[0]

    # function to map the rooms and print the rooms to the terminal
    def printRooms(self):
        rotatedRoomGrid = []
        for i in range(0, len(self.roomGrid)):
            rotatedRoomGrid.append([None] * len(self.roomGrid))
        for i in range(len(self.roomGrid)):
            for j in range(len(self.roomGrid[0])):
                rotatedRoomGrid[len(self.roomGrid[0]) -
                                j - 1][i] = self.roomGrid[i][j]
        roomGrid = rotatedRoomGrid
        map_str = ""
        for row in roomGrid:
            map_str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    map_str += "  |  "
                else:
                    map_str += "     "
            map_str += "#\n"
            # Print room row
            map_str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    map_str += "-"
                else:
                    map_str += " "
                if room is not None:
                    map_str += f"{room.id}".zfill(3)
                else:
                    map_str += "   "
                if room is not None and room.e_to is not None:
                    map_str += "-"
                else:
                    map_str += " "
            map_str += "#\n"
            map_str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    map_str += "  |  "
                else:
                    map_str += "     "
            map_str += "#\n"
        print(map_str)
