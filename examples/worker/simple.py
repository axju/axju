from axju.generic import BasicWorker

class Worker(BasicWorker):
    steps = {
        'run':{
            'info': 'Print only Hello World',
            'func': 'hello',
        },
    }
    def hello(self):
        print('Hello world')


if __name__ == '__main__':
    w = Worker()
    w.cli()
