from typing import List

import requests


class ReminderApiProvider(object):
    def __init__(self, service: str):
        self._api_url = f'{service}/api/collections'

    def get_collections(self) -> List[str]:
        return requests.get(self._api_url).json()

    def get_objects(self, collection: str) -> List[str]:
        return requests.get(f'{self._api_url}/{collection}').json()

    def get_object(self, collection: str, key: str) -> dict:
        return requests.get(f'{self._api_url}/{collection}/{key}').json()

    def add_object(self, collection: str, key: str, data: dict):
        requests.post(f'{self._api_url}/{collection}/{key}', json=data)

    def update_object(self, collection: str, key: str, data: dict):
        requests.put(f'{self._api_url}/{collection}/{key}', json=data)

    def delete_object(self, collection: str, key: str):
        requests.delete(f'{self._api_url}/{collection}/{key}')
