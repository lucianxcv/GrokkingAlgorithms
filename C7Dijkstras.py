graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Track processed nodes
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Main algorithm
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("Costs:", costs)
print("Parents:", parents)


""" 
 Line-by-Line Explanation
📍 Define the graph
python
Copy
Edit
graph = {}
Initializes an empty graph using a dictionary.

python
Copy
Edit
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
Adds two neighbors from the "start" node: node "a" with cost 6, and "b" with cost 2.

python
Copy
Edit
graph["a"] = {}
graph["a"]["fin"] = 1
"a" has a neighbor "fin" with cost 1.

python
Copy
Edit
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
"b" has two neighbors: "a" with cost 3, and "fin" with cost 5.

python
Copy
Edit
graph["fin"] = {}
"fin" has no outgoing edges.

📍 Set up the costs table
python
Copy
Edit
infinity = float("inf")
Represents infinite cost. Used for unreachable nodes at first.

python
Copy
Edit
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
Initial costs from "start" to each node:

"a": 6 (direct path)

"b": 2 (direct path)

"fin": not yet known (∞)

📍 Set up the parents table
python
Copy
Edit
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
Used to reconstruct the path later.

📍 List of processed nodes
python
Copy
Edit
processed = []
Keeps track of which nodes we've already processed.

📍 Helper function to find the lowest-cost unprocessed node
python
Copy
Edit
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
Iterates through the costs table.

Finds the node with the lowest cost that hasn’t been processed yet.

📍 Main loop (Dijkstra’s Algorithm)
python
Copy
Edit
node = find_lowest_cost_node(costs)
while node is not None:
Continues looping until all nodes are processed.

python
Copy
Edit
    cost = costs[node]
    neighbors = graph[node]
Gets the current cost and all neighbors of the current node.

python
Copy
Edit
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
For each neighbor:

Calculates how much it would cost to get there through the current node.

If this path is cheaper, update the cost and parent.

python
Copy
Edit
    processed.append(node)
    node = find_lowest_cost_node(costs)
Marks current node as processed.

Finds the next lowest-cost node.

📍 Final output
python
Copy
Edit
print("Costs:", costs)
print("Parents:", parents)
Displays the final shortest costs and the parent path.

"""