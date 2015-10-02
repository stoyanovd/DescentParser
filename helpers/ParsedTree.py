from helpers import Consts


class ParsedTree:
    def __init__(self, name, *args):
        self.name = name
        self.children = []
        for sub_tree in args:
            self.children.append(sub_tree)

    def __str__(self):
        if self.children:
            children_string = ', '.join([str(i) for i in self.children])
            return ''.join(['[', self.name, ', ', children_string, ']'])
        return '(' + self.name + ')'

    def mix_list_view(self):
        if self.children:
            return {self.name: [x.mix_list_view() for x in self.children]}
        return self.name

    def result(self):
        if not self.children:
            return int(self.name)
        if len(self.children) == 1:
            return self.children[0].result()
        if len(self.children) == 3:
            return Consts.operations[self.children[0].name](self.children[1].result(),
                self.children[2].result())
        else:
            raise InvalidParsedTree


class InvalidParsedTree(Exception):
    pass