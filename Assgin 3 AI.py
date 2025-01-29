class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dls(self, start, limit):
        print(f"Nodes up to depth {limit} from '{start}':")
        visited_nodes = []
        self._dls_recursive(start, limit, 0, visited_nodes)
        print("Visited Nodes:", visited_nodes)

    def _dls_recursive(self, node, limit, depth, visited_nodes):
        if depth > limit:
            return
        if node not in visited_nodes:
            visited_nodes.append(node)
        for neighbor in self.graph.get(node, []):
            self._dls_recursive(neighbor, limit, depth + 1, visited_nodes)


edges = [
    ('a', 'b'), ('a', 'c'),
    ('b', 'd'), ('c', 'e'),
    ('d', 'f'), ('e', 'f')
]

graph = Graph()
for u, v in edges:
    graph.add_edge(u, v)
    graph.add_edge(v, u)

start_node = 'a'
depth_limit = 2

graph.dls(start_node, depth_limit)
