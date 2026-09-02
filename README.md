**Greedy Algorithm
3. Network Cable Installation**

A company wants to connect several offices with minimum total cable cost.

**Question**

Which greedy algorithm could be useful for this problem? Explain the basic idea.

**Solution**

For the given scenario, Kruskal's Algorithm is a suitable greedy algorithm.

Kruskal's Algorithm is used to find the Minimum Spanning Tree (MST) of a weighted graph. It connects all offices with the minimum possible total cable cost without forming a cycle.

Kruskal's Algorithm – Greedy Approach
Basic Idea

Kruskal's Algorithm follows a greedy approach by selecting the cheapest available cable connection at every step.

**The algorithm:**

List all possible cable connections with their costs.
Sort all connections in increasing order of cost.
Select the cable with the lowest cost.
Check whether adding the cable creates a cycle.
If it does not create a cycle, add the cable to the network.
If it creates a cycle, reject the cable.
Repeat until all offices are connected.
Add the costs of the selected cables to get the minimum total cost.

**Example**

Consider four offices:

A, B, C, D

Possible cable connections:

Cable	Cost
A-B	10
A-C	6
B-C	5
B-D	15
C-D	4
Step 1: Sort the Cables

Arrange all cable connections in increasing order of cost:

C-D = 4
B-C = 5
A-C = 6
A-B = 10
B-D = 15

Step 2: Select the Cheapest Cable

C-D = 4

There is no cycle, so select it.

Selected:

C-D → 4

Step 3: Select the Next Cheapest Cable

B-C = 5

There is no cycle, so select it.

Selected:

C-D → 4
B-C → 5

Now B, C and D are connected.

Step 4: Select the Next Cheapest Cable

A-C = 6

There is no cycle, so select it.

Selected:

C-D → 4
B-C → 5
A-C → 6

Now all four offices are connected.

Therefore, we stop.

Step 5: Calculate Minimum Cost

Minimum Cost = 4 + 5 + 6

Minimum Cost = 15

Therefore, the minimum total cable installation cost is:

₹15

**Algorithm**

Input
Set of offices (vertices)
Cable connections (edges)
Cost of each cable connection
Steps
Start with an empty Minimum Spanning Tree.
Sort all edges in increasing order of cost.
Select the edge with the smallest cost.
Check whether the selected edge forms a cycle.
If no cycle is formed, add the edge to the MST.
If a cycle is formed, reject the edge.
Repeat until V - 1 edges are selected.
Calculate the total cost of the selected edges.

**Python Implementation**

# Kruskal's Algorithm

edges = [
    (10, 'A', 'B'),
    (6, 'A', 'C'),
    (5, 'B', 'C'),
    (15, 'B', 'D'),
    (4, 'C', 'D')
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
count = 0

for cost, a, b in edges:
    x = find(a)
    y = find(b)

    if x != y:
        parent[x] = y
        total_cost += cost
        count += 1

        print(a, "-", b, "=", cost)

    if count == 3:
        break

print("Minimum Cost =", total_cost)
Output
C - D = 4
B - C = 5
A - C = 6
Minimum Cost = 15
Time Complexity
Sorting

Sorting all E edges takes:

O(E log E)

Overall Time Complexity

O(E log E)

Space Complexity

O(V + E)

Where:

V = number of offices (vertices)
E = number of cable connections (edges)
