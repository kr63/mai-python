from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from lab03.custom_list import CustomList


class TestCustomList(TestCase):

    def test01(self):
        """CustomList + CustomList"""
        self.assertEqual(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), CustomList([6, 3, 10, 7]))

    def test02(self):
        """CustomList + List"""
        self.assertEqual(CustomList([1]) + [2, 5], CustomList([3, 5]))

    def test03(self):
        """List + CustomList"""
        self.assertEqual([2, 5] + CustomList([1]), CustomList([3, 5]))

    def test04(self):
        """CustomList - CustomList"""
        self.assertEqual(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), CustomList([4, -1, -4, 7]))

    def test05(self):
        """CustomList - List"""
        self.assertEqual(CustomList([1]) - [2, 5], CustomList([-1, -5]))

    def test06(self):
        """List - CustomList"""
        self.assertEqual([2, 5] - CustomList([1]), CustomList([1, 5]))

    def test07(self):
        """CustomList == CustomList"""
        self.assertTrue(CustomList([2]) == CustomList([1, 1]))

    def test08(self):
        """CustomList != CustomList"""
        self.assertTrue(CustomList([1]) != CustomList([1, 1]))

    def test09(self):
        """CustomList > CustomList"""
        self.assertTrue(CustomList([1]) > CustomList([0, 0]))

    def test10(self):
        """CustomList >= CustomList"""
        self.assertTrue(CustomList([1]) >= CustomList([0, 0]))

    def test11(self):
        """CustomList > CustomList"""
        self.assertTrue(CustomList([0]) < CustomList([1, 0]))

    def test12(self):
        """CustomList <= CustomList"""
        self.assertTrue(CustomList([0]) <= CustomList([1, 0]))

    def test13(self):
        """CustomList __str__"""
        with patch('sys.stdout', new=StringIO()) as out:
            print(CustomList([1, 2, 3]))
            self.assertEqual(out.getvalue().strip(), "List: [1, 2, 3], sum: 6")
