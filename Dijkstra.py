import heapq
import networkx as nx
import matplotlib.pyplot as plt


def Dijkstra(graph, start, end):
    # initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    # create a priority queue and add the start node
    priority_queue = [(0, start)]

    while len(priority_queue) > 0:
        # get the node with the smallest distance from the start node
        current_distance, current_node = heapq.heappop(priority_queue)

        # if we have found the end node, we can stop searching
        if current_node == end:
            break

        # update the distances and previous nodes of neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # reconstruct the shortest path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()

    return path, distances[end]


# define the graph
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

# define the start and end nodes
start_node = 'Kingston'
end_node = 'Montego-bay'

# run Dijkstra's algorithm to find the shortest path and distance
shortest_path, distance = Dijkstra(graph, start_node, end_node)
print(f'The shortest path from {start_node} to {end_node} is {shortest_path} with a distance of {distance} km.')

# create a NetworkX graph object
G = nx.Graph(graph)

# create a dictionary of node colors for the visual component
node_colors = {node: 'white' for node in graph}
node_colors[start_node] = 'green'
node_colors[end_node] = 'red'

# create a dictionary of edge colors for the visual component
edge_colors = {edge: 'black' for edge in G.edges()}

# Draw graph with shortest path
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, width=1, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_family='sans-serif')
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='r', node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
plt.axis('off')
plt.show()