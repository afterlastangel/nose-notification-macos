from subprocess import Popen
import random

from nose.plugins import Plugin


class Notifier(object):

    @classmethod
    def notify(cls, title, message, group=""):
        Popen(
            ["terminal-notifier",
             "-message", message,
             "-title", title,
             "-group", group,
             "-timeout", "5",
             "-sound", "default"])


class NNMPlugin(Plugin):
    name = 'NNMPlugin'
    enabled = True

    success_messages = [
        'Hurrah!',
        'Awesome!',
        'Good work!',
        'Well done!',
    ]

    failure_messages = [
        'Boo!',
        'Doh!',
    ]

    @property
    def failure_msg(self):
        return random.choice(self.failure_messages)

    @property
    def success_msg(self):
        return random.choice(self.success_messages)

    def finalize(self, result):
        failures = len(result.failures)
        errors = len(result.errors)
        folder = result.config.workingDir.strip('/').split('/')[-1]

        if result.wasSuccessful():
            title = "Tests passed in: %s" % folder
            msg = '%s All of your %s test(s) passed!' % (
                self.success_msg,
                result.testsRun,
            )
        else:
            msg = '%s %s failures, %s errors from %s tests' % (
                self.failure_msg,
                failures,
                errors,
                result.testsRun,
            )
            title = "Tests failed in: %s" % folder

        Notifier.notify(
            message=msg,
            title=title,
            group='%s_%s_tests' % (folder, self.name),
        )
