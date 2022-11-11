# coding=utf-8
#!/usr/bin/env python3
from random import choice
from colorama import  Fore,Style,Back

logo =  """ 

__     __
\ \   / /_ _ _ __ ___  _ __
 \ \ / / _` | '_ ` _ \| '_ \
  \ V / (_| | | | | | | |_) |
   \_/ \__,_|_| |_| |_| .__/
                      |_|

  ___           _
 |_ _|_ __  ___| |_ __ _
  | || '_ \/ __| __/ _` |
  | || | | \__ \ || (_| |
  |___|_| |_|___/\__\__,_|
  
█▀█ █▀▀ █▀█ █▀█ █▀█ ▀█▀ █▀▀ █▀█
█▀▄ ██▄ █▀▀ █▄█ █▀▄ ░█░ ██▄ █▀▄
                                  
  """
def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)                                                  
    print(Fore.RED + "                            Github" + Fore.CYAN + " - Aruack ")
    print(Fore.RED + "                            BY     " + Fore.CYAN + " - @Aruack")
    print(Fore.RED + "                            Telegram"+ Fore.CYAN + " - t.me/Aruack_official ")
    print(Fore.GREEN + "      Aruack: https://t.me/Aruack_official"+ Style.RESET_ALL + Style.BRIGHT)
