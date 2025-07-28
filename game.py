# inventory
inventory = {
    "has_map": False,
    "has_basket": False,
    "has_wand": False
}


def game_over():
    print("GAME OVER")
    exit()

# cottage parts (repeat for the prompt whenever items r picked)
def fairy_tale_cottage():
    if inventory["has_map"] and inventory["has_basket"] and inventory["has_wand"]:
        print("You have already explored the cottage.")
        open_field()
        return

    print("You find an empty cottage. The lights are off and the door is locked. Do you: ")
    print("1. Knock on the door")
    print("2. Go back")
    action = input("INPUT ACTION (1-2): ")

    if action == "1":
        fairy_tale_cottage_2()
    elif action == "2":
        open_field()
    else:
        print("Invalid response. Please select 1 or 2.")
        fairy_tale_cottage()

def fairy_tale_cottage_2():
    print("You knock on the door, but no one responds. As you back off of the doormat, you hear a loud crunch.")
    print("You search under the doormat and find a key. Do you: ")
    print("1. Pick up the key and break in.")
    print("2. Put it back and walk back.")
    action = input("INPUT ACTION (1-2): ")

    if action == "1":
        fairy_tale_cottage_3()
    elif action == "2":
        open_field()
    else:
        print("Invalid response. Please select 1 or 2.")
        fairy_tale_cottage_2()

def fairy_tale_cottage_3():
    print("Inside the cottage, you see a table with maps, a picnic basket, and drawers. Do you:")
    print("1. Piece the papers together to complete the maps.")
    print("2. Pick up the picnic basket.")
    print("3. Look through the drawers.")
    print("4. Leave the cottage.")

    action = input("INPUT ACTION (1-4): ")

    if action == "1":
        if not inventory["has_map"]:
            print("You piece together a map of a hedge maze. You roll it up and put it in your bag.")
            inventory["has_map"] = True
        else:
            print("You’ve already taken the map.")
        fairy_tale_cottage_3()

    elif action == "2":
        if not inventory["has_basket"]:
            print("You grab the picnic basket and hold onto it.")
            inventory["has_basket"] = True
        else:
            print("You’ve already taken the basket.")
        fairy_tale_cottage_3()

    elif action == "3":
        if not inventory["has_wand"]:
            print("You find a glowing fairy wand and put it in your bag.")
            inventory["has_wand"] = True
        else:
            print("You’ve already taken the wand.")
        fairy_tale_cottage_3()

    elif action == "4":
        print("You leave the cottage and return to the field.")
        open_field()
    else:
        print("Invalid action. Please select option 1-4.")
        fairy_tale_cottage_3()

# maze parts
def hedge_maze():
    print("You reach a hedge maze stretching far to the east and west. The hedges tower over you.")
    print("Do you:")
    print("1. Step into the maze")
    print("2. Go back north to the open field")
    action = input("INPUT ACTION (1-2): ")

    if action == "1":
        inside_maze()
    elif action == "2":
        open_field()
    else:
        print("Invalid action. Please choose 1 or 2.")
        hedge_maze()

def inside_maze():
    print("You are inside the maze. The hedges loom high and the paths twist in all directions.")
    print("Do you:")
    print("1. Go deeper into the maze")
    print("2. Try to go back the way you came")

    action = input("INPUT ACTION (1-2): ")

    if action == "1":
        enter_maze()
    elif action == "2":
        print("You turn around and retrace your steps back to the clearing.")
        open_field()
    else:
        print("Invalid response. Please choose 1 or 2.")
        inside_maze()

def enter_maze():
    print("You press forward, deeper into the maze. The air grows colder and the sounds of the forest fade away...")

    if inventory["has_map"] and inventory["has_basket"] and inventory["has_wand"]:
        print("Your map helps you navigate, your wand lights hidden paths, and your basket sustains you.")
        print("After hours of twists and dead ends, you see sunlight through the hedges...")
        print("A familiar path unfolds ahead of you, and you follow it back to your local village.")
        print("Congratulations! You escaped the maze and lived to tell the tale.")
        exit()
    else:
        print("You wander in circles. The hedges seem to shift and trap you.")
        print("You didn’t come prepared. The maze has claimed another victim.")
        print("You got lost in the maze, stuck for all eternity. ")
        game_over()

# quicksand
def quicksand_pit():
    print("You fall into a quicksand pit and sink rapidly.")
    game_over()

# rabbit hole
def rabbit_hole():
    print("You trip and fall into a rabbit hole. Luckily, you land in a pile of soft leaves.")
    print("You look around and realize that you are in a shallow cave. You look up, but it is impossible to go back the way you came.")
    print("Ahead of you is a whimsical flower garden with oversized plants. You also spot an exit gate. Do you:")
    print("1. Relax in the cave")
    print("2. Turn left and explore the garden")
    print("3. Turn right and explore the garden")
    print("4. Try to exit the garden")

    action = input("INPUT ACTION (1-4): ")

    if action == "1" and inventory["has_basket"]:
      print("You lay down on top of the leaves, but soon get hungry. You open the picnic basket and see a sandwich and a flask.")
      print("You eat the sandwich and drink from the flask, but soon begin to feel dizzy.")
      print("The world spins and fades to black.")
      game_over()

    elif action == "1":
      print("You lay down on top of the leaves, and quickly drift off to sleep. When you wake up, you see that your surroundings have changed again.")
      print("The garden has been replaced by a new path. You follow it and soon recognize it as the path back to your local village.")
      print("You brush off the events of the day and head home.")
      exit()

    elif action == "2":
      print("You follow the path leading through the garden on the left. You pass rows of colorful flowers before running into a giant hedge maze.")
      print("You gather your wits and venture into the maze.")
      enter_maze()

    elif action == "3":
      print("You follow the path leading through the garden on the right. The path twists and turns and seems to go on endlessly.")
      print("The oversized flowers loom over your head. As you keep walking, your limbs begin to feel heavy.")
      print("Suddenly tired, you decide to take a nap under a giant poppy. You fall into a deep slumber...")
      game_over()

    elif action =="4":
      print("When you walk through the exit gate of the garden, you realize that you are familiar with this area of the forest.")
      print("Confused as to why you had never discovered the garden before, you turn around. The gate has disappeared.")
      print("How mysterious. You walk home to get a good night's sleep.")
      exit()

# field/main area
def open_field():
    print("You are standing in a clearing surrounded by forest. Paths lead in all directions. Do you:")
    print("1. Go north")
    print("2. Go south")
    print("3. Go east")
    print("4. Go west")

    action = input("INPUT ACTION (1-4): ")

    if action == "1":
        print("You walk north and find a fairytale cottage.")
        fairy_tale_cottage()
    elif action == "2":
        hedge_maze()
    elif action == "3":
        rabbit_hole()
    elif action == "4":
        quicksand_pit()
    else:
        print("Invalid action. Please try again.")
        open_field()

# game start
open_field()
