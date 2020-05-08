import unittest

from pygraph.algos.bfs import *
from pygraph.entities.utils import *


class TestBFS(unittest.TestCase):
    """"""

    def test_bfs_edges(self):

        ug = get_sample_graph()
        edges = bfs_edges(ug, 'a')
        self.assertListEqual(list(edges), [('a', 'b'), ('a', 'c'), ('b', 'e'), ('c', 'd')])