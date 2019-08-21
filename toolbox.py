#!/usr/bin/python3

"""
Useful functions and classes
"""

import os
import pathlib


def enabled_in_env(var, fallback_var=None):
    """Returns True for environment variables with non-zero value."""
    val1 = os.environ.get(var)
    val2 = os.environ.get(fallback_var) if fallback_var else None
    return (val1 and val1 != '0') or (val2 and val2 != '0')


def guess_game_install_dir(directory=None):
    """Return absolute path pointing to game installation directory.

    Path will be escaped in a way, that allows it to be injected into
    quoted shell commands.

    This function assumes current working directory is a subdirectory
    of an installation directory.
    """
    path = directory or os.getcwd()
    posix_path = pathlib.PurePosixPath(path)
    assert posix_path.is_absolute()
    posix_parts = posix_path.parts
    steam_lib_pattern = ('steamapps'.casefold(), 'common'.casefold())
    share_games_pattern = ('share', 'games')
    lib_pattern_found, pos = False, -1
    prev_part_2, prev_part_1, this_part = '', '', ''
    for i, part in enumerate(posix_parts):
        prev_part_2 = prev_part_1
        prev_part_1 = this_part
        this_part = part.casefold()
        if steam_lib_pattern == (prev_part_2, prev_part_1) or \
           share_games_pattern == (prev_part_2, prev_part_1):
            lib_pattern_found = True
            pos = i
            break
    if not lib_pattern_found:
        return None
    found_path = os.path.join(*posix_parts[:pos + 1])
    return found_path.replace(' ', r'\ ').replace('&', r'\&')


class PidFile:
    """Helper class to create and remove PID file"""

    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        with open(self.file_name, 'w') as pid_file:
            pid_file.write(str(os.getpid()))
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            os.remove(self.file_name)
        except FileNotFoundError:
            pass
