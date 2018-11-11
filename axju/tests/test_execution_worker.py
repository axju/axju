import unittest

from axju.generic import ExecutionWorker

class TestExecutionWorker(unittest.TestCase):

    def setUp(self):
        self.steps={
            'hello': {
                'info': 'Hello World',
                'commands': ['echo "Hello World"']
            }
        }
        self.worker = ExecutionWorker(steps=self.steps)

    def test_run(self):
        step = self.worker.run('hello')
        self.assertEqual(step, self.steps['hello'])


if __name__ == '__main__':
    unittest.main()
