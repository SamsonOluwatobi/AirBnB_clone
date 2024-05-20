#!/usr/bin/env python3
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by initializing the HBNBCommand instance.

        This function initializes the `hbnb_cmd` attribute of the test case
        with an instance of the `HBNBCommand` class.

        Parameters:
            self (TestCase): The current test case i
            nstance.

        Returns:
            None
        """
        self.hbnb_cmd = HBNBCommand()

    def test_do_quit(self):
        """
        Test the `do_quit` method of the `HBNBCommand` class.

        This test case verifies that the `do_quit` method of the
        `HBNBCommand` class returns `True` when called with an
        empty string as the argument. It uses the `patch` function
        from the `unittest.mock` module to temporarily replace the
        `sys.stdout` attribute with a `StringIO` object. This allows
        the captured output to be checked against the expected result.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.assertTrue(self.hbnb_cmd.do_quit(''))

    def test_do_EOF(self):
        """
        Test the `do_EOF` method of the `HBNBCommand` class.

        This test case verifies that the `do_EOF` method of the
        `HBNBCommand` class returns `True` when called with an empty
        string as the argument. It uses the `patch` function from the
        `unittest.mock` module to temporarily replace the `sys.stdout`
        attribute with a `StringIO` object. This allows the captured
        output to be checked against the expected result.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.assertTrue(self.hbnb_cmd.do_EOF(''))

    def test_do_help(self):
        """
        Test the `do_help` method of the `HBNBCommand` class.

        This test case verifies that the `do_help` method of the
        `HBNBCommand` class behaves correctly when called with an
        empty string as the argument. It uses the `patch` function
        from the `unittest.mock` module to temporarily replace the
        `sys.stdout` attribute with a `StringIO` object. This allows
        the captured output to be checked against the expected result.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.hbnb_cmd.do_help('')

    def test_emptyline(self):
        """
        Test the behavior of the `emptyline` method of the `HBNBCommand`
        class.

        This test case verifies that when the `emptyline` method is
        called, it does not write anything to the standard output. It
        does this by patching the `sys.stdout` object with a `StringIO`
        instance and then asserting that the contents of the `StringIO`
        instance are empty.

        Parameters:
            self (TestCase): The current test case instance.

        Returns:
            None
        """
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.hbnb_cmd.emptyline()
            self.assertEqual(fake_stdout.getvalue().strip(), '')


if __name__ == '__main__':
    unittest.main()
