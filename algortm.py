
from itertools import permutations

nodes = ["A", "B", "C", "D", "E", "F"]

distance = {
    "A": {"B": 10, "C": 15, "D": 20, "E": 18, "F": 12},
    "B": {"A": 10, "C": 9, "D": 10, "E": 14, "F": 16},
    "C": {"A": 15, "B": 9, "D": 8, "E": 12, "F": 10},
    "D": {"A": 20, "B": 10, "C": 8, "E": 7, "F": 11},
    "E": {"A": 18, "B": 14, "C": 12, "D": 7, "F": 9},
    "F": {"A": 12, "B": 16, "C": 10, "D": 11, "E": 9}
}

all_routes = []
shortest_distance = float("inf")
shortest_route = []


for perm in permutations(nodes[1:]):
    route = ["A"] + list(perm) + ["A"]
    total = 0

    
    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    all_routes.append({
        "route": route,
        "total": total
    })

    
    if total < shortest_distance:
        shortest_distance = total
        shortest_route = route

print("Jumlah kemungkinan rute:", len(all_routes))
print("\nSemua kemungkinan rute:")

for index, item in enumerate(all_routes, start=1):
    print(f"{index}. {' -> '.join(item['route'])} = {item['total']}")

print("\nRute tercepat:")
print(" -> ".join(shortest_route))
print("Total jarak:", shortest_distance)
