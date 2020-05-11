from unittest import TestCase

from pygraph.algos.mst import prim_mst
from pygraph.entities.graph import UndirectedGraph


class TestMst(TestCase):

    def test_prime_mst(self):
        gp = UndirectedGraph()
        gp.add_edge(1, 2, weight=1.)
        gp.add_edge(1, 3, weight=2.)
        gp.add_edge(2, 3, weight=3.)
        gp.add_edge(2, 5, weight=4.)

        mst = prim_mst(gp)
        self.assertListEqual([(1, 2, {'weight': 1.0}), (1, 3, {'weight': 2.0}), (2, 5, {'weight': 4.0})],
                             list(mst))