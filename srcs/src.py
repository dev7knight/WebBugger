import time
from colorama import Fore
import requests
from pywebcopy import save_website
import collections
import os

def setup():
   os.system("pip3 install -r requirements.txt")
   os.system('cls' if os.name == 'nt' else 'clear')


def weebTester():
    target = input(Fore.CYAN +"Targted website: ")
    r = requests.get(target)
    output = (r.status_code)
    print (output)
    print(Fore.GREEN + f"""if you got from 100-200 means that you can continue  (success)
            if you got something in the 300s it means moved permanently  (REDIRECTS ERR)   
            if you got something in the 400s it means Client err (UnAUTHORIZED)
            if you somethins in  the 500s it means Server ERROR (INTERNAL SERVER ERROR)
            you got {output}""")

def htmlSteal():
    target = input(Fore.GREEN + "Targted website: ")
    r = requests.get(target)
    html_code = (r.text)
    file_name = input(Fore.CYAN + "file name? ")
    with open(f"{file_name}.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    
    print(f"html code grabbed succecfuly and stored in a {file_name}.html file")

def imgStealer():
    img_address = input(Fore.GREEN + "please enter image addres : ")
    r = requests.get(img_address)
    
    file_name = input(Fore.CYAN +"file name? ")
    with open(f"{file_name}.png", "wb") as f:
        f.write(r.content)
    print(f"image saved succesful as {file_name}.png!")       

def webClonner():
  save_website(
  url="https://httpbin.org/",
  project_folder="E://savedpages//",
  project_name="my_site",
  bypass_robots=True,
  debug=True,
  open_in_browser=True,
  delay=None,
  threaded=False,
  )

def headerPrinter():
    target = input("Targted website: ")
    r = requests.get(target)
    header_info = (r.headers)
    header_info = header_info.__str__()
    file_name = input("file name? ")
    
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(header_info)
    print(f"website header saved and stored in a {file_name}.txt file")

def subdomain():
    def domain_scanner(domain_name,sub_domnames):
        print('----URL after scanning subdomains----')
        
        
        for subdomain in sub_domnames:
        
        
            url = f"https://{subdomain}.{domain_name}"
            
            
            try:
                
                requests.get(url)
                
                
                print(f'[+] {url}')
                
                
            except requests.ConnectionError:
                pass
    
    print("please dont be dumb and put the url just domain name")
    dom_name = input("Enter the Domain Name: ")
 
    
    with open('basiclist.txt','r') as file:
        name = file.read()
        sub_dom = name.splitlines()
        
         

    domain_scanner(dom_name,sub_dom)
    
def subdirectory():
    
    def domain_scanner(domain, direc):
        print('URLS FOUND:')
        
        for directory in direc:
            url = f"https://{domain}/{directory}"
            
            try:
                response = requests.get(url)
                
                if response.status_code == 200:
                    print(Fore.YELLOW + f'[+] {url}')
                
            except requests.ConnectionError:
                pass

    print("Please dont be dumb and enter url only enter domain")
    domain = input(Fore.LIGHTWHITE_EX + "Enter the Domain Name: ")
    with open('dir.txt','r') as file:
            name = file.read()
            directory = name.splitlines()

    domain_scanner(domain,directory)

def crawler():
   print("Under development")

def Adminpanel():
    def domain_scanner(domain, direc):
        print('URLS FOUND:')
        
        for directory in direc:
            url = f"https://{domain}/{directory}"
            
            try:
                response = requests.get(url)
                
                if response.status_code == 200:
                    print(Fore.YELLOW + f'[+] {url}')
                
            except requests.ConnectionError:
                pass

    print("Please dont be dumb and enter url only enter domain")
    domain = input(Fore.LIGHTWHITE_EX + "Enter the Domain Name: ")
    with open('admin.txt','r') as file:
            name = file.read()
            directory = name.splitlines()

    domain_scanner(domain,directory)