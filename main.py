import time
import models
from objects import Area
from scene import Scene
import maps
import random
import pprint
from story import Story


def main ():
  
    # start new player if a returning player pick up where they left off. (thats going to be fun, tracking user location and the decorstion of the room for that user)
    player = models.player

    # todo: don't need  this eventually
    name = "Joe"

    # If not existing user build new map
    user_map = random.choice(maps.get_map())

    if not Area.check_user_data():
        area = Scene.build_scene(user_map)

        # for i, x in enumerate(area):
        #     print('-------------')
        #     print(f"Area id: {x['id']}")
        #     print('-------------')
        #     pprint.pprint(x['exits'])
        #     for p, t in enumerate(x['exits']):
        #         print(f"id: {t['id']}")
        #         print(f"type: {t['type']}")
        #         print(f"connects to: {t['leadsTo']}")
        #     print('-------------')

    # Begin story logic
    thread, user = Story.main_story_thread(area, player)
    print(thread)
    # pprint.pprint(user)

    # Save user story one last time

main()

