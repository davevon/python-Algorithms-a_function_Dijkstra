import networkx as nx
import matplotlib.pyplot as plt

def best_first_search(graph, start_node, goal_node, heuristic):
    open_list = [(heuristic[start_node], start_node)]
    closed_list = set()

    while open_list:
        _, current_node = open_list.pop(0)

        if current_node == goal_node:
            return reconstruct_path(start_node, current_node, graph)

        closed_list.add(current_node)

        neighbors = list(graph.neighbors(current_node))

        for neighbor in neighbors:
            if neighbor not in closed_list:
                open_list.append((heuristic[neighbor], neighbor))
                closed_list.add(neighbor)
                graph.nodes[neighbor]['predecessor'] = current_node

    return None

def reconstruct_path(start_node, goal_node, graph):
    path = [goal_node]
    current_node = goal_node

    while current_node != start_node:
        predecessor = graph.nodes[current_node]['predecessor']
        path.append(predecessor)
        current_node = predecessor

    path.reverse()
    return path

# Create a graph
graph = nx.Graph()
graph.add_nodes_from(['Kingston', 'St. Andrew', 'St. Catherine', 'Clarendon', 'Manchester', 'St. Elizabeth',
                     'Westmoreland', 'Hanover', 'St. James', 'Trelawny', 'St. Ann', 'St. Mary', 'Portland', 'St. Thomas'])

graph.add_edges_from([('Kingston', 'St. Andrew'), ('Kingston', 'St. Catherine'), ('St. Andrew', 'St. Catherine'),
                      ('St. Andrew', 'Clarendon'), ('St. Andrew', 'St. Mary'), ('St. Catherine', 'Clarendon'),
                      ('St. Catherine', 'St. Elizabeth'), ('St. Catherine', 'Manchester'), ('Clarendon', 'Manchester'),
                      ('Clarendon', 'St. Elizabeth'), ('Clarendon', 'St. Ann'), ('Manchester', 'St. Elizabeth'),
                      ('St. Elizabeth', 'Westmoreland'), ('St. Elizabeth', 'Hanover'), ('Westmoreland', 'Hanover'),
                      ('Westmoreland', 'St. James'), ('Hanover', 'St. James'), ('St. James', 'Trelawny'),
                      ('St. James', 'St. Ann'), ('St. James', 'St. Elizabeth'), ('Trelawny', 'St. Ann'),
                      ('Trelawny', 'St. Mary'), ('St. Ann', 'St. Mary'), ('St. Ann', 'St. Thomas'),
                      ('St. Mary', 'St. Thomas'), ('St. Mary', 'Portland'), ('St. Thomas', 'Portland')])


# Define the heuristic values for each node
heuristic = {
    'Kingston': 5,
    'St. Andrew': 4,
    'St. Catherine': 3,
    'Clarendon': 4,
    'Manchester': 3,
    'St. Elizabeth': 4,
    'Westmoreland': 3,
    'Hanover': 2,
    'St. James': 2,
    'Trelawny': 3,
    'St. Ann': 2,
    'St. Mary': 3,
    'Portland': 4,
    'St. Thomas': 5
}

# Define the start and goal nodes
start_node = 'Westmoreland'
goal_node = 'Portland'

# Perform Best-First Search
path = best_first_search(graph, start_node, goal_node, heuristic)

# Visualization
pos = nx.spring_layout(graph)

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(graph, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(graph, pos, font_size=12, font_color='black')

# Highlight the explored nodes in red
explored_nodes = set(path)
nx.draw_networkx_nodes(graph, pos, nodelist=explored_nodes, node_size=500, node_color='red')

# Highlight the start and goal nodes in green and blue, respectively
nx.draw_networkx_nodes(graph, pos, nodelist=[start_node], node_size=500, node_color='green')
nx.draw_networkx_nodes(graph, pos, nodelist=[goal_node], node_size=500, node_color='blue')

# Draw the path in yellow
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(graph, pos, edgelist=path_edges, width=2.0, edge_color='yellow')

plt.axis('off')
plt.title('Best-First Search')
plt.show()
