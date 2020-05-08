import unittest

from pygraph.algos.dfs import dfs_edges, rec_dfs_edges
from pygraph.entities.utils import get_sample_graph, get_disconnected_graph, ex41
from pygraph.entities.graph import UndirectedGraph


class TestDFS(unittest.TestCase):

    def setUp(self) -> None:
        self.sample = get_sample_graph()
        self.disconnected = get_disconnected_graph()

    def test_dfs(self):

        edges = dfs_edges(self.sample)
        self.assertListEqual(list(edges), [('a', 'b'), ('b', 'e'), ('a', 'c'), ('c', 'd')])

        edges = dfs_edges(self.disconnected)
        self.assertListEqual(list(edges), [('a', 'b'), ('c', 'd')])

        gp = ex41()
        edges = dfs_edges(gp)
        self.assertListEqual(list(edges), [(0, 5), (5, 3), (3, 2), (2, 4), (2, 1)])

    def test_rec_dfs(self):
        edges = rec_dfs_edges(self.sample)
        tar = [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c'), ('e', 'b'), ('c', 'a'), ('b', 'e'), ('a', 'c')]
        self.assertListEqual(edges, tar)

