
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_nodes.tetxt_type !=  TextType.TEXT:
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