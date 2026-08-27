from time import sleep # Sleep function to slow down text appearing.
import sys # System functions for a typing effect.
import typing # Same as above, for typing effect.

def show_actions(): # Defines the available actions.
    print("Available actions: \n- left \n- right \n- pick up item \n- view inventory \n- view available actions")

def typingPrint(text): # Function for typing effect - speech.
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.04)

is_alive = True # Checks if the player is alive. If the player dies, the game ends.

def startup():
    print(""" ____                                     
 |  _ \ _   _ _ __   __ _  ___  ___  _ __  
 | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
 | |_| | |_| | | | | (_| |  __/ (_) | | | |
 |____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
                    |___/                  """)
    sleep(2)
    print("Welcome to the dungeon. Your aim is to escape this hellhole by using items you collect on the way. \n")
    sleep(2)
    print("You, the main character, have been trapped in this dungeon after being knocked unconscious during a brawl. \nYour goal is to find a way out. \nInteract with your environment to find items and listen to others to help you escape. \n")
    sleep(2)
    print("Good luck. You are going to need it... \n")
    sleep(2)
    show_actions()

startup()

# A dictionary of scenarios for the game.
SCENARIOS = [
    
    {
        "descriptor": None, ## Description if NPC present, otherwise None.
        "speech": None, ## Speech if NPC present, otherwise None.
        "text": "A narrow cave splits in two. Cold air drafts from the left. Which direction do you choose? ", ## The scenario text presented to the player.
        "correct": "left", ## Whether left or right is the correct decision.
        "item": None, ## Whether there is an item to pick up.
        "requires": None, ## Whether an item is required to proceed.
        "death": "\nYou stumble into a pit in the dark. Game over.", ## Message displayed if the player makes the wrong choice
        "success": "\nYou feel your way down the left tunnel, one hand on the wall, and the passage opens safely ahead." ## Message displayed if the player makes the correct choice.
    },
    
    {
        "descriptor": "A deluded man approaches you. You seem unsure of what to think about him.", 
        "speech": "Ho ho young traveller! I am Kerioyl, and this dungeon has been my home for uhh... It doesn't matter, anyways, here are my pets! \n *He gestures to a couple of rocks, which appear just like rocks* \nAnyways young traveller, here is a torch to help you escape this hellhole! \n",
        "text": "The passage forks again. To the right, crystals adorn the walls, but that seems like all. To the left, only shadow. What do you do? ",
        "correct": "right",
        "item": "torch",
        "requires": None,
        "death": "\nYou trip over loose stone in the pitch black and crack your skull. Game over.",
        "success": "\nYou head down the right tunnel, with your new torch, and arrive safely."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "Ahead the tunnel splits around a jagged rock formation. The left branch is pitch black; the right seems to glow faintly with distant light. " ,
        "correct": "left",
        "item": None,
        "requires": "torch",
        "death": "\nBlind in the dark, you wander into a nest of cave spiders. Game over.",
        "success": "\nYou enter the black left tunnel and hold your torch high. Its flame throws back the darkness, revealing a clear path between the jagged rocks, and you pass through unharmed."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "The corridor opens into a small chamber with two exits. Something metallic rests against the right wall. ",
        "correct": "right",
        "item": "sword",
        "requires": None,
        "death": "\nYou take the left path and are ambushed by a lurking beast. Game over.",
        "success": "\nYou cross the chamber to the right exit and find a rusted sword leaning against the wall. You take it up and continue through, blade in hand."
    },
    
    {
        "descriptor": "Sat inbetween the tunnels is a young maiden warrior who appears to be wounded. ",
        "speech": "Please... wait. I came through here not long ago. Whatever's guarding this place — it took my whole company. I was the only one who made it out.\n *Her eyes flick toward the two tunnels ahead, and something in her expression tightens.* \nI don't know what's down there. But I felt it watching me the whole way through. If you're going in... don't go unprepared.\n *She grips your arm, weaker than she means to.* \nWhichever way you choose — choose it like your life depends on it. Because it does. \n",
        "text": "Snarling echoes come from both tunnels ahead. The right one sounds close and hostile, but the left feels more ominous. ",
        "correct": "right",
        "item": None,
        "requires": "sword",
        "death": "\nYou are overwhelmed by the large creature guarding the path. Game over.",
        "success": "\nYou advance down the right tunnel and a small snarling creature lunges from the dark. You meet it with your sword, driving it back with a few hard strikes, and press on down the now-clear passage."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "Two doorways stand side by side. Scratched into the stone above the left one is a faded warning. A dull shield-like shape leans in the right doorway. ",
        "correct": "right",
        "item": "shield",
        "requires": None,
        "death": "\nYou ignore the warning and trigger a collapsing ceiling. Game over.",
        "success": "\nYou step through the right doorway and find a dented iron shield propped against the frame. You strap it to your arm and move on through the passage beyond."
    },
    
    {
        "descriptor": None,
        "speech": None, 
        "text": "The floor ahead splits into two ledges. The left ledge crumbles as loose rocks rain down from above. A golden shimmer appears in front of you, with the shape of it perhaps resembling a coin. ",
        "correct": "left",
        "item": "golden coin",
        "requires": "shield",
        "death": "\nFalling debris crushes you before you can react. Game over.",
        "success": "\nYou step onto the crumbling left ledge as rocks begin to rain down. You raise your shield overhead, weathering the barrage, and cross the ledge safely to solid ground."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "A deep chasm blocks the way, splitting the path left and right. Coiled near the right edge lies a length of frayed cord. ",
        "correct": "right",
        "item": "rope",
        "requires": None,
        "death": "\nYou misjudge the jump on the left and plunge into darkness. Game over.",
        "success": "\nYou follow the chasm's edge to the right and find a coiled length of rope. You gather it up and continue along the safer right-hand path around the drop."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "The chasm narrows into two crossings. The left crossing is a crumbling stone bridge; the right is a wide gap with no bridge at all. ",
        "correct": "right",
        "item": None,
        "requires": "rope",
        "death": "\nThe crumbling bridge gives way beneath your feet. Game over.",
        "success": "\nYou skip the crumbling bridge and approach the wide gap on the right. You lash your rope to a jutting rock, swing across the open chasm, and land safely on the far side."
    },
    
    {
        "descriptor": "In front of you, inbetween the two doors appears to be a silver box, resembling a vending machine. A small slot is visible on the front, and a faint inscription reads: 'Insert coin to proceed.'",
        "speech": "Hello there. \nThank you. You may now proceed. \n *The screen appears to be making an arrow, pointing left.*\n"
        "text": "Two doors stand before you, bound in iron. A small brass object lies half-buried in the dirt to the left. ",
        "correct": "left",
        "item": "key",
        "requires": "golden coin",
        "death": "\nWithout knowing the correct direction to go,as you didn't have the coin, You approach the sealed door on the right and trigger a hidden dart trap. Game over.",
        "success": "\nYou veer left and kneel to dig a small brass key out of the dirt. You pocket it and turn back toward the doors ahead."
    },
    
    {
        "descriptor": None,
        "speech": None,
        "text": "One final choice remains: a locked door on the left, or an unlocked door hanging ajar on the right, creaking in a draft. ",
        "correct": "left",
        "item": None,
        "requires": "key",
        "death": "\nThe unlocked door was a trap all along, sealing you inside forever. Game over.",
        "success": "\nYou approach the locked left door and fit the brass key into it. The lock turns smoothly, the door swings open, and you step through into daylight. You have escaped the dungeon!"
    }

] 

