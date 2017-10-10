# Parkrun HackApi

This is setup to provide a simple API to interact with parkrun data.

I am no way affiliated with parkrun, and cache the data as to prevent any performance
hits on their site, not for personal gain.

If anyone wants to help with the project, please let me know - as the office parkrun api
unfortunately hit a dead end in 2014.

Cheers,

Andy Loughran

## Installation

Setup your virtualenv:

  $ virtualenv venv
  $ source venv/bin/activate

Install the dependencies:

  $(venv) pip install -r requirements.txt

Execute the api (it'll listen on http://localhost:5000 by default):

  $(venv) python api.py
