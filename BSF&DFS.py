class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {}

    def add_edge(self, from_node, to_node):
        if from_node in self.edges:
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node] = [to_node]

    def bfs(self, start_node):
        visited = [start_node]
        queue = [start_node]
        path = [start_node]

        while queue:
            node = queue.pop(0)

            if node in self.edges:
                for neighbour in self.edges[node]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
                        path.append(neighbour)
            else:
                print(path)
                return

        print(path)


if __name__ == "__main__":
    graph = Graph([0, 1, 2, 3, 4])
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.bfs(1)


# Define the DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited


# Example usage
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print("DFS traversal starting from node 'A':")
dfs(graph, 'C')

