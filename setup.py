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

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    long_description=readme(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'jinja2',
    ],

    entry_points = {
        'console_scripts': [
            'axju=axju.__main__:main',
            'django-deploying=axju.worker.django.__main__:main',
        ],
    },

    keywords='git django deploying devops',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
