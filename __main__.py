import platform
import os
from sys import argv
from zipfile import ZipFile
from .zip_tests import streams


with open(
    f'{argv[0].split(chr(92))[-2]}/easy.py', 'r', encoding='utf-8'
) as file:
    exec(file.read())


def file_transfer_script():
    '''...'''

    with open('zip_save.txt', mode="a+", encoding='utf-8') as file:
        '''A context manager that overwrites data in
        zip_save.txt if necessary.'''
        file.seek(0)
        old_name = file.readline()
        if old_name:
            print(f'To continue working with file {old_name}, '
                  'press Enter, or,')
        new_name = input("Specify the name of the file without .zip: ")

        if not old_name and not new_name:
            raise FileNotFoundError('The file is not specified.')
        elif old_name and not new_name:
            flag_new_name = False
        else:
            flag_new_name = True
            new_name += '.zip'
            file.truncate(0)
            file.write(new_name)

    match platform.system():
        case 'Windows':
            file_source = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
        case 'Darwin':
            pass
        case 'Linux':
            pass

    os.chdir(file_source)
    if flag_new_name:
        if (
            os.path.exists(new_name) and
            os.path.exists(old_name) and
            new_name != old_name
        ):
            file_path = os.path.join(file_source, old_name)
            os.unlink(file_path)
        else:
            if not os.path.exists(new_name):
                raise FileNotFoundError(
                    'You have not downloaded the file.'
                    )
        return new_name
    else:
        return old_name


def main():
    '''The body of the program performing the testing.'''

    zip_name = file_transfer_script()

    with ZipFile(zip_name) as zip_file:
        info = zip_file.namelist()
        info = filter(lambda name: name.isdigit(), info)
        for name in info:
            with (zip_file.open(name, 'r', encoding='utf-8') as input_file,
                  zip_file.open(
                      f'{name}.clue', 'r', encoding='utf-8'
                  ) as answer_file):
                with streams.CodeStream() as x:
                    exec(input_file.read())
                input_data = x.data
                answer_data = answer_file.read() + '\n'
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
