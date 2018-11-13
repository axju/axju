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

Functions
---------
::

  axju
  django-deploying


Quick start
-----------
The basic entry point is the command axju. This is a loader to different worker.
You can write you own worker or uses or the predefined ones.

Show the different worker::

  axju --show

For now, this show the predefined worker. You have several ways to define your
own. A single file, dynamical import of a single class or a directory with
multiple worker.

There are some examples in the example folder. To run the simple worker uses::

  axju --file example/simple.py

Your own file only have to define a class called Worker. This class should be
inherited from the Basic Worker, to give you some basic functionality. If you
need more functions use other basic class like ExecutionWorker or
TemplateWorker. The script also create a worker object an call the cli
function::

  if __name__ == '__main__':
    w = Worker()
    w.cli()

This three liens make it possible, to execute the file directly with python::

  python example/simple.py

The command::

  axju --cls axju.worker.django.DjangoWorker

load the predefined django worker. Maybe you wanted to write you own package
with your worker. This is how you can run them.


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
