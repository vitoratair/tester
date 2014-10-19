# coding: utf-8
from production.core.headers import *
from production.ping.models import Test as PingTest
from fabric import tasks
from fabric.api import run
from fabric.api import settings
from fabric.api import env
from fabric.network import disconnect_all
import os


class ExecPing(object):

    """
        Class responsible to implement all methods to ping access
    """

    def __init__(self, tests, product, sshUser, sshPassword):
        """
        Class constructor, must be set the values passed by parameter
        """

        self.product = product
        self.testList = tests
        env.user = sshUser
        env.password = sshPassword
        self.checkLocalhost()

    def savePingResult(self, resultPing, ping):
        """
            Must be saved the result of each test done
        """

        if resultPing == PASSED:
            PingTest(product_id=self.product, test_id=ping, result=PASSED).save()
        else:
            PingTest(product_id=self.product, test_id=ping, result=REPROVED).save()

    def getCommandPing(self, test):
        """
            Must be returned a string with the complete ping test
        """

        command = 'ping '

        if test.packetNumber is not None:
            command = command + ' -c ' + str(test.interval)
        else:
            command = command + ' -c ' + str(DEFAULT_PACKET_NUMBER)

        if test.interval is not None:
            command = command + ' -s ' + str(test.interval)

        return command + ' ' + str(test.ipDestination)

    def execCommand(self, tests):
        """
            Must be exec a command from a external machine
        """

        resultPing = PASSED

        for test in tests:
            with settings(parallel=False, host_string=test.ipOrigin):
                try:
                    run(self.getCommandPing(test))
                except:
                    resultPing = REPROVED

                self.savePingResult(resultPing, test.id)

    def execPingByExternalIp(self, tests):
        """
            Must be done a ping test from of a external IP
        """

        tasks.execute(self.execCommand, tests)

        disconnect_all()

    def execPingByLocalhost(self, tests):
        """
            Must be done a ping test by localhost
        """

        for test in tests:
            try:
                resultPing = os.system(self.getCommandPing(test))
            except:
                print "Command not found >>> " + self.getCommandPing(test)

            self.savePingResult(resultPing, test.id)

    def checkLocalhost(self):
        """
            Must be checked if a test should be made from localhost or not
        """
        localhostTest = []
        externalIpTest = []

        for test in self.testList:
            if test.ping.ipOrigin == LOCALHOST:
                localhostTest.append(test.ping)
            else:
                externalIpTest.append(test.ping)

        self.execPingByLocalhost(localhostTest)
        self.execPingByExternalIp(externalIpTest)
