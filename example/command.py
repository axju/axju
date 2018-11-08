from axju.core import StepWorker, ArgparseMixin

class Worker(ArgparseMixin, StepWorker):
    steps = {
        'run':{
            'info': 'Do stupid stuff',
            'func': 'cmd',
        },
    }

    def setup_parser(self):
        parser = super(Worker, self).setup_parser()
        parser.add_argument('cmd', type=str, help='The cmd :D')
        return parser

    def parse(self, args=None):
        super(Worker, self).parse(args)
        self._cmd = self.args.cmd

    def cmd(self):
        self.execute([self._cmd])


if __name__ == '__main__':
    w = Worker()
    w.run()

    #w = Worker()
    #w.run(['dir'])

    #w = Worker()
    #w.parse()
    #w.run()
