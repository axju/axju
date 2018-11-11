import logging
import argparse

class BasicWorker(object):
    """This is the basic structur of a worker class."""

    steps = {}

    def __init__(self, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        self.parser = self.setup_parser()

        self.error = False

        for key, value in kwargs.items():
            setattr(self, key, value)


    def logger_verbose(self):
        """Set logger level to debug"""
        self.logger.setLevel(logging.DEBUG)

    def logger_add_file(self, filename):
        fh = logging.FileHandler(filename)
        fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(message)s'))
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def check_step(self, name):
        if name not in self.steps:
            self.logger.warning('No step definition for "%s"', name)
            self.error = True
            return False
        return True


    def setup_parser(self):
        parser = argparse.ArgumentParser(description='Some atomation stuff, have fun')
        parser.add_argument('-v', '--verbose', action='store_true', help='For debugging ;)')
        parser.add_argument('-l', '--log', type=str, help='Logfile')
        parser.add_argument('-s', '--steps', nargs='+', type=str, default=['run'], help='All the steps')
        parser.add_argument('--export', type=str, help='Create a script')
        parser.add_argument('--show', action='store_true', help='Show the steps.')
        return parser


    def parse(self, args=None):
        self.args, unknown = self.parser.parse_known_args(args)


    def run(self, name):
        """Run the one step"""
        if not self.check_step(name): return None

        step = self.steps[name]
        self.logger.info('run step "%s"', name)

        if 'func' in step:
            getattr(self, step['func'])(**step.get('kwargs', {}))
            self.logger.info('finished step "%s"', name)

        elif 'steps' in step:
            for s in step['steps']:
                self.run(s)
            self.logger.info('finished step "%s"', name)

        return step


    def export(self, name, file):
        """Export the step to a file. So you can this scrip to setup your
        system"""
        if not self.check_step(name): return None

        file.write('# Step: {}'.format(name))

        return step


    def cli(self, args=None):
        self.parse(args)

        if self.args.verbose: self.logger_verbose()

        if self.args.log: self.logger_add_file(self.args.log)


        if self.args.show:
            return self.show()

        for step in self.args.steps:
            self.run(step)


    def show(self):
        """Display some infos about the steps."""
        n = max([ len(s) for s in self.steps ])
        for step, data in self.steps.items():
            print(step.ljust(n+1, '.'), data.get('info', 'missing'), sep='')
