from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from datetime import datetime
import copy
import random
import json
import asyncio
import pyz3r
import os

glitches_dropdown = DropDown()
glitches_options = [
    ["none", "No Glitches"],
    ["overworld_glitches", "Overworld Glitches"],
    ["hybrid_major_glitches", "Hybrid Major Glitches"],
    ["major_glitches", "Major Glitches"],
    ["no_logic", "No Logic"],
]
glitches_container = ["glitches", "Glitches", glitches_dropdown, glitches_options]

item_placement_dropdown = DropDown()
item_placement_options = [
    ["basic", "Basic"],
    ["advanced", "Advanced"],
]
item_placement_container = [
    "item_placement",
    "Item Placement",
    item_placement_dropdown,
    item_placement_options,
]

shuffle_dropdown = DropDown()
shuffle_options = [
    ["standard", "Standard"],
    ["mc", "Maps / Compasses"],
    ["mcs", "Maps / Compasses / Small Keys"],
    ["full", "Keysanity"],
]
shuffle_container = ["shuffle", "Shuffle", shuffle_dropdown, shuffle_options]

accessibility_dropdown = DropDown()
accessibility_options = [
    ["inventory", "100% Inventory"],
    ["locations", "100% Locations"],
    ["none", "Beatable Only"],
]
accessibility_container = [
    "accessibility",
    "Accessibility",
    accessibility_dropdown,
    accessibility_options,
]

goal_dropdown = DropDown()
goal_options = [
    ["ganon", "Defeat Ganon"],
    ["fast_ganon", "Fast Ganon"],
    ["dungeons", "All Dungeons"],
    ["pedestal", "Master Sword Pedestal"],
    ["triforce-hunt", "Triforce Pieces"],
    ["ganonhunt", "Ganon Hunt"],
    ["completionist", "Completionist"],
]
goal_container = ["goal", "Goal", goal_dropdown, goal_options]

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
open_tower_container = [
    "open_tower",
    "Open Tower",
    open_tower_dropdown,
    open_tower_options,
]

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
    "ganon_vulnerable",
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
world_state_container = [
    "world_state",
    "World State",
    world_state_dropdown,
    world_state_options,
]

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
    "entrances",
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
boss_shuffle_container = [
    "boss_shuffle",
    "Boss Shuffle",
    boss_shuffle_dropdown,
    boss_shuffle_options,
]

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
swords_container = ["enemy_shuffle", "Swords", swords_dropdown, swords_options]

item_pool_dropdown = DropDown()
item_pool_options = [
    ["normal", "Normal"],
    ["hard", "Hard"],
    ["expert", "Expert"],
    ["crowd_control", "Crowd Control"],
]
item_pool_container = ["item_pool", "Item Pool", item_pool_dropdown, item_pool_options]

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
enemy_damage_container = [
    "enemy_damage",
    "Enemy Damage",
    enemy_damage_dropdown,
    enemy_damage_options,
]

enemy_health_dropdown = DropDown()
enemy_health_options = [
    ["default", "Default"],
    ["easy", "Easy"],
    ["hard", "Hard"],
    ["expert", "Expert"],
]
enemy_health_container = [
    "enemy_health",
    "Enemy Health",
    enemy_health_dropdown,
    enemy_health_options,
]

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

settings = {
    "glitches": "none",
    "item_placement": "advanced",
    "shuffle": "standard",
    "accessibility": "items",
    "goal": "ganon",
    "open_tower": "7",
    "ganon_vulnerable": "7",
    "world_state": "open",
    "entrances": "none",
    "boss_shuffle": "none",
    "enemy_shuffle": "none",
    "swords": "randomized",
    "item_pool": "normal",
    "item_function": "normal",
    "spoilers": "on",
    "enemy_damage": "default",
    "enemy_health": "default",
    "hints": "on",
}

sprites = []
with open("sprites.json", "r") as file:
    data = json.load(file)
    sprites = data
base_path = "/sdcard"
debug_dir = "/Users/jayshaffer/dev/agaseed"
agaseed_dir = "/agaseed_output"

status_label = Label(
    text="", 
    size_hint_y=None, 
    size_hint_x=1,
    height=50, 
    color=(0, 0, 0, 1),
    pos=(1300, 400),
)


