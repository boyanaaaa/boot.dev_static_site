import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    items = os.listdir(dir_path_content)

    for item in items:
        full_path = os.path.join(dir_path_content, item)

        if os.path.isdir(full_path):

            generate_pages_recursive(
                full_path,
                template_path,
                os.path.join(dest_dir_path, item),
                basepath
            )

        elif item.endswith(".md"):

         
            os.makedirs(dest_dir_path, exist_ok=True)

            dest_path = os.path.join(dest_dir_path, "index.html")

            generate_page(
                full_path,
                template_path,
                dest_path,
                basepath
            )