from subprocess import call
from tempfile import NamedTemporaryFile
from jinja2 import Environment, BaseLoader, PackageLoader

from axju.generic.execution import ExecutionWorker

class TemplateWorker(ExecutionWorker):
    """..."""

    templates = None

    def __init__(self, **kwargs):
        super(TemplateWorker, self).__init__(**kwargs)

        templateLoader = PackageLoader(*self.templates)
        self.templateEnv = Environment(loader=templateLoader)

    def render_template(self, filename):
        template = self.templateEnv.get_template(filename)
        return template.render(self.render_data())

    def run(self, name):
        step = super(TemplateWorker, self).run(name)
        if not step: return None

        if 'template' in step:
            t = self.render_template(step['template'])

            if 'filename' in step:
                filename = self.render_str(step['filename'])

                with NamedTemporaryFile() as f:
                    f.write(t.encode())
                    f.flush()
                    if step.get('sudo', False):
                        call(['sudo', 'cp', f.name, filename])
                    else:
                        call(['cp', f.name, filename])

            else:
                self.execute(t.split('\n'))
            self.logger.info('finished step "%s"', name)

        return step
