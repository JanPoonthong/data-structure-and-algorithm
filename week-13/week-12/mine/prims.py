import heap_code


def convert_to_undirected(graph):
    undirected_graph = {}

    for node in range(1, len(graph) + 1):
        for i in graph[node]:
            node1, node2 = i[0], i[1]
            weight = i[2]
            if node2 not in undirected_graph:
                undirected_graph[node2] = [(node1, node2, weight),
                                           (node2, node1, weight)]
            else:
                undirected_graph[node2].extend(
                    [(node1, node2, weight), (node2, node1, weight)])

    return undirected_graph


def read_input():
    _ = input()
    vertex, edge = map(int, input().split())

    data = {}
    for i in range(edge):
        node_one, node_two, weight = map(int, input().split())

        if node_one in data:
            data[node_one].append((node_one, node_two, weight))
        else:
            data[node_one] = [(node_one, node_two, weight)]

        if node_two in data:
            data[node_two].append((node_two, node_one, weight))
        else:
            data[node_two] = [(node_two, node_one, weight)]

    return vertex, data


class myClass:
    def __init__(self, k, node_one, node_two):
        self.key = k
        self.node_one = node_one
        self.node_two = node_two


def myCompare(x, y):
    return x.key < y.key


def prims(data, starting_node):
    unvisited = list(data.keys())
    visited = []
    total_weight = 0
    mst = []

    unvisited.remove(starting_node)
    visited.append(starting_node)

    starting_data_heap = data[starting_node]

    heap = heap_code.Heap(cmp=myCompare)

    for key in starting_data_heap:
        heap.insert(myClass(key[2], key[0], key[1]))

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

            for node in data[new_node]:
                heap.insert(myClass(node[2], node[0], node[1]))

    return mst, total_weight


def main():
    vertex, data = read_input()
    data = convert_to_undirected(data)
    mst, total_weight = prims(data, 1)

    print("Minimum spanning tree:", mst)
    print("Total cost:", total_weight)


main()
