#!/bin/python3
import unittest
import os
import anagram_tools as anagram_tools
import file_tools as file_tools

# Define test cases for each tool

class TestAnagramTool(unittest.TestCase):

    """Set up test fixture with some strings"""

    def setUp(self) -> None:
        
        self.anagram_string_1 = "the classroom"
        self.anagram_string_2 = "school master"
        self.non_anagram_string = "this is not an anagram"

    def test_is_anagram_true(self):

        self.assertTrue(anagram_tools.is_anagram(
            self.anagram_string_1,
            self.anagram_string_2
        ))

    def test_is_anagram_false(self):

        self.assertFalse(anagram_tools.is_anagram(
            self.anagram_string_1,
            self.non_anagram_string
        ))

    def test_is_anagram_upper(self):

        self.assertTrue(anagram_tools.is_anagram(
            self.anagram_string_1.upper(),
            self.anagram_string_2
        ))

    def test_get_count_representation(self):

        self.assertEqual(
            anagram_tools._get_count_representation("logging"),
            "g3ilno"
        )


class TestStringTool(unittest.TestCase):

    """Set up test fixture consisting of a folder with three files
    
    .folder/
        -- file1
        -- file2
        -- file3

    self.folder: str
    self.files: list[str]
    """

    def setUp(self) -> None:
        self.folder = ".folder"
        self.files = [os.path.join(self.folder, f"file{i}") for i in range(3)]

        os.mkdir(self.folder)
        for f in self.files: open(f, "a").close()

    def tearDown(self) -> None:
        for f in self.files:
            if os.path.exists(f): os.remove(f)

        if os.path.exists(self.folder): os.rmdir(self.folder)

    def test_remove_file(self) -> None:
        self.assertTrue(os.path.exists(self.files[0]))
        file_tools.remove_file(self.files[0])
        self.assertFalse(os.path.exists(self.files[0]))

    def test_remove_files(self) -> None:
        for f in self.files: self.assertTrue(os.path.exists(f))
        file_tools.remove_files(*self.files)
        for f in self.files: self.assertFalse(os.path.exists(f))

    def test_clear_folder(self) -> None:
        self.assertTrue(os.listdir(self.folder))
        file_tools.clear_folder(self.folder)
        self.assertFalse(os.listdir(self.folder))

    def test_remove_folder(self) -> None:
        self.assertTrue(os.path.exists(self.folder))
        file_tools.remove_folder(self.folder)
        self.assertFalse(os.path.exists(self.folder))

if __name__ == "__main__":
    unittest.main()

