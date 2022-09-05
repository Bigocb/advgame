#### Notes


flow idea:
    - user logs on (browser cookie like tivia)
    - check last location
    - check db to see if user has that room and config stored. if not create and save room. do we genertate first x number of rooms. as the user gets withing 1 room of the edge gen the next 4 rooms. load those to memory

room generator function to be run if user doesnt have the room stored.

maybe if the generation is fast we start put by generating all rooms. then we can add complexity

phase 1: 
    small 4 room map.

map = {
    "start" : "",
    "hall_1" : "",
    "hall_2" : "",
    "hall_3" : ""
}