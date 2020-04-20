import sys

from Commands.AbstractCommand import AbstractCommand


class EchoCommand(AbstractCommand):
    @property
    def name(self):
        return 'ECHO_START'

    @property
    def help(self) -> str:
        return 'Starts an echo loop.'

    @property
    def arguments(self) -> list:
        return list()

    def execute(self, options: dict):
        while True:
            message = sys.stdin.readline()

            if message.strip() == 'ECHO_STOP':
                break

            sys.stdout.write(message)
