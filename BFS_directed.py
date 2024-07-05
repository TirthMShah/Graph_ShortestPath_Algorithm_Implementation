# Find's the path for both directed graph using BFS.


import networkx as nx
import matplotlib.pyplot as plt
import random,time


class Node:
    parent = -1
    visited = False

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor) #For directed graph.


def create_nodes(node_names,G):
    nodes = []
    for name in node_names:
        nodes.append(Node(name))
        G.add_node(name)
    return nodes


def add_random_neighbors(nodes, probability,G):
    other_nodes = nodes.copy()
    for node in nodes:
        count = 0
        random.shuffle(other_nodes)
        for other_node in other_nodes:

            if node != other_node and count <= 3 :

                node.add_neighbor(other_node) #For directed graph. 
                G.add_edge(node.name, other_node.name, weight=1) #For directed graph.
                
            count+=1


def bfs(start:Node):
    start.visited = True
    queue = [start]
 
    while queue:
        node = queue[0]
        queue.pop(0)
        for i in node.neighbors:
            time.sleep(0.01)
            if not i.visited:
                i.parent = node
                i.visited = True
                queue += [i]


def find_path(start,end):
    path = [end.name]

    while end.parent != start :

        if end.parent != -1:
            path+=[end.parent.name]
            end = end.parent
        else: return []

    path += [start.name]

    return path[::-1]


def main():

    G = nx.DiGraph() #For directed graph.

    nodes = create_nodes([i for i in range(10)], G)
    add_random_neighbors(nodes, 0.5, G)  # Adjust the probability as needed

    pos = nx.spring_layout(G)  # positions for all nodes
    labels = {node: node for node in G.nodes()}
    nodes = {node.name : node for node in nodes}

    # Draw the graph
    nx.draw(G, pos, with_labels=False, node_color='b', font_color='white', font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_weight='bold')

    nx.draw_networkx_edges(G, pos, alpha=0.4, arrows=True) #For directed graph.

    plt.show()
    start_node = input("Enter the start node: ").strip().upper()

    try:
        start_node = int(start_node) # In case if node has an interger value.
    except:
        ...

    try:
        start_node = nodes[start_node]
    except:
        ...
    start_time = time.time()

    # Execute your method
    bfs(start_node) # Set's the parent for each node starting with start_node as enterd by user.

    # Calculate the runtime
    end_time = time.time()
    runtime = end_time - start_time
    print("\nRuntime(0.01 sec pause after each iteration in BFS) : ", runtime, "seconds\n")

    while True:
        
        end_node = input("Enter the node to be travelled (Quit to return): ").strip().upper()

        if (end_node).lower() == 'quit':
            return

        try:
            end_node = int(end_node) # In case if node has an interger value.
        except:
            ...

        try:
            end_node = nodes[end_node]
        except:
            print("invalid Node")
            continue

        shortest_path = find_path(start_node,end_node)

        if shortest_path == []:
            print(f"No connection between {start_node.name} and {end_node.name}.")
            continue

        # Highlight the final path
        nx.draw(G, pos, with_labels=False, node_color='b', font_color='white', font_weight='bold')
        nx.draw_networkx_labels(G, pos, labels=labels, font_color='black', font_weight='bold')
        
        for i in range(len(shortest_path) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1])], edge_color='r', width=2)
            plt.pause(0.5)
        plt.show()

