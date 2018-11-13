import logging

from axju.worker.django import DjangoWorker

def main():
    worker = DjangoWorker()
    worker.logger_add_stream()
    worker.cli()

if __name__ == '__main__':
    main()
