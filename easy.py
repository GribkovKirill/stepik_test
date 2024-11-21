class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, num: int):
        self.numbers.append(num)

    def get_even(self):
        evens = filter(lambda n: not n % 2, self.numbers)
        return list(evens)

    def get_odd(self):
        odds = filter(lambda n: n % 2, self.numbers)
        return list(odds)
