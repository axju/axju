import subprocess

class ProjectTemplates(object):
    """docstring for ProjectTemplates."""

    __version__ = '0.0.1'

    def __init__(self, **kwargs):
        super(ProjectTemplates, self).__init__()

        self.settings = kwargs.get('settings', {})

    def __templates(self):
        return self.settings.get('templates', [])

    def show(self):
        """Show the posible templates."""
        for t in self.__templates():
            print(t)


class Alias(object):
    """Some alias."""

    def __init__(self, **kwargs):
        super(Alias, self).__init__()

        self.alias = kwargs.get('settings', {}).get('alias', {})

    def run(self, name):
        """execute the alias"""
        if name not in self.alias:
            print('Alias "{}" not found'.format(name))
            return False

        for cmd in self.alias[name]['linux']:
            subprocess.call([cmd, ], shell=True)#self.alias[name]['linux'], shell=True)

    def show(self):
        for arg in self.alias:
            print(arg)


class System(object):
    """docstring for Blueprint."""

    __version__ = '0.0.1'

    def __init__(self, **kwargs):
        super(System, self).__init__()

        self.settings = kwargs.get('settings', {})

    def __dirs(self):
        return self.settings.get('dirs', [])

    def __progs(self):
        return self.settings.get('progs', [])

    def show(self, kinds=['dirs', 'progs']):
        """Display some information about your settings
        :kind list sender: The person sending the message
        :type kind: list"""

        if 'dirs' in kinds:
            print("\nYour direcorys:")
            for dir in self.__dirs():
                print("  ", dir)

        if 'progs' in kinds:
            print("\nYour programms:")
            for prog in self.__progs():
                print("  ", prog)

    def home(self, test, test2='hallo', test3=[1,2,3]):
        """Setup your home folder"""
        pass

    def setup(self):
        """Install all your programms"""
        pass
