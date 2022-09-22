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
        room_description, user = Story.describe_room(initial_room, user)
        user_facing = user['facing']
        user_view = user['views'][user_facing]
        room_description += user_view['desc']

        return room_description, user

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

        # if len(doors) > 0:
        #     if len(doors) == 1:
        #         room_description += f"There is {len(doors)} door. "
        #     else:
        #         room_description += f"There are {len(doors)} doors. " \
        #
        #
        # if len(windows) > 0:
        #     if len(windows) == 1:
        #         room_description += f"And {len(windows)} window."
        #     else:
        #         room_description += f"And {len(windows)} windows."

        # add user views
        user['views'] = Story.describe_view(doors, windows, room_shape)

        return room_description, user

    @staticmethod
    def describe_view(doors, windows, room_shape):

        print("DV: Start")
        print(room_shape)
        if room_shape == 'square':
            views = []
            view = models.create_view()
            for i in range(4): # todo: feed value in for range from shape map
                view['id'] = i


                windows_num = len(windows)
                door_num = len(doors)

                # Add doors to view todo: add randomness
                if door_num > 0:
                    door = random.choice(doors)
                    doors.remove(door)
                    view['door'] = [door]
                    view['desc'] = f"the wall you are facing has {len(view['door'])} doors. "

                # Add windows to view todo: add randomness
                if windows_num > 0:
                    window = random.choice(windows)
                    windows.remove(window)
                    view['window'] = [window]
                    view['desc'] += f"and {len(view['window'])} windows."

                views.append(view.copy())

            # pprint.pprint(views)

            return views
