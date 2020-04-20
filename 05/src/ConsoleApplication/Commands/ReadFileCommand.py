import os
import sys

from Commands.AbstractCommand import AbstractCommand


class ReadFileCommand(AbstractCommand):
    @property
    def name(self) -> str:
        return 'READ_FILE'

    @property
    def help(self) -> str:
        return 'Print the content of the given file.'

    @property
    def arguments(self) -> list:
        return ['filename']

    def execute(self, options):
        filename = options['filename']

        with open(filename, 'rb') as f:
            sys.stdout.write(f.read(os.stat(filename).st_size).decode())
