class Graph:

    def __init__(self, graph_dictionary=None):

        if graph_dictionary is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dictionary

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        (vertex1, vertex2) = edge
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            if vertex1 not in self.graph_dict and vertex2 not in self.graph_dict:
                self.graph_dict[vertex1] = [vertex2]
                self.graph_dict[vertex2] = [vertex1]
            else:
                if vertex1 not in self.graph_dict and vertex2 in self.graph_dict:
                    self.graph_dict[vertex1] = [vertex2]
                    self.graph_dict[vertex2].append(vertex1)
                elif vertex1 in self.graph_dict and vertex2 not in self.graph_dict:
                    self.graph_dict[vertex1].append(vertex2)
                    self.graph_dict[vertex2] = [vertex1]


graph_adjacency_list = {
    "a": ["b", "e", "d"],
    "b": ["a", "c", "d"],
    "c": ["b", "d"],
    "d": ["a", "b", "c"],
    "e": ["a"],
    "g": []
}

graph = Graph(graph_adjacency_list)
print("graph vertices")
print(graph.vertices())
print("graph edges")
print(graph.edges())

graph.add_vertex("t")

print("graph vertices")
print(graph.vertices())

print("graph add an edge")
graph.add_edge(("a", "g"))
print(graph.edges())

print("graph add an edge with new vertices")
graph.add_edge(("p", "r"))
print(graph.vertices())
print(graph.edges())