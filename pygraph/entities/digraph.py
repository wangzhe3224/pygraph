from typing import Hashable

from pygraph.entities.graph import GraphBase


class DiGraph(GraphBase):
    """"""

    dict_dict_dict = dict
    dict_dict = dict
    node_factory = dict
    edge_factory = dict

    def __init__(self, **kwargs):
        """"""
        super().__init__(kwargs)
        self._succ = self._adj
        self._pred = self.dict_dict_dict()

    def add_node(self, node: Hashable, **kwargs):
        """ Add node to graph,

        :param node:
        :param kwargs: node's meta data
        :return:
        """
        if node not in self._succ:
            self._succ[node] = self.dict_dict()
            self._pred[node] = self.dict_dict()
            attr_dict = self._nodes[node] = self.node_factory()
            attr_dict.update(kwargs)
        else:  # already existed
            self._nodes[node].update(kwargs)

    def add_edge(self, node_a: Hashable, node_b: Hashable, **kwargs):
        """ add edge to graph: node_a -> node_b

        :param node_a:
        :param node_b:
        :param kwargs: meta data for edge, weights can go here!
        :return:
        """
        if node_a not in self._succ:
            self._succ[node_a] = self.dict_dict()
            self._pred[node_a] = self.dict_dict()
            self._nodes[node_a] = self.node_factory()
        if node_b not in self._succ:
            self._succ[node_b] = self.dict_dict()
            self._pred[node_b] = self.dict_dict()
            self._nodes[node_b] = self.node_factory()

        data = self._adj[node_a].get(node_b, self.edge_factory())
        data.update(kwargs)
        self._succ[node_a][node_b] = data
        self._pred[node_b][node_a] = data

    def adj_nodes(self, node: Hashable):
        """ find adj nodes view

        :param node:
        :return:
        """
        return self._succ[node]

    def reverse(self) -> GraphBase:
        """ reverse the graph """
        gp = self.__class__()
        for a in self.nodes:
            for b in self._adj[a]:
                gp.add_edge(b, a)

        return gp
