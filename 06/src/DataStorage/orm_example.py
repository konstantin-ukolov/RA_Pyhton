from peewee import *

db = SqliteDatabase('person.db')


class Person(Model):
    name = CharField(unique=True)
    age = IntegerField()
    city = CharField()
    job = CharField(null=True)

    class Meta:
        database = db


def __print_person(_person: Person):
    print(f'{_person.name}, {_person.age}, {_person.city}, {_person.job}')


if __name__ == '__main__':
    Person.create_table()

    try:
        Person.create(name='Alice', age=25, city='Tomsk')
        Person.create(name='Bob', age=34, city='Moscow', job='python developer')
        Person.create(name='Carlos', age=19, city='Ufa')
    except IntegrityError:
        pass

    print('all')

    for person in Person.select():
        __print_person(person)

    print()
    print('unemployed')

    for person in Person.select().where(Person.job == str()):
        __print_person(person)

    bob = Person.select().where(Person.name == 'Bob').get()
    __print_person(bob)

    bob.job = 'Java developer'
    bob.save()
    __print_person(bob)

    Person.delete().where(Person.age < 20)
