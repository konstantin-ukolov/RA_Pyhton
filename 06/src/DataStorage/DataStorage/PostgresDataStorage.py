import asyncpg

from typing import AsyncIterable

from DataStorage import DataStorage


class PostgresDataStorage(DataStorage):
    def __init__(self):
        self._connection = None

    async def create(self, options: dict):
        self._connection = await asyncpg.connect(**options)

        await self._connection.execute('''
            CREATE TABLE IF NOT EXISTS objects (
                key TEXT, name TEXT, age INT, city TEXT, job TEXT
            )
        ''')

    async def get_objects(self) -> AsyncIterable:
        async with self._connection.transaction():
            async for row in self._connection.cursor('SELECT * FROM objects'):
                yield self.__extract_object(row)

    async def get_object(self, key: str) -> dict:
        async with self._connection.transaction():
            cursor = await self._connection.cursor('SELECT * FROM objects WHERE key = $1', key)
            return self.__extract_object(await cursor.fetchrow())

    async def put_object(self, key: str, value: dict):
        await self.delete_object(key)

        name = value.get('name', str())
        age = value.get('age', -1)
        city = value.get('city', str())
        job = value.get('job', str())

        async with self._connection.transaction():
            await self._connection.execute(
                'INSERT INTO objects VALUES ($1, $2, $3, $4, $5)',
                key, name, age, city, job,
            )

    async def delete_object(self, key: str):
        async with self._connection.transaction():
            await self._connection.execute('DELETE FROM objects WHERE key = $1', key)

    @staticmethod
    def __extract_object(row):
        return {
            'name': row[1],
            'age': int(row[2]),
            'city': row[3],
            'job': row[4],
        } if row else None
