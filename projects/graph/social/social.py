import random

# user class creates user with parameter name


class User:
    def __init__(self, name):
        self.name = name
# evalues string representation of name from the user object

    def __repr__(self):
        return self.name

# social graph class creates a social graph with users as the verticies


class SocialGraph:
    def __init__(self):
        # initialize last id to 0
        self.lastID = 0
        # initialize users to empty dict
        self.users = {}
        # initialize friendships to an empty dict
        self.friendships = {}

    # add friendship method adds friendships to a user, accepts two arguments, userID and friendID, creates a bidirectional edge
    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        # cannot be friends with self
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        # if friendship already, dont do anything
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        # to add friendship connection or bidirectional edge, add friendID to key of userID in friendship dict
        # also add userID to key of friendID in friendship dict
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
    # add user method adds a user to the users dict and auto increments the lastID to assign a new user number

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        # assigns the user object to the users dict's key
        self.users[self.lastID] = User(name)
        # creates an empty set for friendships dict with the key of lastid or username
        self.friendships[self.lastID] = set()

    # populate graph generates a social graph with two arguments, the number of users and average friendships
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # for loop that adds users to the graph range numUsers argument
        for i in range(numUsers):
            # add user to graph, which increments lastID and sets users key to username, so key will be user i+1
            self.addUser(f'User {i+1}')
        # Create friendships, possible friendships is initially set to an empty list
        possibleFriendships = []
        # for all keys in self.users
        for userID in self.users:
            # nested for loop for friendID in range userID + 1 to resolve index starting at 0, until self.lastID + 1 to resolve no-inclusive end range
            for friendID in range(userID + 1, self.lastID + 1):
                # append to the possible friendships list the tupple userID and friendID
                possibleFriendships.append((userID, friendID))
        # print(possibleFriendships)
        # use the fisher-yates shuffle, to randomize possibleFriendships,
        random.shuffle(possibleFriendships)
        #
        # possibleFriendships = possibleFriendships[:20]
        # # print(possibleFriendships)
        # for i in possibleFriendships:
        #     # print(f'user:{i[0]},friend:{i[1]}')
        #     if i[0] in self.friendships and i[1] in self.friendships:
        #         self.friendships[i[0]].add(i[1])
        # print(len(possibleFriendships))

        for friendship in possibleFriendships[: (numUsers * avgFriendships)//2]:
            self.addFriendship(friendship[0], friendship[1])

    # method getAllSocialPaths takes a userID and returns a dict containing every user in that user's
    # extended network along with the shortest friendship path between each
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #
        # print(self.friendships)

        # if userID not in self.friendships:
        #     return "not valid userID"
        # # for each key in friendships dict, do a bfs, and find shortest path between each
        # # value, if path does not exist skip
        # for friendID in self.friendships:
        #     # print(friendID)
        #     # print(userID)
        #     route = self.bfs(f'{userID}', friendID)
        #     if route:
        #         visited[friendID] = route
        # # print(f'visited: {visited}')
        # return visited
        #
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)
        return visited

    def bfs(self, starting_vertex_id, destination_vertex_id):
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex_id)
        # print(f'queue: {queue}')
        while queue.size() > 0:
            path = queue.dequeue()
            # print(f'path: {path}')
            vertex = path[-1]
            if vertex not in visited:
                # print(f'vertex: {vertex}')
                visited.add(vertex)
                for neighbor in self.friendships[int(vertex)]:
                    route = list(path)
                    # print(f'route: {route}')
                    route.append(neighbor)
                    # print(f'route after append: {route}')
                    queue.enqueue(route)
                    if neighbor == destination_vertex_id:
                        return route
                    else:
                        pass


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


# test where a social graph is created
# then the social graph is populated with 10 users and an average of two friends
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.users)
    print(sg.friendships[1])
    print("********")
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print("********")
    print(len(connections))
    total_len = 0
    for friendID in connections:
        total_len += len(connections[friendID])
    print(f"avg length: {total_len/ len(connections)}")

# avg = total/count
# 2 = total/10
# 20 = total
# total = avg * num_users

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 10 choose 2
# n! / 2 * (n-2)!
# n! = n * (n-1) * (n-2)!
# n * (n-1) / 2
# O(n^2)
# 10 * (9) / 2

# build friend-based social network.
# users are able to view friends, friend's friend, friends friend's friend, etc
# people connected through any number of connections are considered part of extended social network

# functionality users and friendships completed
# implement function that shows all the friends in a user's extended social netowrk and chain of friendships that link them
# the number of connections between one user and another are called the degrees of separation

# client also interested in how the performace will scale as more users join
# implement feature that creates large numbers of users to the network and assigns random distribution of friends

# 3 Questions:

# 1. To create 100 users with an average of 10 friends each, how many times would
# you need to call addFriendship()? why?

# total = avg * num_users
# total = 10 * 100
# 1000 / 2 = 500

# 2. If you create 1000 users with an avg of 5 random friends, what percentage of
# the other users will be in a particular user's extended social network?
# what is the average degree of separation between a user and those in his/her extended network?
# 99%
# 5 deg avg
