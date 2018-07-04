"""consui tests"""
import unittest
from unittest.mock import patch

from pack import consui


class BaseUtilsTestCase(unittest.TestCase):
    """Test base utils from consui"""
    @patch("builtins.print")
    def test_write(self, print_mock):
        """Test consui.write function"""
        test_str = "test"
        expected_str = "\n{}\n".format(test_str)
        consui.write(test_str)
        print_mock.assert_called_with(expected_str)

    @patch("builtins.input")
    def test_read(self, input_mock):
        """Test consui.read function"""
        read_mess = "mess"
        input_line = "line"
        input_mock.return_value = input_line
        expected_input_print = "{}>".format(read_mess)
        real_result = consui.read(read_mess)
        # Check input
        input_mock.assert_called_with(expected_input_print)
        # Check result
        self.assertEqual(real_result, input_line)

    @patch("builtins.input")
    def test_confirm_simple_positive(self, input_mock):
        """Test consui.confirm standart positive behavior"""
        confirm_mess = "confirm?"
        expected_result = True
        expected_print = "{}>".format(confirm_mess)
        input_lines = ('y', "yes")
        for line in input_lines:
            input_mock.return_value = line
            real_result = consui.confirm(confirm_mess)
            # Check input
            input_mock.assert_called_with(expected_print)
            # Check result
            self.assertEqual(real_result, expected_result)

    @patch("builtins.input")
    def test_confirm_simple_negative(self, input_mock):
        """Test consui.confirm standart negative behavior"""
        confirm_mess = "confirm?"
        expected_result = False
        expected_print = "{}>".format(confirm_mess)
        input_lines = ('n', "no")
        for line in input_lines:
            input_mock.return_value = line
            real_result = consui.confirm(confirm_mess)
            # Check input
            input_mock.assert_called_with(expected_print)
            # Check result
            self.assertEqual(real_result, expected_result)
