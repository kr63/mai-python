from unittest import TestCase

from lab03.custom_meta import CustomClass


class TestCustomClass(TestCase):

    def test01(self):
        custom = CustomClass()
        assert CustomClass.custom_x == 50
        with self.assertRaises(AttributeError):
            custom.x

    def test02(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(str(inst), "Custom_by_metaclass")
        with self.assertRaises(AttributeError):
            inst.x
            inst.val
            inst.line()
            inst.yyy

    def test03(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            inst.dynamic
