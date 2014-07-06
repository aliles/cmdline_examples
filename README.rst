Command line examples
=====================

This repository contains example programs for my presentation 'Command line
programs for busy developers' at PyConAU 2014. Each example in the repository
demonstrate the use of a different command line library.

Using the Twitter API
---------------------

To use the example programs you will need to register a new client application
with Twitter. To do this, login into https://dev.twitter.com/ with your Twitter
account and browser to 'My Applications'. Now click 'Create New App' and
complete the form. Once the application is created you will need to generate
your access token from the API tab. You will have the necessary API Key, API
Secret, Access Token and Access Secret necessary to continue.

The command line
----------------

All sample applications will fetch the necessary API and access tokens from the
current environment. The environment variables are ``API_KEY``,
``API_SECRET``, ``ACCESS_TOKEN`` and ``ACCESS_SECRET``. Alternatively the API
and access tokens can be passed using command line arguments.

Each application accepts 3 sub-commands, ``timeline``, ``mentions`` and
``retweets``. Each of these selects a different timeline for the authenticated
user and prints the last 20 tweets from it.

The programs
------------

The following example applications demonstrate using standard library modules
for command line parsing.

* ``tw_getopt.py``, the `getopt`_ module.
* ``tw_optparse.py``, the `optparse`_ module.

.. _getopt: https://docs.python.org/dev/library/getopt.html
.. _optparse: https://docs.python.org/dev/library/optparse.html

While the following example applications demonstrate using third party packages
from PyPI.

* ``tw_begins.py``, the `begins`_ package.

.. _begins: https://pypi.python.org/pypi/begins
