import unittest
from pygraph.entities.graph import UndirectedGraph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.udg = UndirectedGraph()
        self.sample = UndirectedGraph()
        self.sample.add_edge('a', 'b')
        self.sample.add_edge('a', 'c')
        self.sample.add_edge('b', 'c')

    def test_add_node(self):
        ud = self.udg
        ud.add_node('a')
        self.assertDictEqual(ud.nodes, {'a': {}})

        ud.add_node('b')
        self.assertDictEqual(ud.nodes, {'a': {}, 'b': {}})

    def test_add_edge(self):
        ud = self.udg
        ud.add_edge('a', 'b')
        self.assertDictEqual(ud.nodes, {'a': {}, 'b': {}})
        self.assertDictEqual(ud.adj, {'a': {'b': {}}, 'b': {'a': {}}})

    def test_adj_node(self):
        adj = self.sample.adj_nodes('a')
        self.assertDictEqual(adj, {'b': {}, 'c': {}})

        adj = self.sample.adj_nodes('b')
        self.assertDictEqual(adj, {'a': {}, 'c': {}})

    def test_number_of_edge(self):
        num = self.sample.number_of_edge()
        self.assertEqual(3, num)

        num = self.sample.number_of_edge('a', 'b')
        self.assertEqual(1, num)