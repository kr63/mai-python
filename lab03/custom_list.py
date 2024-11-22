import itertools
from typing import List


class CustomList(List):
    def __add__(self, other):
        return CustomList([item1 + item2 for item1, item2 in itertools.zip_longest(self, other, fillvalue=0)])

    def __radd__(self, other):
        return CustomList([item1 + item2 for item1, item2 in itertools.zip_longest(self, other, fillvalue=0)])

    def __sub__(self, other):
        return CustomList([item1 - item2 for item1, item2 in itertools.zip_longest(self, other, fillvalue=0)])

    def __rsub__(self, other):
        return CustomList([item1 - item2 for item2, item1 in itertools.zip_longest(self, other, fillvalue=0)])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return "List: {0}, sum: {1}".format(str(list(self)), sum(self))
