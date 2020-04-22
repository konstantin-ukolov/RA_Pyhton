import sqlite3
import uuid

from typing import AsyncIterable

from DataStorage import DataStorage


class SqliteDataStorage(DataStorage):
    def __init__(self):
        self._collection = str()
        self._connection = None
        self._cursor = None

    async def create(self, filename: str, collection: str):
        self._collection = collection
        self._connection = sqlite3.connect(filename)
        self._cursor = self._connection.cursor()

        self._cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self._collection} (
                key TEXT, original TEXT, translation TEXT, transcription TEXT
            )
        ''')

    async def get_objects(self) -> AsyncIterable:
        self._cursor.execute(f'SELECT * FROM {self._collection}')

        for row in self._cursor:
            yield self.__extract_object(row)

    async def get_object(self, key: uuid) -> dict:
        self._cursor.execute(f'SELECT * FROM {self._collection} WHERE key = ?', (str(key),))
        return self.__extract_object(self._cursor.fetchone())

    async def put_object(self, key: uuid, value: dict):
        await self.delete_object(key)

        original = value.get('original', str())
        translation = value.get('translation', str())
        transcription = value.get('transcription', str())

        self._cursor.execute(
            f'INSERT INTO {self._collection} VALUES (?, ?, ?, ?)',
            (str(key), original, translation, transcription,)
        )

        self._connection.commit()

    async def delete_object(self, key: uuid):
        self._cursor.execute(f'DELETE FROM {self._collection} WHERE key = ?', (str(key),))
        self._connection.commit()

    @staticmethod
    def __extract_object(row):
        return {
            'key': row[0],
            'original': row[1],
            'translation': row[2],
            'transcription': row[3],
        } if row else None
