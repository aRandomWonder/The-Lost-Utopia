from character import Player
from item import Item, basic_health_potion
from skillset import Skill, MAGIC_BULLET
from time import sleep as wait # Out of habbit, no particular reason

# I hereby confirm this is my own project and this idea is completely mine.
# (Yes, this is remenscent of all those rpgs, but hey.)
# The story and code, specifically.

# Side project. Free to use (though you probably wouldn't) with credit.
# I suck at commenting. Especially in HTML. Unrelated.
print("Little side project. Developement for main system of Eclipse.")
print("Still a work in progress, might become its own little thing, IDK.")
print("\"import this\"")
print("Also test ground. There are some examples in the main code area.\n\n\n")
wait(1)

player = Player()
player.skillset.append(MAGIC_BULLET)
player.inventory.append(basic_health_potion)
item = Item(name = "Testing Item", 
            description = "A little watter bottle that looks rather familiar.",
            effect = {})
skill = Skill(name = "Test Skill",
              effect = {"physical_damage": 10000},
              rs = 2,
              cooldown = 2
             )

# Testing Player ATTR - Success
"""
player.free_attr_points = 2
player.get_stats()
player.add_stats()
player.get_stats()
player.add_stats()
player.get_stats()
"""

# Testing Player Item Gain - Success
"""
player.add_item(item)
player.add_item("Hello World!")
"""

# Testing Player Skill Gain - Success
"""
player.free_skill_points = 3
player.show_skills()
player.learn_skill(MAGIC_BULLET)
player.show_skills()
player.learn_skill(skill)
player.show_skills()
"""

# Testing Player Inventory Viewing - Success
"""
player.get_inventory()
player.add_item(item)
player.get_inventory()
"""
