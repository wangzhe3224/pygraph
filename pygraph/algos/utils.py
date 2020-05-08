

def intersect(nodes_a, nodes_b) -> {}:
    """ get nodes in a and in b back with nodes meta data, empty if none

    :param nodes_a: nodes set a, dict of dict
    :param nodes_b: nodes set b, dict of dict
    :return common nodes set. dict of dict
    """

    return {k: v for k, v in nodes_a.items() if k in nodes_b}