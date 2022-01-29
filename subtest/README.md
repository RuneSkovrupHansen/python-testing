# subtest/

### Description

The goal is to use subtests to test similar testing scenarios in a single test and illustrate how is can be useful to show several failed cases of a test.

The *unittest* library will be used for testing.

The file `coal_mine.py` contains some simple dummy functions functionality dependent on operating system.

The file `test_coal_mine.py` contains the test case.

### Usage

To run the tests use the following command:

`python3 -m unittest -v test_coal_mine.py`

Remember to run the tests from the subtest/ directory.

Note that the `-v` option is used to run the tests in verbose mode, which shows the reasons why tests are skipped.