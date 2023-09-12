from unionfind import unionfind


def make_graph():
    # tuple = (weight, N1, N2)
    data = {}
    vertex, edge = map(int, input().split())
    for i in range(edge):
        node_one, node_two, weight = input().split()

        node_one = int(node_one)
        node_two = int(node_two)
        weight = int(weight)

        if node_two in data:
            data[node_two].append((weight, node_one, node_two))
        else:
            data[node_two] = [(weight, node_one, node_two)]

    return vertex, data


def load_edges(data):
    edges = []

    for _, value in data.items():
        edges.extend(value)

    return sorted(edges)


def kruskals(data, vertex):
    total_weight = 0
    mst = []

    edges = load_edges(data)
    uf = unionfind(vertex)
    for edge in edges:
        weight, node_one, node_two = edge[0], edge[1], edge[2]

        if type(node_one) == int and type(node_two) == int:
            if not uf.issame(node_one, node_two):
                total_weight += int(weight)
                uf.unite(node_one, node_two)
                mst.append((node_one, node_two, weight))

    return mst, total_weight


def main():
    vertex, data = make_graph()
    mst, total_weight = kruskals(data, vertex)
    print(f"Minimum spanning tree: {mst}")
    print(f"Total cost: {total_weight}")


main()
