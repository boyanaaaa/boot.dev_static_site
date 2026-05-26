


def markdown_to_blocks(markdown):
    new_list = []

    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            new_list.append(stripped)
    return new_list