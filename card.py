import random
import pyfiglet
from colorama import init
init()
#from colorama import Fore, Back, Style
from colorama import Fore, Back, Style
import os
import time
os.system('cls')
time.sleep(0.5)
banner = pyfiglet.figlet_format("CARDS", font = "banner3" )
print(banner)
print(Fore.CYAN,  """                         cc generator v1.5
""", Style.RESET_ALL)
CorrectUsername = "og yazeed"
CorrectPassword = "og abbalo"
loop = 'true'
while loop == 'true':
	print(Fore.GREEN, """
	please put the correct details 
	
	""", Style.RESET_ALL)
	username = input("username: ")
	if username == CorrectUsername:
								
		password = input("password: ")
		if password == CorrectPassword:
			time.sleep(5)
				
			print(Style.DIM, " successfully logged as yahoo boi", Style.RESET_ALL)
			loop = 'false'
			break
		else:
			print(Fore.RED, "wrong password ❌❌❌", Style.RESET_ALL)
			time.sleep(3)
			os.system('cls')
	else:
			print(Fore.RED, "wrong username ❌❌❌", Style.RESET_ALL)
			time.sleep(3)
			os.system('cls')
os.system('cls')
#time.sleep(5)
result = pyfiglet.figlet_format("carding", font = "banner3-D" )
print(result)

print(Style.DIM, """
+=========================================+
|..........   V̿•I̿•P̿➸➸H̿A̿C̿K̿E̿R̿✔✔  ...........|
              ▇▇▇▇▇▇▇▇▇▇▇▇
Author: ABDULGEE 

member in: HAUSA_HACKERS/HAUSA_PROGRAMNERS/CYBER_XPLOIT_HAUSA

phone info: +2348131116661

fb_account: Abdul gee

☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠

_______________HAUSA PROGRAMMERS_________________
::::::::::----------TOOL----------::::::::::

CARD GENERATOR

""", Style.RESET_ALL)
print(Fore.GREEN, """
➊: VISA""")
print("➋: MASTERCARD")
print("➌: ABOUT THE AUTHOR")
print("➍: BYPASS CARD OTP", Style.RESET_ALL)
gee = ""
while True:
	
#gee != "1, 2, 3":
		
	gee = input("select option ⇛ ").lower()
	a = ("Access bank", "UBA bank", "keystone bank", "polaris bank", "GT bank", "unio bank", "unity bank", "wema bank", "zenith bank", "sterling bank", "stanbic bank", "skye bank", "heritage bank", "GTB bank", "first bank", "fidelity bank", "fcmb bank", "eco bank", "Diamond bank", )
	b = ("03/2023", "07/2023", "09/2023", "10/2023", "01/2024", "06/2023", "08/2024", "04/2025", "05/2024", "03/2024", "08/2025", "06/2025", "09/2025", "04/2026")
	if gee == "1":
		os.system('cls')
		time.sleep(5)
		print(Fore.RED, """
		
CARD NUMBER: """, random.randint(1000000000000000, 9999999999999999))
		print("""
CV NUMBER: """, random.randint(100, 999))
		print("""
EXPIRE DATE: """, random.choice(b))
		print("""
BRAND: """, random.choice(a), Style.RESET_ALL)
		print("""
		
	       BOOM BOOM BOOM
	       card has been hacked for you
		
		""")
		break
		
	elif gee == "2":
		os.system('cls')
		time.sleep(5)
		print(Fore.RED, """

card number: """, random.randint(1000000000000000, 9999999999999999))
		print("CV number: ", random.randint(100, 999))
		print("expire date: ", random.choice(b))
		print("BRAND: ", random.choice(a), Style.RESET_ALL)
		print("""
		
	       BOOM BOOM BOOM 
	       
	       card has been hacked for you
		
		""")
		break
		
	elif gee == "3":
		time.sleep(5)
		os.system('cls')
		print("""+=========================================+
|..........   V̿•I̿•P̿➸➸H̿A̿C̿K̿E̿R̿✔✔  ...........|
              ▇▇▇▇▇▇▇▇▇▇▇▇
Author: ABDULGEE 

member in: HAUSA_HACKERS/HAUSA_PROGRAMNERS/CYBER_XPLOIT_HAUSA

phone info: +2348131116661

fb_account: Abdul gee

☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠

_______________HAUSA PROGRAMMERS_________________
::::::::::----------TOOL----------::::::::::

		""")
		break
	elif gee == "4":
		os.system('cls')
		time.sleep(3)
		print("coming soon.....")
		break
 	
 	