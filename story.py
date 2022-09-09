import models
import random
import pprint

class Story:


    #Main story thread here function
    @staticmethod
    def main_story_thread(user_map, user):
        print("MST: Start")
        #   - Describe view of the initial room
        initial_room = user_map[0]
        room_description = Story.describe_room(initial_room, user)


        return room_description

    @staticmethod
    def describe_room(room, user):
        print("DR: Start")

        room_shape = room['shape']
        room_exits = room['exits']
        doors = []
        windows = []

        for _, i in enumerate(room_exits):
            if i['type'] == 'door':
                doors.append(i)
            else:
                windows.append(i)

        # Logic for building desc
        room_description = f"You are in a {room_shape} room. "

        if len(doors) > 0:
            if len(doors) == 1:
                room_description += f"There is {len(doors)} door. "
            else:
                room_description += f"There are {len(doors)} doors. " \


        if len(windows) > 0:
            if len(windows) == 1:
                room_description += f"And {len(windows)} window."
            else:
                room_description += f"And {len(windows)} windows."

        if room_shape == 'square':
            views = models.views
            view = models.view
            for i in range(4):

                view['id'] = i
                view, doors = Story.describe_view(doors, windows, view)
                views.append(view.copy())
                print("--------------------------")
            user['views'] = views

        # # Explain what is to the left right and in front
        # user_view = Story.describe_view(doors, windows, user)

        return room_description

    @staticmethod
    def describe_view(doors, windows, view):
        print("DV: Start")
        windows_num = len(windows)
        door_num = len(doors)

        if door_num > 0:
            door = random.choice(doors)
            # print(f"door choice: {door}")
            doors.remove(door)
            view['door'] = [door]

            view['desc'] = f"the wall you are facing has {len(view['door'])} doors. "

        if windows_num > 0:
            window = random.choice(windows)

            windows.remove(window)
            view['window'] = [window]

            view['desc'] += f"and {len(view['window'])} windows."


        pprint.pprint(view)

        return view, doors
