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
    To work on your system, change the path to the directories.'''

    file_source = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
    file_destination = os.getcwd()
    os.chdir(file_source)
    print('Pay attention to the file download.. '
          'File names may be repeated.')
    zip_name = f'{input("Enter the name of the file without .zip: ")}.zip'
    if os.path.exists(zip_name):
        os.chdir(file_destination)

        for filename in os.listdir(file_destination):
            '''The cycle of deleting unnecessary archives.'''
            if filename.endswith('.zip'):
                file_path = os.path.join(file_destination, filename)
                os.unlink(file_path)

        shutil.move(file_source + zip_name, file_destination)
    else:
        os.chdir(file_destination)
        if not os.path.exists(f'{zip_name}'):
            raise FileNotFoundError('You have not downloaded the file.')
    return zip_name


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
