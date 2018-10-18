import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

def readme():
    with open('README.rst') as f:
        return f.read()

about = {}
with open(os.path.join(base_dir, 'axju', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    long_description=readme(),
    #long_description_content_type='text/markdown',
    keywords='github wordpress backup sync',
    packages=find_packages(),
    install_requires=[
        'gitpython',
    ],
    entry_points = {
        'console_scripts': [
            'axju=axju.__main__:main',
            'axju-proj=axju.proj.__main__:main',
        #    'axju-alias=axju.func:alias_cli',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
