# Testing Graphs
graph = {}
graph["A"] = [["B", 10], ["D", 5]]
graph["B"] = [["A", 10], ["C", 5]]
graph["C"] = [["B", 5], ["D", 15]]
graph["D"] = [["C", 15], ["A", 5]]
og = {}
og["A"] = 0
og["B"] = 10
og["C"] = 10
og["D"] = 15
v = ["B", "C", "D"]

def infty(graph):
    total = 0
    visited = []
    for key, value in graph.items():
        if key in visited:
            continue
        visited.append(key)
        for sub_key in value:
            if sub_key[0] not in visited:
                total += sub_key[1]
    return total + 1


def initial(graph):
    inf = infty(graph)
    edges = {}
    for key, _ in graph.items():
        if key == "A":
            edges[key] = 0
        else:
            edges[key] = inf
    return edges


def find_min(graph, verticies):
    smallest = 100000000
    small = None
    for vertex in verticies:
        if graph.get(vertex) < smallest:
            small = vertex
            smallest = graph.get(vertex)
    return small


def dijkstra(graph):
    init = initial(graph)
    for key in graph:
        for edge in graph[key]:
            if init[key] + edge[1] < init[edge[0]]:
                init[edge[0]] = init[key] + edge[1]
    return init


def is_connected(graph):

print(dijkstra(graph))
