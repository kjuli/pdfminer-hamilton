import os.path
import unittest
import io

import tools.dumppdf
from tools.dumppdf import dumpoutline_legacy, dumpoutline_new, OutlineList, dumpchapters
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

# Contains tuples of actual pdf and directory to chapter output
sampleoutlinetuples = [(
    "samples/test_samples/Introduction_To_Modern_Cryptography.pdf",
    "samples/IntroChapters",
    ["chapter__Series Page.txt"]
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
    def enclose_test(self, test):
        for (sample, _) in sample_outline_pairs:
            with open(sample, "rb") as fp:
                parser = PDFParser(fp)

                try:
                    outlines = OutlineList(PDFDocument(parser, b""))
                    test(outlines)
                except PDFNoOutlines:
                    pass

                parser.close()

    def test_outlines_as_list(self):
        def test(outlines):
            outline_list = outlines.as_list()
            i = 0

            for elem in outlines:
                self.assertEqual(elem, outline_list[i])
                i += 1

        self.enclose_test(test)

    def test_title_pageno_pairs(self):
        def test(outlines):
            outline_list = outlines.as_list()
            i = 0

            for elem in outlines.title_pageno_pairs():
                self.assertEqual(elem, (outline_list[i][1], outline_list[i][5]))
                i += 1

        self.enclose_test(test)

    def test_title_pageno_pair_list(self):
        def test(outlines):
            pair_list = outlines.title_pageno_pair_list()
            i = 0

            for pair in outlines.title_pageno_pairs():
                self.assertEqual(pair, pair_list[i])
                i += 1

        self.enclose_test(test)


class TestChapterCreation(unittest.TestCase):

    def test_dump_chapters(self):
        """
        Tests whether the correct directory was created and that all the chapters are extracted.
        """
        dc = dumpchapters(level=1)  # Extractor method
        for (file, outputdirectory, outputfiles) in sampleoutlinetuples:
            dc(None, file, None, None, extractdir=outputdirectory)

            self.assertTrue(os.path.exists(outputdirectory))
            for outputfile in outputfiles:
                actualFile = os.path.join(outputdirectory, outputfile)
                self.assertTrue(actualFile)


if __name__ == "__main__":
    unittest.main()
