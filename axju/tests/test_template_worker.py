import unittest

from axju.generic import TemplateWorker

class TestTemplateWorker(unittest.TestCase):

    def setUp(self):
        self.steps={
            'hello': {
                'info': 'Hello World',
                'commands': ['echo "Hello World"']
            }
        }
        self.worker = TemplateWorker(
            steps=self.steps,
            templates = ('axju', 'tests/templates/'))

    def test_run(self):
        step = self.worker.run('hello')
        self.assertEqual(step, self.steps['hello'])



if __name__ == '__main__':
    unittest.main()
