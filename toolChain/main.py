##!usr/bin/python3

from login import login
import datetime
import subprocess
from Tool import tshark
from Tool import metasploit
from Tool import scrapy

logo =   """ 
 /$$   /$$ /$$                     /$$$$$$                               /$$$$$ /$$          
| $$  /$$// $$                    /$$__  $$                             |__  $$|__/          
| $$ /$$/ | $$ /$$$$$$/$$$$       | $$  \__/ /$$   /$$ /$$   /$$            | $$ /$$ /$$$$$$$ 
| $$$$$/  | $$| $$_  $$_  $$      | $$ /$$$$| $$  | $$| $$  | $$            | $$| $$| $$__  $$
| $$  $$  | $$| $$ \ $$ \ $$      | $$|_  $$| $$  | $$| $$  | $$       /$$  | $$| $$| $$  \ $$
| $$\  $$ | $$| $$ | $$ | $$      | $$  \ $$| $$  | $$| $$  | $$      | $$  | $$| $$| $$  | $$
| $$ \  $$| $$| $$ | $$ | $$      |  $$$$$$/|  $$$$$$$|  $$$$$$/      |  $$$$$$/| $$| $$  | $$
|__/  \__/|__/|__/ |__/ |__/       \______/  \____  $$ \______/        \______/ |__/|__/  |__/
                                             /$$  | $$                                        
                                            |  $$$$$$/                                        
                                             \______/                                         
                            

                           [v]  version 1.1.0 realease [v]
                           [v]              2021.02.11 [v] 
"""\

menu1 ="""
----------------------------------------------
[1]Network
[2]Crowling
[3]None
----------------------------------------------
"""\

menu2 ="""
----------------------------------------------
[1]tshark
[2]metasploit
----------------------------------------------
"""\




if __name__ == "__main__":
     try:
         ### menu access ###
         login.login()
         print(logo + "\n\n" + "access time :" + str(datetime.datetime.now()) )
         print(menu1)
         choice = input("Select Menu --> ")
         if choice == "1" :
             print(menu2)
             choice = input("Select Tool --> " )
             if choice == "1" :
                 tshark.tshark()
             if choice == "2" :
                 metasploit.metasploit()
         
         if choice == "2":
            scrapy.scrapy.startproject()

     except KeyboardInterrupt:
         print("exiting...")
         sleep(2)   
