import networkx as nx
import matplotlib.pyplot as plt


class Graphs:
    def __init__(self, graphs) -> None:
        self.graphs = graphs
        pass

    def draw_initial_graphs(self):
        for graph in self.graphs:
            key = list(graph.keys())[0]
            edges = graph[key]
            G = nx.DiGraph()
            G.add_edges_from(edges)
            pos = nx.spring_layout(G)
            nx.draw_networkx_nodes(G, pos, node_size=500)
            nx.draw_networkx_edges(G, pos,
                                   edgelist=G.edges(data=True), edge_color='black')
            nx.draw_networkx_labels(G, pos)
            plt.title(key)
            plt.savefig(key + '.png')
            plt.show()


# different types of graphs which will produce very different transtive closures.
equivalence_relation = {"equivalence_relation": [(1, 2),
                                                 (2, 3),
                                                 (3, 1),
                                                 (4, 5),
                                                 (5, 6),
                                                 (6, 4)]
                        }

finer_equivalence = {"finer_equivalence": [(1, 2),
                                           (2, 1),
                                           (3, 4),
                                           (4, 3),
                                           (5, 6),
                                           (6, 6)]}


total_ordering = {"total_ordering": [(1, 2),
                                     (2, 3),
                                     (3, 4),
                                     (4, 5),
                                     (5, 6),
                                     (6, 7),
                                     (7, 8),
                                     ]}

partial_ordering = {"partial_ordering": [(1, 2),
                                         (2, 3),
                                         (3, 4),
                                         (5, 6),
                                         (6, 7),
                                         (7, 8),
                                         ]}
universal_relation = {"universal_relation": [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 1),
]}


if __name__ == "__main__":

    graphs = [equivalence_relation, finer_equivalence, universal_relation,
              total_ordering, partial_ordering, universal_relation]

    G = Graphs(graphs=graphs)
    G.draw_initial_graphs()
