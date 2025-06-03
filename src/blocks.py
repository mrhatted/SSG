from enum import Enum
from textnode import *
from htmlnode import *
import re
from splitdelimeter import *

def markdown_to_blocks(markdown):
    list_to_return = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        
        if block == []:
            pass
        else:
            block_to_add = block.strip("\n").strip()
            if block_to_add == "":
                pass
            else:
                list_to_return.append(block_to_add)
    return list_to_return

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_block_type(block):
    if block[0]=="#":
        return BlockType.heading
    elif block[0:3] == "```":
        return BlockType.code
    elif block[0]==">":
        return BlockType.quote
    elif block[0:2]=="- ":
        return BlockType.unordered_list
    elif block[0:3]=="1. ":
        return BlockType.ordered_list
    else:
        return BlockType.paragraph

def text_to_children(text):
    Textnodes = text_to_textnodes(text)
    pass


def markdown_to_html_node(markdown):
    
    list_of_htmlnodes =[]
    code_to_return = ""
    blocks = markdown_to_blocks(markdown)
    #print (f"blocks = {blocks}")
    for block in blocks:
        
        #print (f"block thats about to get matched = {block}")
        
        #print (f"block to blocktype = {block_to_block_type(block)}")
        match block_to_block_type(block):
            case BlockType.heading:
                i = 0
                while block[i] == "#":
                    i+=1
                block = block[i:]
                tag = f"h{i}"   
                list_of_textnodes = text_to_textnodes(block)
                list_to_hold = []
                for textnode in list_of_textnodes:
                    list_to_hold.append(textnode.text_node_to_html_node())
                
                block_heading = ParentNode(tag,list_to_hold)
                #print (f"block identified as heading = {block}") 
                #print (f"block paragraph = {block_paragraph}")
                list_of_htmlnodes.append(block_heading)
            case BlockType.code:
                #print (f"block identified as code = {block}")
                
                #print (f"leafnode about to add = {LeafNode("```",block,None,None)}")
                list_of_htmlnodes.append(ParentNode("pre",[LeafNode("code",block,None)]))
            case BlockType.quote:
                list_of_textnodes = text_to_textnodes(block)
                list_to_hold = []
                for textnode in list_of_textnodes:
                    list_to_hold.append(textnode.text_node_to_html_node())
                block_paragraph = ParentNode("blockquote",list_to_hold)
                #print (f"block identified as quote = {block}") 
                #print (f"block paragraph = {block_paragraph}")
                list_of_htmlnodes.append(block_paragraph)
            case BlockType.unordered_list:
                #print (f"block identified as unordered list = {block}")
                list_listitems = block.split("\n- ")
                #print (f"list listitmes = {list_listitems}")
                list_of_parentnodes = []
                list_to_hold = []
                for listitem in list_listitems:
                    list_of_textnodes = text_to_textnodes(listitem)
                    list_to_hold = []
                    for textnode in list_of_textnodes:
                        list_to_hold.append(textnode.text_node_to_html_node())
                    list_of_parentnodes.append(ParentNode("li",list_to_hold))
                block_unordered_list = ParentNode("ul",list_of_parentnodes)
                
                list_of_htmlnodes.append(block_unordered_list)
            case BlockType.ordered_list:
                #print (f"block identified as ordered list = {block}")
                list_listitems = re.split(r"\d. ",block)
                del list_listitems [0]
                for i in range (0,len(list_listitems)-1):
                    list_listitems[i] = list_listitems[i][:-1]
                #print (f"list listitmes = {list_listitems}")
                list_of_parentnodes = []
                list_to_hold = []
                for listitem in list_listitems:
                    list_of_textnodes = text_to_textnodes(listitem)
                    list_to_hold = []
                    for textnode in list_of_textnodes:
                        list_to_hold.append(textnode.text_node_to_html_node())
                    list_of_parentnodes.append(ParentNode("li",list_to_hold))
                block_unordered_list = ParentNode("ol",list_of_parentnodes)
                
                list_of_htmlnodes.append(block_unordered_list)
            case BlockType.paragraph:
                list_of_textnodes = text_to_textnodes(block)
                list_to_hold = []
                for textnode in list_of_textnodes:
                    list_to_hold.append(textnode.text_node_to_html_node())
                block_paragraph = ParentNode("p",list_to_hold)
                #print (f"block identified as paragraph = {block}") 
                #print (f"block paragraph = {block_paragraph}")
                list_of_htmlnodes.append(block_paragraph)
                #print (f"list of textnodes = {list_of_textnodes}")
                #print (list_of_textnodes)
                
        
    #print (f"list of htmlnodes = {list_of_htmlnodes}")
   
    return ParentNode("div",list_of_htmlnodes)
    
