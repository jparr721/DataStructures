"""
Determines if there is a route between two provided nodes
in a directed graph
"""


def between_two_nodes(graph, n1, n2):
    print(graph[n2][n1])
    return graph[n1][n2] == 1 or graph[n2][n1] == 1


def main():
    adj = [[0, 1, 0, 0],
           [0, 0, 1, 0],
           [1, 0, 0, 0],
           [0, 0, 1, 0]]

    print(between_two_nodes(adj, 1, 0))


main()
