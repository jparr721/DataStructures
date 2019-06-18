#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import random
import sys
from typing import List, Tuple, Dict


def get_degree(vertex: int, edges: List[Tuple[int]]):
    degree = 0

    for edge in edges:
        if vertex in edge:
            degree += 1

    return degree


def opposite(vertex: int, edge: Tuple[int]) -> int:
    return edge[1] if edge[0] == vertex else edge[0]


def edge_coloring(input_data):
    # Show our colors
    colors: Dict[int, int] = {}

    edges: Dict[int, List[int]] = {}

    counts: Dict[int, int] = {}

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges_list = []
    verticies = set()
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges_list.append((int(parts[0]), int(parts[1])))
        verticies.add(parts[0])
        verticies.add(parts[1])

    verticies = sorted(verticies)
    verticies = [int(e) for e in verticies]

    max_degree: int = 0

    for vertex in verticies:
        for edge in edges_list:
            if vertex in edge:
                if vertex in edges:
                    edges[vertex].append(opposite(vertex, edge))
                else:
                    edges[vertex] = [opposite(vertex, edge)]
        max_degree = max(max_degree, get_degree(vertex, edges_list))

    print(f'Chromatic Index: {max_degree}')

    for vertex in verticies:
        print(vertex)
        possible_colors: List[int] = copy.deepcopy(verticies)
        adjacents: List[int] = edges[vertex]

        for adjacency in adjacents:
            adjacent_color: int = colors.get(adjacency)
            if adjacent_color and adjacent_color in possible_colors:
                possible_colors.remove(adjacent_color)

        selected = -1
        for color in possible_colors:
            if color in counts:
                selected = max(counts[color], selected)
        if selected == -1:
            selected = random.choice(possible_colors)

        if selected in counts:
            counts[selected] += 1
        else:
            counts[selected] = 0

        colors[vertex] = selected

    print(colors)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, solution))

    return output_data


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(edge_coloring(input_data))
    else:
        print('usage: python solver.py ./data/gc_4_1)')
