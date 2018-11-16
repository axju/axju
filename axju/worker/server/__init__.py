from axju.generic import BasicWorker

class ServerWorker(BasicWorker):
    """Create backups and export log files"""

    steps = {
        'run': {
            'info': 'Run all steps',
            'steps': [],
        },

    }
