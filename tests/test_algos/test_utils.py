from pygraph.algos.utils import intersect


def test_intersect():

    a = {'a': {}, 'b': {}}
    b = {'b': {}}
    inter = intersect(a, b)
    assert {'b': {}} == inter