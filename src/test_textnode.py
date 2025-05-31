import unittest
from textnode import *
from splitdelimeter import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.bold,None)
        self.assertEqual(node,node3)
        node4 = TextNode("this is not a text node", TextType.italic)
        node5 = TextNode("this is not a text node",TextType.bold)
        self.assertNotEqual(node4,node5)
        self.assertNotEqual(node,node5)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.text)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_nodes_delimeter(self):
        node6 = TextNode("This is text with a `code block` word", TextType.text)
        self.assertEqual(split_nodes_delimeter([node6], "`", TextType.code), [TextNode("This is text with a ",TextType.text,None), TextNode("code block",TextType.code,None), TextNode(" word",TextType.text,None)])
        node7 = TextNode("This is bold with a _italic block_ word", TextType.bold)
        self.assertEqual(split_nodes_delimeter([node7], "_", TextType.italic), [TextNode("This is bold with a ",TextType.bold,None), TextNode("italic block",TextType.italic,None), TextNode(" word",TextType.bold,None)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()