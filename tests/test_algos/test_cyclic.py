import unittest

from pygraph.algos.cyclic import is_cyclic
from pygraph.entities.utils import *


class TestCyclic(unittest.TestCase):

    def test_cyclic(self):

        gp = get_cyclic_graph()
        is_c = is_cyclic(gp)
        self.assertEqual(True, is_c)
