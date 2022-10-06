#!/usr/bin/env python
#
# dumppdf.py - dump pdf contents in XML format.
#
#  usage: dumppdf.py [options] [files ...]
#  options:
#    -i objid : object id
#
from pdfminer.utils import isnumber, q
from pdfminer.pdfpage import PDFPage
from pdfminer.pdftypes import PDFStream, PDFObjRef, resolve1, stream_value
from pdfminer.pdftypes import PDFObjectNotFound, PDFValueError
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfparser import PDFParser
from pdfminer.psparser import PSKeyword, PSLiteral, LIT
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from io import StringIO
import os.path
import sys
from memory_profiler import profile  # noqa: F401 add @profile for memory_profiler

ESCAPE = set(map(ord, '&<>"'))


class OutlineList:
    def __init__(self, doc):
        self.doc = doc
        self.pages = dict(
            (page.pageid, pageno)
            for (pageno, page) in enumerate(PDFPage.create_pages(self.doc))
        )
        self.outlines = self.doc.get_outlines()  # raises PDFNoOutlines

    def __iter__(self):
        for (level, title, dest, a, se) in self.outlines:
            pageno = None
            if dest:
                dest = self.resolvedest(dest)
                pageno = self.pages[dest[0].objid]
            elif a:
                action = a.resolve()
                if isinstance(action, dict):
                    subtype = action.get("S")
                    if subtype and repr(subtype) == "/'GoTo'" and action.get("D"):
                        dest = self.resolvedest(action["D"])
                        pageno = self.pages[dest[0].objid]

            yield (level, title, dest, a, se, pageno)

    def resolvedest(self, dest):
        if isinstance(dest, (str, bytes)):
            dest = resolve1(self.doc.get_dest(dest))
        elif isinstance(dest, PSLiteral):
            dest = resolve1(self.doc.get_dest(dest.name))
        if isinstance(dest, dict):
            dest = dest["D"]
        return dest

    def aslist(self):
        return [e for e in self]

    def titlepagenopairs(self):
        for (_, title, _, _, _, pageno) in self:
            yield (title, pageno)

    def titlepagenopairlist(self):
        return [e for e in self.titlepagenopairs()]


def encode(data):
    buf = StringIO()
    for b in data:
        if b < 32 or 127 <= b or b in ESCAPE:
            buf.write(f"&#{b};")
        else:
            buf.write(chr(b))
    return buf.getvalue()


# dumpxml
def dumpxml(out, obj, mode=None):
    if obj is None:
        out.write("<null />")
        return

    if isinstance(obj, dict):
        out.write('<dict size="%d">\n' % len(obj))
        for (k, v) in obj.items():
            out.write("<key>%s</key>\n" % k)
            out.write("<value>")
            dumpxml(out, v)
            out.write("</value>\n")
        out.write("</dict>")
        return

    if isinstance(obj, list):
        out.write('<list size="%d">\n' % len(obj))
        for v in obj:
            dumpxml(out, v)
            out.write("\n")
        out.write("</list>")
        return

    if isinstance(obj, bytes):
        out.write('<string size="%d">%s</string>' % (len(obj), encode(obj)))
        return

    if isinstance(obj, PDFStream):
        if mode == "raw":
            out.buffer.write(obj.get_rawdata())
        elif mode == "binary":
            out.buffer.write(obj.get_data())
        else:
            out.write("<stream>\n<props>\n")
            dumpxml(out, obj.attrs)
            out.write("\n</props>\n")
            if mode == "text":
                data = obj.get_data()
                out.write('<data size="%d">%s</data>\n' % (len(data), encode(data)))
            out.write("</stream>")
        return

    if isinstance(obj, PDFObjRef):
        out.write('<ref id="%d" />' % obj.objid)
        return

    if isinstance(obj, PSKeyword):
        out.write("<keyword>%s</keyword>" % obj.name)
        return

    if isinstance(obj, PSLiteral):
        out.write("<literal>%s</literal>" % obj.name)
        return

    if isnumber(obj):
        out.write("<number>%s</number>" % obj)
        return

    raise TypeError(obj)


# dumptrailers
def dumptrailers(out, doc):
    for xref in doc.xrefs:
        out.write("<trailer>\n")
        dumpxml(out, xref.trailer)
        out.write("\n</trailer>\n\n")
    return


# dumpallobjs
def dumpallobjs(out, doc, mode=None):
    visited = set()
    out.write("<pdf>")
    for xref in doc.xrefs:
        for objid in xref.get_objids():
            if objid in visited:
                continue
            visited.add(objid)
            try:
                obj = doc.getobj(objid)
                if obj is None:
                    continue
                out.write('<object id="%d">\n' % objid)
                dumpxml(out, obj, mode=mode)
                out.write("\n</object>\n\n")
            except PDFObjectNotFound as e:
                print(f"not found: {e!r}", file=sys.stderr)
    dumptrailers(out, doc)
    out.write("</pdf>")
    return


