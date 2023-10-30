import importlib.util
import importlib.abc
import logging
import pkgutil
from pathlib import Path
import sys
import inspect
import builtins
import warnings
from typing import Union, Dict, Iterable, Coroutine
warnings.filterwarnings("ignore", category=SyntaxWarning)

try:
    delattr(builtins, "copyright")
    delattr(builtins, "license")
    delattr(builtins, "credits")
except AttributeError:
    pass

parent = Path(__file__).resolve().parent
__path__ = [str(parent)]
extend_path = []
__package__ = __name__


def is_finder_class(finder):
    if inspect.isclass(finder) and not finder.__name__.startswith("_") and issubclass(
            finder, (importlib.abc.Finder, importlib.abc.MetaPathFinder, importlib.abc.PathEntryFinder)
    ) and getattr(finder, "__is_custom__", None):
        return True

    return False


for finder, name, is_pkg in pkgutil.iter_modules(__path__):
    spec = finder.find_spec(name)
    if not spec:
        continue
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    members = inspect.getmembers(module, is_finder_class)
    for n, v in members:
        extend_path.append(v())


def import_module(name):
    """导入一个模块, 优先导入utils包中的子模块, 如未找到, 则按正常的模块导入机制进行查找 导入模块"""
    for _finder in extend_path + sys.meta_path:
        _spec = _finder.find_spec(name, __path__)
        if not _spec:
            continue
        _module = importlib.util.module_from_spec(_spec)
        _module_name = get_module_qualified_name(_module)
        sys.modules[_module_name] = _module
        _spec.loader.exec_module(_module)
        return _module


def get_module_qualified_name(module_obj):
    path = Path(module_obj.__file__).resolve()
    parts = []

    for parent in path.parents:
        init_file = parent / "__init__.py"
        if init_file.is_file():
            parts.insert(0, parent.name)
        else:
            break

    parts.append(path.stem)

    return ".".join(parts)


# pretend: smawe_pyppeteer.utils.pretend module
pretend = import_module("pretend")
# smawe_pyppeteer: smawe_pyppeteer.utils.smawe_pyppeteer module
smawe_pyppeteer = import_module("smawe_pyppeteer")

"""
declare PyppeteerRequest PyppeteerResponse logger get run
"""
logger: logging.Logger = None


class PyppeteerResponse:

    @property
    def text(self):
        """
        获取页面的完整HTML内容。
        :return: str
        """
        pass

    @property
    def cookies(self):
        """
        返回当前页面URL的cookie
        :return: list[dict]
        """
        pass

    @property
    def headers(self):
        """
        返回响应headers
        :return:
        """
        pass

    @property
    def status(self):
        """
        返回响应状态码
        :return:
        """
        pass

    @property
    def request(self):
        """
        返回响应对应的请求对象
        :return:
        """
        pass

    @property
    def script_result(self):
        """
        返回js脚本的执行结果, 未提供script, 默认返回None
        :return:
        """
        pass


class PyppeteerRequest:
    """使用pyppeteer对指定网站进行渲染"""

    def __init__(self, **kwargs):
        pass

    async def init(self):
        """执行初始化"""
        pass

    async def request(
            self, url, ua=None, callable=None, cookies: Union[Dict, Iterable[Dict]] = None, **kwargs
    ) -> PyppeteerResponse:
        """访问url, 返回PyppeteerResponse对象"""
        pass

    @staticmethod
    async def handle_request(request):
        """实现处理请求拦截"""
        pass

    @staticmethod
    def check(iterable: Iterable[Dict]):
        """检查iterable是否是一个包含dict的可迭代对象(不包括迭代器)"""
        pass

    def enabled_interception(self, value):
        """是否启动请求拦截"""
        pass

    async def close(self, page):
        """执行关闭操作"""
        pass


class PyppeteerFinder(importlib.abc.MetaPathFinder):
    """模块查找器"""
    pass


class PyppeteerLoader(importlib.abc.Loader):
    """模块加载器"""
    pass


async def get(
    url, delay=None, wait_for=None, page_width=None, page_height=None,
    enabled_interception=None, script=None, callable=None, cookies=None, **kwargs
) -> PyppeteerResponse:
    """
    使用pyppeteer对指定url进行渲染
    :param url: url
    :param wait_for: css选择器或者xpath, 等待指定的元素出现在页面上
    :param delay: 打开指定url后要等待的秒数, 默认为None不进行等待(同时指定了delay和wait_for,则先delay,然后再wait_for)
    :param page_width: 页面宽度
    :param page_height: 页面高度
    :param enabled_interception: 是否启用请求拦截
    :param callable: 启动了请求拦截后要调用的协程函数, 它接受单个request参数, 未提供则使用默认实现.
    :param script: js表达式/js函数, 脚本在最后才执行, 即page关闭前执行. 结果可通过PyppeteerResponse.script_result属性获取.
    :param cookies: 一个字典或者包含字典的可迭代对象, 在当前打开的page中设置cookie(在访问页面之前设置), e.g. {"name": "n1", "value": "v1"}
    :param kwargs:
        headless(bool): 是否启动无头模式, 默认是True.(启用了此参数(参数被设置为True时), auto_close被强制设为True)
        path(str): 要运行的 Chromium 或 Chrome 可执行文件的路径.
        auto_close(bool): 脚本完成后自动关闭浏览器进程. 默认为 True.
        window_width(str): 浏览器窗口宽度, 以像素为单位.注意window_width和window_height必须同时设置, 否则会不生效
        window_height(str): 浏览器窗口高度, 以像素为单位.注意window_width和window_height必须同时设置, 否则会不生效
        args(list[str]): 传递给浏览器进程的附加参数.
        enabled_maximize(bool): 是否启用窗口最大化, 默认为True, 如果同时指定了注意window_width和window_height, 此参数不会生效
    :return: PyppeteerResponse
    """
    pass


def run(f: Coroutine):
    """run future, return future result"""
    pass


# import "PyppeteerRequest", "PyppeteerResponse", "get", "run", "PyppeteerFinder", "PyppeteerLoader", "logger"
for n in smawe_pyppeteer.__all__:
    globals()[n] = getattr(smawe_pyppeteer, n)

__all__ = [
    "PyppeteerRequest", "PyppeteerResponse", "get", "run", "PyppeteerFinder", "PyppeteerLoader", "logger",
    "pretend", "smawe_pyppeteer"
]
