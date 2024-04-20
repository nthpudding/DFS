def read_graph_from_file(file_path):
    graph = {}
    start_node = None
    end_node = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start_node = lines[0].strip()
        end_node = lines[1].strip()
        if len(start_node) > 1 or len(end_node) > 1:
            raise ValueError("Start node and end node should only contain one character.")
        for line in lines[2:]:
            parts = line.strip().split(':')
            node = parts[0].strip()
            if len(parts) > 1:
                neighbors = parts[1].strip().split()
                graph[node] = neighbors
            else:
                graph[node] = []
    return start_node, end_node, graph


def dfs(graph, start, goal, output_file_path):
    stack = [(start, [])]
    visited = set()

    with open(output_file_path, 'w') as output_file:

        output_file.write(f"{'Node':<15}  {'Adj List':<30} {'Open':<30} {'Path':<30} {'Close':<20}\n")

        open_nodes = [start]
        close_nodes = []

        while stack:
            node, path = stack.pop()

            if node not in visited:
                visited.add(node)
                path = path + [node]

                if node in open_nodes:
                    open_nodes.remove(node)
                close_nodes.append(node)

                if node == goal:
                    output_file.write(
                        f"{node:<15} {', '.join(graph.get(node, [''])):<30} {', '.join(open_nodes):<30} {', '.join(path):<30} {', '.join(close_nodes):<20}\n")
                    output_file.write(f"Path from {start} to {goal}: {', '.join(path)}\n")
                    break

                children = graph.get(node, [])
                next_open_nodes = [child for child in children if child not in visited and child not in open_nodes]
                open_nodes = open_nodes + next_open_nodes

                output_file.write(
                    f"{node:<15} {', '.join(graph.get(node, [''])):<30} {', '.join(open_nodes):<30} {', '.join(path):<30} {', '.join(close_nodes):<20}\n")

                stack.extend([(child, path) for child in children if child not in visited])


input_file_path = 'input.txt'
start_node, end_node, graph = read_graph_from_file(input_file_path)

output_file_path = 'output.txt'

dfs(graph, start_node, end_node, output_file_path)