# dumpoutlinelegacy
def dumpoutlinelegacy(
        outfp,
        fname,
        objids,
        pagenos,
        password=b"",
        dumpall=False,
        mode=None,
        extractdir=None,
):
    with open(fname, "rb") as fp:
        parser = PDFParser(fp)
        doc = PDFDocument(parser, password)
        pages = dict(
            (page.pageid, pageno)
            for (pageno, page) in enumerate(PDFPage.create_pages(doc))
        )

        def resolve_dest(dest):
            if isinstance(dest, str):
                dest = resolve1(doc.get_dest(dest))
            elif isinstance(dest, PSLiteral):
                dest = resolve1(doc.get_dest(dest.name))
            if isinstance(dest, dict):
                dest = dest["D"]
            return dest

        try:
            outlines = doc.get_outlines()
            outfp.write("<outlines>\n")
            for (level, title, dest, a, se) in outlines:
                if dest:
                    dest = resolve_dest(dest)
                    pageno = pages[dest[0].objid]
                elif a:
                    action = a.resolve()
                    if isinstance(action, dict):
                        subtype = action.get("S")
                        if subtype and repr(subtype) == "/'GoTo'" and action.get("D"):
                            dest = resolve_dest(action["D"])
                            pageno = pages[dest[0].objid]
                s = encode(bytes(title, "utf-8"))
                outfp.write('<outline level="%r" title="%s">\n' % (level, q(s)))
                if dest is not None:
                    outfp.write("<dest>")
                    dumpxml(outfp, dest)
                    outfp.write("</dest>\n")
                if pageno is not None:
                    outfp.write("<pageno>%r</pageno>\n" % pageno)
                outfp.write("</outline>\n")
            outfp.write("</outlines>\n")
        except PDFNoOutlines:
            pass
        parser.close()
    return


# dumpoutlinenew
def dumpoutlinenew(
        outfp,
        fname,
        objids,
        pagenos,
        password=b"",
        dumpall=False,
        mode=None,
        extractdir=None,
):
    with open(fname, "rb") as fp:
        parser = PDFParser(fp)

        try:
            outlines = OutlineList(PDFDocument(parser, password))
            outfp.write("<outlines>\n")
            for (level, title, dest, a, se, pageno) in outlines:
                s = encode(bytes(title, "utf-8"))
                outfp.write('<outline level="%r" title="%s">\n' % (level, q(s)))
                if dest is not None:
                    outfp.write("<dest>")
                    dumpxml(outfp, dest)
                    outfp.write("</dest>\n")
                if pageno is not None:
                    outfp.write("<pageno>%r</pageno>\n" % pageno)
                outfp.write("</outline>\n")
            outfp.write("</outlines>\n")
        except PDFNoOutlines:
            pass
        parser.close()
    return


# dumpoutline
dumpoutline = dumpoutlinelegacy

# extractembedded
LITERAL_FILESPEC = LIT("Filespec")
LITERAL_EMBEDDEDFILE = LIT("EmbeddedFile")


def extractembedded(
        outfp,
        fname,
        objids,
        pagenos,
        password=b"",
        dumpall=False,
        mode=None,
        extractdir=None,
):
    def extract1(obj):
        filename = os.path.basename(obj["UF"] or obj["F"])
        fileref = obj["EF"]["F"]
        fileobj = doc.getobj(fileref.objid)
        if not isinstance(fileobj, PDFStream):
            raise PDFValueError(
                "unable to process PDF: reference for %r is not a PDFStream"
                % (filename)
            )
        if fileobj.get("Type") is not LITERAL_EMBEDDEDFILE:
            raise PDFValueError(
                "unable to process PDF: reference for %r is not an EmbeddedFile"
                % (filename)
            )
        path = os.path.join(extractdir, filename)
        if os.path.exists(path):
            raise IOError("file exists: %r" % path)
        print(f"extracting: {path!r}", file=sys.stderr)
        with open(path, "wb") as out:
            out.write(fileobj.get_data())
        return

    with open(fname, "rb") as fp:
        parser = PDFParser(fp)
        doc = PDFDocument(parser, password)
        for xref in doc.xrefs:
            for objid in xref.get_objids():
                obj = doc.getobj(objid)
                if isinstance(obj, dict) and obj.get("Type") is LITERAL_FILESPEC:
                    extract1(obj)
    return


