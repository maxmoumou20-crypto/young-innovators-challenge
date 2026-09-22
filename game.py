from engine.display import (
    show_intro,
    show_destination,
    show_encounter,
)
from engine.galaxy import create_galaxy
from engine.encounters import process_water_planet
from engine.journey import process_encounter
import constants

# function to decide whether to stop at planet or not
def should_stop():
    answer = input("  Should stop? (y/n): ")
    if answer == "y":
        return True
    else:
        return False

def check_defeat_status(oxygen, hull):
    if oxygen <= 0:
        return "  Oxygen depleted"
    elif hull <= 0:
        return "  Hull destroyed"
    return None

def scan_destination(planet):
    danger_level = planet["danger_level"]
    if danger_level < 3: # 1 or 2
        return "SAFE"
    elif danger_level == 3: 
        return "RISKY"
    return "DANGEROUS"

def process_destination(destination, oxygen, hull):
    if should_stop():
        oxygen, hull, narration = process_encounter(destination, oxygen, hull)
        show_encounter(narration)
        if destination["has_water"]:
            oxygen, hull, water_narration = process_water_planet(oxygen, hull)
            show_encounter(water_narration)
    else:
        show_encounter("  You fly past without stopping")
    return oxygen, hull

def show_resources(oxygen, hull):
    print(f"  Oxygen levels: {oxygen}, Hull integrity: {hull}")

def main(): 

    oxygen = constants.STARTING_OXYGEN 
    hull = constants.STARTING_HULL
    ship_name = constants.SHIP_NAME
    crew_desc = constants.CREW_DESCRIPTION
    galaxy = constants.GALAXY_SIZE

    show_intro(ship_name, crew_desc)
    galaxy = create_galaxy(galaxy)

    # game loop
    for i in range(len(galaxy)): 
        destination = galaxy[i]
        oxygen -= 8

        show_destination(destination, i, len(galaxy))
        scan_destination(destination)
        oxygen, hull = process_destination(destination, oxygen, hull)
        show_resources(oxygen, hull)
        cause = check_defeat_status(oxygen, hull)

        if cause:
            print(cause)
        
if __name__ == "__main__":
    main()
player.py
class Ship:
    # "data" a.k.a. attributes
    def __init__(self, 
                 oxygen, 
                 hull, 
                 name, 
                 crew): # constructor
        self.oxygen = oxygen
        self.hull = hull
        self.name = name
        self.crew = crew

    # methods a.k.a "behaviour"
    def check_defeat_status(self):
        if self.oxygen <= 0:
            return "  Oxygen depleted"
        elif self.hull <= 0:
            return "  Hull destroyed"
        return None

    # special methods
    def __str__(self):
        return f"""
        Ship object with the following parameters:
        oxygen = {self.oxygen}
        hull = {self.hull}
        name = {self.name}"""

# one "instance" of the "Ship" class
ship_one = Ship(10, 
                100, 
                "Python Crew",
                "Awesome People")