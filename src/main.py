from textnode import *
from htmlnode import *

print ("hello world")

def main():
    #stuff = TextNode("some things",TextType.link, "rabbit.url")
    #print (stuff)
    #otherstuff = HTMLNode("a","a rabbit walked through the desert",None,{"href": "https://www.google.com","target": "_blank"})
    #print (otherstuff)
    #print (otherstuff.props_to_html())
    #leafstuff = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #print (leafstuff.to_html())
    node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
    print (node)
    print(node.to_html())
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print (parent_node.to_html())

main()
