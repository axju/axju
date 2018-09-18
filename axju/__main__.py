import argparse

from axju.me import AxJu
from axju.__about__ import __version__

def main():
    parser = argparse.ArgumentParser(description='axju')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    args = parser.parse_args()

    axel = AxJu(format="table")
    axel = AxJu()
    print(axel)

    parser.print_help()


if __name__ == '__main__':
    main()
