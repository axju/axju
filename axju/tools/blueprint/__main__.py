import argparse

settings = {
    'dirs': ['projects/', 'storage/music/', 'storage/mamorys/', 'storage/.../', ],
    'progs': {
        'git': {},
        'thundbird': {},
        'atom': {
            'linux':[ {'cmd': ['sudo add-apt-repository ppa:webupd8team/atom', 'sudo apt update', 'sudo apt install atom']}],
            'win': [{'exe': 'https://atom.io/download/windows_x64'}],
        },
    }
}

class Blueprint(object):
    """docstring for Blueprint."""
    def __init__(self, settings):
        self.settings = settings

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



def structur():
    pass


def main():
    parser = argparse.ArgumentParser()
    #parser.parse_args()
    #parser.print_help()

    blueprint = Blueprint(settings)
    blueprint.show()



if __name__ == '__main__':
    main()
