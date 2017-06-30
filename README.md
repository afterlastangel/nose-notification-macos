nose-notification-macos
========================

A plugin to raise a useful notification message in the OS X Notification Center when a nose test run is complete. 

This is a fork from https://github.com/dreynolds/nose-notification-centre as It use pync which is not maintain. Directly call terminal-notifier


Installation
------------

First install terminal notifier:
https://github.com/julienXX/terminal-notifier

Install from source:

    $ git clone https://github.com/afterlastangel/nose-notification-macos.git
    $ cd nose-notification-macos
    $ python setup.py install


Basic Usage
-----------

    $ nosetests --with-NNMPlugin
