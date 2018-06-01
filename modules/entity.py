from uuid import uuid4 as gen_uuid4
from random import choice as rchoice
from random import randint as rint

from modules import vitals

class Entity:
    def __init__(self):
        """
        Initialize all essential values here, make sure that
        more complex values are set to some undifined state,
        then call a function that sets them.
        """
        # Basic assignments here
        self.gender = rchoice(["male", "female"])
        self.name = "undefined"
        self.id = gen_uuid4()
        self.skills = {"undefined": True}
        self.vitals = {"undefined": True}
        self.stats = {"undefined": True}
        self.position = {"x": 0, "y": 0, "z": 0}

        # List of functions to set more complex characteristics
        self.give_name()
        self.initialize_skills()
        self.initialize_stats()
        self.initialize_vitals()

    def move(self, dx: int = 0, dy: int = 0 , dz: int = 0):
        """
        This function should be callable from any other event
        to change the position of an entity.
        """
        current_position = self.position
        current_position['x'] = current_position['x'] + dx
        current_position['y'] = current_position['y'] + dy
        current_position['z'] = current_position['z'] + dz

        self.position = current_position

    def give_name(self):
        """
        Randomizer function to give an entity a random name. Arbitrary
        amounts of names can be added to these arrays.
        """
        if self.gender == "male":
            self.name = rchoice([
              "albert", "brutus", "chris",
            ])

        if self.gender == "female":
            self.name = rchoice([
              "ally", "beatrix", "chloe",
            ])

    def initialize_skills(self):
        """
        Initializes the skills array, can be moved to another class later, like vitals.
        """
        # Nested function because we want some randomness to these skills
        def radder(x: int = 1) -> int: return x + rint(0, 5)

        skill_line = {
            "cooking": radder(),
            "hauling": radder(),
            "shooting": radder(),
            }

        self.skills = skill_line

    def initialize_stats(self):
        stat_line = {}

        # Nested function because we want some randomness to these skills
        def radder(x: int = 1) -> int: return x + rint(0, 5)

        stat_line = {
            "insight": radder(),  # Would love for this to be the machine learning speed
            "common_sense": radder(),
            "strength": radder(),
            "dexterity": radder(),
            }

        self.stats = stat_line

    def initialize_vitals(self):
        self.vitals = vitals.Vitals()

    def receive_damage(self, amount: int, part: str):
        self.vitals.damage(amount, part)
        # References nonexistant code
