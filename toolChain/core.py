import webdriver
import os
import sys
import platform from system
import traceback from print_exc
from typing import Any
from typing import Callable
from typing import List
from typing import Tuple


def claer_screen():
    os.system("clear")

def validate_input(ip,val_range):
    try:
        ip = int(ip)
        if ip in  val_range():
            return ip
        else:
            return None
    except:
        return None

class tool(object):
    
    def __init__(self,option= None,installable:bool=true,runnable:bool=true):
        if  optinos is None:
            options = []
        
        if isinstance(OPTIONS,list):
            self.OPTIONS = []
            if installable : 
                self.OPTIONS.append("install",self.install)
            if runnable:
                self.OPTIONS.append("RUN",self.run)
            self.OPTIONS.extend(options)
        
        else:
             raise Exception(
                     "option must be in list of (option_name.option_fn) tuples")

    def show_info(self):
        desc = self.DISCRIPTION
        if.self.DISCRIPTION:
            desc += "\n\t[*]"
            desc += self.PROJECTURL
           

    def show_options(self,parent = None):
        clear_screen()
        self.show_info()
        for index,





