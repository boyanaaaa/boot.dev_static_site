import unittest

from block_types import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Hello"),
            BlockType.HEADING,
        )

    def test_code(self):
        self.assertEqual(
            block_to_block_type("```python\nprint('hi')\n```"),
            BlockType.CODE,
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> hello\n> world"),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- item 1\n- item 2"),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. one\n2. two\n3. three"),
            BlockType.ORDERED_LIST,
        )

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is just a paragraph"),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()