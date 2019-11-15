
Developing / Testing
====================

Clone the repo:

::

   git clone https://github.com/feluxe/sty.git

Run tests:

::

   cd sty
   python3 -m tests

Read test results in your terminal and see if things match up.

If you want to dig deeper, you should install the dev-dependencies in a virtual env:

::

   pipenv install --dev

Now you can use sty's build script:

::

   pipenv run python make.py --help








