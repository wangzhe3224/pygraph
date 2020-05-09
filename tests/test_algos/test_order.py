import unittest

from pygraph.algos.order import dfs_order, topological_order
from pygraph.entities.utils import *


class TestOrder(unittest.TestCase):

    def test_order(self):
        gp = get_sample_graph()
        pre, post, res = dfs_order(gp)
        self.assertListEqual(list(pre), ['a', 'b', 'e', 'c', 'd'])
        self.assertListEqual(list(post), ['e', 'b', 'd', 'c', 'a'])

    def test_topological_order(self):
        gp = DiGraph()
        gp.add_edge(0, 1)
        gp.add_edge(1, 2)
        gp.add_edge(2, 3)
        gp.add_edge(3, 1)
        tp = topological_order(gp)
        self.assertEqual(0, len(tp))
