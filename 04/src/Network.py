import asyncio
import os
import re

from abc import abstractmethod
from asyncio.streams import StreamReader, StreamWriter


class AbstractCommand(object):
    def __init__(self, reader, writer):
        self._reader: StreamReader = reader
        self._writer: StreamWriter = writer

    @abstractmethod
    async def execute(self):
        pass

    async def _readline(self):
        return (await self._reader.readline()).decode().strip()

    def _writeline(self, line: str):
        self._writer.write((line + '\n').encode())


class EchoCommand(AbstractCommand):
    async def execute(self):
        while True:
            message = await self._readline()

            if message == 'ECHO_STOP':
                break

            self._writeline(message)


class GetProductCommand(AbstractCommand):
    async def execute(self):
        match = re.search(r'^(\d+) (\d+)$', await self._readline())

        if match:
            self._writeline(f'{int(match.group(1)) * int(match.group(2))}')
        else:
            self._writeline('Invalid params')


class ReadFileCommand(AbstractCommand):
    async def execute(self):
        filename = await self._readline()

        with open(filename, 'rb') as f:
            self._writer.write(f.read(os.stat(filename).st_size))


class CommandFactory(object):
    class __UnknownCommand(AbstractCommand):
        async def execute(self):
            self._writeline('Error: "Unknown command"')

    _commands = {
        'ECHO_START': EchoCommand,
        'GET_PRODUCT': GetProductCommand,
        'READ_FILE': ReadFileCommand,
    }

    def __init__(self, reader, writer):
        self.__reader: StreamReader = reader
        self.__writer: StreamWriter = writer

    def get_command(self, command) -> AbstractCommand:
        return self._commands.get(command, self.__UnknownCommand)(
            self.__reader, self.__writer
        )


async def process(reader: StreamReader, writer: StreamWriter):
    host, port = writer.transport.get_extra_info('peername')
    print(f'Connected to: {host}:{port}')

    factory = CommandFactory(reader, writer)

    try:
        while True:
            line = (await reader.readline()).decode().strip()
            command = factory.get_command(line)
            await command.execute()
    except ConnectionResetError:
        writer.close()
        print(f'Disconnected from {host}:{port}')


async def main():
    server = await asyncio.start_server(process, 'localhost', 3333)

    async with server:
        await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
