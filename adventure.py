import sys
from game_data import Player, Location, Item

class World:
    """A class to store all map, location and item data for game world."""

    def __init__(self, mapfile, locfile, itemfile):
        """
        (World, str filename, str filename, str filename) -> None

        Initialize a World using data from given filenames.
        """
        self.map = []
        self.locations = {}
        self.items = {}

        self.load_map(mapfile)
        self.load_locations(locfile)
        self.load_items(itemfile)

    def load_map(self, filename):
        '''
        (World, str filename) -> None
        Store map from filename in self.map as a nested list
        of strings like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']]
        The given 'filename' is a string that gives name of text file
        in which map data is located.
        '''

        map = open(filename,'r')
        for line in map:
            line=line.strip()
            self.map.append(line.split())
        map.close()


    def load_locations(self, filename):
        '''
        (World, str filename) -> None
        Store all locations from filename in self.locations
        as a dictionary where integer location numbers are the keys,
        and Location objects are the values:
        {integer location number: Location object}.

        The given 'filename' is a string that gives name of text file
        in which location data is located.
        '''

        # TODO:
        # Open and read given filename
        # For each location, create a new Location object with data from file.
        #   e.g. new_location = Location(location id, short desc, long desc, ...)
        # Add this location to self.locations dict with key as integer
        # of location id and value as this new_location object

        file = open(filename,'r')
        new_locations={}
        brief_description = " "
        long_description = " "
        points= 0
        index_of_location= " "
        key= " "

        for line in file:

            if "LOCATION" in line:
                new_locations[line] = new_locations
                index_of_location = line.split(" ")[0].strip("\n")
                line = key


            if "brief description:" in line:
                new_locations[key]=line
                brief_description = line.strip("brief description:")

            if "long description:" in line:
                new_locations[key]=line
                long_description = line.strip("long description:").strip("\n")


            if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15" in line:
                new_locations[key] = line

            if "Item" in line:
                new_locations[key] = line


        self.locations = new_locations
        file.close()


    def load_items(self, filename):
        '''
        (World, str filename) -> None
        Store all items from filename in self.items
        with item name as the key, and an Item object as the value.
        Each item should also be added into self.locations as
        based on the item's starting location as given in text file.

        The given 'filename' is a string that gives name of text file
        in which item data is located.
        '''

        # TODO:
        # Open and read given filename
        # For each item, create a new Item object with data from file.
        # Then, two things must be done:
        # 1. Using item's starting location, append Item object
        #    to that starting location's ".items" list
        #    i.e. (add Item to self.locations[starting_location_id].items)
        # 2. Store item in self.items dict with key as str item name
        #    and value as Item object

        file = open(filename,'r')
        items_list = []
        i = 0

        for line in file:
            line.split(" ")[0].strip("\n")
            items_list.append(line)
            self.items[line] = self.items
            self.items[line] = items_list[i]
            i= i + 1



    def get_room(self, x, y):
        '''
        (World, int, int) -> Location
        Return the Location object associated with x, y values given.
        '''

        # TODO:
        # 1. Get location id at given x, y coordinates in self.map list
        # 2. Return Location object associated with this location number in self.locations dictionary


    def get_moves(self, x, y):
        '''
        (World, int, int) -> lst of str
        The given x and y represent the player's current position.
        Using x, y coordinates, check self.map list for what directions the player can currently move in.
        Return list of possible moves based on map data and boundaries.
        e.g. The returned list should look something like: ["go north", "go south"]
        '''
        if len(self.map) > x and x >= 0:
            if len(self.map[x]) > y and y >=0:
                location = self.map[x][y]
                return self.locations[location]
        return

# --- END of World class --- #


# --- Functions to handle player's actions in the game --- #

def view_inventory():
    '''
    Suggested helper function.
    You may use or remove this as you see fit.
    TODO: Update this docstring based on how you use this method.
    '''

    pass

def use_item(current_item, current_location):
    '''
    Suggested helper function.
    You may use or remove this as you see fit.
    TODO: Update this docstring based on how you use this method.
    '''

    pass


def do_action(WORLD, PLAYER, choice, current_loc):
    '''
    (object, object, str, Location) -> None
    This function takes str choice and Location current_loc and
    carries out consequences of making the given choice.
    You may update this docstring based on how you choose to code this function.
    '''

if __name__ == "__main__":

    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(4, 3)

    print ("\n \n")
    game = open('game_intro.txt', 'r')
    for line in game:
        print(line.strip('\n'))
    print ("---------------------------------")
    print (" \t Note that you are limited to 200 moves to find the necessary objects and take the exam or you'll automatically lose.")
    print ("---------------------------------")
    print ("\n")
    commands = ["Go [Direction]","Look", "Inventory", "Score", "Quit"]

while not PLAYER.victory:
    current_loc = WORLD.get_room(PLAYER.x, PLAYER.y)

    # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
    # Depending on whether or not it's been visited before,
    # print either full description (first time visit) or brief description (every subsequent visit)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("The following commands are available to you at any time: ", commands, " and other special commands are accessible when you go to certain locations.")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    choice = input(" \n Please select a command: ")


    if choice == "Go North":
        PLAYER.move_north()
        location = WORLD.get_moves(PLAYER.x, PLAYER.y)

    elif choice == "Go South":
        PLAYER.move_south()
        location = WORLD.get_moves(PLAYER.x, PLAYER.y)

    elif choice == "Go West":
        PLAYER.move_west()
        location = WORLD.get_moves(PLAYER.x, PLAYER.y)

    elif choice == "Go East":
        PLAYER.move_east()
        location = WORLD.get_moves(PLAYER.x, PLAYER.y)

    elif choice == "Look":
        print (location.get_full_description())

    elif choice == "Inventory":
        print("Your inventory:")
        for x in PLAYER.get_inventory:
            print(self.inventory)

    elif choice == "Score":
         print(PLAYER.score())

    #ENHANCEMENT used at LOCATION 3
    elif choice == "Examine Object":
        print ("I heard that there are bonus items in DH \n")

    #ENHANCEMENT used at LOCATION 6
    elif choice == "Examine Cup":
        print ("Whoa! The RRRoll up the Rim gave us a clue! It says you will find your TCard in the library. \n")

     #ENHANCEMENT used at LOCATION 8
    elif choice == "Examine Key":
        print ("Looks like it's a magical key. Let's keep it afe until we have to use it. \n")

    #ENHANCEMENT used at 5
    elif choice == "Eat Donut":
        print("Yummy! Energy boosted! \n")
        PLAYER.remove_item("Donut")

    #ENHANCEMENT used at 5
    elif choice == "Drink Coffee":
        print("Careful! It's hot!")
        PLAYER.remove_item("Second Cup Coffee \n")

    elif choice == "Quit":
        print ("Thanks for playing \n")
        exit()
    else:
        print ("I didn't know understand. Please choose a valid command. \n")
    #return PLAYER
