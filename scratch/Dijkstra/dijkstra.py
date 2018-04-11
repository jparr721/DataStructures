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

proper_coloring = {}


def infty(graph):
    global proper_coloring
    total = 0
    visited = []
    for key, value in graph.items():
        if key in visited:
            continue
        visited.append(key)
        for sub_key in value:
            if sub_key[0] not in visited:
                total += sub_key[1]
                proper_coloring[sub_key[0]] = sub_key[1]
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
    global proper_coloring
    proper_coloring["A"] = 0
    infty(graph)
    print(proper_coloring)

    visited = []
    init = initial(graph)
    init["A"] = 0
    for key, value in graph.items():
        verticies = []
        for vertex in value:
            if vertex[0] not in visited:
                verticies.append(vertex[0])
        next_val = find_min(proper_coloring, verticies)
        for vertex in value:
            if vertex[0] == next_val:
                init[next_val] = min(vertex[1], init.get(next_val))
                visited.append(next_val)
    return init


print(dijkstra(graph))
