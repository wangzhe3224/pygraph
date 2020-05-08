from pygraph.entities.graph import UndirectedGraph


def is_connected(graph, node_a, node_b) -> bool:
    """ are node a and node b connected?
    DFS uses preprocessing time and space proportional to V􏰁E to
    support constant-time connectivity queries in a graph.

    _id will provide information about disconnected components.
    """
    _visited = set()
    _id = {}  #
    _count = 0

    def _dfs(_graph, start):
        """"""
        _visited.add(start)
        _id[start] = _count

        for _node in _graph[start]:
            if _node in _visited:
                continue

            _dfs(_graph, _node)

    # call dfs
    for node in graph.nodes:
        if node not in _visited:
            _dfs(graph, node)
            _count += 1

    return _id[node_a] == _id[node_b]