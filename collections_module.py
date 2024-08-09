import csv
from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple

# OrderedDict нужен для действий со словарем, где необходим порядок элементов, например,
# сравнение с учетом порядка, перестановки элементов с сохранением порядка. Платим памятью,
# занимает в 2 раза больше места, чем обычный.

first = {1: 1, 2: 2}
second = {2: 2, 1: 1}

ordered1 = OrderedDict(first)
ordered2 = OrderedDict(second)

print(first == second)
print(ordered1 == ordered2)

print(first.popitem())
print(ordered1.popitem(last=False))

third = {1: 1, 2: 2, 3: 3}
ordered3 = OrderedDict(third)
ordered3.move_to_end(1)
ordered3.move_to_end(3, last=False)
print(ordered3)

# ---------------------------------

# ChainMap нужен для логического объединения словарей для поиска информации,
# но при изменениях меняется первый словарь

first1 = {1: 1, 2: 2, 3: 3}
second1 = {4: 4, 5: 5}

chain = ChainMap(first1, second1)

print(chain)
first1[1] = 100
print(chain)
print(1 in chain)

chain[1] = 200
print(chain)
chain[5] = 200
print(chain)

# ---------------------------------

# Counter нужен для подсчета элементов в последовательности, работатет только
# c hashable

counter = Counter('hello')
print(counter)
counter.update('world')
print(counter.most_common(1))

# ---------------------------------

# defaultdict нужен для создания словаря со значением по умолчанию. Значение подставляется
# при обращении к несуществующему ключу

a_dict = defaultdict(int)
for char in 'hello':
    a_dict[char] += 1

print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))
print(a_dict['dsghsgdhhj'])
print('1' in a_dict)

b_dict = defaultdict(list)
for char in 'hello':
    b_dict[char].append(char)

print(b_dict)

# ---------------------------------

# deque потокобезопасная, быстро оперирует с обеими сторонами

a_deque = deque()
a_deque.append(1)
print(a_deque)
a_deque.appendleft(2)
print(a_deque)

a_deque.pop()
a_deque.popleft()

a_deque = deque([1, 2, 3], maxlen=3)
print(a_deque)
a_deque.append(4)
print(a_deque)

# ---------------------------------

# namedtuple нужен для создания структуры данных, нечто среднее между
# стандартными типами и самописным классом. Неизменяемый, позволяет обращаться
# по имени атрибута, позволяет использовать индексы.

Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)
print(tom[0])
print(tom.name)
print(tom.age)

Point = namedtuple('Point', 'x y')
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)
