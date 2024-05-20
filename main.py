import heapq


def get_min_cost(wires):
    heapq.heapify(wires)

    total_cost = 0

    while len(wires) > 1:
        first_min = heapq.heappop(wires)
        second_min = heapq.heappop(wires)

        new_cable = first_min + second_min

        total_cost += new_cable

        heapq.heappush(wires, new_cable)

    return total_cost


if __name__ == "__main__":
    l = [ 1, 1, 9, 2, 1, 2]

    res = get_min_cost(l)

    print(res)
