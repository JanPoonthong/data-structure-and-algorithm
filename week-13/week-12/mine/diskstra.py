import heap_code

infinity = float("inf")

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

    return vertex, data


class myClass:
    def __init__(self, short, start):
        self.short = short
        self.start = start

def myCompare(x, y):
    return x.short < y.short


def diskstra_heap(data, start=1):
    shortest_paths = {}
    visited = {}

    for node in list(data.keys()):
        shortest_paths[node] = infinity
        visited[node] = False

    shortest_paths[start] = 0
    visited[start] = True

    heap = heap_code.Heap(cmp=myCompare)

    heap.insert(myClass(0, 1))

    while heap.heapsize > 0:
        a = heap.extract()

        (distance, node) = a.short, a.start
        visited[node] = True

        for edge in data[node]:
            cost = edge[2]
            to_node = edge[1]

            if (not visited[to_node]) and (distance + cost < shortest_paths[to_node]):
                shortest_paths[to_node] = distance + cost
                heap.insert(myClass(shortest_paths[to_node], to_node))

    return shortest_paths

def main():
    vertex, data = read_input()
    shortest_paths = diskstra_heap(data)

    # Calculate the total weight of the minimum spanning tree (MST)
    total_weight = sum(shortest_paths.values())

    print(total_weight)

main()
