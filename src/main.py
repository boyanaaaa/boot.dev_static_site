from textnode import TextNode
from texttype import TextType


def main():
    node = TextNode(
        "This is some random text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    print(node)


if __name__ == "__main__":
    main()