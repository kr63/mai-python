from unittest import TestCase

from lab03.descriptor import Data


class TestData(TestCase):

    def test01(self):
        """Test integer"""
        with self.assertRaises(TypeError):
            Data(1.1, 'name', 1)

    def test02(self):
        """Test name"""
        with self.assertRaises(TypeError):
            Data(1, 'name123', 1)

    def test03(self):
        """Test price"""
        with self.assertRaises(TypeError):
            Data(1, 'Name', -1)
            Data(1, 'Name', 1.0)
