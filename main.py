from pyfiglet import Figlet
from colorama import init, Fore, Style
import random
import time
import os


init(autoreset=True)

f = Figlet(font="digital")
hello = f.renderText("DUNGEON & DICE")

print(Fore.GREEN + hello)

prologue = """
Legends speak of the Obsidian Dice, relics forged by the gods of chance and fate.
Each roll shapes fate and gods themselves - warriors have risen, kingdoms have fallen.
You are Orpehus the Wanderer - a down-on-their-luck adveturer who discovers an entrance of the Endless Dungeon. 
The dungeon is cursed: every creature inside is bound by the rules of the dice - and you once you are inside. 
To survive, you must duel monsters in games of chance and strength - rolling the dice that decides your destiny.

The Dicebound Curse: No one can attack without rolling.
The Dungeons Whisper: After  a voice taunts or encourages you.
Potions of Fortune: Rare brews that tilt - or twist - your odds.
"""
print(Fore.CYAN + prologue.strip())
input(Fore.LIGHTGREEN_EX + "Press any key to continue...")
os.system('cls' if os.name == 'nt' else 'clear')
