import time
import networkx as nx
import matplotlib.pyplot as plt
import os
import ast

def dfs(graph, start_node, end_node):
    stack = [start_node]
    visited = set()
    order = []
    stack_list = []

    while stack:
        stack_list.append(stack.copy())
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)

            if node == end_node:
                break

            stack.extend(n for n in graph[node] if n not in visited)

    return order, stack_list

def print_result(order, stack_list, G):
    adjacency_list = {}

    for i, node in enumerate(order, start=1):
        if i == len(order):
            adjacency_list[node] = ['']
        else:
            adjacency_list[node] = [n for n in G.neighbors(node) if n not in order[:i]]

    print("\nExpanded Nodes: ", order)
    print("Adjacency List:", adjacency_list)
    print("List L:", stack_list)

    shortest_path = nx.shortest_path(G, source=order[0], target=order[-1])
    print("Path:", shortest_path, end = "\n\n")

    with open('output.txt', 'w') as f:
        f.write("\nExpanded Nodes: " + str(order) + "\n")
        f.write("Adjacency List: " + str(adjacency_list) + "\n")
        f.write("List L: " + str(stack_list) + "\n")
        f.write("Path: " + str(shortest_path) + "\n\n")

def visualize(order, title, G, pos,start_node,end_node):

    plt.figure()

    for i, node in enumerate(order, start=1):

        pos = nx.planar_layout(G)
        pos[start_node] = (0, 1)
        pos[end_node] = (0, -0.5)
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['red' if n == node else 'grey' for n in G.nodes()])
        plt.draw()
        plt.pause(0.5)
    time.sleep(0.5)
    plt.show()

def perform_dfs(file_path):
    start_node, end_node, dfs_data = read_file(file_path)
    G = nx.Graph()
    G.add_edges_from(dfs_data)
    order, stack_list = dfs(G, start_node, end_node)
    return order, 'DFS', G, nx.spring_layout(G), stack_list, start_node, end_node

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    start_node = data[0].strip()
    end_node = data[1].strip()
    dfs_data = ast.literal_eval(data[2].strip())

    if len(start_node) != 1 or len(end_node) != 1:
        raise ValueError("The first and second rows of the input file should contain only one character.")

    return start_node, end_node, dfs_data

def main(file_path):
    order, title, G, pos, start_node, end_node = perform_dfs(file_path)
    visualize(order, title, G, pos,start_node,end_node)
if __name__ == "__main__":
    main("input.txt")
