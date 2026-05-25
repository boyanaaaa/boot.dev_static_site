import unittest

from textnode import TextNode, TextType
from split_node_delimeter import (split_nodes_image, split_nodes_link, )


class TestSplitNodesImage(unittest.TestCase):

    def test_split_images_single(self):

        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_multiple(self):

        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):

        node = TextNode(
            "This is just normal text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "This is just normal text",
                    TextType.TEXT
                )
            ],
            new_nodes,
        )

    def test_split_images_non_text_node(self):

        node = TextNode(
            "Bold text",
            TextType.BOLD,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "Bold text",
                    TextType.BOLD
                )
            ],
            new_nodes,
        )

    def test_split_images_text_after_image(self):

        node = TextNode(
            "Start ![cat](cat.png) end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "cat.png"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )
import unittest



class TestSplitNodesLink(unittest.TestCase):

    def test_split_links_single(self):

        node = TextNode(
            "This is a link [google](https://google.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is a link ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_links_multiple(self):

        node = TextNode(
            "A [one](https://1.com) and [two](https://2.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("A ", TextType.TEXT),
                TextNode("one", TextType.LINK, "https://1.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.LINK, "https://2.com"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):

        node = TextNode(
            "Just plain text here",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Just plain text here", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links_non_text_node(self):

        node = TextNode(
            "Already bold",
            TextType.BOLD,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Already bold", TextType.BOLD)
            ],
            new_nodes,
        )

    def test_split_links_text_after_link(self):

        node = TextNode(
            "Start [boot](https://boot.dev) end",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("boot", TextType.LINK, "https://boot.dev"),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()
