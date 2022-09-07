import random
import models


class Area:

    @staticmethod
    def build_area(user_map):

        area = models.area

        # randomize shape of area
        shape = random.choice(models.shapes)
        area['shape'] = shape[0]

        # num of exits based on num of walls
        area['exits'] = (Area.get_exits(shape[1]))


        # add magic
        #area['magic'].append(Area.get_magic())

        # add npc
        #area['others'].append(Area.get_others())

        # add monsters
        # has_monsters = random.randint(0,4)
        # num_monsters = random.randint(0,4)

        # if has_monsters == 1:
            #for i in range(num_monsters):
                #area['monsters'].append(Area.get_monster())

        # add items
        #num_items = random.randint(0,shape[1])
        #for i in range(num_items):
            #area['items'].append(Area.get_items())

        # add description

        return area

    @staticmethod
    def get_exits(top):
        
        num_exits = random.randint(1,top)
        exits = []
        
        for i in range(num_exits):
            exit = models.exit
            e = random.randint(0,4)
            exit['id'] = i
            
            if e < 3:
                exit['type'] = "door"
            else:
                exit['type'] = "window"

            exits.append(exit.copy())
            
        return exits

    @staticmethod
    def get_others():
        return models.other

    @staticmethod
    def check_user_data():
        return False

    @staticmethod
    def get_magic():
        return models.magic

    @staticmethod
    def get_monster():
        return models.monster
        
        
class Items:

    @staticmethod
    def get_items():
        
        return models.item