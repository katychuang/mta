Simple scripts to help clean MTA data for analysis. Still a work in progress.

https://github.com/katychuang/mta

This is intended to provide lightweight functionality for cleaning raw MTA data to make it easier to import into databases or spreadsheets.

Features:
  * Shell script that curls through a list of turnstile files to download them as a batch.
  * Clean-turnstyle.py module for cleaning turnstile data.


Dependencies
------------

  * A unix/linux/osx operating system
  * Python 2.7


Usage
-----

0) Install the dependencies listed above.

1) Start new Python projects by cloning this repo:

    git clone git@github.com:katychuang/mta.git

2) Download data with

    ./download-turnstile-data.sh

3) Run the cleaning module

    python clean-turnstile.py


Known Issues
------------

This is still a work in progress.


Thanks
------

The modest contents of this directory owe much to @MonsieurCactus's tutorials on the data format provided by the MTA website.

Many thanks also to MTA for providing data publically. http://web.mta.info/developers/
