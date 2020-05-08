"""
Define problem: Degree of separation
"""
from pygraph.algos.path import bfs_path


def degree_of_separation(graph, node_a, node_b):
    """ find min degree of separation of a and b. if not connected, -1

    :param graph:
    :param node_a: the hash of node a
    :param node_b: the hash of node b
    :return: int. -1 if not connected.
    """
    paths = bfs_path(graph, node_a)
    if node_b in paths:
        short_path_a_b = paths[node_b]
        return len(short_path_a_b)
    else:  # there is no path
        return -1

