from typing import List

from DataStorage import DataStorage, DataStorageFactory


class CollectionManager(object):
    def __init__(self, collections: list, storage_settings: dict):
        self._collections = collections
        self._storage_settings = storage_settings
        self._storages = dict()

    def collections(self) -> List[str]:
        return self._collections

    async def data_storage(self, collection: str) -> DataStorage:
        if collection not in self._storages:
            self._storages[collection] = await self.__create_data_storage(collection)

        return self._storages[collection]

    async def __create_data_storage(self, collection: str) -> DataStorage:
        self._storage_settings['collection'] = collection
        return await DataStorageFactory.create_storage(self._storage_settings)
