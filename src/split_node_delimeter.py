
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from extract_markdown_images import ( extract_markdown_images, extract_markdown_links,)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type !=  TextType.TEXT:
            new_list.append(old_node)
            continue
    
        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
             raise Exception("Invalid markdown syntax")
        
        for i in range(len(split_text)):
     
            if split_text[i] == "":
                continue

    
            if i % 2 == 0:
                new_list.append(
                    TextNode(split_text[i], TextType.TEXT)
                )

           
            else:
                new_list.append(
                    TextNode(split_text[i], text_type)
                )
    return new_list



def split_nodes_image(old_nodes):
    new_list = []
    
    for old_node in old_nodes:  
        if old_node.text_type !=  TextType.TEXT:
            new_list.append(old_node)
            continue
    
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
             new_list.append(old_node)
             continue
        
        original_text = old_node.text

        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})",
                1)
            
            if sections[0] != "":
                new_list.append(
                    TextNode(sections[0], TextType.TEXT)
                )

            new_list.append(
                TextNode(
                    image_alt,
                    TextType.IMAGE,
                    image_link
                )
            )

            original_text = sections[1]
            
        if original_text != "":
            new_list.append(
                TextNode(original_text, TextType.TEXT)
            )

    return new_list
            







def split_nodes_link(old_nodes):

    new_list = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            new_list.append(old_node)
            continue

        original_text = old_node.text

        for link_text, link_url in links:

            sections = original_text.split(
                f"[{link_text}]({link_url})",
                1
            )

            if sections[0] != "":
                new_list.append(TextNode(sections[0], TextType.TEXT))

            new_list.append(
                TextNode(link_text, TextType.LINK, link_url)
            )

            original_text = sections[1]

        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))

    return new_list