from pyfiglet import Figlet
from colorama import init, Fore, Style
import random
import time
import os
import math

# Predefined constants to  make u lose this game.
levels = [
    {"id": 1, "name": "Training Hall", "monster": "Goblin", "enemy_die": 4, "hp": 8, "special": None, "reward": "armor_shard"},
    {"id": 2, "name": "Rat Warrens", "monster": "Giant Rat", "enemy_die": 6, "hp": 10, "special": None, "reward": "armor_shard"},
    {"id": 3, "name": "Bandit Ambush", "monster": "Bandit", "enemy_die": 6, "hp": 14, "special": "advantage", "reward": "armor_shard"},
    {"id": 4, "name": "Cave Beetle", "monster": "Armored Beetle", "enemy_die": 6, "hp": 18, "special": "armor", "reward": "armor_shard"},
    {"id": 5, "name": "Cultist Circle", "monster": "Dice Caster", "enemy_die": 8, "hp": 16, "special": "variable_die", "reward": "fortune_potion"},
    {"id": 6, "name": "Shadow Scout", "monster": "Stalker", "enemy_die": 6, "hp": 15, "special": "preemptive", "reward": "stealth_cloak"},
    # Special level 7
    {"id": 7, "name": "Void Nexus", "monster": "Void Sentinel", "enemy_die": 12, "hp": 100, "special": "void_absorb", "reward": "void_essence", "special_level": True},
    {"id": 8, "name": "Ruinous Bridge", "monster": "Troll", "enemy_die": 8, "hp": 24, "special": "regenerate", "reward": "healing_herb"},
    {"id": 9, "name": "Blighted Grove", "monster": "Elemental", "enemy_die": 8, "hp": 20, "special": "status_affect", "reward": "ember_seal"},
    {"id": 10, "name": "Knight's Trial", "monster": "Champion Knight", "enemy_die": 8, "hp": 26, "special": "parry", "reward": "ring_of_parry"},
    {"id": 11, "name": "Hall of Echoes", "monster": "Echo Wraith", "enemy_die": 10, "hp": 22, "special": "mirror_roll", "reward": "echo_shard"},
    {"id": 12, "name": "Fungal Depths", "monster": "Mire Fungus", "enemy_die": 6, "hp": 18, "special": "poison_spore", "reward": "antidote"},
    # Special level 13
    {"id": 13, "name": "Eternal Flame", "monster": "Infernal Phoenix", "enemy_die": 12, "hp": 110, "special": "rebirth", "reward": "phoenix_feather", "special_level": True},
    {"id": 14, "name": "Ironworks", "monster": "Golem", "enemy_die": 10, "hp": 30, "special": "heavy_armor", "reward": "metal_fragment"},
    {"id": 15, "name": "Frozen Hall", "monster": "Frost Warden", "enemy_die": 8, "hp": 22, "special": "freeze", "reward": "cold_essence"},
    {"id": 16, "name": "Siren's Hall", "monster": "Siren", "enemy_die": 6, "hp": 20, "special": "charm", "reward": "focus_charm"},
    {"id": 17, "name": "Graveyard Gate", "monster": "Bone Lord", "enemy_die": 10, "hp": 28, "special": "necrotic", "reward": "bone_token"},
    {"id": 18, "name": "Tower of Luck", "monster": "Fortune Sprite", "enemy_die": 4, "hp": 12, "special": "reroll_grant", "reward": "reroll_token"},
    # Special level 19
    {"id": 19, "name": "Crystal Cavern", "monster": "Crystal Colossus", "enemy_die": 12, "hp": 120, "special": "reflect", "reward": "crystal_heart", "special_level": True},
    {"id": 20, "name": "Mad Altar", "monster": "Chaos Priest", "enemy_die": 12, "hp": 26, "special": "swap_effects", "reward": "chaos_draught"},
    {"id": 21, "name": "Brimstone Pits", "monster": "Fire Hound", "enemy_die": 8, "hp": 24, "special": "burn", "reward": "flame_gland"},
    {"id": 22, "name": "Glass Maze", "monster": "Mirror Knight", "enemy_die": 10, "hp": 26, "special": "copy", "reward": "mirror_shard"},
    {"id": 23, "name": "Storm Gallery", "monster": "Tempest Drake", "enemy_die": 10, "hp": 32, "special": "multi_attack", "reward": "storm_scale"},
    {"id": 24, "name": "Hidden Arena", "monster": "Duelist", "enemy_die": 8, "hp": 28, "special": "skill_rolls", "reward": "duelist_banner"},
    # Special level 25
    {"id": 25, "name": "Shadow Realm", "monster": "Shadow Overlord", "enemy_die": 12, "hp": 130, "special": "shadow_clone", "reward": "shadow_orb", "special_level": True},
    {"id": 26, "name": "Cursed Library", "monster": "Librarian Shade", "enemy_die": 6, "hp": 20, "special": "curse", "reward": "cursed_tome"},
    {"id": 27, "name": "Broken Sewers", "monster": "Muck Leviathan", "enemy_die": 12, "hp": 36, "special": "acid", "reward": "slime_core"},
    {"id": 28, "name": "Sunken Vault", "monster": "Treasure Wight", "enemy_die": 10, "hp": 30, "special": "loot_steal", "reward": "vault_key"},
    {"id": 29, "name": "Warden's Keep", "monster": "Iron Warden", "enemy_die": 12, "hp": 38, "special": "stun_on_high", "reward": "warden_plate"},
    {"id": 30, "name": "Chamber of Whispers", "monster": "Whisperer", "enemy_die": 8, "hp": 24, "special": "voice_debuff", "reward": "whisper_note"},
    # Special level 31
    {"id": 31, "name": "Time Rift", "monster": "Chronos Beast", "enemy_die": 12, "hp": 140, "special": "time_rewind", "reward": "chrono_crystal", "special_level": True},
    {"id": 32, "name": "Feral Pits", "monster": "Ravager", "enemy_die": 10, "hp": 34, "special": "berserk", "reward": "raging_fang"},
    {"id": 33, "name": "Veil of Mist", "monster": "Phantom", "enemy_die": 8, "hp": 26, "special": "ethereal", "reward": "veil_cloth"},
    {"id": 34, "name": "Abyssal Gate", "monster": "Abyssal Knight", "enemy_die": 12, "hp": 42, "special": "phase_shift", "reward": "abyss_medallion"},
    {"id": 35, "name": "Obsidian Sanctum", "monster": "Guardian of the Obsidian Dice", "enemy_die": 12, "hp": 80, "special": "phases", "reward": "obsidian_dice"},
    # fun last level ig. Matches the terminalcraft theme...
    {"id": 36, "name": "Terminal", "monster": "Commander Terminal", "enemy_die": 200, "hp": 100, "special":"knows every linux command and has been learning haskell since fire was invented!!!!!!!!"}
]

