# author: Smawe
# Home-page: https://github.com/Smawexi/SmawePyppeteer
from pathlib import Path
from .utils import *

_root = Path(__file__)
__path__ = [str(_root.parent), str(_root.parent.joinpath("utils"))]
__package__ = __name__
