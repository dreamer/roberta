#!/usr/bin/python3

# pylint: disable=missing-docstring

"""
Settings file creation and handling.
"""

import configparser
import os
import shlex

import xdg
import xlib

from log import log, log_err

SETTINGS_FILE = os.path.join(xdg.CONF_HOME, 'roberta.conf')

DEFAULT_CONFGEN_FORCE = False

DEFAULT_SCUMMVM_CMD = 'scummvm'

DEFAULT_FULLSCREEN_MODE = 'screen 0'

DEFAULT_SETTINGS = """
[confgen]
# Set this value to 'true' if you want Roberta to re-create ScummVM
# configuration on every run.
force = {confgen_force}

[scummvm]
# Available modes:
# - screen 0, screen 1, etc:
#   The game will use fullscreen on selected screen, without changing
#   the native resolution of your display.  Mouse will be locked to the screen.
#   Default is 'screen 0', which is your primary display.
#   You can override this selection per-game with LUX_USE_SCREEN environment
#   variable, e.g: 'LUX_USE_SCREEN=2 %command%'
# - default:
#   Roberta will not attempt to affect the default ScummVM behaviour.
#   ScummVM uses windowed mode by default; it can be changed in ScummVM
#   options per-game.
fullscreenmode = {fullscreen_mode}

# Uncomment following line to specify a different ScummVM command:
{cmd_example}
"""


class Settings():

    def __init__(self, conf=None):
        self.store = configparser.ConfigParser(interpolation=None)
        self.store.add_section('confgen')
        self.store.add_section('scummvm')
        self.store.read(conf or SETTINGS_FILE)
        self.fullresolution = None
        self.finalized = False
        self.distdir = os.path.dirname(os.path.abspath(__file__))

    def setup(self):
        """Finalize settings initialization on request.

        Some settings need more involved initialization/detection procedure,
        which might fail or leave extensive logs on stderr.  We want this
        part of settings initialization only when actually needed.
        """
        self.__setup_fullscreen__()
        self.finalized = True

    def __setup_fullscreen__(self):
        user_choice = self.get_scummvm_fullscreenmode()

        env_override = 'LUX_USE_SCREEN' in os.environ or \
                       'SDL_VIDEO_FULLSCREEN_DISPLAY' in os.environ or \
                       'SDL_VIDEO_FULLSCREEN_HEAD' in os.environ

        if user_choice == 'default' and not env_override:
            return

        screen = self.__get_screen_number__()
        all_screens = xlib.query_screens()

        if all_screens == {}:
            log_err('no screens detected')
        for number, info in all_screens.items():
            log("screen '{}': {}x{}".format(number, info.width, info.height))

        if screen not in all_screens:
            log("screen '{}' not found".format(screen))
            if '0' in all_screens:
                screen = '0'
                log("using '" + screen + "' instead")
            else:
                log("using ScummVM default fullscreen mode")
                return

        log("selected screen '{}'".format(screen))
        os.putenv('SDL_VIDEO_FULLSCREEN_DISPLAY', screen)  # SDL >= 1.2.14
        os.putenv('SDL_VIDEO_FULLSCREEN_HEAD', screen)  # SDL >= 1.2.10
        info = all_screens[screen]
        self.fullresolution = (info.width, info.height)

    def __get_screen_number__(self):
        tokens = self.get_scummvm_fullscreenmode().split()
        screen = '0'
        if tokens == [] or tokens[0] != 'screen':
            log_err('unknown option value:', tokens[0])
        if len(tokens) >= 2 and tokens[0] == 'screen':
            screen = tokens[1]
        screen = os.environ.get('SDL_VIDEO_FULLSCREEN_HEAD', screen)
        screen = os.environ.get('SDL_VIDEO_FULLSCREEN_DISPLAY', screen)
        screen = os.environ.get('LUX_USE_SCREEN', screen)
        return screen

    def get_bool(self, section, val, default):
        return self.store.getboolean(section, val, fallback=default)

    def get_str(self, section, val, default):
        return self.store.get(section, val, fallback=default)

    def get_confgen_force(self):
        return self.get_bool('confgen', 'force', DEFAULT_CONFGEN_FORCE)

    def get_scummvm_cmd(self):
        scummvm_cmd = self.get_str('scummvm', 'cmd', DEFAULT_SCUMMVM_CMD)
        cmd = os.environ.get('LUX_SCUMMVM_CMD', scummvm_cmd)
        try:
            split = shlex.split(cmd, comments=True)
            return [os.path.expanduser(s) for s in split]
        except ValueError as err:
            log_err('invalid scummvm.cmd value:', err)
            return [DEFAULT_SCUMMVM_CMD]

    def set_scummvm_cmd(self, value):
        self.store.set('scummvm', 'cmd', value)

    def get_scummvm_fullscreenmode(self):
        return self.get_str('scummvm', 'fullscreenmode',
                            DEFAULT_FULLSCREEN_MODE)

    def get_scummvm_fullresolution(self):
        assert self.finalized
        return self.fullresolution


def init_settings_file():
    os.makedirs(xdg.CONF_HOME, exist_ok=True)
    new_file_exists = os.path.isfile(SETTINGS_FILE)
    if not new_file_exists:
        content = DEFAULT_SETTINGS.format(
            confgen_force=str(DEFAULT_CONFGEN_FORCE).lower(),
            fullscreen_mode=DEFAULT_FULLSCREEN_MODE,
            cmd_example='# cmd = ~/projects/scummvm/scummvm')
        with open(SETTINGS_FILE, 'w') as file:
            file.write(content.lstrip())


init_settings_file()

SETTINGS = Settings()
