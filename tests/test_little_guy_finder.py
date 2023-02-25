import unittest
from src.little_guy_finder import *
from src.util import *


class test_LGF(unittest.TestCase):

    # Test table build
    def test_build_db(self):
        # Setup
        build_db()

        # Invoke
        result = [exec_get_all("""SELECT * FROM Little_Guys""", args={}),
                  exec_get_all("""SELECT * FROM Traits""", args={})]

        # Analyze
        self.assertEqual([[], []], result)
