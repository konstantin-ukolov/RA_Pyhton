from Commands.AbstractCommand import AbstractCommand
from Commands.EchoCommand import EchoCommand
from Commands.GetProductCommand import GetProductCommand
from Commands.ReadFileCommand import ReadFileCommand


class CommandFactory(object):
    def __init__(self):
        self.commands = [
            EchoCommand(),
            GetProductCommand(),
            ReadFileCommand(),
        ]

    def get_command(self, line: str) -> AbstractCommand:
        for command in self.commands:
            if command.name == line:
                return command
