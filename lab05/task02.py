import time
import weakref


class MyClass:
    def __init__(self, atr):
        self.atr = atr


class MyClassWithAttributes:
    def __init__(self, atr1: MyClass, atr2: MyClass):
        self.atr1 = atr1
        self.atr2 = atr2


class MyClassWithSlots:
    __slots__ = ("atr1", "atr2")


class MyClassWithWeakRef:
    def __init__(self, atr1: MyClass, atr2: MyClass):
        self.atr1 = weakref.ref(atr1)
        self.atr2 = weakref.ref(atr2)


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        return res, time.time() - start_time

    return wrapped


@time_of_function
def create_clazz(clazz_, atr1, atr2, count_):
    # if clazz_ == MyClassWithAttributes:
    #     return [(clazz_(atr1, atr2)) for _ in range(count_)]
    if clazz_ == MyClassWithSlots:
        result = list()
        for _ in range(count_):
            obj = MyClassWithSlots()
            obj.atr1 = atr1
            obj.atr2 = atr2
            result.append(obj)
        return result
    return [(clazz_(atr1, atr2)) for _ in range(count_)]

@time_of_function
def update_list(list_):
    for item in list_:
        item.atr1 = MyClass(42)
        item.atr2 = MyClass(42)
    return list_


if __name__ == "__main__":
    count = 1_000_000
    val1 = MyClass('42')
    val2 = MyClass('42')

    clazz, clazz_time = create_clazz(MyClassWithAttributes, val1, val2, count)
    print(f'Time to create class with attributes: {clazz_time:.4f}')
    slots, slots_time = create_clazz(MyClassWithSlots, val1, val2, count)
    print(f'Time to create class with slots: {slots_time:.4f}')
    weak_refs, weak_time = create_clazz(MyClassWithWeakRef, val1, val2, count)
    print(f'Time to create class with weak refs: {weak_time:.4f}')


    clazz_update, clazz_time_update = update_list(clazz)
    print(f'Time to update list of classes with attributes: {clazz_time_update:.4f}')
    slots_update, slots_time_update= update_list(slots)
    print(f'Time to update list of classes with slots: {slots_time_update:.4f}')
    weak_update, weak_time_update= update_list(weak_refs)
    print(f'Time to update list of classes with weak refs: {weak_time_update:.4f}')

