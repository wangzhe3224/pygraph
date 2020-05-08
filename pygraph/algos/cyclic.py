

def is_cyclic(graph):
    """ is a graph has cyclic?

    """

    _visited = set()
    _cyclic = {'status': False}

    def _dfs(graph, node_a, node_b):
        _visited.add(node_a)
        for _node in graph[node_a]:
            if _node not in _visited:
                _dfs(graph, _node, node_a)
            elif _node == node_b:
                _cyclic['status'] = True

    for node in graph.nodes:  # This is for unconnected graph
        if node not in _visited:
            _dfs(graph, node, node)

    return _cyclic['status']