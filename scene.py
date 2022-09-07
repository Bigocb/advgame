import time
from objects import Area, Items


class Scene:

    @staticmethod
    def build_scene(user_map):

        areas = []
        num_areas = user_map['areas']
        # print(f"num areas: {num_areas}")
        areas.append({"start" : False})

        # Build out the rooms
        for i in range(num_areas):
            area = Area.build_area(user_map)

            # set first area to start when there are multiple rooms
            area['start'] = False
            if not areas[0]['start'] and len(area['exits']) > 0:
                area['start'] = True
                areas[0]['start'] = True

            # Add itmes
            items = Items.get_items()
            area['items'].append(items.copy())

            # Add magic

            # Add others

            # Add monsters

            # Set area id
            area['id'] = i

            areas.append(area.copy())

        # How do we decide how to connect the rooms
        areas.remove(areas[0])
        if len(areas) > 2:
            # Connecting logic here
            areas = Scene.connect_areas(areas)

        return areas

    @staticmethod
    def connect_areas(areas):
        # print(f"areas: {len(areas)}")
        # for a, b in enumerate(areas):
        #     print(b)

        return areas
