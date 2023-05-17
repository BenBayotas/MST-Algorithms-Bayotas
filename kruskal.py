class Graph:

    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])
    
    def find_subtree(self, parent, i):
        if parent[i] == i:
             return i
        return self.find_subtree(parent, parent[i])


    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1


    def kruskals_mst(self):
        result = []
    
        i = 0
        e = 0

        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        
        parent = []
        subtree_sizes = []

        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        while e < (self.m_num_of_nodes - 1):
            
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        
        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1, node2, weight))


g = Graph(8)
g.add_edge(0, 1, 6)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 4)
g.add_edge(3, 6, 9)
g.add_edge(3, 7, 2)
g.add_edge(4, 5, 5)
g.add_edge(4, 7, 3)
g.add_edge(5, 6, 3)
g.add_edge(5, 7, 1)
g.add_edge(6, 7, 4)

g.kruskals_mst()