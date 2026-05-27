from split_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from parentnode import ParentNode
from text_to_text_nodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        # ---------------- PARAGRAPH ----------------
        if block_type == BlockType.PARAGRAPH:
            paragraph = block.replace("\n", " ")
            children.append(
                ParentNode("p", text_to_children(paragraph))
            )

        # ---------------- HEADING ----------------
        elif block_type == BlockType.HEADING:
            heading_level = 0

            for char in block:
                if char == "#":
                    heading_level += 1
                else:
                    break

            text = block[heading_level + 1:]

            children.append(
                ParentNode(f"h{heading_level}", text_to_children(text))
            )

        # ---------------- CODE ----------------
        elif block_type == BlockType.CODE:
            text = block[4:-3]  # remove ``` ... ```
            code_node = LeafNode("code", text)

            children.append(
                ParentNode("pre", [code_node])
            )

        # ---------------- QUOTE ----------------
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")

            cleaned_lines = []
            for line in lines:
                cleaned_lines.append(line.lstrip(">").strip())

            quote_text = " ".join(cleaned_lines)

            children.append(
                ParentNode("blockquote", text_to_children(quote_text))
            )

        # ---------------- UNORDERED LIST ----------------
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")

            items = []
            for line in lines:
                text = line[2:]  # remove "- "
                items.append(
                    ParentNode("li", text_to_children(text))
                )

            children.append(
                ParentNode("ul", items)
            )

        # ---------------- ORDERED LIST ----------------
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")

            items = []
            for line in lines:
                text = line.split(". ", 1)[1]
                items.append(
                    ParentNode("li", text_to_children(text))
                )

            children.append(
                ParentNode("ol", items)
            )

    return ParentNode("div", children)