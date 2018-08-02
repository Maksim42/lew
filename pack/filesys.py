"""Provide file system operation"""
from os import path
from os import listdir
from os import remove

from . import consui as ui

def find_and_delete(file_name):
    """If file exist then request remove him\n
    Return True if conflict resolve
    """
    if exist(file_name):
        mes = 'Replace {} ?'.format(file_name)
        if not ui.confirm(mes):
            return False
        remove(file_name)
    return True

def open_file_dialogue(dir_name="./"):
    """Console open file dialogue"""
    files = [f for f in listdir(dir_name) if path.isfile(path.join(dir_name, f))]

    menu = ui.MenuList(name="bd file")
    result = None
    def create_delegate(name):
        def set_result(file_name):
            nonlocal result
            result = file_name
        return lambda: set_result(name)
    for name in files:
        menu.add_option(name, create_delegate(name))

    menu.show()
    return path.join(dir_name, result)


def exist(file_name):
    """Check file existing by path
    Return True if file exist
    """
    if path.exists(file_name) and path.isfile(file_name):
        return True
    return False
