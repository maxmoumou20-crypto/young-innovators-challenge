# ============================================================
# SPACE EXPLORER — Your Ship, Your Story
# ============================================================
# Change these values to make the game your own.
# Run the game after each change to see what happens!
# ============================================================

# --- Your ship ---
SHIP_NAME = "Victoria Express"
CREW_DESCRIPTION = "Python enthusiasts learning how to code"

# --- Starting resources ---
STARTING_OXYGEN = 100
STARTING_HULL = 100

# --- Galaxy ---
GALAXY_SIZE = 8
USE_CUSTOM_PLANETS = True
PLANETS = ["Darrin", "Pluto", "Mars", "Jupiter", "Earth"]

print(len(PLANETS))
PLANETS[2]= "Mars"

PLANETS.append({
    "name": "Jupiter",
    "description": "A gas giant with a strong magnetic field.",
    "danger_level":1,
    "has-water": True,
    "encounter": "empty"
    
})

PLANETS.append({
    "name": "Earth",
    "description": "A planet with abundant water and life.",
    "danger_level": 4,
    "has-water": True,
    "encounter": "raider"
    
})

PLANETS.append({
    "name": "Mars",
    "description": "A cold desert planet with a thin atmosphere.",
    "danger_level": 2,
    "has-water": True,
    "encounter": "empty"
    
}) 

PLANETS.append({
    "name": "Darrin",
    "description": "A cold desert planet with a thin atmosphere.",
    "danger_level": 2,
    "has-water": False,
    "encounter": "empty"   
})

PLANETS.append({
    "name": "pluto",
    "description": "A cold desert planet with a thin atmosphere.",
    "danger_level": 2,
    "has-water": False,
    "encounter": "raider"   
})