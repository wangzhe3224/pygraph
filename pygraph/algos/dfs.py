

def dfs_edges(graph, source=None, depth=None, trace_stack=False):
    """ Iterate over edges in a depth first way. with stack

    Note: a-b and b-a only show one of them, so undirected graph algo.

    :param graph:
    :param source:
    :param depth:
    :return:
    """
    if source is None:
        nodes = graph
    else:
        nodes = [source]

    if depth is None:
        depth = len(graph)

    visited = set()

    for start in nodes:  # this layer make sure that disconnected graph is ok
        if start in visited:
            continue

        visited.add(start)
        stack = [(start, depth, iter(graph[start]))]
        while stack:
            if trace_stack:
                print(stack)
            parent, depth_now, children = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    yield parent, child
                    visited.add(child)
                    if depth_now > 1:
                        stack.append((child, depth_now-1, iter(graph[child])))
            except StopIteration:
                stack.pop()


def rec_dfs_edges(graph):
    """ recursive way for above
    Note: a-b and b-a are different in this case..
    """
    nodes = graph.nodes  # type: dict
    visited = set()
    start = list(nodes.keys())[0]
    edges = []

    def _rec_dfs(graph, _start, _nodes):
        for _node in nodes:
            if _node in visited:
                continue
            # new node
            visited.add(_node)
            children = graph[_node]
            for child in children:
                edges.append((_node, child))
                _rec_dfs(graph, child, _nodes)

    _rec_dfs(graph, start, nodes)
    return edges

