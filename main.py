import time

import models
from objects import Area
from scene import Scene

import pprint

# player model

# so we're going to have to have user persistence if you've been in a room one time then that should be what you get the next time you go into that room so the system that I've come up with for having an empty container of a room and then having another pass to put items and chest contents in will have to initially paint or build a room for the user and then that will be the rooms state going forward. For that individual we can use the same cookie user control I have in the trivia game

def main ():
  
    # start new player if a returning player pick up where they left off. (thats going to be fun, tracking user location and the decorstion of the room for that user)
    player = models.player
    
    name = "Joe"


    if not Area.check_user_data():
        area = Scene.build_scene(name)
        
        pprint.pprint(area)
        

main()

