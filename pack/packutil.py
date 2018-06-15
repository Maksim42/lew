import inspect
import os.path

def CurentPath():
    """Return real curent path for executed file"""
    return os.path.abspath(inspect.getsourcefile(lambda:0))