# Roberta

[![Build Status](https://travis-ci.com/dreamer/roberta.svg?branch=master)](https://travis-ci.com/dreamer/roberta)
[![Luxtorpeda project Discord](https://img.shields.io/discord/514567252864008206.svg?label=discord)](https://discord.gg/8mFhUPX)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/dreamer)

Steam Play compatibility tool to run adventure games using native Linux
[ScummVM](https://www.scummvm.org/)

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

    $ sudo zypper install scummvm inotify-tools

#### Debian, Ubuntu et consortes

    $ sudo apt install scummvm inotify-tools

#### Arch, Manjaro

    $ sudo pacman -S scummvm inotify-tools


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

- Switching game language in Steam is not supported yet.
- Some games hang after triggering Steam overlay.
