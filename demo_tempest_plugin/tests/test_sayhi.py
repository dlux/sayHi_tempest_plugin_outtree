'''
Integration test case for say hi command

@author:luzC
'''
import subprocess

from demo_tempest_plugin.tests.api import base
from tempest import test


class TestSayHi(base.BaseSayHi):

    @classmethod
    def resource_setup(cls):
        super(TestSayHi, cls).resource_setup()

    @test.attr(type="smoke")
    def test_hi(self):
        # Run dluxsay command
        result = subprocess.Popen("dluxsay personA", shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertIn('personA', result.stdout.read())

    @test.attr(type='smoke')
    def test_with_opts(self):
        # Run dluxsay command plus extra text
        result = subprocess.Popen("dluxsay personA", shell=True,
                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertIn('personA', result.stdout.read())

    @test.attr(type='smoke')
    def test_with_opts(self):
        cmd = ['dluxsay']
        if CONF.share.is_extra:
             cmd.append(' ' + CONF.share.extra_msg)

        # Run dluxsay command plus extra text
        result = subprocess.Popen(cmd, shell=True,
                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertIn(CONF.share.extra_msg, result.stdout.read())

    @classmethod
    def resource_cleanup(cls):
        super(TestSayHi, cls).resource_cleanup()

