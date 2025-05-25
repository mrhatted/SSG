from enum import Enum

class TextType(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"
    
class TextNode:    
    def __init__(self,text,text_type,url=None):
        if isinstance(text_type,TextType):
            self.text = text
            self.text_type = text_type
            self.url = url
        else:
            raise Exception (f"{text_type} must be a TextType")
    
    def __eq__(self,node1):
        return (self.text == node1.text) and (self.text_type == node1.text_type) and (self.url == node1.url)
    
    def __repr__(self):
        return (f"TextNode({self.text},{self.text_type.value},{self.url})")