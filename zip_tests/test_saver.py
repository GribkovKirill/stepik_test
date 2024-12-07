import os
import platform
import shelve
from sys import argv
from pathlib import Path


class Saver:
    def __init__(self):
        _path = os.path.join(os.getcwd(), argv[0].split(chr(92))[-2])
        if not os.path.exists(os.path.join(_path, 'save')):
            os.mkdir(os.path.join(_path, 'save'))
        self.sh_file = shelve.open(
            os.path.join(_path, 'save', 'zip_save'), 'c'
        )

    def __enter__(self):
        self.old_name = self.zip_name
        if self.old_name:
            print(f'To continue working with file {self.old_name}, '
                  'press Enter, or,')
            self.new_name = \
                input("specify the name of the file without .zip: ")
        else:
            self.new_name = \
                input("Specify the name of the file without .zip: ")
        if not self.zip_name and not self.new_name:
            raise FileNotFoundError('The file is not specified.')
        elif self.zip_name and not self.new_name:
            self.flag = False
        else:
            self.flag = True
            self.new_name += '.zip'
            self.sh_file['zip_name'] = self.new_name
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sh_file.close()
        return False

    @property
    def zip_name(self) -> str:
        return self.sh_file.get('zip_name', '')

    @property
    def dir_path(self):
        self.sh_file['dir_path'] = os.getcwd()
        return self.sh_file['dir_path']

    @property
    def module_name(self):
        self.sh_file['module_name'] = argv[0].split(chr(92))[-2]
        return self.sh_file['module_name']

    @property
    def file_source(self):
        match platform.system():
            case 'Windows':
                self.sh_file['file_source'] = \
                    os.path.join(Path.home(), 'Downloads')
            case 'Darwin':
                self.sh_file['file_source'] = \
                    os.path.join(Path.home(), '')
            case 'Linux':
                self.sh_file['file_source'] = \
                    os.path.join(Path.home(), '')
        return self.sh_file['file_source']
