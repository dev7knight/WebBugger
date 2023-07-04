#this is version 2
from srcs import src
from srcs import banner
from srcs import port
from srcs import dos
from colorama import Fore
import socket

src.setup()

banner.banner()
command = input(Fore.BLUE + """
╭┈───────WEBSITE-BUG version:2.0 BY:DEV7KNIGHT 
╰┈➤ """)
   
if command == "1":
    src.weebTester()

elif command == "2":
    src.htmlSteal()

elif command == "3": #fixing
    src.webClonner()

elif command == "4":
    src.headerPrinter()

elif command == "5": 
    dos.Dos()

elif command == "6": #port scanner
    port.portScanner()

elif command == "7": 
    src.subdomain()

elif command == "8": 
    src.subdirectory()

elif command == "9":      
    src.Adminpanel()

elif command == "10": #crawler      
   src.crawler()

elif command == "11":      
    print("BYE!")

