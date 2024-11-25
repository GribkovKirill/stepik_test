import shutil
import os
import sys
from zipfile import ZipFile
from easy import *  # Подскажите как избавиться от Flake(F403), Flake(F401)


class StrStream:
    '''A brazenly stolen and slightly modified class
       that creates a string of task results to compare
       the latter with the correct answer.'''
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
        old_zip_name = file.readline()
        print('The last one in the work was a zip archive with the name:',
              f'{old_zip_name}.')
        answer = input('Do you want to continue working with it? ')
        if not answer and file.readable():
            flag_new_zip_name = False
        else:
            flag_new_zip_name = True
            new_zip_name = answer + '.zip'
            file.truncate(0)
            file.write(new_zip_name)

    if flag_new_zip_name:
        file_source = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
        file_destination = os.getcwd()
        os.chdir(file_source)
        if os.path.exists(new_zip_name):
            os.chdir(file_destination)
            file_path = os.path.join(file_destination, old_zip_name)
            os.unlink(file_path)
            shutil.move(file_source + new_zip_name, file_destination)
        else:
            os.chdir(file_destination)
            if not os.path.exists(f'{new_zip_name}'):
                raise FileNotFoundError('You have not downloaded the file.')
        return new_zip_name
    else:
        return old_zip_name


def main():
    '''The body of the program performing the testing.'''

    zip_name = file_transfer_script()

    with ZipFile(f'{zip_name}') as zip_file:
        info = zip_file.namelist()
        info = filter(lambda name: name.isdigit(), info)
        for name in info:
            with (zip_file.open(f'{name}', 'r') as input_file,
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


main()
