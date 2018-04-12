# Testing Graphs
graph = {}
graph["A"] = [["B", 5], ["C", 5]]
graph["B"] = [["A", 5], ["C", 5]]
graph["C"] = [["B", 5], ["A", 15]]
graph["D"] = [["E", 5]]
graph["E"] = [["D", 5]]
og = {}
og["A"] = 0
og["B"] = 10
og["C"] = 10
og["D"] = 15
v = ["B", "C", "D"]


def infty(graph):
    """
    This function takes a weighted graph as input
    and returns the sum of all the edge
    weights + 1 (how they appear on the graph)
    """
    total = 0  # Initialize the total to 0
    visited = []  # Keep track of visited nodes
    for key, value in graph.items():
        # Reset to the next val if it was already visited
        if key in visited:
            continue
        visited.append(key)
        for sub_key in value:
            if sub_key[0] not in visited:
                total += sub_key[1]
    return total + 1


def initial(graph):
    """
    This makes the "initial" graph where
    the root is 0 and the other values are
    infinity since the optimal path to
    get there is not yet known at the beginning
    """
    inf = infty(graph)  # Get the value of infinity
    edges = {}  # Keep track of the edges to store them
    for key, _ in graph.items():
        # Since A is our root, set it to 0 always
        if key == "A":
            edges[key] = 0
        # Otherwise add the value with inf to the dict
        else:
            edges[key] = inf
    return edges


def find_min(graph, verticies):
    """
    Finds the minimum between the provided
    verticies considering the weights provided
    by the weighted graph.
    """
    # Our initial "Smallest" value
    smallest = 100000000
    # Keep track of the smallest value
    small = None
    for vertex in verticies:
        if graph.get(vertex) < smallest:
            # Assign small
            small = vertex
            # Change the new smallest valuee
            smallest = graph.get(vertex)
    return small


def dijkstra(graph):
    """
    Runs dijkstras algorithm on the
    provided graph and returns the final
    edge set.
    """
    # Get the initial graph
    init = initial(graph)
    for key in graph:
        # Compare every edge against all others it can reach
        for edge in graph[key]:
            # If the value is better, use it instead
            if init[key] + edge[1] < init[edge[0]]:
                init[edge[0]] = init[key] + edge[1]
    return init


def is_connected(graph):
    """
    Checks to see if a given graph is
    connected.
    """
    # Grab the value of inf to check with
    inf = infty(graph)
    # Run Dijkstras to see if any outliers exist
    dj = dijkstra(graph)
    # Check to see if the outliers are in the graph
    for val in dj:
        if dj[val] >= inf:
            return False
    return True
