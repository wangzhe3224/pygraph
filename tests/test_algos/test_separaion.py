import unittest
from pygraph.algos.separation import degree_of_separation
from pygraph.entities.utils import get_sample_graph, get_disconnected_graph


class TestAlgo(unittest.TestCase):

    def test_separation(self):

        gp = get_sample_graph()
        degree = degree_of_separation(gp, 'a', 'c')
        self.assertEqual(2, degree)

        gp = get_disconnected_graph()
        degree = degree_of_separation(gp, 'a', 'z')
        self.assertEqual(-1, degree)
