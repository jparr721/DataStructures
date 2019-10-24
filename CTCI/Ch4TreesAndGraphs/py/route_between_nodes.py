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


def route_between_nodess2(adj, n1, n2):
    if not len(adj[n1]):
        return False

    visited = [n1]
    locations = [[0, adj[n1]]]

    while locations:
        current = locations.pop()
        i = current[0]

        if not current[1] and i + 1 >= len(current[1]):
            continue
        else:
            locations.append([i + 1, current[1]])

        if current[1] not in visited:
            visited.append(current[1])

        if current[1][i] == n2:
            return True

        # 1 -> 2
        if len(current[1]):
            locations.append([0, adj[current[1][i]]])
        else:
            locations.append([i + 1, current[1]])  # 2, 3

    return False


if __name__ == "__main__":
    adj = {1: [2, 5, 6], 2: [5], 3: [4], 4: [3], 5: [6], 6: []}

    print(route_between_nodes(adj, 1, 5))
    print(route_between_nodes(adj, 1, 6))
    print(route_between_nodes(adj, 1, 3))
    print(route_between_nodes(adj, 5, 6))

    adj = {1: [2, 3], 2: [], 3: [4, 5], 4: [], 5: [1]}

    print(route_between_nodess2(adj, 1, 5))
    print(route_between_nodess2(adj, 5, 1))
    print(route_between_nodess2(adj, 3, 4))
