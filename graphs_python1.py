class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            self.graph_dict = []
        self.graph_dict = graph_dict

    def print_vertices(self):
        print("--------\nVertices are: ",end = " ")
        for keys in self.graph_dict.keys():
            print(keys,end=" ")
        print("")

    def print_edges(self):
        print("--------\nEdges are: ")
        ls = []
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                if {neighbour,node} not in ls:
                    ls.append({node,neighbour})
        for item in ls:
            print(item)

    def add_vertex(self,vertex):
        print("--------")
        if vertex in self.graph_dict:
            print("Vertex '{}' is already present.".format(vertex))
        else:
            print("Vertex '{}' is added.".format(vertex))
            a = {vertex:[]}
            self.graph_dict.update(a)

    def add_edge(self,edge):
        if edge[0] in self.graph_dict:
            self.graph_dict[edge[0]] = edge[1]
        else:
            self.add_vertex(edge[0])
            self.graph_dict[edge[0]] = edge[1]

    def isolated_nodes(self):
        isolated = []
        print('')
        print("--------")
        for node in self.graph_dict:
            if not self.graph_dict[node]:
                    isolated.append(node)
        print("Isolated vertices (ie, with no vertices): ",isolated)

    def delete_vertex(self,vertex):

        if vertex in self.graph_dict:
            self.graph_dict.pop(vertex)
        else:
            print('')
            print("--------")
            print("Vertex does'nt exist.")

    def delete_edge(self,start,endd):
        if start in self.graph_dict:
            self.graph_dict[start].remove(endd)




if __name__ == '__main__':
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
        }
    graph = Graph(g)
    print("--------\nSTRUCTURE OF GRAPH.")
    for i in g:
        print(i," : ",g[i])
    # graph.print_edges()
    # graph.print_vertices()
    # graph.add_vertex('c')
    # graph.add_vertex('l')
    # graph.print_vertices()
    # graph.add_edge(['a','x'])
    # graph.print_edges()

    graph.delete_edge('c','c')
    graph.print_edges()




    # graph.isolated_nodes()
    print("--------")

# g = {"a": ["d"],
#      "b": ["c"]
#      }
# a = {'a':[]}
# g.update(a)
# print(g)
# a = {'a': 1,
#      'b': 2,
#      'c': 4}
# a.pop('b')
# print(a)