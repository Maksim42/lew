"""filesys tests"""
import unittest
from unittest.mock import patch
from os.path import join

from pack import filesys


class BaseUtilsTestCase(unittest.TestCase):
    @patch("pack.filesys.ui.read")
    @patch("pack.filesys.listdir")
    def test_open_file_dialogue(self, listdir_mock, input_mock):
        FILES_LIST = [c for c in "abcd"]
        home_dir = "./"
        listdir_mock.return_value = FILES_LIST
        with patch("pack.filesys.path.isfile", return_value=True):
            with patch("pack.filesys.ui.write", new=self.out_checker):
                for selected_file_num in range(1, len(FILES_LIST)):
                    input_mock.return_value = str(selected_file_num)
                    result = filesys.open_file_dialogue(home_dir)
                    expected_path = join(home_dir, FILES_LIST[selected_file_num-1])
                    self.assertEqual(result, expected_path)

    def out_checker(self, arg, *args):
        if arg == "Unsupported command!":
            self.fail("Bad output")
