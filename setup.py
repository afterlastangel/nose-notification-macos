import os
from setuptools import setup


setup(name='NNMPlugin',
    version='0.1',
    author='Truc Le',
    author_email='afterlastangel@gmail.com',
    description=('Nose plugin to raise an OS X Notification'
        ' Center alert when a test run has finished'),
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md',
        ), 'r').read(),
    url='https://github.com/afterlastangel/nose-notification-macos',
    license='GNU LGPL',
    py_modules=['nnmplugin'],
    platforms='MacOS X',
    entry_points = {
        'nose.plugins.0.10': [
            'nnmplugin = nnmplugin:NNMPlugin'
            ]
        },
    )
