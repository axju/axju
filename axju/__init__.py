from axju.me import AxJu
from axju.blueprint import Blueprint
from .__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __url__, __version__
)

__all__ = [
    '__title__', '__summary__', '__url__', '__version__', '__author__',
    '__email__', '__license__', '__copyright__',
]

axel = AxJu()

blueprint = Blueprint(settings={
    'dirs': ['projects/', 'storage/music/', 'storage/mamorys/', 'storage/.../', ],
    'progs': {
        'git': {},
        'thundbird': {},
        'atom': {
            'linux':[ {'cmd': ['sudo add-apt-repository ppa:webupd8team/atom', 'sudo apt update', 'sudo apt install atom']}],
            'win': [{'exe': 'https://atom.io/download/windows_x64'}],
        },
    }
})
