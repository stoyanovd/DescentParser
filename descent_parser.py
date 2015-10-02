import io

import pprint
from helpers import NiceTree
from helpers.Parser import Parser
import graphviz
import pydotplus


def main():
    f = io.StringIO("* + 2 2 + 3 1")
    parser = Parser()
    tree = parser.parse(f)
    print(tree)

    r = tree.mix_list_view()
    pprint.pprint(r, indent=4, width=1)

    graph = pydotplus.Dot(graph_type='graph')
    NiceTree.make_tree(tree, graph)
    graph.write(path='a.png', format='png')

    print('result:', tree.result())


if __name__ == '__main__':
    main()