import os
import time
from colorama import init, Fore, Style
from pystyle import Colors, Colorate, Center

# Initialize colorama
init(autoreset=True)

load1 = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗
██║   ██║
██║   ██║
╚██╗ ██╔╝
 ╚████╔╝ 
  ╚═══╝     
{Style.RESET_ALL}"""

load2 = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗ ██████╗ 
██║   ██║██╔═══██╗
██║   ██║██║   ██║
╚██╗ ██╔╝██║   ██║
 ╚████╔╝ ╚██████╔╝
  ╚═══╝   ╚═════╝ 
{Style.RESET_ALL}"""

load3 = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗ ██████╗ ██████╗ 
██║   ██║██╔═══██╗██╔══██╗
██║   ██║██║   ██║██████╔╝
╚██╗ ██╔╝██║   ██║██╔══██╗
 ╚████╔╝ ╚██████╔╝██║  ██║
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝
{Style.RESET_ALL}"""

load4 = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗ ██████╗ ██████╗ ████████╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝
██║   ██║██║   ██║██████╔╝   ██║   
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
{Style.RESET_ALL}"""

load5 = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██║   ██║██████╔╝   ██║   █████╗  
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝  
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
{Style.RESET_ALL}"""

# Banners
BANNER = f"""{Fore.CYAN}{Style.BRIGHT}
██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}"""

BANNER1 = f"""{Fore.CYAN}{Style.BRIGHT}
     [+] Vortex Tools [+]
[+] Programmed By (Itz_Me) [+]
{Style.RESET_ALL}"""


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(load1)))
    time.sleep(0.03)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(load2)))
    time.sleep(0.03)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(load3)))
    time.sleep(0.03)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(load4)))
    time.sleep(0.03)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(load5)))
    time.sleep(0.03)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(BANNER)))
    done_msg = Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("LOADED!"))
    print(done_msg)
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.cyan_to_blue, Center.XCenter(BANNER)))
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(BANNER1)))
    input(f"{Fore.GREEN}[SYSTEM]{Style.RESET_ALL} {Fore.CYAN}Press Enter To Close...{Style.RESET_ALL}")