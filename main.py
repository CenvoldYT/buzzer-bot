import time
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style
from selenium.webdriver.common.by import By
import os

url = 'https://ccg.buzz'
options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome("C:\chromedriver.exe", chrome_options=options)
driver.get(url)
driver.maximize_window()

title = '''
                      ██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗     ██████╗  ██████╗ ████████╗
                      ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
                      ██████╔╝██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝    ██████╔╝██║   ██║   ██║   
                      ██╔══██╗██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║   ██║   
                      ██████╔╝╚██████╔╝███████╗███████╗███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
                      ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝                                              
'''

script = '''
setInterval(function() {
    submitBuzz()
}, 10);
'''

os.system('cls')
print(5*'\b' + Style.BRIGHT + Fore.CYAN + title)
print(Style.BRIGHT + Fore.GREEN + '                             Made by Cenvold#0026 for myself but I decided to release it ;)')
print('\n')

def autoclicker():
  session = requests.Session()
  session.get(url)

  game_id = input(Style.BRIGHT + Fore.WHITE + '                             [ ROOM CODE ]: ' + Style.BRIGHT + Fore.RED)
  new_plr_name = input(Style.BRIGHT + Fore.WHITE + '                             [ PLAYER NAME ]: ' + Style.BRIGHT + Fore.RED)
  new_team_name = input(Style.BRIGHT + Fore.WHITE + '                             [ TEAM NAME ]: ' + Style.BRIGHT + Fore.RED)
  print('\n')
  print(Style.BRIGHT + Fore.WHITE + '                             [ STATUS ]: ' + Style.BRIGHT + Fore.YELLOW + 'Logging into Game ID "' + game_id + '"...', end='\r')
  time.sleep(1)
  game = driver.find_element(By.ID, "roomID")
  game.send_keys(game_id)
  driver.find_element(By.ID, "playerJoinNextBTN").click()

  time.sleep(1)

  print(Style.BRIGHT + Fore.WHITE + '                             [ STATUS ]: ' + Style.BRIGHT + Fore.YELLOW + 'Setting Player Name to  "' + new_plr_name + '"...', end='\r')
  time.sleep(1)
  player_name = driver.find_element(By.ID, "playerNameFree")
  player_name.send_keys(new_plr_name)

  print(Style.BRIGHT + Fore.WHITE + '                             [ STATUS ]: ' + Style.BRIGHT + Fore.YELLOW + 'Setting Team Name to "' + new_team_name + '"...', end='\r')
  time.sleep(1)
  team_name = driver.find_element(By.ID, "teamName")
  team_name.send_keys(new_team_name)
  driver.find_element(By.ID, "quizShowNextBTN").click()
    
  time.sleep(1)

  print(Style.BRIGHT + Fore.WHITE + '                             [ STATUS ]: ' + Style.BRIGHT + Fore.YELLOW + 'Running Autoclicker Script...', end='\r')
  time.sleep(1)
  driver.execute_script(script)
  print(Style.BRIGHT + Fore.WHITE + '                             [ STATUS ]: ' + Style.BRIGHT + Fore.MAGENTA + 'Successfully started Autoclicker!', end='\r')
autoclicker()
input()
