import argparse

from Commands.CommandFactory import AbstractCommand
from Commands.CommandFactory import CommandFactory


if __name__ == '__main__':
    factory = CommandFactory()

    parser = argparse.ArgumentParser(
        description='Console app with sub-commands.'
    )

    subparsers = parser.add_subparsers(title='commands', dest='command')

    for command in factory.commands:
        command_parser = subparsers.add_parser(command.name, help=command.help)

        for argument in command.arguments:
            command_parser.add_argument(argument)

    options = vars(parser.parse_args())

    command: AbstractCommand = factory.get_command(options['command'])
    command.execute(options)
