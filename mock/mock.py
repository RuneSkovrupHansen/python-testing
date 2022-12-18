#!/bin/python3

import unittest
from unittest.mock import MagicMock, Mock

class DummyClass:

    def __init__(self) -> None:
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0

    def m1(self) -> bool:
        return True

    def m2(self) -> bool:
        return True

    def m3(self) -> bool:
        return True

    def call_all_methods(self) -> None:
        self.m1()
        self.m2()
        self.m3()

    def call_m2_twice(self) -> None:
        self.m2()

class TestDummyClass(unittest.TestCase):

    def test_m1_mock(self):

        # Initialize mock spec of the actual method to retain calls
        dc = DummyClass()
        dc.m1 = Mock(spec=dc.m1)

        m1_return = dc.m1()
        dc.call_all_methods()

        self.assertTrue(m1_return)
        self.assertAlmostEqual(dc.m1.call_count, 2)

    def test_m1_magic_mock(self):

        dc = DummyClass()
        dc.m1 = MagicMock(return_value=True)

        m1_return = dc.m1()
        dc.call_all_methods()

        self.assertTrue(m1_return)
        self.assertAlmostEqual(dc.m1.call_count, 2)

def main():

    unittest.main()

    return
    
    dc = DummyClass()
    dc.m1 = MagicMock()


if __name__ == "__main__":
    main()