import networkx as nx
from graph import City, load_graph

print("Testing the modules installed")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(nodes["london"])
print(graph)
print()
print("Identifying the neighbor cities of the said city")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)
print()
print("Identifying the neighbor cities with the best path of the said city")
for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)
print()
print("Sorting the neighbor cities by distance")
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
print()
print("Identify which places in the UK attained the city status in the 20th century starting with Edinburgh")
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

for node in nx.bfs_tree(graph, nodes["edinburgh"]):
        print("📍", node.name)
        if is_twentieth_century(node.year):
            print("Found:", node.name, node.year)
            break
else:
    print("Not found")
print()
print("Sorting which places in the UK attained the city status in the 20th century starting with Edinburgh by higher alttude first")

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")
print()

