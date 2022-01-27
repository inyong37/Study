class Test:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def calculate(self):
        self.score = self.score + 1

    def print_score(self):
        print(self.name, self.score)

    def print_name(self):
        print(self.name)

    def print_score_name(self):
        print(self.score, self.name)
