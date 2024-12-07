from sys import argv
from zipfile import ZipFile
from .zip_tests import streams
from .zip_tests import zip_replacer as zr


with open(
    f'{argv[0].split(chr(92))[-2]}/easy.py', 'r', encoding='utf-8'
) as file:
    exec(file.read())


def prog(zf, file_name: str) -> None:
    with streams.TestStream(
            zf.open(file_name, 'r'),
            zf.open(f'{file_name}.clue', 'r'), file_name
    ) as ts:
        with streams.CodeStream() as cs:
            exec(ts.input_code)
        ts.compare(cs.data)


def main():
    '''The body of the program performing the testing.'''
    zip_file = zr.get_paths()
    with (ZipFile(zip_file) as zf):
        for name in filter(lambda name: name.isdigit(), zf.namelist()):
            prog(zf, name)
        else:
            print('SOLVED!!!!')


if __name__ == '__main__':
    main()
