import unittest

from split_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):

        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",

                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",

                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks_removed(self):

        md = """
Hello



World
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "Hello",
                "World",
            ],
        )

    def test_strip_whitespace(self):

        md = """
   Hello world   

   Another block   
"""

        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "Hello world",
                "Another block",
            ],
        )


if __name__ == "__main__":
    unittest.main()