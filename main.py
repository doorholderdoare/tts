from gtts import gTTS
import os
from colored import fg
import ctypes
from time import sleep

ctypes.windll.kernel32.SetConsoleTitleW("Text To Speech - By Kqcy")

msg = input(f"Message -\n{fg(204)}> {fg(15)}")
lang = "en"
os.system("cls")

print(f"{fg(204)}> {fg(15)}Creating file{fg(15)}")
sleep(.4)
os.system("cls")
print(f"{fg(204)}> {fg(15)}Creating file.{fg(15)}")
sleep(.4)
os.system("cls")
print(f"{fg(204)}> {fg(15)}Creating file..{fg(15)}")
sleep(.4)
os.system("cls")
print(f"{fg(204)}> {fg(15)}Creating file...{fg(15)}")
sleep(.4)
und = msg.replace(" ", "_")
tts = gTTS(text=msg, lang=lang, slow=False)
tts.save(f"{und}.mp3")

os.system("cls")

sleep(.4)
print(f"{fg(204)}> {fg(15)}Saved file under {fg(204)}{und}.mp3{fg(15)}")
sleep(0.7)
os.system("cls")
input(f"{fg(204)}> {fg(15)}Press enter to exit")
os.system("cls")
exit()