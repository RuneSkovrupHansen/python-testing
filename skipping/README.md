# skipping/

### Description

The goal is to use the unittest decorators to skip tests.

The *unittest* library will be used for testing.

The file `os_functionality.py` contains some simple dummy functions functionality dependent on operating system.

The file `test_os_functionality.py` contains the test case.

### Usage

To run the tests use the following command:

`python3 -m unittest -v test_os_functionality.py`

Remember to run the tests from the skipping/ directory.

Note that the `-v` option is used to run the tests in verbose mode, which shows the reasons why tests are skipped.