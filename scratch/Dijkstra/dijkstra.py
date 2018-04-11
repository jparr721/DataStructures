from copy import deepcopy

graph = {}
graph["A"] = [["B", 10], ["D", 5]]
graph["B"] = [["A", 10], ["C", 5]]


def infty(graph):
    """
    Why did you make me do this father
    """
    total = 0
    for weight in graph.items():
        for val in weight:
            for numberList in val:
                for number in numberList:
                    if type(number) == int:
                        total += number

    return total + 1

def initial(graph):



print(infty(graph))
