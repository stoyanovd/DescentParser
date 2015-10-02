from helpers import Consts


class LexicalAnalyzer:
    def __init__(self, stream):
        self.stream = stream

        self.cur_pos = 0
        self.cur_char = ''
        self.cur_token = None

        self.next_char()

    def next_char(self):
        self.cur_pos += 1
        try:
            self.cur_char = self.stream.read(1)
        except IOError as e:
            raise ParseException('IOError ' + e + ' pos: ' + str(self.cur_pos))

    def next_token(self):
        while Consts.is_blank(self.cur_char):
            self.next_char()

        if self.cur_char in Consts.digits:
            number_digits = [self.cur_char]
            self.next_char()
            while self.cur_char in Consts.digits:
                number_digits.append(self.cur_char)
                self.next_char()
            self.cur_token = 'number', ''.join(number_digits)

        elif self.cur_char in Consts.operations.keys():
            self.cur_token = 'sign', self.cur_char
            self.next_char()

        elif not self.cur_char:
            self.cur_token = 'end',

        else:
            raise ParseException(
                "Illegal character at " + str(self.cur_pos))


class ParseException(Exception):
    pass