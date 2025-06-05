from textnode import *
from htmlnode import *
from splitdelimeter import *
from blocks import *
import os
import shutil
import sys

def copy_src_to_target(src,target):
    #print (f"{public} is bestand? {os.path.isfile(public)}")
    #print (f"{src} is bestand? {os.path.isfile(src)}")
    shutil.rmtree(target,ignore_errors=True)
    if os.path.isfile(src):
        #is bestand, geen file, kopiëren die handel indien niet in target
        if os.path.isfile(target):
            #bestaat al in target
            return
        else:
            #bestaat nog niet in target, moet kopiëren
            shutil.copy(src,target)
        
        
    else: 
        #is file  
        if  not os.path.isdir(target):
            #bestaat nog niet in doelmap, maken3
            os.mkdir(target)
            #bestaat al in doelmap
        
            
        directories = os.listdir(src)      
        for directory in directories:
            copy_src_to_target(f"{src}/{directory}",f"{target}/{directory}")

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path,"r").read()
    template = open(template_path,"r").read()
    html_string = markdown_to_html_node(markdown).to_html()
    
    title = extract_title(markdown)
    unservered_template = template.replace("{{ Title }}",title).replace("{{ Content }}",html_string)
    templateforserver = unservered_template.replace('href="/',f'href="{basepath}')
    filled_in_template = templateforserver.replace('src="/',f'src="{basepath}')
    if not (os.path.exists(os.path.dirname(dest_path))):
        
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path,"w") as f:
        f.write(filled_in_template)

def fun_vr_debug(from_path, template_path):
    markdown = open(from_path,"r").read()
    template = open(template_path,"r").read()
    html_string = markdown_to_html_node(markdown).to_html()
    
    title = extract_title(markdown)
    filled_in_template = template.replace("{{ Title }}",title).replace("{{ Content }}",html_string)
    return filled_in_template

def change_filename_to_html(dest_dir):
    
    return ".".join(dest_dir.split(".")[:-1])+".html"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    
    htmlname = dest_dir_path[:-2]+"html"
    if os.path.isfile(dir_path_content):
        
        if os.path.isfile(dest_dir_path):
            
            return
        else:
            
            generate_page(dir_path_content, template_path, change_filename_to_html(dest_dir_path))
        
        
    else: 
        
        if  not os.path.isdir(dest_dir_path):
           
            os.mkdir(dest_dir_path)
            
        
            
        directories = os.listdir(dir_path_content)      
        for directory in directories:
            generate_pages_recursive(f"{dir_path_content}/{directory}", template_path,f"{dest_dir_path}/{directory}")


def grab_basepath():
    # Check if an argument was provided
    global basepath
    if len(sys.argv[0]) == 0:
        basepath = "/"       
    else:
        basepath = sys.argv[1]       

    # Now you can use basepath in your program
    print(f"Using basepath: {basepath}")
    
    return basepath 



def main():
    print ("hello world")
    #print (fun_vr_debug("./content/index.md","template.html"))
    basepath = grab_basepath()
    
    
    
    #shutil.rmtree("{basepath}docs",ignore_errors=True)
    copy_src_to_target(f".{basepath}static",f".{basepath}docs")
    #generate_page(f".{basepath}content/index.md", f".{basepath}template.html", f".{basepath}docs/index.html")
    generate_pages_recursive(f".{basepath}content",f".{basepath}template.html",f".{basepath}docs")
    
    
main()
