#please install- "python3 -m pip install networkx"
#please install-"python -m pip install --upgrade pip"
#please install- "python3 -m pip install matplotlib"


import heapq
import networkx as nx
import matplotlib.pyplot as plt
import time
def astar(graph, start, goal, heuristics):
    #Find the shortest path from start to goal using A* algorithm
    frontier = []
    heapq.heappush(frontier, (0, start, []))
    explored = set()
    while frontier:
        (cost, current, path) = heapq.heappop(frontier)
        if current == goal:
            return path + [current]
        if current in explored:
            continue
        explored.add(current)
        for neighbor, weight in graph[current].items():
            new_cost = cost + weight
            new_path = path + [current]
            priority = new_cost + heuristics[neighbor]
            heapq.heappush(frontier, (priority, neighbor, new_path))
    return None

# Define graph
graph = {
    'Kingston': {'St. Andrew': 75, 'Portland': 140, 'St. Thomas': 118},
    'St. Andrew': {'Kingston': 75, 'St. Catherine': 71},
    'St. Catherine': {'St. Andrew': 71, 'Portland': 151},
    'Portland': {'Kingston': 140, 'St. Catherine': 151, 'St. Mary': 99, 'St. Ann': 80},
    'St. Mary': {'Portland': 99, 'Manchester': 211},
    'St. Ann': {'Portland': 80, 'Clarendon': 97, 'Honover': 146},
    'St. Thomas': {'Kingston': 118, 'Westmoreland': 111},
    'Westmoreland': {'St. Thomas': 111, 'St. James': 70},
    'St. James': {'Westmoreland': 70, 'Trelawny': 75},
    'Trelawny': {'St. James': 75, 'Honover': 120},
    'Honover': {'Trelawny': 120, 'St. Ann': 146, 'Clarendon': 138},
    'Clarendon': {'Honover': 138, 'St. Ann': 97, 'Manchester': 101},
    'Manchester': {'St. Mary': 211, 'Clarendon': 101, 'St. Elizabeth': 90, 'Montego-bay': 85},
    'St. Elizabeth': {'Manchester': 90},
    'Montego-bay': {'Manchester': 85, 'Spanish town': 98, 'Portmore': 142},
    'Spanish town': {'Montego-bay': 98, 'Porus': 86},
    'Porus': {'Spanish town': 86},
    'Portmore': {'Montego-bay': 142, 'NM-Air port': 92},
    'NM-Air port': {'Portmore': 92, 'Morant bay': 87},
    'Morant bay': {'NM-Air port': 87}
}

# Create a Graph object from the dictionary
G = nx.Graph(graph)

# Define heuristics
heuristics = {
    'Kingston': 366,
    'St. Andrew': 374,
    'St. Catherine': 380,
    'Portland': 253,
    'St. Mary': 178,
    'St. Ann': 193,
    'St. Thomas': 329,
    'Westmoreland': 244,
    'St. James': 241,
    'Trelawny': 242,
    'Honover': 160,
    'Clarendon': 100,
    'Manchester': 0,
    'St. Elizabeth': 77,
    'Montego-bay': 80,
    'Spanish town': 151,
    'Porus': 161,
    'Portmore': 199,
    'NM-Air port': 226,
    'Morant bay': 234
}

# define start and goal nodes here
start = 'Kingston'
goal = 'Montego-bay'

# find the shortest path using A* algorithm
path = astar(graph, start, goal, heuristics)
print(path)

# Draw graph with shortest path
pos = nx.spring_layout(G)
t0 = time.time()
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
plt.axis('off')
t1 = time.time()
print('Time:', t1-t0)
plt.show()

