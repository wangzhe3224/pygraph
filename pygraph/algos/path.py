from pygraph.entities.graph import UndirectedGraph


class DfsPath:

    def __call__(self, graph, source):
        """"""
        return dfs_path(graph, source)


def dfs_path(graph, source):
    """ get paths from source to other nodes.

    Note: not all the path, but one of the path if exist

    :param graph: Graph
    :param source: the source node
    :return:
    {target: [source, x, x, node2]}
    """
    visited = set()
    edge_to = {}  # magic path..

    def _dfs_path(graph, start):
        for _node in graph[start]:  # all its neighbour
            if _node in visited:
                continue
            visited.add(_node)
            edge_to[_node] = start
            _dfs_path(graph, _node)

    # DFS
    _dfs_path(graph, source)

    paths = {}
    # find path
    for node in graph.nodes:
        if node in edge_to:  # has a path
            path = []
            _next = node
            while _next != source:
                path.append(_next)
                _next = edge_to[_next]
            path.append(source)
            paths[node] = path

        else:
            paths[node] = None   # no path

    return paths

def bfs_path(graph, source):
    """"""