from pipe import chain
from pipe import dedup
from pipe import groupby
from pipe import select, where
from pipe import traverse

arr = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, arr))))

# -------------------------------------
print("--" * 20)

arr = [1, 2, 3, 4, 5]
print(list(arr
           | where(lambda x: x % 2 == 0)
           | select(lambda x: x * 2)))

# -------------------------------------
print("--" * 20)

nested = [[1, 2, [3]], [4, 5]]
print(list(nested | chain))

# -------------------------------------
print("--" * 20)

nested = [[1, 2, [3]], [4, 5]]
print(list(nested | traverse))

# -------------------------------------
print("--" * 20)

fruits = [
    {"name": "apple", "price": [20, 50]},
    {"name": "orange", "price": 40},
    {"name": "grapefruit", "price": 50},
]

print(list(fruits
           | select(lambda fruit: fruit["price"])
           | traverse))

# -------------------------------------
print("--" * 20)

arr = [1, 2, 3, 4, 5]

print(list(arr
           | groupby(lambda x: "Even" if x % 2 == 0 else "Odd")
           | select(lambda x: {x[0]: list(x[1])})))

# -------------------------------------
print("--" * 20)

print(list(arr
           | groupby(lambda x: "Even" if x % 2 == 0 else "Odd")
           | select(lambda x: {x[0]: list(x[1] | where(lambda x: x > 2))})))

# -------------------------------------
print("--" * 20)

arr = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 9]
print(list(arr | dedup))

# -------------------------------------
print("--" * 20)

print(list(arr | dedup(lambda key: key < 5)))

# -------------------------------------
print("--" * 20)


def step1(data):
    return data + 1


def step2(data):
    return data * 2


def step3(data):
    return data - 3


def pipeline(data):
    return step3(step2(step1(data)))


print(pipeline(5))

# -------------------------------------
print("--" * 20)
