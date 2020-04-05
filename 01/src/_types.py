# Пустой тип
var = None

# Булев тип
isCat = True
isDog = False

isAnimal = isCat or isDog

# Числа
a = -1
b = 19.0
c = 19 + 12j
print(c.imag, c.real)

d = a + b * 12 / 3
print(d)

# Деление целых чилел
print(9 / 7)
print(9 // 7)
print(9 % 7)

bin_var = 0b101
oct_var = 0o066
hex_var = 0xff

# Строки
string = 'just a string'
print(string)

multi_line_text = 'line_1\nline_2\nline_3'
print(multi_line_text)

raw_string = r'line_1\nline_2\nline_3'
print(raw_string)

# Списки
numbers = [1, 2, 3, 5, 6]
users = ['Alice', 'Bob', 'Carlos']
things = [1, True, 'Text', None, [1, 2, 3]]

numbers += [34, 35, 35]
print(numbers[2])
print(numbers[1:3], numbers[2:-2])

# Кортежи
location = (56.484640, 84.947649, 'Tomsk')
print(location)

latitude, longitude, label = location
assert location[0] == latitude
assert location[1] == longitude
assert location[2] == label

# Словари
location = {
    'latitude': 56.484640,
    'longitude': 84.947649,
    'label': 'Tomsk',
}

print(location)

assert location['latitude'] == 56.484640
assert location['longitude'] == 84.947649
assert location['label'] == 'Tomsk'

location['label'] = 'Tomsk, Russia'
location['population'] = 500_000

print(location)
