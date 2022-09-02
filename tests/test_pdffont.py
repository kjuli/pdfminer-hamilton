import unittest
from pdfminer.pdffont import PDFFont
#  Simplistic Test cases


class TestPDFFont(unittest.TestCase):

    def test_get_widths(self):
        self.assertEqual(PDFFont.get_widths([1]), {})
        self.assertEqual(PDFFont.get_widths([1, 2, 3]), {1: 3, 2: 3})
        self.assertEqual(PDFFont.get_widths(
            [1, [2, 3], 6, [7, 8]]), {1: 2, 2: 3, 6: 7, 7: 8})
        return

    def test_get_widths2(self):
        self.assertEqual(PDFFont.get_widths2([1]), {})
        self.assertEqual(PDFFont.get_widths2([1, 2, 3, 4, 5]), {
                         1: (3, (4, 5)), 2: (3, (4, 5))})
        self.assertEqual(PDFFont.get_widths2(
            [1, [2, 3, 4, 5], 6, [7, 8, 9]]), {1: (2, (3, 4)), 6: (7, (8, 9))})
        return


if __name__ == "__main__":
    unittest.main()
