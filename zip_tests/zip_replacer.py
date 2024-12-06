import os
from . import zip_saver


def get_name() -> str:
    '''...'''

    with zip_saver.Saver() as save:
        old_name = save.old_name
        new_name = save.zip_name
        flag_new_name = save.flag
        file_source = save.file_source

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
