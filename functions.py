from engine.display import show_defeat


def check_Defeat(ship_name, oxygen,  hull ):
 if oxygen <= 0:
    return "oxygen depleted"

 elif hull <= 0:
    return "hull destroyed"
 return None



