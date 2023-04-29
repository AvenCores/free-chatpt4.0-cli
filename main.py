from gpt4free import Provider
from termcolor import colored
from sys import platform
from os import system
import gpt4free

def clear():
	if platform == "linux" or platform == "linux2" or platform == "unix":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		system("clear")

clear()
colors = ['red', 'yellow', 'green', 'cyan', 'light_blue', 'magenta']
color_index = 0
bannercli ="""███████╗██████╗░███████╗███████╗  ░█████╗░██╗░░██╗░█████╗░████████╗░██████╗░██████╗░████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝  ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔════╝░██╔══██╗╚══██╔══╝
█████╗░░██████╔╝█████╗░░█████╗░░  ██║░░╚═╝███████║███████║░░░██║░░░██║░░██╗░██████╔╝░░░██║░░░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░  ██║░░██╗██╔══██║██╔══██║░░░██║░░░██║░░╚██╗██╔═══╝░░░░██║░░░
██║░░░░░██║░░██║███████╗███████╗  ╚█████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░"""

for i in range(len(bannercli)):
    color = colors[i % len(colors)]
    print(colored(bannercli[i], color), end="")
print(colored("\n\nAuthor: ", "red") + "@avencores")
print(colored("Telegram channel: ", "red") + "@hzfnews")
while True:
    youinput = input(colored("\n👨 You ", "yellow") + colored(">> ", "green"))
    try:
        response = gpt4free.Completion.create(Provider.Theb, prompt=youinput)
        output = response
        print(colored("\n🤖 CHATGPT V4.0 ", "cyan") + colored(">> ", "green") +  output)
    except Exception as e:
	    print(colored("\n🛑 ERROR ", "light_red") + colored(">> ", "green") + str(e))
