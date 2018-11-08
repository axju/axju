import argparse
import sys
from axju.tools import WorkLoader
from axju.worker.django import ArgparseDjangoWorker
from axju.worker.git import GitWorker

def main():
    parser = argparse.ArgumentParser(description='Manage custom worker')

    parser.add_argument('--directory', type=str, help='...')
    parser.add_argument('--file', type=str, help='...')
    parser.add_argument('--show', action='store_true', help='...')
    parser.add_argument('--setup', action='store_true', help='...')
    parser.add_argument('worker', nargs='?', help='...')

    #subparsers = parser.add_subparsers(help='worker', dest='worker')
    args = parser.parse_args()

    loader = WorkLoader()
    n = 2

    if args.file:
        loader.load_file(args.file)
        n += 2

    if args.directory:
        loader.load_directory(args.directory)
        n += 2

    if not loader.worker:
        loader.load_class('django', ArgparseDjangoWorker)
        loader.load_class('git', GitWorker)

    if args.show: return loader.show()

    if args.worker: return loader.run(args.worker, sys.argv[n:])

    parser.print_help()

if __name__ == '__main__':
    main()
