from typing import AsyncIterable

from motor.motor_asyncio import AsyncIOMotorClient

from DataStorage import DataStorage


class MongoDataStorage(DataStorage):
    def __init__(self):
        self._client = AsyncIOMotorClient()
        self._collection = None

    async def create(self, database: str, collection: str):
        self._collection = self._client[database][collection]

    async def get_objects(self) -> AsyncIterable:
        async for value in self._collection.find():
            yield self.__pure_value(value)

    async def get_object(self, key: str) -> dict:
        return self.__pure_value(await self._collection.find_one({'_id': key}))

    async def put_object(self, key: str, value: dict):
        value['_id'] = key

        await self._collection.find_one_and_replace(
            {'_id': key}, value, upsert=True
        )

    async def delete_object(self, key: str):
        await self._collection.delete_one({'_id': key})

    @staticmethod
    def __pure_value(value: dict):
        if value:
            value.pop('_id')

        return value
