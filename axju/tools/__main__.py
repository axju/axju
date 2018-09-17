import argparse

def main():
    parser = argparse.ArgumentParser(description='axju tools', add_help=False)
    parser.add_argument('action', nargs='?', choices=('help', 'list', 'version'))
    args = parser.parse_args()

    if args.action == 'help':
        parser.print_help()

    parser.print_help()


if __name__ == '__main__':
    main()
