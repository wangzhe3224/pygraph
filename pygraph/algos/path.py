from collections import deque

from pygraph.entities.graph import UndirectedGraph


class DfsPath:

    def __call__(self, graph, source):
        """"""
        return dfs_path(graph, source)


def dfs_path(graph, source):
    """ get paths from source to other nodes.

    edge_to is a parent-link representation of the tree which has source as root.
    Note: not all the path, but one of the path if exist

    :param graph: Graph
    :param source: the source node
    :return:
    {target: [source, x, x, node2]}
    """
    visited = set()
    edge_to = {source: [source]}  # node is connected to itself.

    def _dfs_path(graph, start):
        for _node in graph[start]:  # all its neighbour
            if _node in visited:
                continue
            visited.add(_node)
            edge_to[_node] = start
            _dfs_path(graph, _node)

    # DFS
    _dfs_path(graph, source)

    return path_view(graph.nodes, edge_to, source)


def bfs_path(graph, source):
    """ a breadth first search for paths. These suppose to be the shortest paths.

    edge_to is a parent-link representation of the tree which has source as root.

    Reference
    ---------
    <Algorithms 4th edition> by Robert Sedgewick. P540

    :param source: a source node
    """
    _queue = deque([])
    _visited = set()
    _queue.append(source)
    _edge_to = {source: source}
    while _queue:
        cur_node = _queue.popleft()
        for child in graph[cur_node]:
            if child in _visited:
                continue

            _visited.add(cur_node)
            _edge_to[child] = cur_node
            _queue.append(child)

    return path_view(graph.nodes, _edge_to, source)


def path_view(nodes, edge_to: dict, source):
    """ convert edge_to to path view """
    _paths = {}

    for node in nodes:
        if node in edge_to:  # has a path
            path = []
            _next = node
            while _next != source:
                path.append(_next)
                _next = edge_to[_next]
            path.append(source)
            _paths[node] = path

        else:
            _paths[node] = None   # no path

    return _paths
