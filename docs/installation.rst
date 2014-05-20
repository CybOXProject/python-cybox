.. _installation:

Installation
============

Recommended Installation
------------------------

Use pip_:

.. code-block:: bash

    $ pip install cybox

You might also want to consider using a virtualenv_.

.. _pip: http://pip.readthedocs.org/
.. _virtualenv: http://virtualenv.readthedocs.org/


Dependencies
------------

The python-cybox library is developed on Python 2.7 and tested against both
Python 2.6 and 2.7. Besides the Python Standard Library, python-cybox relies on
the following Python libraries:

* lxml_ - A Pythonic binding for the C libraries **libxml2** and
  **libxslt**.
* python-dateutil_ - A library for parsing datetime information.
* importlib_ (Python 2.6) - Convenience wrappers for ``__import__()``.

.. note::

  ``importlib`` is `built into`_ Python 2.7, and is available on PyPI for
  Python 2.6.

Each of these can be installed with ``pip`` or by manually downloading packages
from PyPI. On Windows, you will probably have the most luck using `pre-compiled
binaries`_ for ``lxml``. On Ubuntu (12.04 or 14.04), you should make sure the
following packages are installed before attempting to compile ``lxml`` from
source:

* libxml2-dev
* libxslt1-dev
* zlib1g-dev

.. _lxml: http://lxml.de/
.. _python-dateutil: http://labix.org/python-dateutil
.. _importlib: https://pypi.python.org/pypi/importlib
.. _built into: https://docs.python.org/2.7/library/importlib.html
.. _pre-compiled binaries: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml


Manual Installation
-------------------

If you are unable to use pip, you can also install python-cybox with
setuptools_. If you don't already have setuptools installed, please install it
before continuing.

1. Download and install the dependencies_ above. Although setuptools will
   generally install dependencies automatically, installing the dependencies
   manually beforehand helps distinguish errors in dependency installation from
   errors in python-cybox installation. Make sure you check to ensure the
   versions you install are compatible with the version of python-cybox you
   plan to install.

2. Download the desired version of python-cybox from PyPI_ or the GitHub
   releases_ page. The steps below assume you are using the |release| release.

3. Extract the downloaded file. This will leave you with a directory named
   cybox-|release|.

.. parsed-literal::
    $ tar -zxf cybox-|release|.tar.gz
    $ ls
    cybox-|release| cybox-|release|.tar.gz

OR

.. parsed-literal::
    $ unzip cybox-|release|.zip
    $ ls
    cybox-|release| cybox-|release|.zip

4. Run the installation script.

.. parsed-literal::
    $ cd cybox-|release|
    $ python setup.py install

5. Test the installation.

.. parsed-literal::
    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cybox
    >>>

If you don't see an ``ImportError``, the installation was successful.

.. _setuptools: https://pypi.python.org/pypi/setuptools/
.. _PyPI: https://pypi.python.org/pypi/cybox/
.. _releases: https://github.com/CybOXProject/python-cybox/releases


Further Information
-------------------

If you're new to installing Python packages, you can learn more at the `Python
Packaging User Guide`_, specifically the `Installing Python Packages`_ section.

.. _Python Packaging User Guide: http://python-packaging-user-guide.readthedocs.org/
.. _Installing Python Packages: http://python-packaging-user-guide.readthedocs.org/en/latest/tutorial.html#installing-python-packages
