import argparse
import inspect

def obj2cli(obj, **kwargs):
    parser = argparse.ArgumentParser(
        prog=obj.__class__.__name__,
        description=obj.__class__.__doc__,
        epilog="This CLI uses the axju.cli module, by axju",
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
                        parser_a.add_argument('--'+k, type=type(v.default), default=v.default)
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

def cls2cli(cls, **kwargs):
    obj = cls(load=True)
    obj2cli(obj, **kwargs)
