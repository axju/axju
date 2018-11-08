from axju.worker.django import ArgparseDjangoWorker

def main():
    worker = ArgparseDjangoWorker()
    worker.parse()
    worker.run()

if __name__ == '__main__':
    main()
