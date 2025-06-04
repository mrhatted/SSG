from textnode import *
from htmlnode import *
from splitdelimeter import *
from blocks import *
import os
import shutil

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
                         
        
            
                
        
         


                        

        


def main():
    print ("hello world")
    copy_src_to_target("./static","./public")
    
main()
