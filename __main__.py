import shutil
import platform
import os
import sys
from zipfile import ZipFile
from easy import *  # Подскажите как избавиться от Flake(F403), Flake(F401)


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

        file_destination = os.path.join(os.getcwd(), 'stepik')
        if flag_new_name:
            system_name = platform.system()
            match system_name:
                case 'Windows':
                    file_source = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
                case 'Darwin':
                    pass
                case 'Linux':
                    pass
            os.chdir(file_source)
            if os.path.exists(new_name):
                os.chdir(file_destination)
                if os.path.exists(old_name):
                    file_path = os.path.join(file_destination, old_name)
                    os.unlink(file_path)
                shutil.move(file_source + new_name, file_destination)
            else:
                os.chdir(file_destination)
                if not os.path.exists(f'{new_name}'):
                    raise FileNotFoundError(
                        'You have not downloaded the file.'
                        )
            return new_name
        else:
            os.chdir(file_destination)
            return old_name


def main():
    '''The body of the program performing the testing.'''

    zip_name = file_transfer_script()

    with ZipFile(f'{zip_name}') as zip_file:
        info = zip_file.namelist()
        info = filter(lambda name: name.isdigit(), info)
        for name in info:
            with (zip_file.open(f'{name}', 'r') as input_file,
                  zip_file.open(f'{name}.clue', 'r') as new_name_file):
                with StrStream() as x:
                    exec(input_file.read().decode('utf-8'))
                input_data = x.data
                new_name_data = new_name_file.read().decode('utf-8') + '\n'
                if input_data != new_name_data:
                    print(f'wrong new_name in test №{name}')
                    print(f'your new_name:\n{input_data}')
                    print(f'correct new_name:\n{new_name_data}')
                    break
                print(f'№{name} - OK!')
        else:
            print('SOLVED!!!!')


if __name__ == '__main__':
    main()
