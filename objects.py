import random
import models


class Area:

    @staticmethod
    def build_area(user_map):

        area = models.create_area()

        # randomize shape of area
        shape = random.choice(models.get_room_shapes())
        area['shape'] = shape[0]

        # num of exits based on num of walls
        area['exits'] = (Area.get_exits(shape[1]))

        # add magic
        # area['magic'].append(Area.get_magic())

        # add npc
        # area['others'].append(Area.get_others())

        # add monsters
        # has_monsters = random.randint(0,4)
        # num_monsters = random.randint(0,4)

        # if has_monsters == 1:
        # for i in range(num_monsters):
        # area['monsters'].append(Area.get_monster())

        # add items
        # num_items = random.randint(0,shape[1])
        # for i in range(num_items):
        # area['items'].append(Area.get_items())

        # add description

        return area

    @staticmethod
    def get_exits(top):

        num_exits = random.randint(1, top)
        exits = []

        for i in range(num_exits):
            has_door = False
            exit = models.create_exit()
            e = random.randint(0, 4)
            exit['id'] = i
            for _, a in enumerate(exits):

                if a['type'] == 'door':
                    has_door = True

            if not has_door:
                exit['type'] = "door"
            elif e < 3:
                exit['type'] = "door"
            else:
                exit['type'] = "window"

            exits.append(exit.copy())

        return exits

    @staticmethod
    def check_user_data():
        return False


