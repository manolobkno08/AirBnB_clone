#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
from datetime import datetime
from unittest import mock
import pycodestyle
import time
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.base_model import __doc__

# base_model = __import__('base_model').__init__


class Test_pycodestyle(unittest.TestCase):
    """
    base_model TestCase
    """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    """Main Unitest"""
    unittest.main()
