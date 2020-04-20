import asyncio

from dataclasses import dataclass

from ApplicationSettings import application_settings
from DataStorage import SqliteDataStorage
from Desktop import Desktop


@dataclass
class Notification:
    original: str
    translation: str
    transcription: str

    def __init__(self, notification: dict):
        self.original = notification['original']
        self.translation = notification['translation']
        self.transcription = notification['transcription']


class DefaultNotifier(object):
    def send_notification(self, notification: Notification):
        pass


class StdOutputNotifier(DefaultNotifier):
    def send_notification(self, notification: Notification):
        print(notification)


class DesktopNotifier(DefaultNotifier):
    def send_notification(self, notification: Notification):
        Desktop.send_notification(
            notification.original,
            f'{notification.translation} {notification.transcription}'
        )


async def main():
    notifiers = {
        'stdout': StdOutputNotifier,
        'desktop': DesktopNotifier,
    }

    notifier = notifiers.get(application_settings.notifier, DefaultNotifier)()
    storage = SqliteDataStorage(application_settings.collection)

    while True:
        await asyncio.sleep(application_settings.timeout)
        notifier.send_notification(Notification(storage.get_any_object()))

if __name__ == '__main__':
    asyncio.run(main())
