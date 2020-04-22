import uuid

from typing import AsyncIterable

from DataStorage.DataStorage import DataStorage


class MemoryDataStorage(DataStorage):
    def __init__(self):
        self._storage = dict()

    async def get_objects(self) -> AsyncIterable:
        for value in self._storage.values():
            yield value

    async def get_object(self, key: uuid) -> dict:
        return self._storage.get(key)

    async def put_object(self, key: uuid, value: dict):
        self._storage[key] = value

    async def delete_object(self, key: uuid):
        self._storage.pop(key)
