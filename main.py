from selenium.webdriver.support.ui import Select
from colorama import Fore, Back, Style
from pypresence import Presence
from selenium import webdriver
from os import system
from time import sleep
import os, time, sys
import random


   

# Menu Logo & Presence! Classic animation, Chromeoptions etc  #
os.system('cls')
os.system("mode con cols=50 lines=30")
rpc = Presence("887882999151083560")
rpc.connect()
rpc.update(state="Main Menu",details="Insta Stalker 2.0",large_image="instagramicon",large_text="Discord.Link/200IQ",start=time.time())
def logo():
	menu = Fore.RED +  Fore.MAGENTA +                       """                 Discord.Link/200IQ
                                                    ╔════════════════════════════════════════════╗
                                                                    Insta Stalker v2.0
                                                    ╚════════════════════════════════════════════╝
"""
	print(menu) 
logo()
animation = "%-\\"
for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
sleep(1)
os.system('cls')
logo()
os.system('title Type Username to Boost:')
Username = input(Fore.WHITE +  ' [' + Fore.GREEN +'$' + Fore.WHITE + ']' + Fore.WHITE + f' Username: ' + Fore.MAGENTA +'')
options = webdriver.ChromeOptions()
rpc.update(state=f"Boosting @ {Username}",details=f"Submited username..",large_image="instagramicon")
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # Prevents console messages, only important Errors will be printed. #
options.add_argument('--disable-gpu') # necessary. #
options.headless = True
driver = webdriver.Chrome(options=options, executable_path="[DATA]/DrivingAutomatically.exe")
# -------------------------------------------------------------------------- #
# Main part of automation #
def Instagram(StoryViews):
    os.system('title Insta Stalker ^| Loading...')
    driver.get('https://igtor.com/instagram-hikaye-izlenme-hilesi')
    sleep(2)
    try:
        driver.find_element_by_xpath('/html/body/main/div/div/div[4]/div[3]/div/div/form/div/input').send_keys(Username) 
         # Username Input
        driver.find_element_by_xpath('/html/body/main/div/div/div[4]/div[3]/div/div/form/button').click()              
         # Gonder " Submit "
        os.system('title Insta Stalker ^| Username submited!')
    except:
        print(Fore.WHITE +  '  [' + Fore.RED +'?' + Fore.WHITE + ']' + Fore.WHITE + f' xPath Needs Update / discord.link/200IQ')
        driver.refresh()
        Instagram(StoryViews)
    else:
        try:
            sleep(10) 
             # Sleep 10 seconds until the StoryViews Loads
            driver.find_element_by_xpath('/html/body/main/div/div/div[4]/div[3]/div/div/div/div[2]/div[3]/div/div').click() # Clicks the story Icon # Upload only [1] Story so it can select class="col-6 col-sm-3 col-md-2" 
            sleep(2)
            driver.find_element_by_id("miktar").click() 
             # Click input amount
            driver.find_element_by_id("miktar").clear() 
             # Clear input amount
            driver.find_element_by_id("miktar").send_keys("120") # Send amount max "120"
            sleep(2)


            while True: 
                # Looping after 1800 seconds: aka 30min of / rate limititation
             driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div[2]/button').click() # Submit "gonderim"
             os.system(f'title Successfully Sent @{Username} ^| Looping...')
             print(Fore.WHITE +  '  [' + Fore.GREEN +'$' + Fore.WHITE + ']' + Fore.WHITE + ' Submited: ' + Fore.MAGENTA + f'{Username}')
             rpc.update(state=f"Successfully Sent @ {Username}",details="100-120 Story Views!",large_image="instagramicon",large_text="Successfully Looping Story Views")
             sleep(1800) 
        except:
            print(Fore.WHITE +  '  [' + Fore.RED +'?' + Fore.WHITE + ']' + Fore.WHITE + f' Rate Limited, or Loop died')
            rpc.update(state=f"ERROR Wrong Username: {Username}",details="LINE: 61",large_image="instagramicon",large_text="Restarting InstaStalker2.0")
            driver.refresh()
            sleep(10)
Instagram(Instagram)
