import os
import shutil
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    
    os.mkdir(destination)

    items = os.listdir(source)

    for item in items:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
              print(f"Copying file: {source_path} -> {destination_path}")

              shutil.copy(source_path, destination_path)
        else:
             print(f"Entering directory: {source_path}")

             copy_static(source_path, destination_path)




def main():
    copy_static("static", "public")
    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )


if __name__ == "__main__":
    main()