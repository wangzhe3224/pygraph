import abc

from pygraph.exceptions import *


class Graph(abc.ABC):
    """ Graph interface """

    @abc.abstractmethod
    def add_edge(self, *args, **kwargs):
        """ add edge """

    @abc.abstractmethod
    def add_node(self, *args, **kwargs):
        """ add node """

    @abc.abstractmethod
    def adj_nodes(self, node):
        """ find adjacent nodes """


class UndirectedGraph(Graph):
    """"""
    dict_dict_dict = dict
    dict_dict = dict

    def __init__(self):
        """"""
        self.__adj = self.dict_dict_dict()  # dict of dict of dict
        self.__nodes = self.dict_dict()  # dict of dict

    def add_node(self, node, **kwargs):
        """ add node

        :param node: hashable object
        :param kwargs: metadata of the node
        :return:
        """
        if node not in self.__nodes:
            self.__adj[node] = {}
            metadata = self.__nodes[node] = {}
            metadata.update(kwargs)
        else:
            self.__nodes[node].update(kwargs)

    def add_edge(self, node_a, node_b, **kwargs):
        """ add edge, an edge is pair of nodes, order is not important in undirected graphs.

        :param node_a:
        :param node_b:
        :param kwargs: the meta data of the edge
        :return:
        """
        # add nodes
        if node_a not in self.__nodes:
            self.__nodes[node_a] = {}  # holds nodes meta data
            self.__adj[node_a] = {}
            self.__adj[node_a][node_b] = {}
        if node_b not in self.__nodes:
            self.__nodes[node_b] = {}
            self.__adj[node_b] = {}
            self.__adj[node_b][node_a] = {}
        # add edge
        metadata = self.__adj[node_a].get(node_b, {})
        metadata.update(kwargs)
        self.__adj[node_a][node_b] = metadata
        self.__adj[node_b][node_a] = metadata

    def adj_nodes(self, node) -> dict:
        """ return the adjacent nodes of given node """
        if node in self.__adj:
            return self.__adj[node]
        else:  # is this a good idea to return empty when node is not there?
            return {}

    def degree(self, node=None) -> int:
        """ get degree of node, if node is None, return total degree sum """
        if node:
            if node not in self.__nodes:
                raise ValueError('node %s not in the graph' % node)
            else:
                return int(sum(self.__adj[node]))
        else:
            return sum(len(e) for n, e in self.__adj.items()) // 2

    def number_of_edge(self, a=None, b=None) -> int:
        """ get the edge number of node a and b, if no a, get total number of edge """
        if a and not b:
            raise ValueError('Second node must be provided if first node is given')
        if not a:
            return self.degree()
        if a in self.__adj[b]:
            return 1

        return 0

    @property
    def nodes(self):
        return self.__nodes

    @property
    def adj(self):
        return self.__adj

    def neighbors(self, node):
        """ return the adjacent nodes list of node """
        try:
            return iter(self.__adj[node])
        except KeyError:
            raise NodeNotExist(f'Node {node} does not exist in the graph')

    def __len__(self):
        return len(self.__nodes)

    def __iter__(self):
        return iter(self.__nodes)

    def __contains__(self, item):
        try:
            return item in self.__nodes
        except TypeError:
            return False

    def __getitem__(self, item):
        return self.adj[item]