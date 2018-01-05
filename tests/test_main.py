import unittest

from hephaestus.main import Hephaestus


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.hephaestus = Hephaestus()

    def test_hello(self):
        self.assertEqual(self.hephaestus.calculate_total(3), 27)
