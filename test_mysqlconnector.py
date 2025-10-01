# test_mysqlconnector.py
"""
Tests for MysqlConnector module.
"""

import unittest
from mysqlconnector import MysqlConnector

class TestMysqlConnector(unittest.TestCase):
    """Test cases for MysqlConnector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MysqlConnector()
        self.assertIsInstance(instance, MysqlConnector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MysqlConnector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
