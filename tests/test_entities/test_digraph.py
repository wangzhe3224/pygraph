import unittest

from pygraph.entities.utils import get_digraph
from pygraph.algos.path import dfs_path


class TestCase(unittest.TestCase):

    def test_add_edge(self):
        gp = get_digraph()
        self.assertDictEqual(gp.nodes, {'a': {}, 'b': {}, 'c': {}})

    def test_path(self):
        gp = get_digraph()
        p = dfs_path(gp, 'a')
        print(p)
