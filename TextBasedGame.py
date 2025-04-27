#Shakira Baker

rooms = {
        'main foyer': {'north': 'garden', 'south': 'master bedroom', 'east': 'kitchen', 'west': 'library'},
        'master bedroom': {'north': 'main foyer'},
        'library': {'east': 'main foyer', 'north': 'witch\'s lair'},
        'witch\'s lair': {'south': 'library'},
        'garden': {'south': 'main foyer', 'east': 'high tower'},
        'kitchen': {'west': 'main foyer', 'south': 'armory'},
        'armory': {'north': 'kitchen'}

    }


items = {
        "master bedroom": "white oak stake",
        "library": "hybrid chronicle",
        "witch\'s lair": "health potion",
        "garden": "wolfsbane",
        "kitchen": "garlic necklace",
        "armory": "armor"

}

#Function that checks if item user enters is in current_room
#If it is it adds item to inventory and removes it from items dictionary
#If not it tells the user that the item entered is not there
def grab_item(room, item):
    if room in items and item == items[room]:
        inventory.append(item)
        del items[room]
        print("You picked up the", item)
    else:
        print("There is no", item, "here.")


#Checks to see if direction user entered is valid direction in rooms dictionary for the current_room
#If it is it returns the key value pair from the rooms dictionary
#If not it tells the user they cant go that way and lists the valid direction options for the current_room
def move_room(current_room, direction):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print('You cannot go that way.')
        print("Valid directions are:", list(rooms[current_room].keys()))
        return current_room


#Assigns current_room to the start room Great hall
current_room = 'main foyer'

#Creates blank inventory list to later store items that the user grabs
inventory = []


#Provides instructions to player at beginning of game
print('Welcome to the Hybrid Slayer text-based video game!')
print("To move between rooms you will use the commands Go North, Go South, Go East, or Go West")
print('You must grab an item from each room except for the main foyer and the high tower.')
print('To grab an item, type "get" and the name of the item that is in the room')
print('You win the game by reaching the high tower with all 6 items in your inventory.')
print("")
print("You are currently in the", current_room)


#Creates loop that tells player what room they are in and the item available in the current_room
#and continues to ask what they would like to do
while True:

    #Displays item in curren_room if the current_room contains an item
    if current_room in items:
        print('You see the', items[current_room], 'in the room.')

    #Displays the current inventory each time user enters a room
    print('Your current inventory:', inventory)

    #Prompts the user for a command which should be a direction or an item to grab
    command = input('What would you like to do? ').lower()

    #Checks to see if command entered has correct starting words
    #If not prompts user to try again
    if command.startswith('go '):
        direction = command.split(' ')[1]
        current_room = move_room(current_room, direction)#passes current_room and direction the user enters to move_room function
        print("")
        print('You are now in the', current_room)
    elif command.startswith('get '):
         item = command.split(' ', 1)[-1]
         grab_item(current_room, item)#passes current_room and item the user enters to grab_item function
    else:
        print("Invalid command. Please try again")


    #Checks to see if user has all required items in inventory once high_tower is reached
    #If inventory has 6 items the user wins, if not they lose
    if current_room == 'high tower' and len(inventory) == 6:
        print('You charge the legendary hybrid and go in for the kill!!!')
        print('The hybrid shrieks in defeat as he embraces his agonizing death!!')
        print('You live to fight another day and the village is finally at peace!')
        print('Congratulations! You have won the game!')
        break
    elif current_room == 'high tower' and len(inventory) < 6:
        print('You Died! X_X')
        print('Sadly you have failed to slay the hybrid due to lack of preparation. The village will perish')
        print('Maybe next time you should remember to grab all of the necessary items.')
        break

