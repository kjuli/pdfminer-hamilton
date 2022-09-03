#!/usr/bin/env python

""" Standard encoding tables used in PDF.

This table is extracted from PDF Reference Manual 1.6, pp.925
  "D.1 Latin Character Set and Encodings"

"""

ENCODING = [
    # (name, std, mac, win, pdf)
    ("A", 65, 65, 65, 65),
    ("AE", 225, 174, 198, 198),
    ("Aacute", None, 231, 193, 193),
    ("Acircumflex", None, 229, 194, 194),
    ("Adieresis", None, 128, 196, 196),
    ("Agrave", None, 203, 192, 192),
    ("Aring", None, 129, 197, 197),
    ("Atilde", None, 204, 195, 195),
    ("B", 66, 66, 66, 66),
    ("C", 67, 67, 67, 67),
    ("Ccedilla", None, 130, 199, 199),
    ("D", 68, 68, 68, 68),
    ("E", 69, 69, 69, 69),
    ("Eacute", None, 131, 201, 201),
    ("Ecircumflex", None, 230, 202, 202),
    ("Edieresis", None, 232, 203, 203),
    ("Egrave", None, 233, 200, 200),
    ("Eth", None, None, 208, 208),
    ("Euro", None, None, 128, 160),
    ("F", 70, 70, 70, 70),
    ("G", 71, 71, 71, 71),
    ("H", 72, 72, 72, 72),
    ("I", 73, 73, 73, 73),
    ("Iacute", None, 234, 205, 205),
    ("Icircumflex", None, 235, 206, 206),
    ("Idieresis", None, 236, 207, 207),
    ("Igrave", None, 237, 204, 204),
    ("J", 74, 74, 74, 74),
    ("K", 75, 75, 75, 75),
    ("L", 76, 76, 76, 76),
    ("Lslash", 232, None, None, 149),
    ("M", 77, 77, 77, 77),
    ("N", 78, 78, 78, 78),
    ("Ntilde", None, 132, 209, 209),
    ("O", 79, 79, 79, 79),
    ("OE", 234, 206, 140, 150),
    ("Oacute", None, 238, 211, 211),
    ("Ocircumflex", None, 239, 212, 212),
    ("Odieresis", None, 133, 214, 214),
    ("Ograve", None, 241, 210, 210),
    ("Oslash", 233, 175, 216, 216),
    ("Otilde", None, 205, 213, 213),
    ("P", 80, 80, 80, 80),
    ("Q", 81, 81, 81, 81),
    ("R", 82, 82, 82, 82),
    ("S", 83, 83, 83, 83),
    ("Scaron", None, None, 138, 151),
    ("T", 84, 84, 84, 84),
    ("Thorn", None, None, 222, 222),
    ("U", 85, 85, 85, 85),
    ("Uacute", None, 242, 218, 218),
    ("Ucircumflex", None, 243, 219, 219),
    ("Udieresis", None, 134, 220, 220),
    ("Ugrave", None, 244, 217, 217),
    ("V", 86, 86, 86, 86),
    ("W", 87, 87, 87, 87),
    ("X", 88, 88, 88, 88),
    ("Y", 89, 89, 89, 89),
    ("Yacute", None, None, 221, 221),
    ("Ydieresis", None, 217, 159, 152),
    ("Z", 90, 90, 90, 90),
    ("Zcaron", None, None, 142, 153),
    ("a", 97, 97, 97, 97),
    ("aacute", None, 135, 225, 225),
    ("acircumflex", None, 137, 226, 226),
    ("acute", 194, 171, 180, 180),
    ("adieresis", None, 138, 228, 228),
    ("ae", 241, 190, 230, 230),
    ("agrave", None, 136, 224, 224),
    ("ampersand", 38, 38, 38, 38),
    ("aring", None, 140, 229, 229),
    ("asciicircum", 94, 94, 94, 94),
    ("asciitilde", 126, 126, 126, 126),
    ("asterisk", 42, 42, 42, 42),
    ("at", 64, 64, 64, 64),
    ("atilde", None, 139, 227, 227),
    ("b", 98, 98, 98, 98),
    ("backslash", 92, 92, 92, 92),
    ("bar", 124, 124, 124, 124),
    ("braceleft", 123, 123, 123, 123),
    ("braceright", 125, 125, 125, 125),
    ("bracketleft", 91, 91, 91, 91),
    ("bracketright", 93, 93, 93, 93),
    ("breve", 198, 249, None, 24),
    ("brokenbar", None, None, 166, 166),
    ("bullet", 183, 165, 149, 128),
    ("c", 99, 99, 99, 99),
    ("caron", 207, 255, None, 25),
    ("ccedilla", None, 141, 231, 231),
    ("cedilla", 203, 252, 184, 184),
    ("cent", 162, 162, 162, 162),
    ("circumflex", 195, 246, 136, 26),
    ("colon", 58, 58, 58, 58),
    ("comma", 44, 44, 44, 44),
    ("copyright", None, 169, 169, 169),
    ("currency", 168, 219, 164, 164),
    ("d", 100, 100, 100, 100),
    ("dagger", 178, 160, 134, 129),
    ("daggerdbl", 179, 224, 135, 130),
    ("degree", None, 161, 176, 176),
    ("dieresis", 200, 172, 168, 168),
    ("divide", None, 214, 247, 247),
    ("dollar", 36, 36, 36, 36),
    ("dotaccent", 199, 250, None, 27),
    ("dotlessi", 245, 245, None, 154),
    ("e", 101, 101, 101, 101),
    ("eacute", None, 142, 233, 233),
    ("ecircumflex", None, 144, 234, 234),
    ("edieresis", None, 145, 235, 235),
    ("egrave", None, 143, 232, 232),
    ("eight", 56, 56, 56, 56),
    ("ellipsis", 188, 201, 133, 131),
    ("emdash", 208, 209, 151, 132),
    ("endash", 177, 208, 150, 133),
    ("equal", 61, 61, 61, 61),
    ("eth", None, None, 240, 240),
    ("exclam", 33, 33, 33, 33),
    ("exclamdown", 161, 193, 161, 161),
    ("f", 102, 102, 102, 102),
    ("fi", 174, 222, None, 147),
    ("five", 53, 53, 53, 53),
    ("fl", 175, 223, None, 148),
    ("florin", 166, 196, 131, 134),
    ("four", 52, 52, 52, 52),
    ("fraction", 164, 218, None, 135),
    ("g", 103, 103, 103, 103),
    ("germandbls", 251, 167, 223, 223),
    ("grave", 193, 96, 96, 96),
    ("greater", 62, 62, 62, 62),
    ("guillemotleft", 171, 199, 171, 171),
    ("guillemotright", 187, 200, 187, 187),
    ("guilsinglleft", 172, 220, 139, 136),
    ("guilsinglright", 173, 221, 155, 137),
    ("h", 104, 104, 104, 104),
    ("hungarumlaut", 205, 253, None, 28),
    ("hyphen", 45, 45, 45, 45),
    ("i", 105, 105, 105, 105),
    ("iacute", None, 146, 237, 237),
    ("icircumflex", None, 148, 238, 238),
    ("idieresis", None, 149, 239, 239),
    ("igrave", None, 147, 236, 236),
    ("j", 106, 106, 106, 106),
    ("k", 107, 107, 107, 107),
    ("l", 108, 108, 108, 108),
    ("less", 60, 60, 60, 60),
    ("logicalnot", None, 194, 172, 172),
    ("lslash", 248, None, None, 155),
    ("m", 109, 109, 109, 109),
    ("macron", 197, 248, 175, 175),
    ("minus", None, None, None, 138),
    ("mu", None, 181, 181, 181),
    ("multiply", None, None, 215, 215),
    ("n", 110, 110, 110, 110),
    ("nbspace", None, 202, 160, None),
    ("nine", 57, 57, 57, 57),
    ("ntilde", None, 150, 241, 241),
    ("numbersign", 35, 35, 35, 35),
    ("o", 111, 111, 111, 111),
    ("oacute", None, 151, 243, 243),
    ("ocircumflex", None, 153, 244, 244),
    ("odieresis", None, 154, 246, 246),
    ("oe", 250, 207, 156, 156),
    ("ogonek", 206, 254, None, 29),
    ("ograve", None, 152, 242, 242),
    ("one", 49, 49, 49, 49),
    ("onehalf", None, None, 189, 189),
    ("onequarter", None, None, 188, 188),
    ("onesuperior", None, None, 185, 185),
    ("ordfeminine", 227, 187, 170, 170),
    ("ordmasculine", 235, 188, 186, 186),
    ("oslash", 249, 191, 248, 248),
    ("otilde", None, 155, 245, 245),
    ("p", 112, 112, 112, 112),
    ("paragraph", 182, 166, 182, 182),
    ("parenleft", 40, 40, 40, 40),
    ("parenright", 41, 41, 41, 41),
    ("percent", 37, 37, 37, 37),
    ("period", 46, 46, 46, 46),
    ("periodcentered", 180, 225, 183, 183),
    ("perthousand", 189, 228, 137, 139),
    ("plus", 43, 43, 43, 43),
    ("plusminus", None, 177, 177, 177),
    ("q", 113, 113, 113, 113),
    ("question", 63, 63, 63, 63),
    ("questiondown", 191, 192, 191, 191),
    ("quotedbl", 34, 34, 34, 34),
    ("quotedblbase", 185, 227, 132, 140),
    ("quotedblleft", 170, 210, 147, 141),
    ("quotedblright", 186, 211, 148, 142),
    ("quoteleft", 96, 212, 145, 143),
    ("quoteright", 39, 213, 146, 144),
    ("quotesinglbase", 184, 226, 130, 145),
    ("quotesingle", 169, 39, 39, 39),
    ("r", 114, 114, 114, 114),
    ("registered", None, 168, 174, 174),
    ("ring", 202, 251, None, 30),
    ("s", 115, 115, 115, 115),
    ("scaron", None, None, 154, 157),
    ("section", 167, 164, 167, 167),
    ("semicolon", 59, 59, 59, 59),
    ("seven", 55, 55, 55, 55),
    ("six", 54, 54, 54, 54),
    ("slash", 47, 47, 47, 47),
    ("space", 32, 32, 32, 32),
    ("sterling", 163, 163, 163, 163),
    ("t", 116, 116, 116, 116),
    ("thorn", None, None, 254, 254),
    ("three", 51, 51, 51, 51),
    ("threequarters", None, None, 190, 190),
    ("threesuperior", None, None, 179, 179),
    ("tilde", 196, 247, 152, 31),
    ("trademark", None, 170, 153, 146),
    ("two", 50, 50, 50, 50),
    ("twosuperior", None, None, 178, 178),
    ("u", 117, 117, 117, 117),
    ("uacute", None, 156, 250, 250),
    ("ucircumflex", None, 158, 251, 251),
    ("udieresis", None, 159, 252, 252),
    ("ugrave", None, 157, 249, 249),
    ("underscore", 95, 95, 95, 95),
    ("v", 118, 118, 118, 118),
    ("w", 119, 119, 119, 119),
    ("x", 120, 120, 120, 120),
    ("y", 121, 121, 121, 121),
    ("yacute", None, None, 253, 253),
    ("ydieresis", None, 216, 255, 255),
    ("yen", 165, 180, 165, 165),
    ("z", 122, 122, 122, 122),
    ("zcaron", None, None, 158, 158),
    ("zero", 48, 48, 48, 48),
]
