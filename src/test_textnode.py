import unittest
from textnode import *

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
        


if __name__ == "__main__":
    unittest.main()