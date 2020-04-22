from abc import abstractmethod
from typing import AsyncIterable


class DataStorage(object):
    @abstractmethod
    def get_objects(self) -> AsyncIterable:
        raise NotImplementedError

    async def create(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_object(self, key: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def put_object(self, key: str, value: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_object(self, key: str):
        raise NotImplementedError
