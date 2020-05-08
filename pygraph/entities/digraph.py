from pygraph.entities.graph import GraphBase


class DiGraph(GraphBase):
    """"""

    dict_dict_dict = dict
    dict_dict = dict
    node_factory = dict

    def __init__(self, **kwargs):
        """"""
        super().__init__(kwargs)

