import unittest

from pygraph.algos.connect import is_connected, strong_connect
from pygraph.entities.utils import *


class TestConnect(unittest.TestCase):

    def test_is_connect(self):
        gp = get_sample_graph()
        is_c = is_connected(gp, 'a', 'b')
        self.assertEqual(True, is_c)

        gp = get_disconnect_graph()
        is_c = is_connected(gp, 'a', 'z')
        self.assertEqual(False, is_c)

    def test_strong_connection(self):

        gp = DiGraph()
        gp.add_edge(0, 1)
        gp.add_edge(1, 0)
        sc = strong_connect(gp, 0, 1)
        self.assertEqual(True, sc)

        gp = DiGraph()
        gp.add_edge(0, 1)
        sc = strong_connect(gp, 0, 1)
        self.assertEqual(False, sc)
