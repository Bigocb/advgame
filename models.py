def create_player():
    return {
        "level" : 1,
        "inventory" : [{}],
        "strength" : '',
        "speed" : "",
        "views" : [],
        "facing" : 0
    }


# def get_view_types():
#     return []


def create_view():
    return {
        "id" : 0,
        "desc" : ""
    }


def create_item():
    return {
        "type" : "",
        "color" : "",
        "material" : ""
    }


def create_exit():
    return {
        "id" : 0,
        "type" : "",
        "open" : False,
        "openable" : True,
        "leadsTo" : "Outside",
    }


def create_monster():
    return {
        "type" : "",
        "health" : 0,
        "power" : 0
    }


def create_other():
    return {}


def create_magic():
    return {
        "type" : '',
        "power" : ""

    }


def create_area():
    return {
        "id" : 0,
        "shape" : "",
        "exits" : [],
        "items" : [],
        "others" : [],
        "monsters" : [],
        "magic" : [],
        "start" : False
    }


def get_room_shapes():
    return [
        ("square", 4)
    ]