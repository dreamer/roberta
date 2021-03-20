# Roberta

[![Build Status](https://travis-ci.com/dreamer/roberta.svg?branch=master)](https://travis-ci.com/dreamer/roberta)
[![Luxtorpeda project Discord](https://img.shields.io/discord/514567252864008206.svg?label=discord)](https://discord.gg/8mFhUPX)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/dreamer)

Steam Play compatibility tool to run adventure games using native Linux
[ScummVM](https://www.scummvm.org/)

This is a sister project of
[Luxtorpeda](https://github.com/dreamer/luxtorpeda) and
[Boxtron](https://github.com/dreamer/boxtron).

![roberta](https://user-images.githubusercontent.com/3967/63626407-3f41f700-c603-11e9-8aff-22c6ab308390.png)

Official mirrors:
[GitHub](https://github.com/dreamer/roberta),
[GitLab](https://gitlab.com/luxtorpeda/roberta).


## Prerequisites

You will need Python (>= 3.5), ScummVM (>= 2.0.0) and inotify-tools.

#### Fedora

    $ sudo dnf install scummvm inotify-tools

#### OpenSUSE

    $ sudo zypper install scummvm inotify-tools

#### Debian, Ubuntu et consortes

    $ sudo apt install scummvm inotify-tools

#### Arch, Manjaro

    $ sudo pacman -S scummvm inotify-tools


## Installation (using tarball)

1. Close Steam.
2. Download and unpack tarball to `compatibilitytools.d` directory (create one if it does not exist):

       $ cd ~/.local/share/Steam/compatibilitytools.d/ || cd ~/.steam/root/compatibilitytools.d/
       $ curl -L https://github.com/dreamer/roberta/releases/download/v0.1.0/roberta.tar.xz | tar xJf -

3. Start Steam.
4. In game properties window select "Force the use of a specific Steam Play
   compatibility tool" and select "Roberta (native ScummVM)".


## Installation (from source)

1. Close Steam.
2. Clone the repository and install the script to user directory:

       $ git clone https://github.com/dreamer/roberta.git
       $ cd roberta
       $ make user-install

3. Start Steam.
4. In game properties window select "Force the use of a specific Steam Play
   compatibility tool" and select "Roberta (dev)".


## Configuration

Settings for Roberta can be found in `~/.config/roberta.conf` (or wherever
[`XDG_CONFIG_HOME`](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
points to).

Additionally, per-game settings can be changed through variables set in the
Steam client.  For example, to force game to use your **secondary** screen,
right-click your game in Steam Library, select
*Properties&nbsp;&nbsp;General&nbsp;→&nbsp;Launch&nbsp;Options*
and set: `LUX_USE_SCREEN=1 %command%`.

You can use `LUX_SCUMMVM_GAME=<game-identifier>` to bypass the ScummVM
launcher menu, and start the game right away, but it will hide important
ScummVM launcher options.  To open launcher menu press **Ctrl+F5** and
select **Return to Launcher**.  The *game-identifier* value is one of
section names in `roberta_scummvm.ini` file in the game installation directory.

| Name               | Values  | Description
|:---                |:---     |:---
| `LUX_SCUMMVM_GAME` | string  | Set to the game identifier to run the specific game in a collection, bypassing the ScummVM launcher menu.
| `LUX_SCUMMVM_CMD`  | command | Use this command to run the game. Overrides value in `scummvm.cmd` setting.
| `LUX_USE_SCREEN`   | number  | Set to the number of the screen, that you want the game to use. Overrides `scummvm.fullscreenmode` setting.


## Development

Read all about it in the
[contributing guide](https://github.com/dreamer/roberta/blob/master/CONTRIBUTING.md) :)


## Known issues

- Some games hang after triggering Steam overlay in ScummVM 2.0.
- As of August 2019, Arch AUR package for ScummVM does not work correctly.
