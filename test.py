import shutil
import os
import sys
from zipfile import ZipFile
from easy import *  # Подскажите как избавиться от Flake(F403), Flake(F401)


class ListStream:
    '''A brazenly stolen and slightly modified class
       that creates a list of task results to compare
       the latter with the correct answer.'''
    def __init__(self):
        self.data = []

    def write(self, s: str):
        if s != '\n':
            self.data.append(s)

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        sys.stdout = sys.__stdout__


def main():
    '''The body of the program performing the testing.'''

    def file_transfer_script():
        '''Script function for transferring a file from
        the download folder to the testing folder.
        To work on your system, change the path to the directories.
        In the 2nd version, the user's autofill appeared and the
        creation of the tests folder in its absence'''

        username = os.getlogin()
        file_source = f'C:\\Users\\{username}\\Downloads\\'
        file_destination = os.getcwd()
        if not os.path.exists('tests'):
            os.mkdir('tests')
        os.chdir(file_source)
        print('Обрати внимание на скачивание файла. '
              'Названия файлов могут повторяться.')
        zip_name = f'{input("Введите название файла без .zip: ")}.zip'
        if os.path.exists(zip_name):
            os.chdir(file_destination + '')
            if os.path.exists(f'tests/{zip_name}'):
                os.remove(os.path.join('tests', zip_name))
            shutil.move(file_source + zip_name, file_destination + '\\tests\\')
        else:
            os.chdir(file_destination)
            if not os.path.exists(f'tests/{zip_name}'):
                raise FileNotFoundError('Искомый файл отсутствует')
        return zip_name

    zip_name = file_transfer_script()

    with ZipFile(f'tests/{zip_name}') as zip_file:
        info = zip_file.namelist()
        info = filter(lambda name: name.isdigit(), info)
        for name in info:
            with (zip_file.open(f'{name}', 'r') as input_file,
                  zip_file.open(f'{name}.clue', 'r') as answer_file):
                with ListStream() as x:
                    exec(input_file.read().decode('utf-8'))
                input_data = x.data
                answer_data = answer_file.read().decode('utf-8').split('\n')
                if input_data != answer_data:
                    print(f'wrong answer in test №{name}')
                    print(f'my answer:\n{input_data}')
                    print(f'correct answer:\n{answer_data}')
                    break
                print(f'№{name} - OK!')
        else:
            print('KRASAVA!!!!')


main()
