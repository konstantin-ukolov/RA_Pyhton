import asyncio

from DataStorage import DataStorage, DataStorageFactory


async def main():
    settings = {
        'storage': 'postgres',
        'connection': {
            'host': 'localhost',
            'port': 5432,
            'user': 'postgres',
            'password': 'password',
            'database': 'testdb',
        }
    }

    storage: DataStorage = await DataStorageFactory.create_storage(settings)

    await storage.put_object('1', {
        'name': 'Alice',
        'age': 25,
        'city': 'Tomsk'
    })

    await storage.put_object('2', {
        'name': 'Bob',
        'age': 34,
        'city': 'Moscow',
        'job': 'python developer'
    })

    await storage.put_object('3', {
        'name': 'Carlos',
        'age': 19,
        'city': 'Ufa',
    })

    async for person in storage.get_objects():
        print(person)

    print()
    print(await storage.get_object('2'))
    await storage.delete_object('2')
    print(await storage.get_object('2'))


if __name__ == '__main__':
    asyncio.run(main())
