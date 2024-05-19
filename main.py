import heapq


def get_min_cost(wires):
    heapq.heapify(wires)

    if not wires or len(wires) == 0:
        return None

    sums_of_connections = [0 for _ in range(len(wires) - 1)]

    prev = heapq.heappop(wires)

    for i in range(len(wires)):
        cur = heapq.heappop(wires)
        cost_of_connection = prev + cur
        sums_of_connections[i] = cost_of_connection
        prev = cost_of_connection

    return sum(sums_of_connections)


if __name__ == "__main__":
    l = [1, 3, 4, 2, 5, 9]

    res = get_min_cost(l)

    print(res)
