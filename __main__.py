from zipfile import ZipFile
from .zip_tests import zip_saver
from .zip_tests import streams
from .zip_tests import zip_replacer


def main():
    '''The body of the program performing the testing.'''
    with open(
            f'{zip_saver.Saver.pack_name}/easy.py', 'r', encoding='utf-8'
    ) as file:
        exec(file.read())
    zip_name = zip_replacer.get_name()
    with ZipFile(zip_name) as zip_file:
        info = zip_file.namelist()
        info = filter(lambda name: name.isdigit(), info)
        for name in info:
            with (zip_file.open(name, 'r') as input_file,
                  zip_file.open(f'{name}.clue', 'r') as answer_file):
                with streams.CodeStream() as x:
                    exec(input_file.read().decode('utf-8'))
                input_data = x.data
                answer_data = answer_file.read().decode('utf-8') + '\n'
                if input_data != answer_data:
                    print(f'wrong answer in test №{name}')
                    print(f'your answer:\n{input_data}')
                    print(f'correct answer:\n{answer_data}')
                    break
                print(f'№{name} - OK!')
        else:
            print('SOLVED!!!!')


if __name__ == '__main__':
    main()
