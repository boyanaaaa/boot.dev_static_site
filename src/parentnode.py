from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=None)



    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.value is None:
            raise ValueError("Missing value!")

        props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        
   
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.props})"