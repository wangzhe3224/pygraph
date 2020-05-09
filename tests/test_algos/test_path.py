import unittest

from pygraph.algos.path import dfs_path, bfs_path
from pygraph.entities.utils import *


class TestPath(unittest.TestCase):

    def test_dfs_path(self):
        gp = get_sample_graph()
        paths = dfs_path(gp, 'a')
        tar = {'a': ['a'], 'b': ['b', 'a'], 'c': ['c', 'a'], 'd': ['d', 'c', 'a'], 'e': ['e', 'b', 'a']}
        self.assertDictEqual(paths, tar)

    def test_bfs_path(self):
        gp = get_sample_graph()
        paths = bfs_path(gp, 'a')
        tar = {'a': ['a'], 'b': ['b', 'a'], 'c': ['c', 'a'], 'd': ['d', 'c', 'a'], 'e': ['e', 'b', 'a']}
        self.assertDictEqual(tar, paths)

    def test_dfs_digraph_path(self):
        gp = get_digraph()
        gp.add_edge('c', 'd')
        gp.add_edge('d', 'c')
        paths = dfs_path(gp, 'a')
        self.assertDictEqual({'a': ['a'], 'b': ['b', 'a'], 'c': ['c', 'a'], 'd': ['d', 'c', 'a']}, paths)
