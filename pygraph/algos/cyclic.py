from pygraph.entities.digraph import DiGraph


def is_cyclic(graph):
    """ is a graph has cyclic?

    """

    _visited = set()
    _cyclic = {'status': False}

    # TODO: add cycle path
    def _dfs(graph, node_a, node_b):
        _visited.add(node_a)
        for _node in graph[node_a]:  # loop all its neighbours
            if _node not in _visited:  # meet a new node
                _dfs(graph, _node, node_a)
            elif _node == node_b:  # meet this node before, check if is same node
                _cyclic['status'] = True

    for node in graph.nodes:  # This is for unconnected graph
        if node not in _visited:
            _dfs(graph, node, node)

    return _cyclic['status']


def directed_cycle(graph: DiGraph):
    """ find directed cycles in DiGraph, is so, return cycles, otherwise empty

    Algorithm
    ---------
    Use a depth-first search method, keep track the stack, if we find a node that
    we already visited once, we then check if the node is in the stack, if so, we
    find a directed cycle. Because every node in the current stack is on the same path.

    :param graph:
    :return:
    """
    _cycles = []
    _visited = set()
    _edge_to = {}
    _on_stack = {}

    for node in graph.nodes:  # go through each nodes once
        if node in _visited:
            continue

        _visited.add(node)
        _stack = [(node, )]  # push a node (append)

        while _stack:
            cur, = _stack.pop()  # unstack a node
            _on_stack[cur] = True
            _visited.add(cur)
            neighbours = graph[cur]
            for child in neighbours:
                if _cycles:  #
                    continue
                elif child not in _visited:
                    _edge_to[child] = cur
                    _stack.append((child, ))  # push stack (recursive)
                elif _on_stack[child]:
                    _cycles = []
                    _tmp = cur
                    while _tmp != child:
                        _cycles.append(_tmp)
                        _tmp = _edge_to[_tmp]
                    _cycles.append(child)
                    _cycles.append(cur)
        # current node is removed from stack
        _on_stack[node] = False

        return _cycles
