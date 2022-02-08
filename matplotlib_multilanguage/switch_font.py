"""
This module provides auto font selection for variable locales
to avoid display mistaken.
"""

from locale import getdefaultlocale
from os.path import join, split, realpath, exists
from os import environ, system
from platform import system as get_system_type
from sys import exit

from matplotlib import rcParams, get_data_path
from matplotlib.font_manager import fontManager

from matplotlib_multilanguage.exceptions import FontNotFoundError, LocaleNotSupported

from .read_map import read_map

locale_font = read_map()


def _match_font_name(lc):
    """
    Find the first font in locale_font[lc][0] that appears in
    matplotlib.font_manager.fontManager.ttflist

    Parameters
    ----------
    lc : str
        locale

    Returns
    -------
    (int, str)
        returns the index and the font name of the font.
        If no fonts were found, return (None, None)
    """
    available_font_names = [f.name for f in fontManager.ttflist]
    expected_fonts = locale_font[lc]["font-names"]
    for i, f in enumerate(expected_fonts):
        if f in available_font_names:
            return i, f
    else:
        return None, None


def _get_ttf_dir():
    """Get the directory that stores the font files used by matplotlib"""
    return join(get_data_path(), "fonts", "ttf")


def _remove_cache():
    """Remove the caches of matplotlib so that it'll scan fonts again"""
    system_type = get_system_type()
    home = environ["HOME"]
    if system_type == "Windows":
        system(f'rmdir /s "{join(home, ".matplotlib")}"')
    elif system_type == "Darwin":
        system(f'rm -rf "{join(home, ".matplotlib")}"')
    else:
        system(f'rm -rf "{join(home, ".cache", "matplotlib")}"')


def install_font(lc):
    """
    Install default font to <data_path>/fonts/ttf
    so that matplotlib will discover it
    """
    filename = locale_font[lc]["font-filenames"][0]
    src_path = join(split(realpath(__file__))[0], "fonts", filename)
    if not exists(src_path):
        raise FontNotFoundError(filename)
    des_path = _get_ttf_dir()
    system(f'cp "{src_path}" "{des_path}"')
    _remove_cache()
    print(
        f"Font {filename} has been installed. Now restart your program and the new font is effective."
    )
    exit(0)


def set_font(lc=getdefaultlocale()[0]):
    """
    Set rc parameter "font.family" as the best font,
    where "best" means it has the minimum index among those 
    available on this computer.
    """
    if lc in locale_font.keys():
        i1, f1 = _match_font_name(lc)
        if i1 is not None:
            rcParams["font.family"] = f1
        else:
            install_font(lc)
    else:
        raise LocaleNotSupported(lc)
