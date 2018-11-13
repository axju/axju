import importlib.util
import os

class WorkLoader(object):
    """Load some custom worker"""

    def __init__(self):
        self.worker = {}

    def load_object(self, obj, name):
        self.worker[name] = obj

    def load_class(self, cls, name=None):
        if isinstance(cls, str):
            components = cls.split('.')
            mod = __import__('.'.join(components[:-1]), fromlist=[components[-1]])
            cls = getattr(mod, components[-1])

        if not name: name = components[-1]
        self.worker[name] = cls()


    def load_directory(self, dir):
        for file in os.listdir(dir):
            if file.endswith(".py"):
                filename = os.path.join(dir, file)
                self.load_file(filename)

    def load_file(self, file):
        name = os.path.splitext(os.path.basename(file))[0]
        spec = importlib.util.spec_from_file_location(name, file)
        worker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(worker)
        cls = getattr(worker, 'Worker', None)
        if cls:
            self.worker[name] = cls()

    def show(self):
        print('Worker:')
        for w in self.worker:
            print(' ', w)

    def run(self, name, argv):
        if name in self.worker:
            self.worker[name].parse(argv)
            self.worker[name].logger_add_stream()
            self.worker[name].cli()
        else:
            print('Now worker "{}"'.format(name))
