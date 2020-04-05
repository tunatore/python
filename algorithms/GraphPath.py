class Node:
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list or []
        self.shortest_path = None


def find_route(node1, node2):
    from collections import deque
    queue = deque()
    node = node1
    node.shortest_path = [node]
    while node:
        for adjacent in node.adjacency_list:
            if not adjacent.shortest_path:
                if adjacent == node2:
                    return node.shortest_path + [adjacent]
                adjacent.shortest_path = node.shortest_path + [adjacent]
            queue.append(adjacent)
        if len(queue) > 0:
            node = queue.pop()
        else:
            break
    return None


def display_path(path):
    if path is None:
        return "Not found"
    return '->'.join([node.data for node in path])

# directed graph adjacency list


node_k = Node('K')
node_i = Node('I', [node_k])
node_g = Node('G')
node_f = Node('F')
node_e = Node('E', [node_i])
node_d = Node('D', [node_e])
node_c = Node('C', [node_g])
node_b = Node('B', [node_f])
node_a = Node('A', [node_b, node_c, node_d])

print("A-E:", display_path(find_route(node_a, node_e)))
print("A-K:", display_path(find_route(node_a, node_k)))
print("E-G:", display_path(find_route(node_e, node_g)))
print("E-A:", display_path(find_route(node_e, node_g)))
