Command line examples
=====================

This repository contains example programs for my presentation 'Command line
programs for busy developers' at PyConAU 2014. Each example in the repository
demonstrate the use of a different command line library.

To use the example programs you will need to register a new client application
with Twitter. To do this, login into https://dev.twitter.com/ with your Twitter
account and browser to 'My Applications'. Now click 'Create New App' and
complete the form. Once the application is created you will need to generate
your access token from the API tab. You will have the necessary API Key, API
Secret, Access Token and Access Secret necessary to continue.

All sample applications will fetch the necessary API and access tokens from the
current environment. The environment variables are ``API_KEY``,
``API_SECRET``, ``ACCESS_TOKEN`` and ``ACCESS_SECRET``. Some application may
also use command line arguments.
