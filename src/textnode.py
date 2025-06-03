from enum import Enum
from  htmlnode import *

class TextType(Enum):
    text = "text"
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
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.text:
                return LeafNode(None,value=text_node.text)
            case TextType.bold:
                return LeafNode("b",text_node.text)
            case TextType.italic:
                return LeafNode("i",text_node.text)
            case TextType.code:
                return LeafNode('code',text_node.text)
            case TextType.link:
                return LeafNode("a",text_node.text,{"href":text_node.url})
            case TextType.image:
                return LeafNode("img",None,{"src":text_node.url,"alt":text_node.text})
            
