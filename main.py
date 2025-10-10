from pyfiglet import Figlet
from colorama import init, Fore, Style
import random
import time
import os
import math

# Predefined constants to  make u lose this game.
levels = [
    {"id": 1, "name": "Training Hall", "monster": "Goblin", "enemy_die" : 4, "hp":8, "special": None, "reward":"potion"},
    {"id": 2, "name": "Rat Warens", "monster": "Giant Rat", "enemy_die" : 6, "hp":10, "special": None, "reward":"potion"},
    {"id": 3, "name": "Bandit Ambush", "monster": "Bandit", "enemy_die": 6, "hp": 14},
    {"id": 4, "name": "Cave Beetle", "monster": "Armored Beetle", "enemy_die": 6, "hp": 18, "special": "armor", "reward": "armor_shard"},
    {"id": 5, "name": "Cultist Circle", "monster": "Dice Caster", "enemy_die": 8, "hp": 16, "special": "variable_die", "reward": "fortune_potion"},
    {"id": 6, "name": "Shadow Scout", "monster": "Stalker", "enemy_die": 6, "hp": 15, "special": "preemptive", "reward": "stealth_cloak"},
    {"id": 7, "name": "Ruinous Bridge", "monster": "Troll", "enemy_die": 8, "hp": 24, "special": "regenerate", "reward": "healing_herb"},
    {"id": 8, "name": "Blighted Grove", "monster": "Elemental", "enemy_die": 8, "hp": 20, "special": "status_affect", "reward": "ember_seal"},
    {"id": 9, "name": "Knight's Trial", "monster": "Champion Knight", "enemy_die": 8, "hp": 26, "special": "parry", "reward": "ring_of_parry"},
    {"id":10, "name": "Hall of Echoes", "monster": "Echo Wraith", "enemy_die": 10, "hp": 22, "special": "mirror_roll", "reward": "echo_shard"},
    {"id":11, "name": "Fungal Depths", "monster": "Mire Fungus", "enemy_die": 6, "hp": 18, "special": "poison_spore", "reward": "antidote"},
    {"id":12, "name": "Ironworks", "monster": "Golem", "enemy_die":10, "hp": 30, "special": "heavy_armor", "reward": "metal_fragment"},
    {"id":13, "name": "Frozen Hall", "monster": "Frost Warden", "enemy_die": 8, "hp": 22, "special": "freeze", "reward": "cold_essence"},
    {"id":14, "name": "Siren's Hall", "monster": "Siren", "enemy_die": 6, "hp": 20, "special": "charm", "reward": "focus_charm"},
    {"id":15, "name": "Graveyard Gate", "monster": "Bone Lord", "enemy_die": 10, "hp": 28, "special": "necrotic", "reward": "bone_token"},
    {"id":16, "name": "Tower of Luck", "monster": "Fortune Sprite", "enemy_die": 4, "hp": 12, "special": "reroll_grant", "reward": "reroll_token"},
    {"id":17, "name": "Mad Altar", "monster": "Chaos Priest", "enemy_die": 12, "hp": 26, "special": "swap_effects", "reward": "chaos_draught"},
    {"id":18, "name": "Brimstone Pits", "monster": "Fire Hound", "enemy_die": 8, "hp": 24, "special": "burn", "reward": "flame_gland"},
    {"id":19, "name": "Glass Maze", "monster": "Mirror Knight", "enemy_die": 10, "hp": 26, "special": "copy", "reward": "mirror_shard"},
    {"id":20, "name": "Storm Gallery", "monster": "Tempest Drake", "enemy_die": 10, "hp": 32, "special": "multi_attack", "reward": "storm_scale"},
    {"id":21, "name": "Hidden Arena", "monster": "Duelist", "enemy_die": 8, "hp": 28, "special": "skill_rolls", "reward": "duelist_banner"},
    {"id":22, "name": "Cursed Library", "monster": "Librarian Shade", "enemy_die": 6, "hp": 20, "special": "curse", "reward": "cursed_tome"},
    {"id":23, "name": "Broken Sewers", "monster": "Muck Leviathan", "enemy_die": 12, "hp": 36, "special": "acid", "reward": "slime_core"},
    {"id":24, "name": "Sunken Vault", "monster": "Treasure Wight", "enemy_die": 10, "hp": 30, "special": "loot_steal", "reward": "vault_key"},
    {"id":25, "name": "Warden's Keep", "monster": "Iron Warden", "enemy_die": 12, "hp": 38, "special": "stun_on_high", "reward": "warden_plate"},
    {"id":26, "name": "Chamber of Whispers", "monster": "Whisperer", "enemy_die": 8, "hp": 24, "special": "voice_debuff", "reward": "whisper_note"},
    {"id":27, "name": "Feral Pits", "monster": "Ravager", "enemy_die": 10, "hp": 34, "special": "berserk", "reward": "raging_fang"},
    {"id":28, "name": "Veil of Mist", "monster": "Phantom", "enemy_die": 8, "hp": 26, "special": "ethereal", "reward": "veil_cloth"},
    {"id":29, "name": "Abyssal Gate", "monster": "Abyssal Knight", "enemy_die": 12, "hp": 42, "special": "phase_shift", "reward": "abyss_medallion"},
    {"id": 30, "name": "Obsidian Sanctum", "monster": "Guardian of the Obsidian Dice", "enemy_die": 12, "hp": 80, "special": "phases", "reward": "obsidian dice"}
]

