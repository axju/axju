import importlib.util
import os

class WorkLoader(object):
    """Load some custom worker"""

    def __init__(self):
        self.worker = {}

    def load_object(self, name, obj):
        self.worker[name] = obj

    def load_class(self, cls):
        if isinstance(cls, str):
            components = cls.split('.')
            mod = __import__('.'.join(components[:-1]), fromlist=[components[-1]])
            cls = getattr(mod, components[-1])

        self.worker[components[-1]] = cls()

    def load_directory(self, dir):
        pass

    def load_file(self, file):
        name = os.path.splitext(os.path.basename(file))[0]
        spec = importlib.util.spec_from_file_location(name, file)
        worker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(worker)
        self.worker[name] = worker.Worker()

    def show(self):
        print('Worker:')
        for w in self.worker:
            print(' ', w)

    def run(self, name, argv):
        if name in self.worker:
            self.worker[name].parse(argv)
            self.worker[name].run()
        else:
            print('error')
