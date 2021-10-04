# class Path:
#     def __init__(self, start, end, time):
#         self.start = start
#         self.end = end
#         self.time = time

class Line:
    def __init__(self, stops, time):
        self.stops = stops
        self.n = len(self.stops)
        self.time = time

class World:
    def __init__(self, n):
        self.n = n
        self.times = [[0 for _ in range(self.n)] for _ in range(self.n)]
        # for path in paths:
        #     self.times[path.start][path.end] = path.time
        #     self.times[path.end][path.start] = path.time
    
    def setPath(self, start, end, time):
        self.times[start][end] = time
        self.times[end][start] = time
    
    def addLine(self, line):
        n = len(line.stops)
        for i in range(n-1):
            for j in range(i+1, n):
                self.setPath(line.stops[i], line.stops[j], (j-i)*line.time)
    
    def printTime(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.times[i][j], end="\t")
            print()
                



# line9stations = 38
# line9paths = []
# for i in range(line9stations-1):
#     line9paths += [Path(i, i+1, 2)]

# line9paths += [
#     Path(1, 4, 3),
#     Path(4, 6, 3),
#     Path(6, 9, 3),
#     Path(9, 12, 3),
#     Path(12, 14, 3),
#     Path(14, 16, 3),
#     Path(16, 19, 3),
#     Path(19, 22, 3),
#     Path(22, 24, 3),
#     Path(24, 26, 3),
#     Path(26, 28, 3),
#     Path(28, 29, 3),
#     Path(29, 32, 3),
#     Path(32, 35, 3),
#     Path(35, 37, 3)
# ]

# line9 = Map(line9stations, line9paths)

# for i in range(line9stations):
#     for j in range(line9stations):
#         print(line9.times[i][j], end=",")
#     print()

world = World(21)
world.addLine(Line([_ for _ in range(21)], 2))
world.addLine(Line([1, 6, 11, 16], 5))
world.addLine(Line([0, 10, 20], 8))

world.printTime()