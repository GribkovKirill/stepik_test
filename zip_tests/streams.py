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
