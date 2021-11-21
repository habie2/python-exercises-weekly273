class RightTriangle:
    def __init__(self, base: int, height: int, answer: str):
        self.base = base
        self.height = height
        while answer != 'a' and answer != 'p':
            answer: str = input('area or perimmeter? (a/p)')
        self.answer = answer

        if base > 0:
            self.base = base
        else:
            self.base = 1

        if height > 0:
            self.height = height
        else:
            self.height = 1

    def __str__(self):
        if self.answer == 'a':
            return str((self.base * self.height / 2)) + ' u\N{SUPERSCRIPT TWO}'
        else:
            return str((self.base + self.height + ((self.base ** 2 + self.height ** 2) ** 1/2))) + ' u'