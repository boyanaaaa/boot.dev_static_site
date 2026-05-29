import os
from markdown_to_html_node import  markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

   
    with open(template_path, "r") as file:
        template = file.read()
    

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    page_title = extract_title(markdown)

    final_html = template.replace(
        "{{ Title }}",
        page_title
    )

    final_html = final_html.replace(
        "{{ Content }}",
        html_content
    )

    directory = os.path.dirname(dest_path)

    if directory != "":
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(final_html)