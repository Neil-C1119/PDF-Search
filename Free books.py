import wget
from googlesearch import search
import requests
import os
import os.path
from os import path
from colorama import init, Fore, Back, Style
import time

init()

print(Fore.GREEN + Style.BRIGHT + """
  ______               ____              _        _
 |  ____|             |  _ \            | |      | |
 | |__ _ __ ___  ___  | |_) | ___   ___ | | _____| |
 |  __| '__/ _ \/ _ \ |  _ < / _ \ / _ \| |/ / __| |
 | |  | | |  __/  __/ | |_) | (_) | (_) |   <\__ \_|
 |_|  |_|  \___|\___| |____/ \___/ \___/|_|\_\___(_)

""")

print(Fore.RED + """//////////////////////////////////////////////////////////////////////////////////////////////
"""
+ Fore.WHITE + """What is the name of the book you want to download? (adding the author may give better results)
"""
+ Fore.RED + """//////////////////////////////////////////////////////////////////////////////////////////////
""" + Fore.WHITE)
bookName = input()

print(Fore.RED + """\n///////////////////////////////////////////////////////////////////////////////////
"""
+ Fore.WHITE + """How many PDFs would you like to download? (a higher number may give better results)
"""
+ Fore.RED + """///////////////////////////////////////////////////////////////////////////////////
""" + Fore.WHITE)
pdfAmount = int(input())

query = bookName + " filetype:pdf"
urlArray = []

print(Fore.RED + """\n//////////////////////////////////////////
"""
+ Fore.WHITE + """Here are the PDFs that will be downloaded:
"""
+ Fore.RED + """//////////////////////////////////////////""" + Fore.CYAN)

for x in search(query, tld="com", num=10, stop=pdfAmount, pause=2):
    print(x)
    urlArray.append(x)

print("\n")

length = len(urlArray)

if path.exists("PDFs"):
    print(Fore.WHITE + "PDFs file already exists. Adding PDFs to existing folder. . .\n")
    time.sleep(1)
    print("Downloading PDFs. Please wait. . .\n")

    for x in range(length):
        url = urlArray[x]
        r = requests.get(url, allow_redirects=True)
        open("PDFs/" + bookName + " PDF " + str(x) + ".pdf", "wb").write(r.content)
else:
    print(Fore.WHITE + "Creating PDF folder. . .\n")
    os.mkdir("PDFs")
    time.sleep(1)
    print("Downloading PDFs. Please wait. . .\n")
    for x in range(length):
        url = urlArray[x]
        r = requests.get(url, allow_redirects=True)
        open("PDFs/" + bookName + " PDF " + str(x) + ".pdf", "wb").write(r.content)

input("Press Enter to terminate program. . .")
