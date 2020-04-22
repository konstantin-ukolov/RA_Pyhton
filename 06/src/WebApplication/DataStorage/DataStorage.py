import uuid

from abc import abstractmethod
from typing import AsyncIterable


class DataStorage(object):
    async def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_objects(self) -> AsyncIterable:
        raise NotImplementedError

    @abstractmethod
    async def get_object(self, key: uuid) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def put_object(self, key: uuid, value: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_object(self, key: uuid):
        raise NotImplementedError

    async def contains(self, key: uuid) -> bool:
        return bool(await self.get_object(key))
