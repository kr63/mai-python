import multiprocessing
from multiprocessing import Process


def sum(connection):
    result = 0
    while connection.poll():
        result += connection.recv()
    print(result)


def square(items, connection):
    for item in items:
        connection.send(item * item)
    connection.close()


if __name__ == "__main__":
    numbers = [item for item in range(1, 11)]
    parent, child = multiprocessing.Pipe()
    p_square = Process(target=square, args=(numbers, child))
    p_square.start()
    p_square.join()
    p_sum = Process(target=sum, args=(parent,))
    p_sum.start()
    p_sum.join()
