""" Minimum spanning tree """
from heapq import heappop, heappush
from itertools import count

from pygraph.entities.graph import UndirectedGraph


def prim_mst(graph: UndirectedGraph, weight_key: str = 'weight'):
    """"""
    nodes = set(graph.nodes.keys())
    c = count()
    while nodes:
        n = nodes.pop()
        visited = {n}
        _heap = []
        # find all edges from node n
        for v, d in graph[n].items():  # the other node and edge payload
            w = d.get(weight_key, 1.0)
            heappush(_heap, (w, next(c), n, v, d))

        # pick min crossing edge:
        while _heap:
            wt, _, n, v, d = heappop(_heap)  # pop min edge

            if v in visited or v not in nodes:
                continue
            # yield an edge
            yield n, v, d

            visited.add(v)
            nodes.discard(v)  # dont look it

            for v2, d2 in graph[v].items():
                if v2 in visited:
                    continue
                wt = d2.get(weight_key, 1.0)
                heappush(_heap, (wt, next(c), v, v2, d2))