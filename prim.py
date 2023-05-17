class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = [[0 for column in range(num_of_nodes)] 
                    for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight
    
    def prims_mst(self):
        postitive_inf = float('inf')
        selected_nodes = [False for node in range(self.m_num_of_nodes)]
        result = [[0 for column in range(self.m_num_of_nodes)] 
                    for row in range(self.m_num_of_nodes)]
        indx = 0
        
        for i in range(self.m_num_of_nodes):
            print(self.m_graph[i])
        print(selected_nodes)

        while(False in selected_nodes):
            minimum = postitive_inf
            start = 0
            end = 0

            for i in range(self.m_num_of_nodes):
                if selected_nodes[i]:
                    for j in range(self.m_num_of_nodes):
                        if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                            if self.m_graph[i][j] < minimum:
                
                                minimum = self.m_graph[i][j]
                                start, end = i, j
            
            selected_nodes[end] = True
            result[start][end] = minimum
            
            if minimum == postitive_inf:
                result[start][end] = 0

            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            result[end][start] = result[start][end]

        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))

g = Graph(9)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 7)
g.add_edge(1, 2, 11)
g.add_edge(1, 3, 9)
g.add_edge(1, 5, 20)
g.add_edge(2, 5, 1)
g.add_edge(3, 6, 6)
g.add_edge(3, 4, 2)
g.add_edge(4, 6, 10)
g.add_edge(4, 8, 15)
g.add_edge(4, 7, 5)
g.add_edge(4, 5, 1)
g.add_edge(5, 7, 3)
g.add_edge(6, 8, 5)
g.add_edge(7, 8, 12)

g.prims_mst()