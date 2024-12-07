import sys


class CodeStream:
    '''A brazenly stolen and slightly modified class
       that creates a string of task results to compare
       the latter with the correct new_name.'''
    def __init__(self):
        self.data = ''

    def write(self, string: str):
        self.data += string

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.stdout = sys.__stdout__


class InputStream:
    pass


class TestStream:
    def __init__(self, i_file, rans_file, name: str) -> None:
        self.i_file = i_file
        self.rans_file = rans_file
        self.name = name
        self.your_answer = ''

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.i_file.close()
        self.rans_file.close()
        return False

    @property
    def input_code(self):
        return self.i_file.read().decode('utf-8')

    @property
    def right_answer(self):
        return self.rans_file.read().decode('utf-8') + '\n'

    def compare(self, your_answer):
        if your_answer != self.right_answer:
            raise ValueError(
                f'wrong answer in test №{self.name}\n'
                f'your answer:\n{your_answer}\n'
                f'correct answer:\n{self.right_answer}\n'
            )
        else:
            print(f'№{self.name} - OK!')