class GenerateSeedButton(Button):
    def on_release(self):
        setattr(generate_button, "disabled", True)
        try:
            asyncio.create_task(self.generate_seed())
        except Exception as e:
            setattr(status_label, "text", "Something went wrong")

        setattr(generate_button, "disabled", False)
            

    async def generate_seed(self):
        output_dir = agaseed_dir
        output_path = base_path
        if os.path.isdir(debug_dir):
            output_path = debug_dir
            print(
                "DEBUG: debug dir present, setting output path to: {}".format(
                    output_path
                )
            )

        if not os.path.isdir(output_path):
            print(
                "DEBUG: No valid destination found for output path: {}".format(
                    output_path
                )
            )
            return

        setattr(status_label, "text", "Generating Seed")
        output_path += output_dir
        print("DEBUG: Output path for seed generation set to: {}".format(output_path))
        try:
            seed = await pyz3r.ALTTPR.generate(
                settings={
                    "glitches": settings["glitches"],
                    "item_placement": settings["item_placement"],
                    "dungeon_items": settings["shuffle"],
                    "accessibility": settings["accessibility"],
                    "goal": settings["goal"],
                    "crystals": {
                        "ganon": settings["ganon_vulnerable"],
                        "tower": settings["open_tower"],
                    },
                    "mode": settings["world_state"],
                    "entrances": settings["entrances"],
                    "hints": settings["hints"],
                    "weapons": settings["swords"],
                    "item": {
                        "pool": settings["item_pool"],
                        "functionality": settings["item_function"],
                    },
                    "tournament": False,
                    "spoilers": "on",
                    "lang": "en",
                    "enemizer": {
                        "boss_shuffle": settings["boss_shuffle"],
                        "enemy_shuffle": settings["enemy_shuffle"],
                        "enemy_damage": settings["enemy_damage"],
                        "enemy_health": settings["enemy_health"],
                    },
                }
            )
        except Exception as e:
            setattr(status_label, "text", "Failed to generate seed: {}".format(e))
            
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        now = datetime.now()
        rom_folder = os.path.join(output_path, "{}-{}".format(now.isoformat(), seed.hash))

        if not os.path.isdir(rom_folder):
            os.mkdir(rom_folder)
            

        print("DEBUG: rom folder for seed: {}".format(rom_folder))
        output_filename = os.path.join(rom_folder, "{}.sfc".format(seed.hash))
        print("DEBUG: output filename for seed: {}".format(output_filename))

        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        try:
            await seed.create_patched_game(
                input_filename="dontsueme.sfc",  # this should be an ALTTP Japan 1.0 ROM
                output_filename=output_filename,  # this is the output ROM
                heartspeed="off",
                heartcolor="red",
                spritename=sprites[random.randint(0, len(sprites) - 1)][
                    "name"
                ],  # can be any sprite listed at https://alttpr.com/sprites
                music=False,  # true or false, defaults true
                quickswap=True,
                menu_speed="normal",
                msu1_resume=True,  # true or false, defaults true
            )
        
        except Exception as e:
            setattr(status_label, "text", "Failed to patch seed: {}".format(e))
            return
        spoiler = seed.get_formatted_spoiler()
        with open(os.path.join(rom_folder, "spoiler.json") , "w") as file:
            file.write(json.dumps(seed.data["spoiler"], indent=4))
            
        setattr(status_label, "text", "Seed saved to {}".format(rom_folder))
        


class BorderedButton(Button):
    def __init__(self, *args, **kwargs):
        super(BorderedButton, self).__init__(*args, **kwargs)
        # self.background_color = (0, 0, 0, 0)
        self.color = (0, 0, 0, 1)
        self.border = (1, 1, 1, 1)
        self.border_radius = 10
        # with self.canvas.before:
        #     Color(1, 1, 1, 1)
        #     self.rect = Rectangle(size=self.size, pos=self.pos)


