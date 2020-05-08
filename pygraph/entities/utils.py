from pygraph.entities.graph import *


def get_disconnect_graph():

    ud = get_sample_graph()
    ud.add_edge('z', 'y')
    ud.add_edge('w', 't')

    return ud


def get_sample_graph():

    ud = UndirectedGraph()
    ud.add_edge('a', 'b')
    ud.add_edge('c', 'd')
    ud.add_edge('a', 'c')
    ud.add_edge('b', 'e')

    return ud


def get_disconnected_graph():
    ud = UndirectedGraph()
    ud.add_edge('a', 'b')
    ud.add_edge('c', 'd')

    return ud


def ex41():
    """ <Algorithm> page 533 example for dfs """
    ud = UndirectedGraph()
    edges = [
        (0, 5), (2, 4), (2, 3), (1, 2), (0, 1), (3, 4), (3, 5), (0, 2)
    ]
    for e in edges:
        ud.add_edge(*e)

    return ud