from setuptools import find_packages, setup
import re
from os.path import join


def get_version():
    with open(join('src', 'playground', '__init__.py'), 'r') as f:
        content = f.read()
    p = re.compile(r'^__version__ = [\'"]([^\'\"]*)[\'"]', re.M)
    return p.search(content).group(1)


setup(
    name='playground',
    author='Lukas Turcani',
    author_email='lukasturcani93@gmail.com',
    url='https://www.github.com/lukasturcani/python-playground',
    version=get_version(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=(),
    python_requires='>=3.9',
)
