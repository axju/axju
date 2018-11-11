from axju.worker.django import DjangoWorker
from axju.worker.git import GitWorker

WORKER = {
    'django': DjangoWorker,
    'git': GitWorker,
}
