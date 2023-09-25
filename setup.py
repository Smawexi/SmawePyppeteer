from setuptools import setup, find_packages
from smawe_pyppeteer.__version__ import version


AUTHOR = "Smawe"
EMAIL = "1281722462@qq.com"
URL = "https://github.com/Smawexi/SmawePyppeteer"
NAME = "smawe_pyppeteer"
DESCRIPTION = "一个使用pyppeteer进行渲染的请求库"
with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()
REQUIRES_PYTHON = '>=3.6.0'
REQUIRED = ["pyppeteer"]

setup(
    name=NAME,
    version=version,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=REQUIRED,
    packages=find_packages(where="."),
    include_package_data=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)

