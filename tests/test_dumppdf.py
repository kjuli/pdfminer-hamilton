import os.path
import unittest
import io

from tools.dumppdf import dumpoutlinelegacy, dumpoutlinenew, OutlineList, dumpchapters
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfparser import PDFParser


# sampleoutlinepairs contains tuples (pdf, txt) such that
# txt contains the expected output of running dumpoutline on pdf
sampleoutlinepairs = [(
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

    def compareoutlines(self, sample, expected, dumpoutline):
        with io.StringIO() as dumpoutput:
            dumpoutline(dumpoutput, sample, [], set())
            dumpoutput.seek(0)
            dumpoutputlines = dumpoutput.readlines()

            with open(expected) as expectfile:
                expectedlines = expectfile.readlines()

                self.assertEqual(dumpoutputlines, expectedlines)

    def test_sampleoutlinepairslegacy(self):
        for (sample, expected) in sampleoutlinepairs:
            self.compareoutlines(sample, expected, dumpoutlinelegacy)

    def test_sampleoutlinepairsclassed(self):
        for (sample, expected) in sampleoutlinepairs:
            self.compareoutlines(sample, expected, dumpoutlinenew)


class TestOutlineList(unittest.TestCase):
    def enclosetest(self, test):
        for (sample, _) in sampleoutlinepairs:
            with open(sample, "rb") as fp:
                parser = PDFParser(fp)

                try:
                    outlines = OutlineList(PDFDocument(parser, b""))
                    test(outlines)
                except PDFNoOutlines:
                    pass

                parser.close()

    def test_outlinesaslist(self):
        def test(outlines):
            outlinelist = outlines.aslist()
            i = 0

            for elem in outlines:
                self.assertEqual(elem, outlinelist[i])
                i += 1

        self.enclosetest(test)

    def test_titlepagenopairs(self):
        def test(outlines):
            outlinelist = outlines.aslist()
            i = 0

            for elem in outlines.titlepagenopairs():
                self.assertEqual(elem, (outlinelist[i][1], outlinelist[i][5]))
                i += 1

        self.enclosetest(test)

    def test_titlepagenopairlist(self):
        def test(outlines):
            pairlist = outlines.titlepagenopairlist()
            i = 0

            for pair in outlines.titlepagenopairs():
                self.assertEqual(pair, pairlist[i])
                i += 1

        self.enclosetest(test)


class TestChapterCreation(unittest.TestCase):

    def test_dumpchapters(self):
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
