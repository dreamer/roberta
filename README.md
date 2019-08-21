# Roberta

[![Luxtorpeda project Discord](https://img.shields.io/discord/514567252864008206.svg?label=discord)](https://discord.gg/8mFhUPX)

Steam Play compatibility tool to run adventure games using native Linux ScummVM

This is a sister project of
[Luxtorpeda](https://github.com/dreamer/luxtorpeda) and
[Boxtron](https://github.com/dreamer/boxtron).

Official mirrors:
[GitHub](https://github.com/dreamer/roberta),
[GitLab](https://gitlab.com/luxtorpeda/roberta).


## Prerequisites

You will need Python (>= 3.5), ScummVM (>= 2.0.0) and inotify-tools.

#### Fedora

    $ sudo dnf install scummvm inotify-tools

#### OpenSUSE

    $ sudo zypper install ??? inotify-tools

#### Debian, Ubuntu et consortes

    $ sudo apt install ??? inotify-tools

#### Arch, Manjaro

    $ sudo pacman -S ??? inotify-tools


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

TODO


## Development

TODO


## Known issues

TODO
