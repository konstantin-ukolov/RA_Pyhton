from Commands.AbstractCommand import AbstractCommand
from Commands.CommandFactory import CommandFactory


if __name__ == '__main__':
    factory = CommandFactory()

    while True:
        line = input('==> ')
        command: AbstractCommand = factory.get_command(line)
        command.execute()
