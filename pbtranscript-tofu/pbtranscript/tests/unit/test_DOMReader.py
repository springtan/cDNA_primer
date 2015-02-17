"""Test pbtools.pbtranscript.Classifier."""

import unittest
import os.path as op
from pbtools.pbtranscript.io.DOMIO import DOMRecord, DOMReader

import filecmp

class Test_DOMReader(unittest.TestCase):
    """Test DOMReader."""
    def setUp(self):
        """Set up test data."""
        self.rootDir = op.dirname(op.dirname(op.abspath(__file__)))
        self.testDir = op.join(self.rootDir, "")

    def test_Reader(self):
        """Test DOMReader."""
        inDOMFN = op.join(self.testDir, "data/test_DOMReader.dom")
        reader = DOMReader(inDOMFN)
        res = [r for r in reader]
        expected_0 = DOMRecord("F1",
            "m131018_081703_42161_c100585152550000001823088404281404_s1_p0/45/ccs",
            23.7, 0, 31, 31, 2170, 2201, 3931)
        expected_1 = DOMRecord("R1",
            "m131018_081703_42161_c100585152550000001823088404281404_s1_p0/45/ccs",
            16.2, 0, 25, 25, 3906, 3931, 3931)
        self.assertEqual(res[0], expected_0)
        self.assertEqual(res[1], expected_1)


