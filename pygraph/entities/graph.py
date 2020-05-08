import abc

from pygraph.exceptions import *


class GraphBase:
    """ Avoid use __variable in base class ... """

    dict_dict_dict = dict
    dict_dict = dict
    node_factory = dict

    def __init__(self, kwargs):
        self._adj = self.dict_dict_dict()  # dict of dict of dict
        self._nodes = self.dict_dict()  # dict of dict
        self._meta = kwargs  # graph's meta data

    @abc.abstractmethod
    def add_edge(self, *args, **kwargs):
        """ add edge """

    @abc.abstractmethod
    def add_node(self, *args, **kwargs):
        """ add node """

    @abc.abstractmethod
    def adj_nodes(self, node):
        """ find adjacent nodes """

    @property
    def nodes(self):
        return self._nodes

    @property
    def adj(self):
        return self._adj

    @property
    def meta(self):
        return self._meta

    def neighbors(self, node):
        """ return the adjacent nodes list of node """
        try:
            return iter(self._adj[node])
        except KeyError:
            raise NodeNotExist(f'Node {node} does not exist in the graph')

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __contains__(self, item):
        try:
            return item in self._nodes
        except TypeError:
            return False

    def __getitem__(self, item):
        return self.adj[item]


class UndirectedGraph(GraphBase):
    """"""

    def __init__(self, **kwargs):
        """"""
        super().__init__(kwargs)

    def add_node(self, node, **kwargs):
        """ add node

        :param node: hashable object
        :param kwargs: metadata of the node
        :return:
        """
        if node not in self._nodes:
            self._adj[node] = {}
            metadata = self._nodes[node] = self.node_factory()
            metadata.update(kwargs)
        else:
            self._nodes[node].update(kwargs)

    def add_edge(self, node_a, node_b, **kwargs):
        """ add edge, an edge is pair of nodes, order is not important in undirected graphs.

        :param node_a:
        :param node_b:
        :param kwargs: the meta data of the edge
        :return:
        """
        # add nodes
        if node_a not in self._nodes:
            self._nodes[node_a] = self.node_factory()  # holds nodes meta data
            self._adj[node_a] = {}
            self._adj[node_a][node_b] = {}
        if node_b not in self._nodes:
            self._nodes[node_b] = self.node_factory()
            self._adj[node_b] = {}
            self._adj[node_b][node_a] = {}
        # add edge
        metadata = self._adj[node_a].get(node_b, {})
        metadata.update(kwargs)
        self._adj[node_a][node_b] = metadata
        self._adj[node_b][node_a] = metadata

    def adj_nodes(self, node) -> dict:
        """ return the adjacent nodes of given node """
        if node in self._adj:
            return self._adj[node]
        else:  # is this a good idea to return empty when node is not there?
            return {}

    def degree(self, node=None) -> int:
        """ get degree of node, if node is None, return total degree sum """
        if node:
            if node not in self._nodes:
                raise ValueError('node %s not in the graph' % node)
            else:
                return int(sum(self._adj[node]))
        else:
            return sum(len(e) for n, e in self._adj.items()) // 2

    def number_of_edge(self, a=None, b=None) -> int:
        """ get the edge number of node a and b, if no a, get total number of edge """
        if a and not b:
            raise ValueError('Second node must be provided if first node is given')
        if not a:
            return self.degree()
        if a in self._adj[b]:
            return 1

        return 0
