"""
Determines if there is a route between two provided nodes
in a directed graph
"""


def route_between_nodes(adj, n1, n2):
    if len(adj) == 0 or len(adj) == 1:
        return False

    history = [(n1, 0)]
    visited = [n1]
    current = n1

    while history:
        pos = history[-1][1]

        if len(adj[current]) > pos:
            current = adj[current][pos]

        if current == n2:
            return True

        if current in visited:
            # Get the last position
            old_pos = history[-1][1]
            if len(adj[current]) > old_pos:
                # So, if we've visited this node, but there's another one
                # then we just continue moving...
                history[-1][1] += 1
            else:
                # Otherwise, ditch this node and keep moving
                history.pop()
        else:
            visited.append(current)
            history.append((current, 0))

    return False


if __name__ == "__main__":
    adj = {
        1: [2, 5, 6],
        2: [5],
        3: [4],
        4: [3],
        5: [6],
        6: [],
    }

    print(route_between_nodes(adj, 1, 5))
    print(route_between_nodes(adj, 1, 6))
    print(route_between_nodes(adj, 1, 3))
    print(route_between_nodes(adj, 5, 6))
