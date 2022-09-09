player = {
    "level" : 1,
    "inventory" : [{}],
    "strength" : '',
    "speed" : "",
    "views" : [],
    "facing" : 0
}

# Defaults to square for now
views = []

view = {
    "id" : 0,
    "desc" : ""
}

item = {
    "type" : "",
    "color" : "",
    "material" : ""
}

exit = {
    "id" : 0,
	"type" : "",
    "open" : False,
    "openable" : True,
    "leadsTo" : "Outside",
}

monster = {
    "type" : "",
    "health" : 0,
    "power" : 0
}

other = {}

magic = {
    "type" : '',
    "power" : ""

}

area = {
    "id" : 0,
    "shape" : "",
    "exits" : [],
    "items" : [],
    "others" : [],
    "monsters" : [],
    "magic" : [],
    "start" : False
    
}

shapes = [
    ("square", 4)
]