import sqlite3

from typing import AsyncIterable

from DataStorage import DataStorage


class SqliteDataStorage(DataStorage):
    def __init__(self):
        self._connection = None
        self._cursor = None

    async def create(self, filename: str):
        self._connection = sqlite3.connect(filename)
        self._cursor = self._connection.cursor()

        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS objects (
                key TEXT, name TEXT, age INT, city TEXT, job TEXT
            )
        ''')

    async def get_objects(self) -> AsyncIterable:
        self._cursor.execute('SELECT * FROM objects')

        for row in self._cursor:
            yield self.__extract_object(row)

    async def get_object(self, key: str) -> dict:
        self._cursor.execute('SELECT * FROM objects WHERE key = ?', key)
        return self.__extract_object(self._cursor.fetchone())

    async def put_object(self, key: str, value: dict):
        await self.delete_object(key)

        name = value.get('name', str())
        age = value.get('age', -1)
        city = value.get('city', str())
        job = value.get('job', str())

        self._cursor.execute(
            'INSERT INTO objects VALUES (?, ?, ?, ?, ?)',
            (key, name, age, city, job,)
        )

        self._connection.commit()

    async def delete_object(self, key: str):
        self._cursor.execute("DELETE FROM objects WHERE key = ? ", key)
        self._connection.commit()

    @staticmethod
    def __extract_object(row):
        return {
            'name': row[1],
            'age': row[2],
            'city': row[3],
            'job': row[4],
        } if row else None
