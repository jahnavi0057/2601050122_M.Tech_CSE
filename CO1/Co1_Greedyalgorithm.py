# Kruskal's Algorithm

edges = [
    (4, 'C', 'D'),
    (5, 'B', 'C'),
    (6, 'A', 'C'),
    (10, 'A', 'B'),
    (15, 'B', 'D')
]

# Sort edges by cost
edges.sort()

parent = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D'
}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

total_cost = 0

for cost, a, b in edges:
    x = find(a)
    y = find(b)

    if x != y:
        parent[x] = y
        total_cost += cost
        print(a, "-", b, ":", cost)

print("Minimum Cost =", total_cost)
