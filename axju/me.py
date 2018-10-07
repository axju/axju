"""This file contains alle the settings for my setup. You can uses it as a
template for your settings"""

from axju.contrib.resume import Resume
from axju.contrib.blueprint import System, ProjectTemplates, Alias

settings={
    'name': 'Axel Juraske',
    'email': 'axel.juraske@short-report.de',
    'dirs': ['projects/', 'storage/music/', 'storage/mamorys/', 'storage/.../', ],
    'progs': {
        'git': {},
        'thundbird': {},
        'atom': {
            'linux':[ {'cmd': ['sudo add-apt-repository ppa:webupd8team/atom', 'sudo apt update', 'sudo apt install atom']}],
            'win': [{'exe': 'https://atom.io/download/windows_x64'}],
        },
    },
    'templates': {
        'pyPackage': [
            {'file': 'README.rst', },
            {'file': 'setup.py', 'content': """ """},
            {'file': '{{ packege_name }}/__init__.py'}
        ]
    },
    'alias': {
        'update': {'linux': ['sudo apt update', 'sudo apt upgrade -y', 'sudo apt autoremove -y']},
    }
}

resume = Resume(settings=settings)

templates = ProjectTemplates(settings=settings)

system = System(settings=settings)

alias = Alias(settings=settings)
