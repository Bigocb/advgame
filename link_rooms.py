areas =  [
    {
    "id" : 1,
    "exits" : [
        {
        "id" : 1,
        "type" : "door",
        "connects_to" : (2,1)
        }
    ],  "start" : True
    },
    {
    "id" : 2,
    "exits" : [
        {
        "id" : 1,
        "type" : "door"
        },
        {
        "id" : 2,
        "type" : "window",
        "connects_to" : (1,1)
        }
    ],
    "start" : False
    }
]

start_room = []
non_start = []

for a, b in enumerate(areas):
    if b['start']:
        start_room.append(b)
    else:
        non_start.append(b)

print(start_room)
print(non_start)

