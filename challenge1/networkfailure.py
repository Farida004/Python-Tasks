class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.routers = []
	
    '''A function that adds all the router connections.'''
    def add_routers(self, node1, node2, weight=1):  

        self.routers.append([node1, node2])
        if not self.directed:
            self.routers.append([node1, node2])

    '''A function that prints out all the router connections.'''
    def print_routers(self):
        num_of_routers = len(self.routers)
        for i in range(num_of_routers):
            print("edge ", i+1, ": ", self.routers[i])

    '''A function that detect the routers with the highest number of connections.'''
    def identify_router(self):
        m = {}
        uniq  = list(set(sum(self.routers, [])))

        for i in range(len(self.routers)) :
            m[self.routers[i][0]] = 0
            m[self.routers[i][1]] = 0
            
        for i in range(len(self.routers)) :
            m[self.routers[i][0]] += 1
            m[self.routers[i][1]] += 1
        maxVal = 0
        for i in uniq :
            maxVal = max(maxVal, m[i])

        for i in uniq :
            if (m[i] == maxVal) :
                print(i, end = " ")

graph = Graph()
# Asking for a user input untill -1 -1 values are entered
i1 = i2 = 0
while i1 != -1  and i2 != -1:
    i1,i2 = map(int, input().split())
    graph.add_routers(i1, i2)

graph.identify_router()