def dumpchapters(level=-1):
    """
    This method extracts each chapter of a PDF file to separate txt files.
    Currently, this only works if there is an outline defined in the PDF file.

    :param level: The level to consider. If it is -1, then every outline level will be considered.
    :returns: A callable procedure handling the interpretation of each page into separate text files
                per chapter (according to level).
    """
    # @profile
    def dump(outfp,
             fname,
             objids,
             pagenos,
             password=b"",
             dumpall=False,
             mode=None,
             extractdir=None):

        with open(fname, "rb") as fp:
            outfpdic = f"{fname}_chapters/" if extractdir is None else extractdir

            if not os.path.exists(outfpdic):
                os.makedirs(outfpdic)

            parser = PDFParser(fp)
            document = PDFDocument(parser, password)
            resourcemanager = PDFResourceManager(caching=True)

            try:
                outline = OutlineList(document)
                lastpage = None  # Extract chapters by page difference
                for (lvl, title, dest, a, se, pageno) in outline:
                    if 0 <= level and lvl != level:
                        # Only consider the right level
                        continue

                    if lastpage is None:
                        lastpage = pageno
                        continue

                    outfpfile = os.path.join(extractdir, f"chapter__{title}.txt")
                    with open(outfpfile, "w", encoding="utf-8") as outfp:
                        # Output chapter to txt file
                        pages = [i for i in range(lastpage, pageno + 1)]
                        device = TextConverter(rsrcmgr=resourcemanager, outfp=outfp)
                        pageinterpreter = PDFPageInterpreter(rsrcmgr=resourcemanager, device=device)

                        pdfpages = PDFPage.get_pages(
                            fp,
                            pages,
                            maxpages=None,
                            password=password,
                            caching=True,
                            check_extractable=True,
                            parsed_doc=document
                        )

                        for page in pdfpages:
                            pageinterpreter.process_page(page)

                    lastpage = pageno

                print("Outline created successfully!")
            except PDFNoOutlines:
                print("Currently, this feature only works if the PDF has an outline")
            parser.close()

    return dump


# dumppdf
def dumppdf(
        outfp,
        fname,
        objids,
        pagenos,
        password=b"",
        dumpall=False,
        mode=None,
        extractdir=None,
):
    with open(fname, "rb") as fp:
        parser = PDFParser(fp)
        doc = PDFDocument(parser, password)
        if objids:
            for objid in objids:
                obj = doc.getobj(objid)
                dumpxml(outfp, obj, mode=mode)
        if pagenos:
            for (pageno, page) in enumerate(PDFPage.create_pages(doc)):
                if pageno in pagenos:
                    if mode is not None:
                        for obj in page.contents:
                            obj = stream_value(obj)
                            dumpxml(outfp, obj, mode=mode)
                    else:
                        dumpxml(outfp, page.attrs)
        if dumpall:
            dumpallobjs(outfp, doc, mode=mode)
        if (not objids) and (not pagenos) and (not dumpall):
            dumptrailers(outfp, doc)
        if mode not in ("raw", "binary"):
            outfp.write("\n")
    return


# main
def main(argv):
    import getopt

    def usage():
        print(
            f"usage: {argv[0]} [-P password] [-a] [-p pageid] [-i objid] [-o output] "
            "[-r|-b|-t] [-T] [-O output_dir] [-d] [-C level] input.pdf ..."
        )
        return 100

    try:
        (opts, args) = getopt.getopt(argv[1:], "dP:ap:i:o:rbtTO:C:e")
    except getopt.GetoptError:
        return usage()
    if not args:
        return usage()
    debug = 0
    objids = []
    pagenos = set()
    mode = None
    password = b""
    dumpall = False
    proc = dumppdf
    outfp = sys.stdout
    extractdir = None
    for (k, v) in opts:
        if k == "-d":
            debug += 1
        elif k == "-P":
            password = v.encode("ascii")
        elif k == "-a":
            dumpall = True
        elif k == "-p":
            pagenos.update(int(x) - 1 for x in v.split(","))
        elif k == "-i":
            objids.extend(int(x) for x in v.split(","))
        elif k == "-o":
            outfp = open(v, "wb")
        elif k == "-r":
            mode = "raw"
        elif k == "-b":
            mode = "binary"
        elif k == "-t":
            mode = "text"
        elif k == "-T":
            proc = dumpoutline
        elif k == "-C":
            proc = dumpchapters(level=int(v))
        elif k == "-O":
            extractdir = v
        elif k == "-e":
            proc = extractembedded
    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    #
    for fname in args:
        proc(
            outfp,
            fname,
            objids,
            pagenos,
            password=password,
            dumpall=dumpall,
            mode=mode,
            extractdir=extractdir,
        )
    return


if __name__ == "__main__":
    sys.exit(main(sys.argv))
