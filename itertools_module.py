import itertools
import operator
from functools import reduce

# count() ------------------------------
print("-----count()")

c = itertools.count()
print(next(c))  # Output:0
print(next(c))  # Output:1
print(next(c))  # Output:2
print(next(c))  # Output:3
print("*****")

c1 = itertools.count(5, 10)
print(next(c1))  # Output:5
print(next(c1))  # Output:15
print(next(c1))  # Output:25
print("*****")

c2 = itertools.count(2.5, 2.5)
for i in c2:
    if i > 25:
        break
    else:
        print(i, end=" ")  # Output:2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5 25.0

print(" ")
print("*****")

c3 = itertools.count(2, -2.5)
print(next(c3))  # Output:2
print(next(c3))  # Output:-0.5
print(next(c3))  # Output:-3.0

print("*****")

# zip() ------------------------------
print("-----zip()")

l1 = [5, 15, 25]
l2 = zip(itertools.count(), l1)
print(list(l2))  # Output:[(0, 5), (1, 15), (2, 25)]

l3 = zip(itertools.count(), l1)
for i in l3:
    print(i)

print("--" * 20)

# map() ------------------------------
print("-----map()")

l1 = map(lambda x: x ** 2, itertools.count())
for i in l1:
    if i > 50:
        break
    else:
        print(i, end=" ")  # Output: 0 1 4 9 16 25 36 49

print("")
print("--" * 20)

# cycle() ------------------------------
print("-----cycle()")

l1 = [1, 2, 3]
l2 = itertools.cycle(l1)

count = 0
for i in l2:
    if count > 15:
        break
    else:
        print(i, end=" ")  # Output:1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1
        count += 1

s1 = "hello"
l3 = itertools.cycle(s1)
print(next(l3))  # Output:h
print(next(l3))  # Output:e
print(next(l3))  # Output:l
print(next(l3))  # Output:l
print(next(l3))  # Output:o

print("--" * 20)

# repeat() ------------------------------
print("-----repeat()")

l1 = itertools.repeat(2)
print(next(l1))  # Output:2
print(next(l1))  # Output:2

l2 = itertools.repeat("hello", times=10)
for i in l2:
    print(i, end=" ")  # Output:hello hello hello hello hello hello hello hello hello hello
print(" ")

l3 = itertools.repeat([1, 2, 3], times=3)
for i in l3:
    print(i, end=" ")  # Output:[1, 2, 3] [1, 2, 3] [1, 2, 3]
print(" ")

l4 = itertools.repeat(('red', 'blue'), times=3)
for i in l4:
    print(i, end=" ")  # Output:('red', 'blue') ('red', 'blue') ('red', 'blue')

print(" ")
print("--" * 20)

l1 = map(pow, range(10), itertools.repeat(2))

for i in l1:
    print(i, end=" ")  # Output:0 1 4 9 16 25 36 49 64 81

print(" ")
print("--" * 20)

l1 = [5, 15, 25]
l2 = zip(itertools.repeat(2), l1)
print(list(l2))  # Output:[(2, 5), (2, 15), (2, 25)]

l3 = zip(itertools.repeat("hello"), l1)
for i in l3:
    print(i)

print("--" * 20)

# accumulate() ------------------------------
print("-----accumulate()")

l1 = itertools.accumulate([1, 2, 3, 4, 5])
print(list(l1))  # Output:[1, 3, 6, 10, 15]
r1 = reduce(operator.add, [1, 2, 3, 4, 5])
print(r1)  # Output:15

l2 = itertools.accumulate([1, 2, 3, 4, 5], operator.add, initial=10)
print(list(l2))  # Output:[10, 11, 13, 16, 20, 25]

l3 = itertools.accumulate([1, 2, 3, 5, 5], operator.mul)
print(list(l3))  # Output:[1, 2, 6, 30, 150]
r2 = reduce(operator.mul, [1, 2, 3, 4, 5])
print(r2)  # Output:120

l4 = itertools.accumulate([2, 4, 6, 3, 1], max)
print(list(l4))  # Output:[2, 4, 6, 6, 6]
r3 = reduce(max, [2, 4, 6, 3, 1])
print(r3)  # Output:6

l5 = itertools.accumulate([2, 4, 6, 3, 1], min)
print(list(l5))  # Output:[2, 2, 2, 2, 1]
r4 = reduce(min, [2, 4, 6, 3, 1])
print(r4)  # Output:1

