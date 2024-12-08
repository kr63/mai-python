import threading


def numbers(start, end, step):
    for item in range(start, end, step):
        print(item, end=' ')


if __name__ == "__main__":
    threads = dict()
    threads['even'] = threading.Thread(target=numbers, args=(30, 52, 2))
    threads['odd']  = threading.Thread(target=numbers, args=(31, 51, 2))

    for key, value in threads.items():
        print('\nList of {} numbers:'.format(key))
        value.start()
        value.join()
