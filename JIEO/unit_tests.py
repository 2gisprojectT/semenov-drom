from unittest import TestCase
from Leo import Leo
import unittest
import string


class Testing(unittest.TestCase):
    def test_statusN(self):
        a = Leo('')
        self.assertEqual('', a.status, "error N")

    def test_statusF(self):
        leo = Leo('full')
        leo = Leo('hungry')
        leo = Leo('full')
        self.assertEqual('full', leo.status, "error F")

    def test_statusH(self):
        leo = Leo('full')
        leo = Leo('hungry')
        leo = Leo('')
        leo = Leo('hungry')
        self.assertEqual('hungry', leo.status, "error H")

    def test_antelopeF(self):
        leo = Leo('full')
        leo.antelope('antelope')
        self.assertEqual('hungry', leo.status, "error AF")

    def test_antelopeH(self):
        leo = Leo('hungry')
        leo.antelope('antelope')
        self.assertEqual('full', leo.status, "error AH")

    def test_treeF(self):
        leo = Leo('full')
        leo.tree('tree')
        self.assertEqual('hungry', leo.status, "error TF")

    def test_treeH(self):
        leo = Leo('hungry')
        leo.tree('tree')
        self.assertEqual('hungry', leo.status, "error TH")

    def test_hunterF(self):
        leo = Leo('full')
        leo.hunter('hunter')
        self.assertEqual('hungry', leo.status, "error HF")

    def test_hunterH(self):
        leo = Leo('hungry')
        leo.hunter('hunter')
        self.assertEqual('hungry', leo.status, "error HH")


if __name__ == '__main__':
    unittest.main()
