import pytest
from character import Character
#from character_updated import Character

class TestCharacter:

    # set_level()

    # Test that set_level() can set level to all values between min and max including
    def test_set_level_range(self):
        c = Character()
        for i in range(Character._MIN_LEVEL, Character._MAX_LEVEL+1):
            c.set_level(i)
            assert c.level == i

    # Test that set_level() cannot set level above max
    def test_set_level_above_max(self):
        c = Character()
        c.set_level(Character._MAX_LEVEL+1)
        assert c.level == Character._MAX_LEVEL

    # Test that set_level() cannot set level below min
    def test_set_level_below_min(self):
        c = Character()
        c.set_level(Character._MIN_LEVEL-1)
        assert c.level == Character._MIN_LEVEL

    # level_up()

    # Test that level_up() works
    def test_level_up(self):
        c = Character()
        c.level_up()
        assert c.level == Character._MIN_LEVEL+1

    # Test that level_up() cannot set level above max
    def test_level_up_above_max(self):
        c = Character()
        for _ in range(Character._MAX_LEVEL - Character._MIN_LEVEL + 1):
            c.level_up()
        assert c.level == Character._MAX_LEVEL

    # contains_profanity()

    # Test that contains_profanity() detects profanity
    def test_contains_profanity(self):
        assert Character.contains_proanity("Damn")

    # Test that contains_profanity() detects profanity when joined with another string
    def test_contains_profanity_join(self):
        assert Character.contains_proanity("DamnMan")

    # Test that contains_profanity() detects profanity with all upper casing
    def test_contains_profanity_all_upper(self):
        assert Character.contains_proanity("ASSHAT")

    # Test that contains_profanity() detects profanity with all upper casing
    def test_contains_profanity_all_lower(self):
        assert Character.contains_proanity("asshat")

    # set_name()

    # Test that set_name() can set a legal name
    def test_set_name_legal(self):
        c = Character()
        new_name = "John Doe"
        assert c.set_name(new_name)
        assert c.name == new_name

    # Test that set_name() cannot set an illegal name
    def test_set_name_illegal(self):
        c = Character()
        original_name = c.name
        new_name = "Asshat Doe"
        assert not c.set_name(new_name)
        assert c.name == original_name

    # Test that set_name() cannot set a name that is a number
    def test_set_name_type_exception(self):
        c = Character()
        with pytest.raises(TypeError):
            c.set_name(100)

if __name__ == "__main__":
    print("Please use the command found in README.md to run pytest")