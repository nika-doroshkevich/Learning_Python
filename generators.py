squares = (e ** 2 for e in range(0, 11, 2))
print(list(squares))

# -------------------------------------
print("--" * 20)


def squares2():
    print("Generator working ...")
    for e in range(0, 11, 2):
        yield e ** 2


gen = squares2()

print(next(gen))
print(next(gen))

for i in gen:
    print(i)
print("=" * 20)
for i in gen:
    print(i)

# -------------------------------------
print("--" * 20)


def pause():
    print("Generator working ...")
    while True:
        print(a)
        yield a


a = 10
gen = pause()
print(gen)
print(next(gen))
a = 20
print(next(gen))

# -------------------------------------
print("--" * 20)


def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("points.csv"):
    print(line)

# -------------------------------------
print("--" * 20)


def f_gen():
    n = 1
    while True:
        yield n ** 2
        n += 1


generator1 = f_gen()
generator2 = f_gen()

for i in generator1:
    print(i)
    if i > 10:
        generator1.close()

# for i in generator2:
#     print(i)
#     if i > 20:
#         generator2.throw(Exception("Плохо!"))


# -------------------------------------
print("--" * 20)


def generator(x):
    while True:
        x = yield x + 1


g = generator(5)
print(g.send(None))
print(g.send(10))
print(g.send(15))
print(g.send(4))

# -------------------------------------
print("--" * 20)


def number_stream():
    num = 0
    while True:
        yield num
        num += 1


def filter_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


even_numbers = filter_even_numbers(number_stream())

for i in range(10):
    print(next(even_numbers))

# -------------------------------------
print("--" * 20)


def generate_numbers():
    for i in range(10):
        yield i


def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


def square_numbers(numbers):
    for num in numbers:
        yield num ** 2


numbers = generate_numbers()
even_numbers = filter_even(numbers)
squared_numbers = square_numbers(even_numbers)

for num in squared_numbers:
    print(num)

# -------------------------------------
print("--" * 20)


def test():
    yield from [1, 2, 3]


for i in test():
    print(i)

# -------------------------------------
print("--" * 20)


def test2():
    yield from [x for x in range(7)]


for i in test2():
    print(i)

# -------------------------------------
print("--" * 20)


def subgen():
    yield "subgen 1"
    yield "subgen 2"


def delegator():
    yield "before subgen"
    yield from subgen()
    yield "after subgen"


for value in delegator():
    print(value)

# -------------------------------------
print("--" * 20)


def subgen():
    yield 1
    yield 2
    return "subgen result"


def delegator():
    result = yield from subgen()
    print("subgen returned:", result)


for _ in delegator():
    pass

# -------------------------------------
print("--" * 20)


def generator_in_expression():
    result = (yield 1) + 2
    yield result


gen = generator_in_expression()
print(next(gen))
print(gen.send(3))

# -------------------------------------
print("--" * 20)
