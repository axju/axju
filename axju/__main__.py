import argparse
from axju.tools import WorkLoader
from axju.worker.django import ArgparseDjangoWorker
from axju.worker.git import GitWorker

def main():
    parser = argparse.ArgumentParser(description='Manage custom worker')

    parser.add_argument('--directory', type=str, help='...')
    parser.add_argument('--file', type=str, help='...')
    parser.add_argument('--cls', type=str, help='...')
    parser.add_argument('--show', action='store_true', help='...')
    parser.add_argument('--setup', action='store_true', help='...')
    parser.add_argument('worker', nargs='?', help='...')

    args, unknown = parser.parse_known_args()

    loader = WorkLoader()

    if args.file:
        loader.load_file(args.file)

    if args.directory:
        loader.load_directory(args.directory)

    if args.cls:
        loader.load_class(args.cls)

    if not loader.worker:
        loader.load_class('django', ArgparseDjangoWorker)
        loader.load_class('git', GitWorker)

    if args.show: return loader.show()

    if args.worker:
        if args.worker in loader.worker:
            return loader.run(args.worker, unknown)
        else:
            unknown.append(args.worker)

    if len(loader.worker) == 1:
        return loader.run(list(loader.worker.keys())[0], unknown)

    parser.print_help()

if __name__ == '__main__':
    main()
