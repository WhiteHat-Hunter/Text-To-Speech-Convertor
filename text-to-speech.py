import pyfiglet

from colorama import init

from termcolor import colored

from gtts import gTTS

from playsound import playsound

init()

figlet = pyfiglet.figlet_format("TEXT-TO-SPEECH-CONVERTER", font = "digital" )

print(colored(figlet,'red'))

print(colored(" --------- Credits: SIDDHESH SURVE --------- ", 'blue'))

print(colored("\n-----------------------------------------------------------", 'green'))

speech = input("\nEnter Name of Speech to Save(*note* - add .mp3 at last of name) > ")
language = "en"

convert = gTTS(text = input("\nType Something you want to Convert into Speech > "),
          lang = language,slow = True)

convert.save(speech)
playsound(speech)
