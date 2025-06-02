from textnode import *
from htmlnode import *
from splitdelimeter import *

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
    #print (node)
    #print(node.to_html())
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    #print (parent_node.to_html())
    node = TextNode("This is text with a `code block` word", TextType.text)
    node2 = TextNode("This some text with a **bold words** wordings", TextType.text)
    #print (node)
    #print(f"result of split delimeter={split_nodes_delimeter([node], "`", TextType.code)}")
    #print(f"result of split delimeter={split_nodes_delimeter([node2], "**", TextType.bold)}")
    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))
    #text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text2))
    node3 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev)",TextType.text)
    print(split_nodes_image([node3]))

main()
