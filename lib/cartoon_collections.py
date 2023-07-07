def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f"{dwarves.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    calls = [f"{planeteer_call.capitalize()}!" for planeteer_call in planeteer_calls]

    return calls

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
a = summon_captain_planet(planeteer_calls)
print(a)

def long_planeteer_calls(planeteer_calls):
    is_long = False

    for planeteer_call in planeteer_calls:
        if len(planeteer_call) >=5:
            is_long = True
            break
    
    return is_long

# cheese_list = ["cheddar", "gouda", "camembert"]
def find_the_cheese(snacks):
    for cheese in snacks:
        if cheese in ("cheddar", "gouda", "camembert"):
            return cheese
    return None  