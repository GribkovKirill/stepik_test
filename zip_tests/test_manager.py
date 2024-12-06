from . import streams


class TestManager:
    def __init__(self, i_file, ans_file, name: str) -> None:
        self.i_file = i_file
        self.ans_file = ans_file
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.i_file.close()
        self.ans_file.close()
        return False

    @property
    def input_data(self):
        with streams.CodeStream() as x:
            exec(self.i_file.read().decode('utf-8'))
        return x.data

    @property
    def answer_data(self):
        return self.ans_file.read().decode('utf-8') + '\n'

    def compare(self):
        if self.input_data != self.answer_data:
            raise ValueError(
                f'wrong answer in test №{self.name}'
                f'your answer:\n{self.input_data}'
                f'correct answer:\n{self.answer_data}'
            )
        else:
            print(f'№{self.name} - OK!')
