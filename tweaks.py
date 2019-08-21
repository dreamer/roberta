#!/usr/bin/python3

"""
Game-specific tweaks and workarounds

"""

TWEAKS_DB = {
}  # yapf: disable


def download_tweak_needed(app_id):
    """Return true if game needs to be download something for installation."""
    return app_id in TWEAKS_DB and 'download' in TWEAKS_DB[app_id]
