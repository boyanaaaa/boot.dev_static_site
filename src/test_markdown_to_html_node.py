import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):

    # ---------------- PARAGRAPHS ----------------
    def test_paragraphs(self):
        md = (
            "This is **bolded** paragraph\n"
            "text in a p\n"
            "tag here\n\n"
            "This is another paragraph with _italic_ text and `code` here\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    # ---------------- CODE BLOCK ----------------
    def test_codeblock(self):
        md = (
            "```\n"
            "This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "```\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
        )

    # ---------------- HEADING ----------------
    def test_heading(self):
        md = "# Hello world"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>Hello world</h1></div>",
        )

    # ---------------- QUOTE ----------------
    def test_quote(self):
        md = (
            "> Hello world\n"
            "> this is a quote\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>Hello world this is a quote</blockquote></div>",
        )

    # ---------------- UNORDERED LIST ----------------
    def test_unordered_list(self):
        md = (
            "- item one\n"
            "- item two\n"
            "- item three\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>",
        )

    # ---------------- ORDERED LIST ----------------
    def test_ordered_list(self):
        md = (
            "1. first\n"
            "2. second\n"
            "3. third\n"
        )

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()