class Player:
    def __init__(self, name="Orpehus"):
        self.name = name
        self.max_hp = 30
        self.hp = self.max_hp
        self.armor = 0
        self.crit_chance = 0.05 # well well well

        self.rerolls = 1 
        self.potions = {"healing": 2, "fortune": 1}
        self.gold = 0
        self.inventory = [] # if u want smthing, earn it lol

        self.player_die = 6
        self.status = {"burn": 0, "stun": 0, "freeze": 0}

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp
    
    def take_damage(self, amount):
        reduced = max(0, amount - self.armor)
        self.hp = max(0, self.hp - reduced)
        return reduced
    
    def use_potion(self, potion):
        if self.potions.get(potion, 0) > 0:
            self.potions[potion] -= 1
            if potion == "healing":
                self.heal(10)
            elif potion == "fortune":
                # externally called lol
                return "fortune_active"
            return True
        return False
    def add_item(self, item):
        self.inventory.append(item)

    def is_alive(self):
        return self.hp > 0
    
def roll(sides=6, times=1, advantage=None):
    """
    Roll 'times' dice of 'sides'.advantage=None | 'adv' | 'dis
    Returns single value (highest/lowest for advantage) for sum if times > 1
    """
    results = [random.randint(1, sides) for _ in range(times)]
    if advantage == 'adv':
        return max(results)
    if advantage == 'dis':
        return min(results)
    return sum(results)
class Enemy:
    def __init__(self, name, hp, die = 6, special=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.die = die
        self.special = special or None
        self.armor = 0
    
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        reduced = max(0, amount - self.armor)
        self.hp = max(0, self.hp - reduced)
        return reduced

    def attack_roll(self):
        return random.randint(1, self.die)
    
def resolve_attack(attacker_is_player, atk_roll, def_roll, player_obj=None):
    """
    Simple resolution
    -higher rolls deals damage equal to roll.
    -player crit double dmage based on crit_chance.
    """
    if atk_roll > def_roll:
        damage = atk_roll
        if attacker_is_player and player_obj and random.random() < player_obj.crit_chance:
            damage *= 2
            return True, damage, "Critical Hit"
        return True, damage, "Hit"
    elif atk_roll < def_roll:
        damage = def_roll
        return False, damage, "Enemy hit"
    else:
        #tie
        return None, 1, "Tie: glancing blows"

def run_encounter(level_cfg, player_obj):
    enemy = Enemy(level_cfg["monster"], level_cfg["hp"], die=level_cfg.get("enemy_die", 6), special=level_cfg.get("special"))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + f"Level {level_cfg['id']}: {level_cfg['name']} — {enemy.name} appears!")
    while player_obj.is_alive() and enemy.is_alive():
        print(Fore.CYAN + f"\nPlayer HP: {player_obj.hp}/{player_obj.max_hp}  Enemy HP: {enemy.hp}/{enemy.max_hp}")
        print("Actions: [r]oll [a]ttack  [p]otion  [d]efend  [q]uit")
        choice = input("> ").strip().lower()
        if choice == 'q':
            print("You flee... save later.")
            return False
        if choice == 'p':
            used = player_obj.use_potion("healing")
            print("Used healing potion." if used else "No potions left.")
            continue
        if choice == 'd':
            print("You brace for impact. (defend reduces next enemy damage)")
            player_obj.armor += 2
            eroll = enemy.attack_roll()
            pr = roll(player_obj.player_die)
            won, dmg, desc = resolve_attack(False, eroll, pr, player_obj)
            dmg_done = player_obj.take_damage(dmg)
            print(Fore.RED + f"Enemy rolled {eroll} and dealt {dmg_done} damage ({desc})")
            player_obj.armor = max(0, player_obj.armor - 2)
            continue
        adv = 'adv' if enemy.special == 'advantage' else None
        player_roll = roll(player_obj.player_die, advantage=adv)
        enemy_roll = enemy.attack_roll()
        res, dmg, desc = resolve_attack(True, player_roll, enemy_roll, player_obj)
        if res is True:
            dealt = enemy.take_damage(dmg)
            print(Fore.GREEN + f"You rolled {player_roll} vs {enemy_roll} — {desc}. Enemy takes {dealt} damage.")
        elif res is False:
            taken = player_obj.take_damage(dmg)
            print(Fore.RED + f"You rolled {player_roll} vs {enemy_roll} — {desc}. You take {taken} damage.")
        else:
            player_obj.take_damage(dmg)
            enemy.take_damage(dmg)
            print(Fore.YELLOW + f"Tie! Both take {dmg} damage.")

    if player_obj.is_alive():
        print(Fore.GREEN + f"You defeated the {enemy.name}!")
        reward = level_cfg.get("reward")
        if reward == "potion":
            player_obj.potions["healing"] = player_obj.potions.get("healing", 0) + 1
            print("Found a healing potion.")
        elif reward == "reroll_token":
            player_obj.rerolls += 1
            print("Gained a reroll token.")
        else:
            if reward:
                player_obj.add_item(reward)
                print(f"Obtained {reward}.")
        dungeon_whisper(victories=level_cfg["id"], mood='encourage')
        return True
    else:
        print(Fore.RED + "You have fallen...")
        dungeon_whisper(mood='taunt')
        return False
