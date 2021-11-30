import base64
import os
import colorama
from colorama import Fore, Back, Style

cls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
cls()

print(f"""{Style.BRIGHT}{Fore.RED}
 ▒█████  ▄▄▄█████▓ ▄▄▄      ▒██   ██▒
▒██▒  ██▒▓  ██▒ ▓▒▒████▄    ▒▒ █ █ ▒░
▒██░  ██▒▒ ▓██░ ▒░▒██  ▀█▄  ░░  █   ░
▒██   ██░░ ▓██▓ ░ ░██▄▄▄▄██  ░ █ █ ▒ 
░ ████▓▒░  ▒██▒ ░  ▓█   ▓██▒▒██▒ ▒██▒
░ ▒░▒░▒░   ▒ ░░    ▒▒   ▓▒█░▒▒ ░ ░▓ ░
  ░ ▒ ▒░     ░      ▒   ▒▒ ░░░   ░▒ ░
░ ░ ░ ▒    ░        ░   ▒    ░    ░  
    ░ ░                 ░  ░ ░    ░  
                                     
{Style.RESET_ALL}""")

ID=input(f"{Fore.LIGHTYELLOW_EX}[{Fore.GREEN}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} User ID: {Fore.MAGENTA}")

ID = ID.encode("ascii")
  
base64_bytes = base64.b64encode(ID)
token = base64_bytes.decode("ascii")

print(f"{Fore.LIGHTYELLOW_EX}[{Fore.GREEN}+{Fore.LIGHTYELLOW_EX}] {Style.DIM} {token}")
