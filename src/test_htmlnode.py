import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p","a rabbit was thirsty","bart",{"href":"https://www.google.com"})
        node2 = HTMLNode("p","a rabbit was thirsty","bart",{"href":"https://www.google.com"})
        node3 = HTMLNode("o","a rabbit was thirsty","bart",{"href":"https://www.google.com"})
        node4 = HTMLNode("p","a rabit was thirsty","bart",{"href":"https://www.google.com"})
        node5 = HTMLNode("p","a rabbit was thirsty","bort",{"href":"https://www.google.com"})
        node6 = HTMLNode("p","a rabbit was thirsty","bart",{"href":"https://www.gogle.com"})
        node7 = HTMLNode("p","a rabbit was thirsty","bart")
        node8 = HTMLNode("p","a rabbit was thirsty","bart",None)
        node9 = HTMLNode("p","a rabbit was thirsty","bart",{"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(node1,node2)
        self.assertNotEqual(node1,node3)
        self.assertNotEqual(node1,node4)
        self.assertNotEqual(node1,node5)
        self.assertNotEqual(node1,node6)
        self.assertEqual(node7,node8)
        self.assertEqual(node9.props_to_html(),' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()

    