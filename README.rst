axju
====

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
  :alt: Gitter
  :target: https://gitter.im/axju/Lobby?utm_source=share-link&utm_medium=link&utm_campaign=share-link

.. image:: https://img.shields.io/twitter/url/https/github.com/axju/axju.svg?style=social
  :alt: Twitter
  :target: https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Faxju%2Faxju

This small project help me, to automate boring stuff. It started with deploying
django, but where will coming more. Hopefully


Install
-------
::

  pip install axju


Quick start
-----------
Create the file (and directory) ~/worker/simple.py, with the following::

  from axju.generic import BasicWorker

  class Worker(BasicWorker):
      steps = {
          'run':{
              'func': 'hello',
          },
      }
      def hello(self):
          print('Hello world')

To run your worker execute::

  axju simple

Write more worker in your worker-folder. You can run them by::

  axju "filename of the worker"


How to uses
-----------
The basic entry point is the command axju. This is a loader to different worker.
You can write you own worker or uses or the predefined ones.

Show the different worker::

  axju --show

For now, this show the predefined worker. You have several ways to define your
own. A single file, dynamical import of a single class or a directory with
multiple worker.

There are some examples in the example folder. To run the simple worker uses::

  axju --file examples/worker/simple.py

Your own file only have to define a class called Worker. This class should be
inherited from the Basic Worker, to give you some basic functionality. If you
need more functions use other basic class like ExecutionWorker or
TemplateWorker. The script also create a worker object an call the cli
function::

  if __name__ == '__main__':
    w = Worker()
    w.cli()

This three liens make it possible, to execute the file directly with python::

  python examples/simple.py

The command::

  axju --cls axju.worker.django.DjangoWorker

load the predefined django worker. Maybe you wanted to write you own package
with your worker. This is how you can run them.

You can also load multiple worker by load multiple files, class or use the dir
argument. It is also possible to combine this. But usual you will use the dir
argument. Create a folder with all your worker, load and show them::

  axju --dir examples/worker --show

To run the simple work, set the worker argument::

  axju --dir examples/worker simple

This command is equal to::

  axju --file examples/worker/simple.py

If you save your worker under ~/worker/, the loader will yours. Otherwise the
predefined will be load. If you copy the worker-folder form the examples to your
home directory. You can run::

  axju simple


Functions
---------
Some predefined worker have a single entry point::

  axju
  django-deploying


Development
-----------
Clone repo::

  git clone https://github.com/axju/axju.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine tox

Install local::

  pip install -e .

Run some tests::

  tox
  python setup.py test

Make the documentation::

  docs/make.bat html

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*
