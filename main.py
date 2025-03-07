from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget


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
item_placement_container = [
    "Item Placement",
    item_placement_dropdown,
    item_placement_options,
]

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
accessibility_container = [
    "Accessibility",
    accessibility_dropdown,
    accessibility_options,
]

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
ganon_vulnerable_container = [
    "Ganon Vulnerable",
    ganon_vulnerable_dropdown,
    ganon_vulnerable_options,
]

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
entrance_shuffle_container = [
    "Entrance Shuffle",
    entrance_shuffle_dropdown,
    entrance_shuffle_options,
]

boss_shuffle_dropdown = DropDown()
boss_shuffle_options = [
    ["none", "None"],
    ["simple", "Simple"],
    ["full", "Full"],
    ["random", "Random"],
]
boss_shuffle_container = ["Boss Shuffle", boss_shuffle_dropdown, boss_shuffle_options]

enemy_shuffle_dropdown = DropDown()
enemy_shuffle_options = [
    ["none", "None"],
    ["shuffled", "Shuffled"],
    ["random", "Random"],
]
enemy_shuffle_container = [
    "Enemy Shuffle",
    enemy_shuffle_dropdown,
    enemy_shuffle_options,
]

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
item_pool_options = [
    ["normal", "Normal"],
    ["hard", "Hard"],
    ["expert", "Expert"],
    ["crowdcontrol", "Crowd Control"],
]
item_pool_container = ["Item Pool", item_pool_dropdown, item_pool_options]

item_function_dropdown = DropDown()
item_function_options = [["normal", "Normal"], ["hard", "Hard"], ["expert", "Expert"]]
item_function_container = [
    "Item Function",
    item_function_dropdown,
    item_function_options,
]

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
class Dropdowns(BoxLayout):
    def __init__(self, name, options=[], *args, **kwargs):
        super(Dropdowns, self).__init__(*args, **kwargs)
        dropdown = DropDown()
        self.add_widget(dropdown)
        button = Button(text=name, size_hint=(None,None), on_release= lambda instance, x: dropdown.open())
        self.add_widget(button)
        for option in options:
            option_button = Button(
                    text=option[1],
                    height=35,
                    size_hint_y=None,
                    on_release=lambda x: dropdown.select(option[1]),
                )
            dropdown.add_widget(option_button)

class AgaseedApp(App):
    def build(self):
        root = GridLayout(cols=2)
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Item Placement", item_placement_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        layout.add_widget(Dropdowns("Glitches", glitches_options))
        root.add_widget(layout)
        root.add_widget(Button(text="right"))
        return root


if __name__ == "__main__":
    AgaseedApp().run()
