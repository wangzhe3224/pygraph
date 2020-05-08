import unittest

from pygraph.algos.connect import is_connected
from pygraph.entities.utils import *


class TestConnect(unittest.TestCase):

    def test_is_connect(self):
        gp = get_sample_graph()
        is_c = is_connected(gp, 'a', 'b')
        self.assertEqual(True, is_c)

        gp = get_disconnect_graph()
        is_c = is_connected(gp, 'a', 'z')
        self.assertEqual(False, is_c)

