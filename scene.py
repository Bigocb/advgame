import time
from objects import Area, Items


class Scene:

    def build_scene(name):
        area = Area.build_area(name)
        items = Items.get_items()
        area['items'].append(items)
        return area