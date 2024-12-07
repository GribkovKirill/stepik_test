import os
from . import test_saver


def get_paths() -> tuple[str]:
    '''...'''

    with test_saver.Saver() as save:
        name = save.old_name
        new_name = save.zip_name
        flag_new_name = save.flag
        file_source = save.file_source
        dir_path = save.dir_path

    os.chdir(file_source)
    if flag_new_name:
        if (
            os.path.exists(new_name) and
            os.path.exists(name) and
            new_name != name
        ):
            os.unlink(os.path.join(file_source, name))
        else:
            if not os.path.exists(new_name):
                raise FileNotFoundError(
                    'You have not downloaded the file.'
                    )
        name = new_name
    os.chdir(dir_path)
    return os.path.join(file_source, name)
