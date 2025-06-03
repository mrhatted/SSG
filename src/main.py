from textnode import *
from htmlnode import *
from splitdelimeter import *
from blocks import *

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
    #grandchild_node = LeafNode("b", "grandchild")
    #child_node = ParentNode("span", [grandchild_node])
    #parent_node = ParentNode("div", [child_node])
    #print (parent_node.to_html())
    #node = TextNode("This is text with a `code block` word", TextType.text)
    #node2 = TextNode("This some text with a **bold words** wordings", TextType.text)
    #print (node)
    #print(f"result of split delimeter={split_nodes_delimeter([node], "`", TextType.code)}")
    #print(f"result of split delimeter={split_nodes_delimeter([node2], "**", TextType.bold)}")
    #text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))
    #text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text2))
    #node3 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.text)
    #print(f"splitlink = {split_nodes_link([node3])}")
    #node4 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) and yadayada",TextType.text)
    #print(f"splitimg = {split_nodes_image([node4])}")
    #print(text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"))
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    print(f"markdown_to_html_node(md)={markdown_to_html_node(md)}")
    md2 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    print(f"markdown_to_html_node(md2)={markdown_to_html_node(md2)}")

    md3 = """
1. first item
2. second item
3. fourth item, just kidding


##### 5 headings
"""
    print(f"markdown_to_html_node(md3)={markdown_to_html_node(md3)}")
main()
