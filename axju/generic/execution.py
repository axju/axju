import sys
from subprocess import Popen, PIPE, STDOUT
from jinja2 import Environment, BaseLoader

from axju.generic.basic import BasicWorker

class ExecutionWorker(BasicWorker):
    """..."""

    def execute(self, commands):
        """Connect to the shell and execute multiple commands. It is necessary
        to activate a virtual environment and then install some packages."""

        cmd = ['/bin/bash', '-i']
        encoding = 'utf-8'
        if sys.platform[:3] == 'win':
            cmd = ['cmd']
            encoding = 'cp437'
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=True)

        for command in commands:

            self.logger.debug('run command "%s"', command)
            p.stdin.write(str(command + "\n").encode())
            p.stdin.flush()

        p.stdin.close()
        self.logger.info('working...')
        self.logger.debug('result:\n%s', p.stdout.read().decode(encoding))

        p.wait()
        p.stdout.close()


    def render_data(self):
        """Get the data for the commands"""
        return {}


    def render_str(self, s):
        template = Environment(loader=BaseLoader()).from_string(s)
        return template.render(self.render_data())


    def render_commands(self, commands):
        """Render a list of commands. That can contain some dummy."""
        return [ self.render_str(c) for c in commands ]


    def run(self, name):
        step = super(ExecutionWorker, self).run(name)
        if not step: return None

        if 'commands' in step:
            self.execute(self.render_commands(step['commands']))
            self.logger.info('finished step "%s"', name)

        return step

    def export(self, name, file):
        step = super(ExecutionWorker, self).export(name, file)
        if not step: return None

        if 'commands' in step:
            for c in self.render_commands(step['commands']):
                file.write('{}\n'.format(c))

        return step
