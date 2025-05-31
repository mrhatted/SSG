from textnode import *
import re

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    
    list_to_return = []
    for i in range(0,len(old_nodes)):
        list_of_text = old_nodes[i].text.split(delimeter)
        for j in range(0,len(list_of_text)):
        #print (f"i loop = {list_of_text[i]}")
            if j%2 == 0:
            #iseven, so should be text type of the original, since change hasnt happened yet
                list_to_return.append(TextNode(list_of_text[j],old_nodes[i].text_type))
                #print (f"added to returnlist = {TextNode(list_of_text[i],old_nodes[0].text_type)}")
            else:
                #uneven, so should change to the new text type
                list_to_return.append(TextNode(list_of_text[j],text_type))
            #print (f"added to returnlist = {TextNode(list_of_text[i], text_type)}")    
    
     
    return list_to_return

def extract_markdown_images(text):
    alt_text = re.findall(r"!\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)",text)
    return list(zip(alt_text, url))

def extract_markdown_links(text):
    alt_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)",text)
    return list(zip(alt_text, url))

def split_nodes_image(old_nodes):
    