print("--" * 20)

# chain() ------------------------------
print("-----chain()")

l1 = itertools.chain(["red", "blue"], [1, 2, 3], "hello")
print(list(l1))  # Output:['red', 'blue', 1, 2, 3, 'h', 'e', 'l', 'l', 'o']

l2 = itertools.chain("ABC", "DEF", "GHI")
print(list(l2))  # Output:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

print("--" * 20)

# chain.from_iterable() ------------------------------
print("-----chain.from_iterable()")

l1 = itertools.chain.from_iterable(["ABC", "DEF", "GHI"])
print(list(l1))  # Output:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

l2 = itertools.chain(["ABC", "DEF", "GHI"])
print(list(l2))  # Output:['ABC', 'DEF', 'GHI']

# l3 = itertools.chain.from_iterable([1, 2, 3])
# print(list(l3))  # Output:TypeError: 'int' object is not iterable

print("--" * 20)

# compress() ------------------------------
print("-----compress()")

selectors = [True, False, True, False]
l1 = itertools.compress([1, 2, 3, 4], selectors)
print(list(l1))  # Output:[1,3]

l2 = filter(lambda x: x % 2 != 0, [1, 2, 3, 4])
print(list(l2))  # Output:[1,3]

print("--" * 20)

# dropwhile() ------------------------------
print("-----dropwhile()")


def predicate(x):
    return x < 5


iterable = [1, 4, 6, 4, 1, 7, 8]
result = itertools.dropwhile(predicate, iterable)
print(list(result))  # Output: [6, 4, 1, 7, 8]

print("--" * 20)

# dropwhile() takewhile() ------------------------------
print("-----dropwhile() takewhile()")

l4 = itertools.takewhile(lambda x: x > 4, [5, 6, 7, 8, 9, 1, 2, 3])
print(list(l4))  # Output:[5, 6, 7, 8, 9]

l2 = itertools.dropwhile(lambda x: x % 2 == 0, [2, 4, 6, 8, 10])
print(list(l2))  # Output:[]
l3 = itertools.takewhile(lambda x: x % 2 == 0, [2, 4, 6, 8, 10])
print(list(l3))  # Output:[2, 4, 6, 8, 10]

print("--" * 20)

# filterfalse() ------------------------------
print("-----filterfalse()")

l1 = itertools.filterfalse(lambda x: x > 4, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(l1))  # Output:[1, 2, 3,4]
l4 = filter(lambda x: x > 4, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(l4))  # Output:[5, 6, 7, 8, 9]

l5 = itertools.filterfalse(None, [0, 1, 2, 3, 4, 5])
print(list(l5))  # Output:[0]
l6 = filter(None, [0, 1, 2, 3, 4])
print(list(l6))  # Output:[1, 2, 3, 4]

print("--" * 20)

# zip_longest() ------------------------------
print("-----zip_longest()")

z1 = itertools.zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'])
print(list(z1))  # Output:[(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

z2 = itertools.zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fillvalue="z")
print(list(z2))  # Output:[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'z'), (5, 'z')]

z3 = zip([1, 2, 3, 4, 5], ['a', 'b', 'c'])
print(list(z3))  # Output:[(1, 'a'), (2, 'b'), (3, 'c')]

print("--" * 20)

# starmap() ------------------------------
print("-----starmap()")

l1 = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(l1))  # Output:[0, 1, 4]

l2 = map(pow, [0, 1, 2], [2, 2, 2])
print(list(l2))  # Output:[0, 1, 4]

a1 = map(lambda x: x ** 2, [1, 2, 3])
print(list(a1))  # Output:[1, 4, 9]

# a2 = itertools.starmap(lambda x: x ** 2, [1, 2, 3])
# print(list(a2))  # Output:TypeError: 'int' object is not iterable

a3 = itertools.starmap(lambda x, y: x + y, [(0, 1), (1, 2), (2, 3)])
print(list(a3))  # Output:[1, 3, 5]

print("--" * 20)

# islice() ------------------------------
print("-----islice()")

l1 = itertools.islice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(list(l1))  # Output:[1, 2, 3, 4, 5]

l2 = itertools.islice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 5)
print(list(l2))  # Output:[3,4,5]

l3 = itertools.islice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, None, 3)
print(list(l3))  # Output:[3,6,9]

# l4 = itertools.islice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, None, -2)
# print(list(l4))  # Output:ValueError: Step for islice() must be a positive integer or None.

