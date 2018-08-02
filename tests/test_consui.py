"""consui tests"""
import unittest
from unittest.mock import patch

from pack import consui


class BaseUtilsTestCase(unittest.TestCase):
    """Test base utils from consui"""
    def setUp(self):
        """Setup test environment"""
        input_patcher = patch("builtins.input")
        self.input_mock = input_patcher.start()
        self.addCleanup(input_patcher.stop)

    @patch("builtins.print")
    def test_write(self, print_mock):
        """Test consui.write function"""
        test_str = "test"
        expected_str = "\n{}\n".format(test_str)
        consui.write(test_str)
        print_mock.assert_called_with(expected_str)

    def test_read(self):
        """Test consui.read function"""
        read_mess = "mess"
        input_line = "line"
        self.input_mock.return_value = input_line
        expected_input_print = "{}>".format(read_mess)
        real_result = consui.read(read_mess)
        # Check input
        self.input_mock.assert_called_with(expected_input_print)
        # Check result
        self.assertEqual(real_result, input_line)

    def test_confirm_simple_positive(self):
        """Test consui.confirm standart positive behavior"""
        confirm_mess = "confirm?"
        expected_result = True
        expected_print = "{}>".format(confirm_mess)
        input_lines = ('y', "yes")
        for line in input_lines:
            self.input_mock.return_value = line
            real_result = consui.confirm(confirm_mess)
            # Check input
            self.input_mock.assert_called_with(expected_print)
            # Check result
            self.assertEqual(real_result, expected_result)

    def test_confirm_simple_negative(self):
        """Test consui.confirm standart negative behavior"""
        confirm_mess = "confirm?"
        expected_result = False
        expected_print = "{}>".format(confirm_mess)
        input_lines = ('n', "no")
        for line in input_lines:
            self.input_mock.return_value = line
            real_result = consui.confirm(confirm_mess)
            # Check input
            self.input_mock.assert_called_with(expected_print)
            # Check result
            self.assertEqual(real_result, expected_result)
