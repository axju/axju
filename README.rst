axju
====
comming soon.

Install
-------
::

  pip install axju


Functions
---------
::

  axju help
  axju setup
  axju me

  axju-sys install
  axju-sys update

  axju-proj show
  axju-proj open --ide atom <name|dir|.>
  axju-proj update <name|dir|.>
  axju-proj backup <name|dir|.>
  axju-proj push <name|dir|.>

  axju-alias <name>

  axju-temp package
  axju-temp readme


Development
-----------
Clone repo::

  git clone https://github.com/axju/axju.git

Create virtual environment and update dev-tools::

  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade wheel pip setuptools twine

Install local::

  pip install -e .

Publish the packages::

  python setup.py sdist bdist_wheel
  twine upload dist/*
