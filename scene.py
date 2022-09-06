import time
from objects import Area, Items


class Scene:

    def build_scene(name, user_map):
        
        areas = []
        num_areas = user_map['areas']
        
        for i in range(num_areas):
            area = Area.build_area(name)
            items = Items.get_items()
            area['items'].append(items.copy())
            areas.append(area.copy())
        return areas