import logging

from axju.worker.django import DjangoWorker

def main():
    worker = DjangoWorker()

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    ch.setLevel(worker.logger.level)

    worker.logger.addHandler(ch)

    worker.cli()

if __name__ == '__main__':
    main()
