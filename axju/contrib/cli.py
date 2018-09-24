import argparse


class BasicCli(object):
    """ """
    def __init__(self, **kwargs):
        self.parser = argparse.ArgumentParser(
            prog=self.__class__.__name__,
            description=self.__class__.__doc__,
            epilog="This CLI uses the BasicCli class, by axju",
            add_help=False
        )

        self.parser.add_argument(
            'action',
            nargs='?',
            choices=set(s for s in self.__class__.__dict__ if s[0] != '_')
        )

        self.parser.add_argument(
            '--help',
            action='store_true',
            help='foo help'
            )

        if '__version__' in self.__class__.__dict__:
            self.parser.add_argument(
                '--version',
                action='version',
                version='%(prog)s ' + self.__class__.__version__
            )

    def help(self):
        for name, item in self.__class__.__dict__.items():
            if name[0] != '_':
                print(name, item.__doc__)

    def main(self):
        self.args = self.parser.parse_args()

        if self.args.help:
            self.help()
            return

        if self.args.action:
            getattr(self, self.args.action)()# self.actions[self.args.action]()
            return

        self.parser.print_help()
