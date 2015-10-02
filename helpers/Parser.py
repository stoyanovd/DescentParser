import io
from helpers.LexicalAnalyzer import LexicalAnalyzer
from helpers.ParsedTree import ParsedTree


class Parser:
    def __init__(self):
        self.lex = None

    def S(self):
        if self.lex.cur_token[0] == 'sign':
            sign = self.lex.cur_token[1]

            self.lex.next_token()

            left_tree = self.S()
            right_tree = self.SPrime()

            return ParsedTree('S', ParsedTree(sign), left_tree, right_tree)

        elif self.lex.cur_token[0] == 'number':
            number = self.lex.cur_token[1]
            self.lex.next_token()

            return ParsedTree('S', ParsedTree(number))

        # elif self.lex.cur_token[0] == 'end':
        # return ParsedTree('S')          # !!!

        else:
            raise BadTokenException(str(self.lex.cur_token))

    def SPrime(self):
        if self.lex.cur_token[0] in ['sign', 'number']:
            sub_tree = self.S()
            return ParsedTree("S'", sub_tree)
        else:
            raise BadTokenException(str(self.lex.cur_token))

    def parse(self, stream):
        self.lex = LexicalAnalyzer(stream)
        self.lex.next_token()
        return self.S()


class BadTokenException(Exception):
    pass


def string_to_result(s):
    f = io.StringIO(s)
    tree = Parser().parse(f)
    return tree.result()
