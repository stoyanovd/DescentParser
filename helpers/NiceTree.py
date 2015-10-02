import pydotplus
from helpers import Consts
from helpers.ParsedTree import ParsedTree


def make_tree(t, graph):
    node = pydotplus.Node(name='name_' + str(Consts.global_counter), label=t.name)
    graph.add_node(node)
    Consts.global_counter += 1
    for sub_tree in t.children:
        sub_node = make_tree(sub_tree, graph)
        edge = pydotplus.Edge(node, sub_node)
        graph.add_edge(edge)

    return node