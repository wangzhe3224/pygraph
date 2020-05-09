import unittest

from pygraph.algos.cyclic import is_cyclic, directed_cycle
from pygraph.entities.utils import *


class TestCyclic(unittest.TestCase):

    def test_cyclic(self):

        gp = get_cyclic_graph()
        is_c = is_cyclic(gp)
        self.assertEqual(True, is_c)

    def test_directed_cycle(self):
        gp = DiGraph()
        gp.add_edge(0, 5)
        gp.add_edge(5, 4)
        gp.add_edge(4, 3)
        gp.add_edge(3, 5)
        cycle = directed_cycle(gp)
        self.assertListEqual([3, 4, 5, 3], cycle)
        gp = get_cyclic_digraph()
        #  a -> c -> d -> a cycle
        cycle = directed_cycle(gp)
        self.assertListEqual(['d', 'c', 'a', 'd'], cycle)

        # no cycle
        gp = get_digraph()
        cycle = directed_cycle(gp)
        self.assertListEqual([], cycle)
