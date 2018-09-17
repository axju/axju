import argparse

from axju.me import AxJu

def main():
    parser = argparse.ArgumentParser(description='axju')
    args = parser.parse_args()

    axel = AxJu(format="table")
    axel = AxJu()
    print(axel)
    #parser.print_help()


if __name__ == '__main__':
    main()
