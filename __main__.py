import platform
import os
import sys
from zipfile import ZipFile
from .easy import *  # Подскажите как избавиться от Flake(F403), Flake(F401)


class StrStream:
    '''A brazenly stolen and slightly modified class
       that creates a string of task results to compare
       the latter with the correct new_name.'''
    def __init__(self):
        self.data = ''

    def write(self, s: str):
        self.data += s

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.stdout = sys.__stdout__


def file_transfer_script():
    '''Script function for transferring a file from
    the download folder.
    To work on your system,
    change the path to the directories.'''

    with open('zip_save.txt', 'a+', encoding='utf-8') as file:
        '''A context manager that overwrites data in
        zip_save.txt if necessary.'''
        file.seek(0)
        old_name = file.readline()
        if old_name:
            print(f'To continue working with file {old_name}, press Enter,')
            new_name = input("otherwise specify the file name without .zip: ")
        else:
            new_name = input("Enter the name of the file without .zip: ")
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
            with (zip_file.open(name, 'r') as input_file,
                  zip_file.open(f'{name}.clue', 'r') as answer_file):
                with StrStream() as x:
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
