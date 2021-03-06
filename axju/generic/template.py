from subprocess import call
from tempfile import NamedTemporaryFile
from jinja2 import Environment, BaseLoader, PackageLoader

from axju.generic.execution import ExecutionWorker

class TemplateWorker(ExecutionWorker):
    """This worker can work with steps like:
    {
        'info': '....',
        'template': 'template name',
        'filename': 'path to rendered template',
        'sudo': True,
    }
    If the key template exist, this worker will execute the step. Only if the
    key filename exist, the worker will save the template as a file. Otherwise,
    it will interpreter lien as an commands and execute it.
    """

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

    def export(self, name, file):
        step = super(TemplateWorker, self).export(name, file)
        if not step: return None

        if 'template' in step:
            t = self.render_template(step['template'])

            if 'filename' in step:
                file.write('# Create a file:\n')
                filename = self.render_str(step['filename'])

                if step.get('sudo', False):
                    file.write('sudo nano "{}"\n'.format(filename))
                else:
                    file.write('nano "{}"\n'.format(filename))

                file.write('# ---- begin file ----\n')
                for c in t.split('\n'):
                    file.write('{}\n'.format(c, filename))
                file.write('# ----- end file -----\n')


            else:
                for c in t.split('\n'):
                    file.write('{}\n'.format(c))

        return step