# Dungeon whispers for flavor text
WHISPERS = [
    "A cold wind fades as you roll.",
    "The dice twist in your palm.",
    "You smell victory... or is it fear?",
    "The dungeon hungers for another soul.",
    "Luck favors the bold, or so they say.",
    "A jealous echo applauds your roll.",
    "The shadows seem to watch your every move.",
    "You hear a faint whisper: 'Roll wisely.'",
    "A distant laugh echoes after your defeat.",
    "The air thickens as you grip the dice.",
    "Your fate is sealed with every toss.",
    "The walls seem to shift with your luck.",
    "A voice murmurs: 'Fortune is fickle.'"
]

def dungeon_whisper(victories=None, mood=None, delay=0.3):
    """
    Print a dungeon whisper.
    - victories: optional int to add story-beat messages
    - mood: 'taunt' | 'encourage' to bias selection
    Returns the chosen message (useful for tests/logging).
    """
    msgs = WHISPERS.copy()
    # add progression-based lines
    if victories is not None:
        if victories >= 10:
            msgs.append("The Guardian watches. Hear its chuckle between rolls.")
        elif victories >= 6:
            msgs.append("A shadow watches you from the steps.")
        elif victories >= 3:
            msgs.append("You find a bloodstained note: 'Luck is a lie.'")

    # simple mood biasing
    if mood == 'encourage':
        biased = [m for m in msgs if any(k in m.lower() for k in ('favor','victory','applaud','smell'))]
        msgs = biased or msgs
    elif mood == 'taunt':
        biased = [m for m in msgs if any(k in m.lower() for k in ('fades','die','jealous','hunger','twist'))]
        msgs = biased or msgs

    msg = random.choice(msgs)
    print(Style.NORMAL + Fore.YELLOW + str(msg))
    time.sleep(delay)
    return msg

# --- NEW: story beats and milestone vignettes ---
STORY_BEATS = {
    1: "The entrance groans shut behind you. The torches smell of old luck.",
    3: "You find a bloodstained note: 'Luck is a lie. The dice choose who deserves to live.'",
    6: "A shadowy figure lingers in the stairwell, watching your hands.",
    9: "You pass an altar of rusted dice. Coins and names are nailed to it.",
    12: "A child's lullaby echoes from deeper halls — you remember nothing of your past.",
    15: "The air tastes metallic. You tighten your grip; something waits above.",
    18: "Carvings on the wall show a face that looks suspiciously like yours.",
    21: "You wake mid-roll in a pile of bones. The dice were still warm.",
    24: "A voice whispers: 'The Obsidian Dice are closer than you think.'",
    27: "You see the Guardian's sigil scorched into the floor ahead.",
    30: "The Obsidian Dice hum in the dark. The final door breathes open."
}
def show_story_beat(victories):
    """
    Print a story beat for the given victory count, or a short vignette
    for milestones. Returns the printed message or None.
    """
    msg = STORY_BEATS.get(victories)
    if not msg:
        # occasional small vignette every 5 levels
        if victories % 5 == 0:
            vignette = [
                "The dungeon's whisper lingers as you move on.",
                "You find a scrap of cloth — the pattern feels important.",
                "Distant metal clanks like a clock counting down.",
            ]
            msg = random.choice(vignette)
    if msg:
        print(Style.BRIGHT + Fore.MAGENTA + msg)
        # short thematic whisper after the beat
        dungeon_whisper(victories=victories, mood='taunt' if victories % 2 == 1 else 'encourage', delay=0.2)
        return msg
    return None

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

# ...existing code...

# GAME ON!!!
init(autoreset=True)

# ...existing code...

player = Player()
for lvl in levels:
    win = run_encounter(lvl, player)
    if not win:
        print(Fore.RED + "Game Over!")
        break
    # show story beats / vignettes tied to progression
    show_story_beat(lvl["id"])
    input(Fore.LIGHTGREEN_EX + "Press Enter for the next floor...")
    os.system('cls' if os.name == 'nt' else 'clear')