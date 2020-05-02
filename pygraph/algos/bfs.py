from collections import deque


def bfs_edges(graph, source, depth=None, neighbors=None):
    """ get all the edges using breanth first method
    """

    visited = {source}
    if depth is None:
        depth = len(graph)
    if neighbors is None:
        neighbors = graph.neighbors

    queue = deque([(source, depth, neighbors(source))])

    while queue:
        parent, depth_now, children = queue[0]
        try:
            child = next(children)
            if child not in visited:
                yield parent, child
                visited.add(child)
                if depth_now > 1:
                    queue.append((child, depth_now, neighbors(child)))
        except StopIteration:
            queue.popleft()