class Dropdowns(BoxLayout):
    def __init__(self, key, name, options, defaultOption, *args, **kwargs):
        super(Dropdowns, self).__init__(*args, **kwargs)
        self.size = Window.size
        # with self.canvas.before:
        #     Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
        #     self.rect = Rectangle(size=self.size, pos=self.pos)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = [100, 5]
        self.height = 100
        self.color = (2, 0, 0, 1)
        self.key = key
        dropdown = DropDown()
        label = Label(
            text=name + ":",
            size_hint=(0.3, 1),
            text_size=(None, None),
            halign="right",
            valign="middle",
            color=(0.2, 0.2, 0.2, 1),  # Dark gray text
            bold=True,
        )
        self.add_widget(label)
        button = Button(
            text=name,
            height=1000,
            size_hint=(0.8, 1),  # Take 40% of width, full height
            background_color=(0.3, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),  # White text
            on_release=lambda button: dropdown.open(button),
        )
        # button.bind(on_release=self.handle_dropdown_open)
        dropdown.bind(
            on_select=lambda instance, text: self.handle_dropdown_click(button, text)
        )
        self.add_widget(button)
        for option in options:
            print(option)
            option_text = copy.copy(option[1])
            option_value = copy.copy(option[0])
            option_button = Button(
                size_hint_y=None,
                height=70,
                background_color=(0.95, 0.95, 0.95, 1),  # Almost white
                background_normal="",  # Remove the default background
                color=(0.2, 0.2, 0.2, 1),  # Dark gray text
                border=(1, 1, 1, 1),
                text=option_text,
                on_release=lambda btn, text=option_text, value=option_value: self.handle_option_click(
                    dropdown, text, value
                ),
            )
            dropdown.add_widget(option_button)
        dropdown.select(defaultOption)

    def handle_option_click(self, dropdown, option, value):
        print("option click: option: {} value: {}".format(option, value))
        settings[self.key] = value
        dropdown.select(option)

    def handle_dropdown_click(self, button, text):
        print("dropdown text: {}".format(text))
        setattr(button, "text", text)

generate_button = GenerateSeedButton(
    text="Generate Seed", 
    size_hint_y=None, 
    pos=(1300, 900),
)

class AgaseedApp(App):
    def build(self):
        Window.clearcolor = [1, 1, 1, 1]
        Window.size = (1334, 750)
        root = GridLayout(cols=2, size=(Window.width, Window.height))
        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None,
            size=(Window.width, Window.height),
        )
        layout.add_widget(
            Label(
                text="Item Placement",
                halign="left",
                size_hint_y=None,
                height=50,
                color=(0, 0, 0, 1),
            )
        )
        layout.add_widget(Dropdowns("glitches", "Glitches", glitches_options, "None"))
        layout.add_widget(
            Dropdowns(
                "item_placement", "Item Placement", item_placement_options, "Advanced"
            )
        )
        layout.add_widget(Dropdowns("shuffle", "Shuffle", shuffle_options, "Standard"))
        layout.add_widget(
            Dropdowns(
                "accessibility", "Accessibility", accessibility_options, "Inventory"
            )
        )
        layout.add_widget(
            Label(
                text="Goal",
                halign="left",
                size_hint_y=None,
                height=50,
                color=(0, 0, 0, 1),
            )
        )
        layout.add_widget(Dropdowns("goal", "Goal", goal_options, "Ganon"))
        layout.add_widget(
            Dropdowns("open_tower", "Open Tower", open_tower_options, "7")
        )
        layout.add_widget(
            Dropdowns(
                "ganon_vulnerable", "Ganon Vulnerable", ganon_vulnerable_options, "7"
            )
        )
        layout.add_widget(
            Label(
                text="Gameplay",
                halign="left",
                size_hint_y=None,
                height=50,
                color=(0, 0, 0, 1),
            )
        )
        layout.add_widget(
            Dropdowns("world_state", "World State", world_state_options, "Open")
        )
        layout.add_widget(
            Dropdowns("entrances", "Entrance Shuffle", entrance_shuffle_options, "None")
        )
        layout.add_widget(
            Dropdowns("boss_shuffle", "Boss Shuffle", boss_shuffle_options, "None")
        )
        layout.add_widget(
            Dropdowns("enemy_shuffle", "Enemy Shuffle", enemy_shuffle_options, "None")
        )
        layout.add_widget(Dropdowns("hints", "Hints", hints_options, "On"))
        layout.add_widget(
            Label(
                text="Difficulty",
                halign="left",
                size_hint_y=None,
                height=50,
                color=(0, 0, 0, 1),
            )
        )
        layout.add_widget(Dropdowns("swords", "Swords", swords_options, "Randomized"))
        layout.add_widget(
            Dropdowns("item_pool", "Item Pool", item_pool_options, "Normal")
        )
        layout.add_widget(
            Dropdowns("item_function", "Item Function", item_function_options, "Normal")
        )
        layout.add_widget(
            Dropdowns("enemy_damage", "Enemy Damage", enemy_damage_options, "Default")
        )
        layout.add_widget(
            Dropdowns("enemy_health", "Enemy Health", enemy_health_options, "Default")
        )
        right_layout = BoxLayout()
        right_float = FloatLayout()
        right_float.add_widget(generate_button)
        right_float.add_widget(
           status_label
        )
        right_layout.add_widget(right_float)
        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll.add_widget(layout)
        root.add_widget(scroll)
        root.add_widget(right_layout)
        return root


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(AgaseedApp().async_run())
