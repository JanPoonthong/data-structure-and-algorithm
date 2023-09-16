import heap_code
import sys

class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        self._add_edge(node1, node2, weight)
        self._add_edge(node2, node1, weight)

    def _add_edge(self, node1, node2, weight):
        if node1 in self.graph:
            self.graph[node1].append((node2, weight))
        else:
            self.graph[node1] = [(node2, weight)]

def read_input():
    _ = input()
    vertex, edge = map(int, input().split())

    graph = UndirectedGraph()

    for i in range(edge):
        node_one, node_two, weight = map(int, input().split())
        graph.add_edge(node_one, node_two, weight)

    return vertex, graph.graph

class MyNode:
    def __init__(self, key, node_one, node_two):
        self.key = key
        self.node_one = node_one
        self.node_two = node_two

def my_compare(x, y):
    return x.key < y.key

def prims(graph, starting_node):
    unvisited = list(graph.keys())
    visited = []
    total_weight = 0
    mst = []

    unvisited.remove(starting_node)
    visited.append(starting_node)

    starting_data_heap = graph[starting_node]

    heap = heap_code.Heap(cmp=my_compare)

    for key in starting_data_heap:
        heap.insert(MyNode(key[1], key[0], key[1]))

    while unvisited:
        a = heap.extract()
        node_one, node_two, weight = a.node_one, a.node_two, a.key

        new_node = None

        if node_one in unvisited and node_two in visited:
            new_node = node_one
            mst.append((node_two, node_one, weight))

        elif node_one in visited and node_two in unvisited:
            new_node = node_two
            mst.append((node_one, node_two, weight))

        if new_node is not None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_weight += weight

            for node in graph[new_node]:
                heap.insert(MyNode(node[1], node[0], node[1]))

    return mst, total_weight

def main():
    vertex, graph = read_input()
    mst, total_weight = prims(graph, 1)

    print("Minimum spanning tree:", mst)
    print("Total cost:", total_weight)

main()