inventory = [] # Holds the items the player has collected. These items are needed to progress through certain stages.



for scenario in SCENARIOS: # Loops through each scenario in the list.
    
    picked_up = False
    
    if not is_alive: # If is_alive = False, game ends.
        print("\nYou have failed to escape the dungeon. Restart to try again.")
        break
    
    if scenario["descriptor"]: # If a description is present, it is printed to the screen.
        
        sleep(2)
        
        print("\n" + scenario["descriptor"] + "\n") 
        
    if scenario["speech"]: # If an NPC is present, their speech is printed to the screen.
            
        sleep(2)

        typingPrint(scenario["speech"])

    sleep(2)
    
    while True: # While the player is alive, the game continues.

        action = input("\n" + scenario["text"]) # Shows the scenario and asks the player for input.
        
        if action == "pick up item": # When the player wants to pick up an item.
            if picked_up: ## Checks if the item has already been picked up.
                print("You have already picked up an item.")
                continue
            if scenario["item"]: ## If not, an item is added to the inventory.
                inventory.append(scenario["item"])
                print(f"\nYou picked up a {scenario['item']}.")
                picked_up = True
            else: ## If no item is present.
                print("\nThere is nothing to pick up here.")
            continue
        
        if action == "view inventory": # When the player wants to view their inventory.
            print("\nInventory:")
            for item in inventory:
                print("- %s" % item)
            if not inventory:
                print("- empty")
            continue
        
        if action == "view available actions": # When the player is unsure of what actions are available.
            show_actions()
            continue
        
        if action not in ["left", "right", "pick up item", "view inventory","view available actions"]: # If there is an unknown input, the player is prompted with the correct inputs.
            print("\nInvalid choice.")
            show_actions()
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
