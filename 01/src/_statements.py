from datetime import datetime
from random import randrange

is_odd_current_second: bool = datetime.now().second % 2 == 0

if is_odd_current_second:
    print(':)')
else:
    print(':(')

print(':)' if is_odd_current_second else ':(')

value: int = randrange(0, 1000)

if value < 10:
    print('too small!')
elif value < 100:
    print('suitable')
elif value < 500:
    print("too big")
else:
    raise ValueError('prohibitively large number')

while not is_odd_current_second:
    print('once again...')

print("))")

for x in [1, 2, 3, 4, 5]:
    print(x * x)

for x in range(10):
    print(x * x)


for x in [1, 20, 3, 7, 4, 5]:
    if x % 2 == 0:
        print('found an even number in the list')

        if x == 20:
            print('but it is 20')
            continue

        break

    print(x)
else:
    print('all of them are odd')

names = ['Alice', 'Bob', 'Carlos', 'David', 'Eva']
name_sizes = [len(name) for name in names]
print(name_sizes)
print([name.upper() for name in names if len(name) > 3])
