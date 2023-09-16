import heapq


def read_input():
    data = {}
    _ = input()
    v, e = map(int, input().split())
    for i in range(e):
        node_one, node_two, weight = map(int, input().split())

        if node_two in data:
            data[node_two].append((weight, node_one, node_two))
        else:
            data[node_two] = [(weight, node_one, node_two)]

    return data


def prims(G, start):
    unvisited = list(G.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = G[start]
    heapq.heapify(heap)

    while unvisited:
        (cost, n1, n2) = heapq.heappop(heap)

        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((n2, n1, cost))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((n1, n2, cost))

        if new_node != None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node in G[new_node]:
                heapq.heappush(heap, node)

    return MST, total_cost


def main():
    data = read_input()
    MST, total_cost = prims(data, 1)

    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')

main()
