def generate_edges(graph):
    edge = []
    for node in graph:
        for neighbour in graph[node]:
            edge.append((node,neighbour))
    for x in edge:
        print(x)
def isolated_nodes(graph):
    isolated = []
    for nodes in graph:
        if not graph[nodes]:
            isolated.append(nodes)
    print("Isolated node: ",isolated)

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
generate_edges(graph)
isolated_nodes(graph)