from time import sleep

queue = []


def counter():
    counter1 = 0
    while True:
        print(counter1)
        counter1 += 1
        yield


def printer():
    counter2 = 0
    while True:
        if counter2 % 3 == 0:
            print('Bang!')
        counter2 += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(1)


if __name__ == '__main__':
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
