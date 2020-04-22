import uuid

from typing import AsyncIterable

import asyncpg

from DataStorage import DataStorage


class PostgresDataStorage(DataStorage):
    def __init__(self):
        self._collection = str()
        self._connection = None

    async def create(self, options: dict, collection: str):
        self._collection = collection
        self._connection = await asyncpg.connect(**options)

        await self._connection.execute(f'''
            CREATE TABLE IF NOT EXISTS {self._collection} (
                key UUID, original TEXT, translation TEXT, transcription TEXT
            )
        ''')

    async def get_objects(self) -> AsyncIterable:
        async with self._connection.transaction():
            async for row in self._connection.cursor(f'SELECT * FROM {self._collection}'):
                yield self.__extract_object(row)

    async def get_object(self, key: uuid) -> dict:
        async with self._connection.transaction():
            cursor = await self._connection.cursor(
                f'SELECT * FROM {self._collection} WHERE key = $1', key
            )

            return self.__extract_object(await cursor.fetchrow())

    async def put_object(self, key: uuid, value: dict):
        await self.delete_object(key)

        original = value.get('original', str())
        translation = value.get('translation', str())
        transcription = value.get('transcription', str())

        async with self._connection.transaction():
            await self._connection.execute(
                f'INSERT INTO {self._collection} VALUES ($1, $2, $3, $4)',
                key, original, translation, transcription,
            )

    async def delete_object(self, key: uuid):
        async with self._connection.transaction():
            await self._connection.execute(
                f'DELETE FROM {self._collection} WHERE key = $1', key
            )

    @staticmethod
    def __extract_object(row):
        return {
            'key': row[1],
            'original': row[1],
            'translation': row[2],
            'transcription': row[3],
        } if row else None
