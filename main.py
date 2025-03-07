from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


glitches_dropdown = DropDown()
glitches_options = [
    ["none", "No Glitches"],
    ["overworld glitches", "Overworld Glitches"],
    ["major glitches", "Major Glitches"],
    ["no logic", "No Logic"],
]
glitches_container = ["Glitches", glitches_dropdown, glitches_options]

item_placement_dropdown = DropDown()
item_placement_options = [
    ["basic", "Basic"],
    ["advanced", "Advanced"],
]
item_placement_container = ["Item Placement", item_placement_dropdown, item_placement_options]

shuffle_dropdown = DropDown()
shuffle_options = [
    ["standard", "Standard"],
    ["mapscompasses", "Maps / Compasses"],
    ["mapscompassessmallkeys", "Maps / Compasses / Small Keys"],
    ["keysanity", "Keysanity"],
]
shuffle_container = ["Shuffle", shuffle_dropdown, shuffle_options]

accessibility_dropdown = DropDown()
accessibility_options = [
    ["100percentinventory", "100% Inventory"],
    ["100percentlocations", "100% Locations"],
    ["beatableonly", "Beatable Only"],
]
accessibility_container = ["Accessibility", accessibility_dropdown, accessibility_options]

goal_dropdown = DropDown()
goal_options = [
    ["ganon", "Defeat Ganon"],
    ["fastganon", "Fast Ganon"],
    ["dungeons", "All Dungeons"],
    ["pedestal", "Master Sword Pedestal"],
    ["triforcepieces", "Triforce Pieces"],
    ["ganonhunt", "Ganon Hunt"],
    ["completionist", "Completionist"],
]
goal_container = ["Goal", goal_dropdown, goal_options]

open_tower_dropdown = DropDown()
open_tower_options = [
    ["7", "7 Crystals"],
    ["6", "6 Crystals"],
    ["5", "5 Crystals"],
    ["4", "4 Crystals"],
    ["3", "3 Crystals"],
    ["2", "2 Crystals"],
    ["1", "1 Crystal"],
    ["0", "0 Crystals"],
    ["random", "Random"],
]
open_tower_container = ["Open Tower", open_tower_dropdown, open_tower_options]

ganon_vulnerable_dropdown = DropDown()
ganon_vulnerable_options = [
    ["7", "7 Crystals"],
    ["6", "6 Crystals"],
    ["5", "5 Crystals"],
    ["4", "4 Crystals"],
    ["3", "3 Crystals"],
    ["2", "2 Crystals"],
    ["1", "1 Crystal"],
    ["0", "0 Crystals"],
    ["random", "Random"],
]
ganon_vulnerable_container = ["Ganon Vulnerable", ganon_vulnerable_dropdown, ganon_vulnerable_options]

world_state_dropdown = DropDown()
world_state_options = [
    ["standard", "Standard"],
    ["open", "Open"],
    ["inverted", "Inverted"],
    ["retro", "Retro"],
]
world_state_container = ["World State", world_state_dropdown, world_state_options]

entrance_shuffle_dropdown = DropDown()
entrance_shuffle_options = [
    ["none", "None"],
    ["simple", "Simple"],
    ["restricted", "Restricted"],
    ["full", "Full"],
    ["crossed", "Crossed"],
    ["insanity", "Insanity"],
]
entrance_shuffle_container = ["Entrance Shuffle", entrance_shuffle_dropdown, entrance_shuffle_options]

boss_shuffle_dropdown = DropDown()
boss_shuffle_options = [["none", "None"], ["simple", "Simple"], ["full", "Full"], ["random", "Random"]]
boss_shuffle_container = ["Boss Shuffle", boss_shuffle_dropdown, boss_shuffle_options]

enemy_shuffle_dropdown = DropDown()
enemy_shuffle_options = [
    ["none", "None"],
    ["shuffled", "Shuffled"],
    ["random", "Random"],
]
enemy_shuffle_container = ["Enemy Shuffle", enemy_shuffle_dropdown, enemy_shuffle_options]

hints_dropdown = DropDown()
hints_options = [["on", "On"], ["off", "Off"]]
hints_container = ["Hints", hints_dropdown, hints_options]

swords_dropdown = DropDown()
swords_options = [
    ["randomized", "Randomized"],
    ["assured", "Assured"],
    ["vanilla", "Vanilla"],
    ["swordless", "Swordless"],
]
swords_container = ["Swords", swords_dropdown, swords_options]

item_pool_dropdown = DropDown()
item_pool_options = [["normal", "Normal"], ["hard", "Hard"], ["expert", "Expert"], ["crowdcontrol", "Crowd Control"]]
item_pool_container = ["Item Pool", item_pool_dropdown, item_pool_options]

item_function_dropdown = DropDown()
item_function_options = [["normal", "Normal"], ["hard", "Hard"], ["expert", "Expert"]]
item_function_container = ["Item Function", item_function_dropdown, item_function_options]

enemy_damage_dropdown = DropDown()
enemy_damage_options = [
    ["default", "Default"],
    ["shuffled", "Shuffled"],
    ["random", "Random"],
]
enemy_damage_container = ["Enemy Damage", enemy_damage_dropdown, enemy_damage_options]

enemy_health_dropdown = DropDown()
enemy_health_options = [
    ["default", "Default"],
    ["easy", "Easy"],
    ["hard", "Hard"],
    ["expert", "Expert"],
]
enemy_health_container = ["Enemy Health", enemy_health_dropdown, enemy_health_options]

all_containers = [
    glitches_container,
    item_placement_container,
    shuffle_container,
    accessibility_container,
    goal_container,
    open_tower_container,
    ganon_vulnerable_container,
    world_state_container,
    entrance_shuffle_container,
    boss_shuffle_container,
    enemy_shuffle_container,
    hints_container,
    swords_container,
    item_pool_container,
    item_function_container,
    enemy_damage_container,
    enemy_health_container,
]



layout = GridLayout(cols=2)
inner_grid = GridLayout(cols=1)
layout.add_widget(inner_grid)


root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
root.add_widget(layout)
layout.bind(minimum_height=layout.setter('height'))

# create a big main button

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).

for name, dropdown, options in all_containers:
  button = Button(text=name, size_hint=(None, None))
  button.bind(on_release=dropdown.open)
  dropdown.bind(on_select=lambda instance, x: setattr(button, "text", x)) 
  for option in options:
      print(option)
      btn = Button(text=option[1], size_hint_y=None, height=44)
      btn.bind(on_release=lambda btn: dropdown.select(btn.text))
      dropdown.add_widget(btn)
  inner_grid.add_widget(button)
runTouchApp(root)

class AgaseedApp(App):
    def build(self):
        return root