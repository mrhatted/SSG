import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node3 = LeafNode("li", "Some rabbits went for a stroll", {"href": "https://www.google.com"})
        
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertNotEqual(node3.to_html(), '"<a href="https://www.google.com">Some rabbits went for a stroll</a>"')
    


if __name__ == "__main__":
    unittest.main()
