import unittest

from axju.generic import BasicWorker

class TestBasicWorker(unittest.TestCase):

    def setUp(self):
        self.steps={
            'hello': {
                'info': 'Hello World',
            }
        }
        self.worker = BasicWorker(steps=self.steps)

    def test_steps(self):
        self.assertEqual(self.worker.steps, self.steps)

    def test_logger(self):
        self.assertEqual(self.worker.logger.level, 20)

        self.worker.logger_verbose()
        self.assertEqual(self.worker.logger.level, 10)

    def test_run(self):
        step = self.worker.run('hello')
        self.assertEqual(step, self.steps['hello'])

    def test_cli(self):
        self.assertEqual(self.worker.logger.level, 20)
        self.worker.cli(['-v', '-s', 'hello'])
        self.assertEqual(self.worker.logger.level, 10)

    def test_parse(self):
        self.worker.parse(['-v'])
        self.assertTrue(self.worker.args.verbose)

        self.worker.parse()
        self.assertFalse(self.worker.args.verbose)

        self.worker.parse(['-l', 'test.log'])
        self.assertEqual(self.worker.args.log, 'test.log')

        self.worker.parse()
        self.assertEqual(self.worker.args.steps, ['run'])

        self.worker.parse(['-s', 'hello'])
        self.assertEqual(self.worker.args.steps, ['hello'])

    def test_error(self):
        self.worker.logger.setLevel(50)
        self.assertFalse(self.worker.error)
        self.worker.run('test')
        self.assertTrue(self.worker.error)



if __name__ == '__main__':
    unittest.main()
