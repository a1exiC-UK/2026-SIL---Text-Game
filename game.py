# A dictionary of scenarios for the game.

scenarios = [
    
    {
        "text": "A narrow cave splits in two. Cold air drafts from the left. Which direction do you choose?", ## The scenario text presented to the player.
        "correct": "left", ## Whether left or right is the correct decision
        "item": None, ## Whether there is an item to pick up
        "requires": None, ## Whether an item is required to proceed
        "death": "You stumble into a pit in the dark. Game over.", ## Message displayed if the player makes the wrong choice
        "success": "You feel your way down the left tunnel, one hand on the wall, and the passage opens safely ahead." ## Message displayed if the player makes the correct choice
    },
    
    {
        "text": "The passage forks again. To the right, something glints faintly on the ground. To the left, only shadow.",
        "correct": "right",
        "item": "torch",
        "requires": None,
        "death": "You trip over loose stone in the pitch black and crack your skull. Game over.",
        "success": "You head down the right tunnel and find a half-burnt torch lying in the dirt. You strike it against the wall and it catches flame, lighting your way onward."
    },
    
    {
        "text": "Ahead the tunnel splits around a jagged rock formation. The left branch is pitch black; the right seems to glow faintly with distant light.",
        "correct": "left",
        "item": None,
        "requires": "torch",
        "death": "Blind in the dark, you wander into a nest of cave spiders. Game over.",
        "success": "You enter the black left tunnel and hold your torch high. Its flame throws back the darkness, revealing a clear path between the jagged rocks, and you pass through unharmed."
    },
    
    {
        "text": "The corridor opens into a small chamber with two exits. Something metallic rests against the right wall.",
        "correct": "right",
        "item": "sword",
        "requires": None,
        "death": "You take the left path and are ambushed by a lurking beast. Game over.",
        "success": "You cross the chamber to the right exit and find a rusted sword leaning against the wall. You take it up and continue through, blade in hand."
    },
    
    {
        "text": "Snarling echoes come from both tunnels ahead. The right one sounds close and hostile.",
        "correct": "right",
        "item": None,
        "requires": "sword",
        "death": "Unarmed, you are overwhelmed by the creature guarding the path. Game over.",
        "success": "You advance down the right tunnel and a snarling creature lunges from the dark. You meet it with your sword, driving it back with a few hard strikes, and press on down the now-clear passage."
    },
    
    {
        "text": "Two doorways stand side by side. Scratched into the stone above the left one is a faded warning. A dull shape leans in the right doorway.",
        "correct": "right",
        "item": "shield",
        "requires": None,
        "death": "You ignore the warning and trigger a collapsing ceiling. Game over.",
        "success": "You step through the right doorway and find a dented iron shield propped against the frame. You strap it to your arm and move on through the passage beyond."
    },
    
    {
        "text": "The floor ahead splits into two ledges. The left ledge crumbles as loose rocks rain down from above.",
        "correct": "left",
        "item": None,
        "requires": "shield",
        "death": "Falling debris crushes you before you can react. Game over.",
        "success": "You step onto the crumbling left ledge as rocks begin to rain down. You raise your shield overhead, weathering the barrage, and cross the ledge safely to solid ground."
    },
    
    {
        "text": "A deep chasm blocks the way, splitting the path left and right. Coiled near the right edge lies a length of frayed cord.",
        "correct": "right",
        "item": "rope",
        "requires": None,
        "death": "You misjudge the jump on the left and plunge into darkness. Game over.",
        "success": "You follow the chasm's edge to the right and find a coiled length of rope. You gather it up and continue along the safer right-hand path around the drop."
    },
    
    {
        "text": "The chasm narrows into two crossings. The left crossing is a crumbling stone bridge; the right is a wide gap with no bridge at all.",
        "correct": "right",
        "item": None,
        "requires": "rope",
        "death": "The crumbling bridge gives way beneath your feet. Game over.",
        "success": "You skip the crumbling bridge and approach the wide gap on the right. You lash your rope to a jutting rock, swing across the open chasm, and land safely on the far side."
    },
    
    {
        "text": "Two final doors stand before you, bound in iron. A small brass object lies half-buried in the dirt to the left.",
        "correct": "left",
        "item": "key",
        "requires": None,
        "death": "You approach the sealed door on the right and trigger a hidden dart trap. Game over.",
        "success": "You veer left and kneel to dig a small brass key out of the dirt. You pocket it and turn back toward the doors ahead."
    },
    
    {
        "text": "One final choice remains: a locked door on the left, or an unlocked door hanging ajar on the right, creaking in a draft.",
        "correct": "left",
        "item": None,
        "requires": "key",
        "death": "The unlocked door was a trap all along, sealing you inside forever. Game over.",
        "success": "You approach the locked left door and fit the brass key into it. The lock turns smoothly, the door swings open, and you step through into daylight. You have escaped the dungeon!"
    }

] 

inventory = [] # Holds the items the player has collected. These items are needed to progress through certain stages.

is_alive = True # Checks if the player is alive. If the player dies, the game ends.

input("Welcome to the dungeon. You can either go: \n- left \n- right \n- pick up item \n- view inventory \n- view available actions \n Type your choice and press enter.") # Gives the player the correct inputs


for scenario in scenarios: # Loopsthrough each scenario in the list.
    
    if not is_alive: # If is_alive = False, game ends.
        print("You have failed to escape the dungeon. Restart to try again.")
        break
    
    while True: # While the player is alive, the game continues.
        
        action = input(scenario["text"]) # Shows the scenario and asks the player for input.
        
        if action == "pick up item" and scenario["item"]: # When the player chooses to pick up an item, and it gets added to the inventory.
            inventory.append(scenario["item"])
            print(f"You picked up a {scenario['item']}.")
            continue
        
        if action == "view inventory": # When the player wants to view their inventory.
            for item in inventory:
                print("Inventory: \n- %s" % item)
            continue
        
        if action == "view available actions": # When the player is unsure of what actions are available.
            print("Available actions: \n- left \n- right \n- pick up item \n- view inventory \n- view available actions")
            continue
        
        if action not in ["left", "right", "pick up item", "view inventory","view available actions"]: # If there is an unknown input, the player is prompted with the correct inputs.
            print("Invalid choice. Please choose: \n- left \n- right \n- pick up item \n- view inventory \n- view available actions")
            continue
        
        if scenario["requires"] and scenario["requires"] not in inventory: # If the player does not have the required item, they die.
            print(scenario["death"])
            is_alive = False
            break
        
        if action != scenario["correct"]: # If the player chooses the wrong direction, they die.
            print(scenario["death"])
            is_alive = False
            break
        
        if action == scenario["correct"]: # If the player chooses the correct direction, they progress to the next stage.
            print(scenario["success"])
            break