import sqlite3

from abc import abstractmethod
from typing import Iterable


class DataStorage(object):
    @abstractmethod
    def get_objects(self) -> Iterable[dict]:
        pass

    @abstractmethod
    def get_object(self, key: str) -> dict:
        pass

    @abstractmethod
    def get_any_object(self,) -> dict:
        pass


class SqliteDataStorage(DataStorage):
    def __init__(self, collection: str):
        self._connection = sqlite3.connect(f'{collection}.db')
        self._cursor = self._connection.cursor()

    def get_objects(self) -> Iterable:
        self._cursor.execute('SELECT * FROM objects')

        for row in self._cursor:
            yield self.__extract_object(row)

    def get_object(self, key: str) -> dict:
        self._cursor.execute('SELECT * FROM objects WHERE key = ?', key)
        return self.__extract_object(self._cursor.fetchone())

    def get_any_object(self) -> dict:
        self._cursor.execute('SELECT * FROM objects ORDER BY RANDOM() LIMIT 1')
        return self.__extract_object(self._cursor.fetchone())

    @staticmethod
    def __extract_object(row):
        return {
            'original': row[0],
            'translation': row[1],
            'transcription': row[2],
        } if row else None
