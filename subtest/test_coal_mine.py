#!/bin/bash

from mimetypes import init
import unittest
import coal_mine

class TestCoalMine(unittest.TestCase):

    def setUp(self):
        self.cm = coal_mine.CoalMine()
    
    # Test that worker property sets values in range correctly
    def test_workers_in_range(self):
        for workers in range(self.cm.WORKER_THRESHOLD+1):
            with self.subTest(workers=workers): # Note that parameter and value name must match
                self.cm.workers = workers
                self.assertEqual(self.cm.workers, workers)
    
    # Test that worker property sets negative values to zero
    def test_workers_negative(self):
        self.cm.workers = -1
        self.assertEqual(self.cm.workers, 0)
    
    # Test that worker property sets values exceeding threshold to threshold
    def test_workers_above_threshold(self):
        self.cm.workers = self.cm.WORKER_THRESHOLD+1
        self.assertEqual(self.cm.workers, self.cm.WORKER_THRESHOLD)

    """Test output for all number of workers
    
    The test is purposely set up to fail since it expects
    that the output scales linearly with the number of workers
    and the diminishing returns are not taken into accout
    
    Because subTest() is used the test will show all of the
    failed example with messages similar to
    
    ======================================================================
    FAIL: test_output (__main__.TestCoalMine) (workers=6)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/home/rune/python_testing/subtest/test_coal_mine.py", line 34, in test_output
        self.assertEqual(self.cm.output, workers*self.cm.BASE_WORKER_OUTPUT)
    AssertionError: 87.0 != 90

    This makes it easy to identify which sub tests are failing"""

    def test_output(self):
        for workers in range(self.cm.WORKER_THRESHOLD+1):
            with self.subTest(workers=workers):
                self.cm.workers = workers
                self.assertEqual(self.cm.output, workers*self.cm.BASE_WORKER_OUTPUT)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()