"""The blueprint tool make yout workflow faster...
"""
from axju.contrib.cli import BasicCli


class Blueprint(BasicCli):
    """docstring for Blueprint."""

    __version__ = '0.0.1'

    def __init__(self, **kwargs):
        super(Blueprint, self).__init__()

        self.settings = kwargs.get('settings', {})

    def __dirs(self):
        return self.settings.get('dirs', [])

    def __progs(self):
        return self.settings.get('progs', [])

    def show(self, kinds=['dirs', 'progs']):
        """Display some information about your settings"""

        if 'dirs' in kinds:
            print("\nYour direcorys:")
            for dir in self.__dirs():
                print("  ", dir)

        if 'progs' in kinds:
            print("\nYour programms:")
            for prog in self.__progs():
                print("  ", prog)


    def home(self, ):
        """Setup your home folder"""
        pass

    def setup(self):
        """Install all your programms"""
        pass
