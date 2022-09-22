import time

import models
from objects import Area
import random
import pprint


class Scene:

    @staticmethod
    def build_scene(user_map):

        areas = []
        num_areas = user_map['areas']
        # print(f"num areas: {num_areas}")
        areas.append({"start": False})

        # Build out the rooms
        for i in range(num_areas):
            area = Area.build_area(user_map)

            # set first area to start when there are multiple rooms
            area['start'] = False
            if not areas[0]['start'] and len(area['exits']) > 0:
                area['start'] = True
                areas[0]['start'] = True

            # Add itmes
            items = models.create_item()
            area['items'].append(items.copy())

            # Add magic

            # Add others

            # Add monsters

            # Set area id
            area['id'] = i

            areas.append(area.copy())

        # connect rooms
        areas.remove(areas[0])
        if len(areas) > 1:
            areas = Scene.connect_areas(areas)

        return areas

    @staticmethod
    def connect_areas(areas):
        start_room = []
        non_start = []
        # print(f"areas: {len(areas)}")
        for x, v in enumerate(areas):
            # print(x)
            if v['start']:
                start_room.append(v)
            else:
                non_start.append(v)

        # find availble doors in non-start
        avail_doors = []
        for f, g in enumerate(non_start):
            # print(f"avail: {g}")
            for k, l in enumerate(g['exits']):
                # print(f"L: {l}")
                if l['type'] == 'door':
                    avail_doors.append((g['id'], l['id']))

        # assign doors for start
        for i, j in enumerate(start_room[0]['exits']):
            # print(f"avail_doors: {avail_doors}")
            # print("-------------")
            if j['type'] == 'door':
                if avail_doors:
                    random.shuffle(avail_doors)
                    aux_door = avail_doors.pop()
                    j['leadsTo'] = aux_door
                    areas[j['leadsTo'][0]]['exits'][j['leadsTo'][1]]['leadsTo'] = \
                        (start_room[0]['id'], j['id'])

        # assign doors for others
        for k, l in enumerate(non_start):
            # print(l['id'])
            for m, n in enumerate(l['exits']):
                if avail_doors:

                    # print("-------------")
                    random.shuffle(avail_doors)
                    # print(f"avail_doors: {avail_doors}")
                    aux_door = avail_doors.pop()
                    # print(f"n[]: {n['leadsTo']}")
                    if aux_door[0] != l['id'] and n['type'] == 'door' and n['leadsTo'] == 'Outside':
                        # print("in")
                        n['leadsTo'] = aux_door
                        areas[n['leadsTo'][0]]['exits'][n['leadsTo'][1]]['leadsTo'] = \
                            (non_start[k]['id'], j['id'])
                    # print(f"avail_doors2: {avail_doors}")

        return areas