print("--" * 20)

# tee() ------------------------------
print("-----tee()")

l1 = [1, 2, 3, 4, 5]
l2 = itertools.tee(l1, 3)
for i in l2:
    print(list(i))

print("--" * 20)

# groupby() ------------------------------
print("-----groupby()")

l1 = [('color', 'red'), ('color', 'blue'), ('color', 'green'), ('Numbers', 1), ('Numbers', 5)]
l2 = itertools.groupby(l1, key=lambda x: x[0])
for key, group in l2:
    result = {key: list(group)}
    print(result)

print("*****")

l1 = [('color', 'red'), ('color', 'blue'), ('color', 'green'), ('Numbers', 1), ('Numbers', 5), ('color', 'purple')]
l2 = itertools.groupby(l1, key=lambda x: x[0])
for key, group in l2:
    result = {key: list(group)}
    print(result)

print("*****")

l1 = [('color', 'red'), ('color', 'blue'), ('color', 'green'), ('Numbers', 1), ('Numbers', 5), ('color', 'purple')]
l2 = itertools.groupby(l1)
for key, group in l2:
    result = {key: list(group)}
    print(result)

print("--" * 20)

# product() ------------------------------
print("-----product()")

l1 = itertools.product("ABCD")
print(list(l1))  # Output:[('A',), ('B',), ('C',), ('D',)]

l2 = itertools.product("ABC", [1, 2])
print(list(l2))  # Output:[('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]

l3 = itertools.product("xy", repeat=2)
print(list(l3))  # Output:[('x', 'x'), ('x', 'y'), ('y', 'x'), ('y', 'y')]

l4 = itertools.product("aa", repeat=2)
print(list(l4))  # Output:[('a', 'a'), ('a', 'a'), ('a', 'a'), ('a', 'a')]

l5 = itertools.product([1, 2], [3, 4], [5, 6])
print(list(l5))  # Output:[(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]

print("--" * 20)

# permutations() ------------------------------
print("-----permutations()")

l1 = itertools.permutations("ABC")
print(list(l1))
# Output:[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'),
# ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

l2 = itertools.permutations([3, 2, 1])
print(list(l2))  # Output:[(3, 2, 1), (3, 1, 2), (2, 3, 1), (2, 1, 3), (1, 3, 2), (1, 2, 3)]

l3 = itertools.permutations([1, 1])
print(list(l3))  # Output:[(1, 1), (1, 1)]

l4 = itertools.permutations(["ABC"])
print(list(l4))  # Output:[('ABC',)]

l5 = itertools.permutations([1, 2, 3, 4], 2)
print(list(l5))
# Output:[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3),
# (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

print("--" * 20)

# combinations() combinations_with_replacement() ------------------------------
print("-----combinations() combinations_with_replacement()")

l1 = itertools.combinations("ABC", 2)
print(list(l1))  # Output:[('A', 'B'), ('A', 'C'), ('B', 'C')]
l1 = itertools.combinations_with_replacement("ABC", 2)
print(list(l1))  # Output:[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

l2 = itertools.combinations([3, 2, 1], 3)
print(list(l2))  # Output:[(3, 2, 1)]
l2 = itertools.combinations_with_replacement([3, 2, 1], 3)
print(list(l2))
# Output:[(3, 3, 3), (3, 3, 2), (3, 3, 1), (3, 2, 2), (3, 2, 1),
# (3, 1, 1), (2, 2, 2), (2, 2, 1), (2, 1, 1), (1, 1, 1)]

l3 = itertools.combinations([1, 1], 2)
print(list(l3))  # Output:[(1, 1)]
l3 = itertools.combinations_with_replacement([1, 1], 2)
print(list(l3))  # Output:[(1, 1), (1, 1), (1, 1)]

l4 = itertools.combinations(["ABC"], 2)
print(list(l4))  # Output:[]
l4 = itertools.combinations_with_replacement(["ABC"], 2)
print(list(l4))  # Output:[('ABC', 'ABC')]

# l5 = itertools.combinations([1, 2, 3, 4])
# print(list(l5))  # Output:TypeError: combinations() missing required argument 'r' (pos 2)
# l5 = itertools.combinations_with_replacement([1, 2, 3, 4])
# print(list(l5))  # Output:TypeError: combinations_with_replacement() missing required argument 'r' (pos 2)