class Player:
    def __init__(self, name="Orpehus"):
        self.name = name
        self.max_hp = 30
        self.hp = self.max_hp
        self.armor = 0
        self.crit_chance = 0.05  # base crit

        self.rerolls = 1 
        self.potions = {"healing": 2, "fortune": 1}
        self.gold = 0
        self.inventory = []  # for non-auto items

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
                # externally called
                return "fortune_active"
            return True
        return False
    
    def add_item(self, item):
        self.inventory.append(item)

    def is_alive(self):
        return self.hp > 0
    
    # NEW: method to apply armor upgrade (increases max HP and heals)
    def upgrade_armor(self, amount=1):
        self.armor += amount
        hp_boost = amount * 5  # each armor point = +5 max HP
        self.max_hp += hp_boost
        self.hp += hp_boost  # heal for the boost
        print(Fore.BLUE + f"Armor upgraded! +{amount} armor, +{hp_boost} max HP (total armor: {self.armor}, max HP: {self.max_hp}).")

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
        elif choice == 'p':
            used = player_obj.use_potion("healing")
            print("Used healing potion." if used else "No potions left.")
            continue
        elif choice == 'd':
            print("You brace for impact. (defend reduces next enemy damage)")
            player_obj.armor += 2
            eroll = enemy.attack_roll()
            pr = roll(player_obj.player_die)
            won, dmg, desc = resolve_attack(False, eroll, pr, player_obj)
            dmg_done = player_obj.take_damage(dmg)
            print(Fore.RED + f"Enemy rolled {eroll} and dealt {dmg_done} damage ({desc})")
            player_obj.armor = max(0, player_obj.armor - 2)
            continue
        elif choice in ('a', 'attack', 'r', 'roll'):
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
        else:
            print(Fore.YELLOW + "Wrong option, adventurer.")
            input("Press ENTER to retry...")
            continue


    if player_obj.is_alive():
        print(Fore.GREEN + f"You defeated the {enemy.name}!")
        reward = level_cfg.get("reward")
        if reward == "potion":
            player_obj.potions["healing"] = player_obj.potions.get("healing", 0) + 1
            print("Found a healing potion.")
        elif reward == "reroll_token":
            player_obj.rerolls += 1
            print("Gained a reroll token.")
        elif reward in ["armor_shard", "metal_fragment", "warden_plate"]:  # armor upgrade items
            player_obj.upgrade_armor(1)
        elif reward == "fortune_potion":
            player_obj.crit_chance += 0.05  # +5% crit chance
            print(Fore.BLUE + f"Obtained {reward}! Crit chance increased to {player_obj.crit_chance * 100:.0f}%.")
        elif reward == "stealth_cloak":
            player_obj.upgrade_armor(1)  # extra armor
            print(Fore.BLUE + f"Obtained {reward}! Extra armor applied.")
        elif reward == "healing_herb":
            player_obj.potions["healing"] += 1
            print(Fore.BLUE + f"Obtained {reward}! Healing potions increased.")
        elif reward == "ember_seal":
            player_obj.player_die = max(player_obj.player_die, 8)  # upgrade die to d8
            print(Fore.BLUE + f"Obtained {reward}! Player die upgraded to d{player_obj.player_die}.")
        elif reward == "ring_of_parry":
            # reduce enemy damage by 1 permanently (simple debuff)
            print(Fore.BLUE + f"Obtained {reward}! Enemy damage reduced by 1 (applied globally).")
            # Note: implement in resolve_attack if needed
        elif reward == "echo_shard":
            player_obj.rerolls += 1  # free reroll
            print(Fore.BLUE + f"Obtained {reward}! Gained an extra reroll.")
        elif reward == "antidote":
            # cure all status effects
            player_obj.status = {"burn": 0, "stun": 0, "freeze": 0}
            print(Fore.BLUE + f"Obtained {reward}! All status effects cured.")
        elif reward == "cold_essence":
            # freeze enemy (reduce their die by 2 for next encounter, but simple: +1 armor vs them)
            print(Fore.BLUE + f"Obtained {reward}! Frost resistance: +1 armor vs cold enemies.")
            player_obj.upgrade_armor(1)
        elif reward == "focus_charm":
            # ignore charm (no effect yet, but placeholder)
            print(Fore.BLUE + f"Obtained {reward}! Charm resistance gained.")
        elif reward == "bone_token":
            # necrotic boost: +2 damage on next attack (temporary)
            print(Fore.BLUE + f"Obtained {reward}! Necrotic power: +2 damage on next roll.")
            # Implement in roll or resolve_attack if needed
        elif reward == "chaos_draught":
            # random effect: +1 crit or -1 armor
            if random.random() > 0.5:
                player_obj.crit_chance += 0.05
                print(Fore.BLUE + f"Obtained {reward}! Chaotic boost: +5% crit chance.")
            else:
                player_obj.armor = max(0, player_obj.armor - 1)
                print(Fore.YELLOW + f"Obtained {reward}! Chaotic curse: -1 armor.")
        elif reward == "flame_gland":
            # burn status: enemy takes 2 damage per turn (placeholder)
            print(Fore.BLUE + f"Obtained {reward}! Flame gland: Enemies burn for 2 damage/turn.")
        elif reward == "mirror_shard":
            # copy enemy roll once
            print(Fore.BLUE + f"Obtained {reward}! Mirror shard: Can copy enemy roll once.")
        elif reward == "storm_scale":
            # multi-attack: roll twice, take higher
            print(Fore.BLUE + f"Obtained {reward}! Storm scale: Advantage on rolls.")
            # Apply in roll function
        elif reward == "duelist_banner":
            # permanent advantage
            print(Fore.BLUE + f"Obtained {reward}! Duelist banner: Permanent advantage on attacks.")
        elif reward == "cursed_tome":
            # curse: -5% crit
            player_obj.crit_chance = max(0, player_obj.crit_chance - 0.05)
            print(Fore.YELLOW + f"Obtained {reward}! Cursed: -5% crit chance.")
        elif reward == "slime_core":
            # acid: ignore 1 enemy armor
            print(Fore.BLUE + f"Obtained {reward}! Slime core: Ignore 1 enemy armor.")
        elif reward == "vault_key":
            player_obj.gold += 50  # extra gold
            print(Fore.BLUE + f"Obtained {reward}! +50 gold.")
        elif reward == "whisper_note":
            # extra whisper
            dungeon_whisper(mood='encourage')
        elif reward == "raging_fang":
            # berserk: +2 damage but take 1 recoil
            print(Fore.BLUE + f"Obtained {reward}! Raging fang: +2 damage, but -1 HP recoil.")
        elif reward == "veil_cloth":
            # ethereal: 20% dodge chance
            print(Fore.BLUE + f"Obtained {reward}! Veil cloth: 20% dodge chance.")
        elif reward == "abyss_medallion":
            # phase shift: heal 10 HP
            player_obj.heal(10)
            print(Fore.BLUE + f"Obtained {reward}! Healed 10 HP.")
        elif reward == "obsidian_dice":
            print(Fore.GREEN + "You have claimed the Obsidian Dice! Victory is yours.")
            return True  # end game
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
input(Fore.LIGHTGREEN_EX + "Press ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

# GAME ON!!!
init(autoreset=True)

player = Player()
level_index = 0
while level_index < len(levels):
    lvl = levels[level_index]
    win = run_encounter(lvl, player)
    if not win:
        if lvl.get("special_level"):
            # Special level failure: halve HP and continue
            player.hp = player.hp // 2
            print(Fore.YELLOW + f"Special level failed! HP halved to {player.hp}.")
        else:
            print(Fore.RED + "Game Over!")
            break
    else:
        if lvl.get("special_level"):
            # Special level win: skip next level and +20 HP
            player.heal(20)
            print(Fore.GREEN + "Special level conquered! Skipped next level and gained +20 HP.")
            level_index += 1  # Skip next
        # show story beats / vignettes tied to progression
        show_story_beat(lvl["id"])
        input(Fore.LIGHTGREEN_EX + "Press Enter for the next floor...")
        os.system('cls' if os.name == 'nt' else 'clear')
    level_index += 1

print(Fore.GREEN + "Congratulations, you have completed the dungeon! Thanks for playing!")