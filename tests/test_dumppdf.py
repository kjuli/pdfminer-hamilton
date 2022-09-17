import unittest
import io

from tools.dumppdf import dumpoutline_legacy, dumpoutline_new, OutlineList
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfparser import PDFParser


# sample_outline_pairs contains tuples (pdf, txt) such that
# txt contains the expected output of running dumpoutline on pdf
sample_outline_pairs = [(
    "samples/simple1.pdf",
    "samples/test_samples/simple1_outline.txt"
), (
    "samples/test_samples/Introduction_To_Modern_Cryptography.pdf",
    "samples/test_samples/Introduction_To_Modern_Cryptography_outline.txt"
), (
    "samples/nonfree/dmca.pdf",
    "samples/test_samples/dmca_outline.txt"
)]


class TestDumpoutline(unittest.TestCase):

    """Asserts that the content of the file with filepath expected is equal to
    the result of running dumpoutline on the .pdf file with filepath sample."""
    def compare_outlines(self, sample, expected, dumpoutline):
        with io.StringIO() as dump_output:
            dumpoutline(dump_output, sample, [], set())
            dump_output.seek(0)
            dump_output_lines = dump_output.readlines()

            with open(expected) as expect_file:
                expected_lines = expect_file.readlines()

                self.assertEqual(dump_output_lines, expected_lines)

    def test_sample_outline_pairs_legacy(self):
        for (sample, expected) in sample_outline_pairs:
            self.compare_outlines(sample, expected, dumpoutline_legacy)

    def test_sample_outline_pairs_classed(self):
        for (sample, expected) in sample_outline_pairs:
            self.compare_outlines(sample, expected, dumpoutline_new)


class TestOutlineList(unittest.TestCase):
    def test_outlines_as_list(self):
        for (sample, expected) in sample_outline_pairs:
            with open(sample, "rb") as fp:
                parser = PDFParser(fp)

                try:
                    outlines = OutlineList(PDFDocument(parser, b""))
                    outline_list = outlines.as_list()
                    i = 0

                    for elem in outlines:
                        self.assertEqual(elem, outline_list[i])
                        i += 1
                except PDFNoOutlines:
                    pass

                parser.close()

    def test_title_pageno_pairs(self):
        for (sample, expected) in sample_outline_pairs:
            with open(sample, "rb") as fp:
                parser = PDFParser(fp)

                try:
                    outlines = OutlineList(PDFDocument(parser, b""))
                    outline_list = outlines.as_list()
                    i = 0

                    for elem in outlines.title_pageno_pairs():
                        self.assertEqual(elem, (outline_list[i][1], outline_list[i][5]))

                except PDFNoOutlines:
                    pass

                parser.close()


if __name__ == "__main__":
    unittest.main()
