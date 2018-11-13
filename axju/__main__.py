import argparse
import os, sys
from axju.tools import WorkLoader

from axju.worker import WORKER


def main():
    parser = argparse.ArgumentParser(description='Manage the worker', add_help=False)

    parser.add_argument('--directory', type=str, help='Load all files from the directory')
    parser.add_argument('--file', nargs='+', type=str, help='Load the worker from a file')
    parser.add_argument('--cls', nargs='+', type=str, help='Load one or more class')
    parser.add_argument('--pre', action='store_true', help='Load the predefined worker')
    parser.add_argument('--show', action='store_true', help='Show the different worker')
    parser.add_argument('--help', action='store_true', help='Display this help text')
    parser.add_argument('worker', nargs='?', help='Select the worker')

    args, unknown = parser.parse_known_args()
    loader = WorkLoader()

    # import some worker
    if args.file:
        for file in args.file:
            loader.load_file(file)

    if args.cls:
        for cls in args.cls:
            loader.load_class(cls)

    if args.directory:
        loader.load_directory(args.directory)

    elif not args.pre:
        homedir = os.path.join(os.path.expanduser('~'), 'worker')
        if os.path.isdir(homedir):
            loader.load_directory(homedir)


    # No worker name requirt only one worker load
    if len(loader.worker) == 1:
        name = list(loader.worker.keys())[0]
        if args.show:
            return loader.worker[name].show()

        return loader.run(name, sys.argv[3:])

    if len(loader.worker) == 0:
        for name, cls in WORKER.items():
            loader.load_class(cls, name)


    # multible worker load
    if args.worker:
        if args.show:
            return loader.worker[args.worker].show()

        n = 4 if args.directory else 2
        return loader.run(args.worker, sys.argv[n:])

    elif args.show:
        return loader.show()

    elif args.help:
        parser.print_help()

    parser.print_help()

if __name__ == '__main__':
    main()
