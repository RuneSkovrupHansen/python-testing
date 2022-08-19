# unit_testing/

### Description

The goal is to test a very simple unit which implements a character class.

Three libraries will be used for testing, the built-in *unittest*, *nose2* and *pytest*.

`test_character_unittest_nose2.py` and `test_character_pytest.py` are test files for the respective libraries. Since nose2 is an extension of unittest the same file is used by both libraries.

The file `character.py` contains a flawed implementation of the character class which is meant to fail several tests. This is the default implementation that is tested.

The file `character_updated.py` contains a correct implementation of the character class which passes all tests. To change which class is tested simply switch the import statement in the top of each test from `from character import Character` to `from character_updated import character`.

Notable differences between unittest, nose2 and pytest, is the syntax, with pytest supporting the built-in "assert" statement.

### Setup

Install requirements using command `pip install -r requirements.txt`

### Usage

To run the tests use the following commands:

`python3 -m unittest test_character_unittest_nose2`

To test the unit using the *unittest* library.

`nose2 test_character_unittest_nose2`

To test the unit using the *nose2* library.

`pytest -q test_character_pytest.py`

To test using the *pytest* library.

To generate test report:

`python -m pytest -q test_character_pytest.py --html=report.html`

### Virtualenv

Please note that running pytest inside a virtual environment can cause some issues.

In case of module errors try installing pytest inside the environment and using the command `python -m pytest -q test_character_pytest.py`