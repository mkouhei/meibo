======================================================
meibo is retrieving users list from mailman admin view
======================================================

This tool retrieves mail address list from Mailman admin view, and convert it to JSON data.

Requirements
------------

* Python 2.7
* httplib2
* PyQuery

Setup
-----

Install Debian packages that ldaptazuna depends on
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

meibo depends on Python2.7. Install these packages.::

  $ sudo apt-get install python-httplib2 python-pyquery


Install meibo
^^^^^^^^^^^^^

Install that choosing with one of three ways.

from source
"""""""""""
::

   $ git clone https://github.com/mkouhei/meibo.git
   $ cd meibo
   $ sudo python setup.py install


Debian package
^^^^^^^^^^^^^^

Download python-meibo-x.x_all.deb from <uri> and install with dpkg command.::

  $ wget http://www.palmtb.net/deb/l/python-meibo_x.x-x_all.deb
  $ sudo dpkg -i python-meibo_x.x-x_all.deb


meibo configuration
^^^^^^^^^^^^^^^^^^^

somethin

Development
-----------

You copy pre-commit hook scripts after git clone.::

  $ cp -f utils/pre-commit.txt .git/hooks/pre-commit

Next install python 2.7 later and setuptools, pytest, pep8, python-httplib2, python-pyquery. Below way is for Debian GNU/Linux Sid system.::

  $ sudo apt-get install python python-setuptools python-pytest pep8 python-httplib2 python-pyquery

Setup test data::

  $ py.test src/tests/setup.py

