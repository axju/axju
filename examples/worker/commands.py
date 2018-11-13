from axju.generic import ExecutionWorker

class Worker(ExecutionWorker):
    steps = {
        'run':{
            'info': 'Hello World',
            'commands': ['echo "Hello World"'],
        },
    }


if __name__ == '__main__':
    w = Worker()
    w.cli()
