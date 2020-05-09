from collections import deque

from pygraph.algos.cyclic import directed_cycle


def dfs_order(graph):
    """
    Note: only when graph is DAG, reverse post order make sense.
    :param graph:
    :return:
    """

    _visited = set()
    pre = deque([])   # queue
    post = deque([])  # queue
    reversed_post = deque([])   # stack

    def _dfs(g, _node):
        pre.append(_node)
        _visited.add(_node)
        for child in g[_node]:
            if child not in _visited:
                _dfs(g, child)

        post.append(_node)
        reversed_post.appendleft(_node)

    for node in graph.nodes:
        if node not in _visited:
            _dfs(graph, node)

    return pre, post, reversed_post


def topological_order(graph):
    """ Reverse postorder in a DAG is a topological sort """
    if not directed_cycle(graph):
        _, _, order = dfs_order(graph)
    else:  # if it is not a DAG, there is no topological order
        order = deque([])

    return order
