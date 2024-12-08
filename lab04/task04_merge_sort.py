from multiprocessing import Manager
from multiprocessing import Process


def sort(items):
    if len(items) <= 1:
        return items

    middle = int(len(items) / 2)
    left = items[0:middle]
    right = items[middle:]
    left = sort(left)
    right = sort(right)
    return merge(left, right)


def merge(left, right):
    result = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def append_to_shared(shared, items):
    shared.append(sort(items))


def main(input: list, proc_num: int):
    size = max(1, len(input) // proc_num)
    sub_lists = [input[item:item + size] for item in range(0, len(input), size)]

    with Manager() as manager:
        shared = manager.list()
        processes = [Process(target=append_to_shared, args=(shared, item)) for item in sub_lists]

        for p in processes:
            p.start()
            p.join()

        while len(shared) > 1:
            shared.append(merge(shared.pop(0), shared.pop(0)))

        return shared[0]


if __name__ == '__main__':
    input = [3, 14, 15, 9, 2, 6, 5, 35]
    print(main(input, 2))
