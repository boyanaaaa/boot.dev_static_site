import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):

        md = "# Hello"

        title = extract_title(md)

        self.assertEqual(title, "Hello")


    def test_extract_title_with_spaces(self):

        md = "#    Hello World   "

        title = extract_title(md)

        self.assertEqual(title, "Hello World")


    def test_no_h1(self):

        md = "## Not h1"

        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()