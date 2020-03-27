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

    def depth_first_search(self, start):
        visited = set()
        nodes_stack = [start]
        while nodes_stack:
            vertex = nodes_stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                nodes_stack.extend(set(self.graph_dict[vertex]) - visited)
        return visited

    def depth_first_search_recursive(self, vertex, visited=None):

        if visited is None:
            visited = set()

        visited.add(vertex)
        node_set = set(self.graph_dict[vertex]) - visited
        for next in node_set:
            self.depth_first_search_recursive(next, visited)
        return visited

    def breadth_first_search(self, start):
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(set(self.graph_dict[vertex]) - set(visited))
        return list(visited)


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

print("depth first search a")
print(graph.depth_first_search("a"))

print("depth first search b")
print(graph.depth_first_search("b"))

print("depth first search e")
print(graph.depth_first_search("e"))

print("depth first search recursive e")
print(graph.depth_first_search_recursive("e"))

print("breadth first search a")
print(graph.breadth_first_search("a"))