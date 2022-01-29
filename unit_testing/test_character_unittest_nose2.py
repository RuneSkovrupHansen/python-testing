#!/bin/python3
import unittest
from character import Character
#from character_updated import Character

class TestCharacter(unittest.TestCase):

    # set_level()

    # Test that set_level() can set level to all values between min and max including
    def test_set_level_range(self):
        c = Character()
        for i in range(Character._MIN_LEVEL, Character._MAX_LEVEL+1):
            c.set_level(i)
            self.assertEqual(c.level, i)

    # Test that set_level() cannot set level above max
    def test_set_level_above_max(self):
        c = Character()
        c.set_level(Character._MAX_LEVEL+1)
        self.assertEqual(c.level, Character._MAX_LEVEL)

    # Test that set_level() cannot set level below min
    def test_set_level_below_min(self):
        c = Character()
        c.set_level(Character._MIN_LEVEL-1)
        self.assertEqual(c.level, Character._MIN_LEVEL)

    # level_up()

    # Test that level_up() works
    def test_level_up(self):
        c = Character()
        c.level_up()
        self.assertEqual(c.level, Character._MIN_LEVEL+1)

    # Test that level_up() cannot set level above max
    def test_level_up_above_max(self):
        c = Character()
        for _ in range(Character._MAX_LEVEL - Character._MIN_LEVEL + 1):
            c.level_up()
        self.assertEqual(c.level, Character._MAX_LEVEL)

    # contains_profanity()

    # Test that contains_profanity() detects profanity
    def test_contains_profanity(self):
        self.assertTrue(Character.contains_proanity("Damn"))

    # Test that contains_profanity() detects profanity when joined with another string
    def test_contains_profanity_join(self):
        self.assertTrue(Character.contains_proanity("DamnMan"))

    # Test that contains_profanity() detects profanity with all upper casing
    def test_contains_profanity_all_upper(self):
        self.assertTrue(Character.contains_proanity("ASSHAT"))

    # Test that contains_profanity() detects profanity with all upper casing
    def test_contains_profanity_all_lower(self):
        self.assertTrue(Character.contains_proanity("asshat"))

    # set_name()

    # Test that set_name() can set a legal name
    def test_set_name_legal(self):
        c = Character()
        new_name = "John Doe"
        self.assertTrue(c.set_name(new_name))
        self.assertEqual(c.name, new_name)

    # Test that set_name() cannot set an illegal name
    def test_set_name_illegal(self):
        c = Character()
        original_name = c.name
        new_name = "Asshat Doe"
        self.assertFalse(c.set_name(new_name))
        self.assertEqual(c.name, original_name)

    # Test that set_name() cannot set a name that is a number
    def test_set_name_type_exception(self):
        c = Character()
        with self.assertRaises(TypeError):
            c.set_name(100)

if __name__ == "__main__":
    unittest.main()
