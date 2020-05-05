from pygraph.entities.graph import UndirectedGraph


def dfs_path(graph, source):
    """ get paths from source to other nodes.

    Note: not all the path, but one of the path if exist

    :param graph: Graph
    :param source: the source node
    :return:
    {target: [source, x, x, node2]}
    """