import argparse
import inspect


class BasicCli(object):
    """First try, but the function below is great"""
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


def obj2cli_old(obj, **kwargs):
    parser = argparse.ArgumentParser(
        prog=obj.__class__.__name__,
        description=obj.__class__.__doc__,
        epilog="This CLI uses the BasicCli class, by axju",
        add_help=False
    )

    parser.add_argument(
        'action',
        nargs='?',
        choices=set(s for s in obj.__class__.__dict__ if s[0] != '_')
    )

    parser.add_argument(
        '--help',
        action='store_true',
        help='foo help'
        )

    if '__version__' in obj.__class__.__dict__:
        parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s ' + obj.__class__.__version__
        )
    args = parser.parse_args()

    if args.help:
        for name, item in obj.__class__.__dict__.items():
            if name[0] != '_':
                print(name, item.__doc__)
        return

    if args.action:
        getattr(obj, args.action)()# self.actions[self.args.action]()
        return

    parser.print_help()


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def obj2cli(obj, **kwargs):
    parser = argparse.ArgumentParser(
        prog=obj.__class__.__name__,
        description=obj.__class__.__doc__,
        epilog="This CLI uses the BasicCli class, by axju",
    )

    if '__version__' in obj.__class__.__dict__:
        parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s ' + obj.__class__.__version__
        )

    subparsers = parser.add_subparsers(help='commands', dest='action')

    for name, item in obj.__class__.__dict__.items():
        if name[0] != '_':
            parser_a = subparsers.add_parser(name, help=item.__doc__)

            signature = inspect.signature(item)
            for k, v in signature.parameters.items():
                if k != 'self':
                    if type(v.default) == type(list()):
                        parser_a.add_argument(k, nargs='?', default=v.default)
                    elif v.default is not inspect.Parameter.empty:
                        parser_a.add_argument(k, type=type(v.default), default=v.default)
                    else:
                        parser_a.add_argument(k)

    if 'default' in kwargs:
        print(kwargs['default'])
        parser.set_defaults(action=kwargs['default'])

    args = parser.parse_args()

    action = args.action
    values = vars(args)
    del values['action']

    if action:
        getattr(obj, action)(**values)
        return

    parser.print_help()
