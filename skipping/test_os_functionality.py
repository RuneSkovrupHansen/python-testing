import sys
import distro
import unittest
import os_functionality

class TestOsFunctionality(unittest.TestCase):

    # Conditional skipping using skipUnless()
    @unittest.skipUnless(sys.platform == "windows", "do_stuff_windows() requires Windows")    
    def test_do_stuff_windows(self) -> None:
        self.assertTrue(os_functionality.do_stuff_windows())

    @unittest.skipUnless(sys.platform == "linux", "do_stuff_windows() requires Linux")
    def test_do_stuff_linux(self) -> None:
        self.assertTrue(os_functionality.do_stuff_linux())

    # Conditional skipping using skipIf()
    @unittest.skipIf(distro.name() != "Ubuntu",  "do_stuff_debian() requires Ubuntu")
    def test_do_stuff_ubuntu(self) -> None:
        self.assertTrue(os_functionality.do_stuff_ubuntu())

    @unittest.skipIf(distro.name() != "Debian GNU/Linux", "do_stuff_debian() requires Debian")
    def test_do_stuff_debian(self) -> None:
        self.assertTrue(os_functionality.do_stuff_debian())

    # Flat out skipping test of deprecated functionality using skip()
    @unittest.skip("'do_stuff_deprecated() is deprecated")
    def test_do_stuff_deprecated(self) -> None:
        self.assertTrue(os_functionality.do_stuff_deprecated())

def main():
    unittest.main()

if __name__ == "__main__":
    main()
