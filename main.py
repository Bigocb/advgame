import time

import models

from objects import Area


# player model

# so we're going to have to have user persistence if you've been in a room one time then that should be what you get the next time you go into that room so the system that I've come up with for having an empty container of a room and then having another pass to put items and chest contents in will have to initially paint or build a room for the user and then that will be the rooms state going forward. For that individual we can use the same cookie user control I have in the trivia game

def main ():
   # print("hey, whats your name?")
  
    # start new player if a returning player pick up where they left off. (thats going to be fun, tracking user location and the decorstion of the room for that user)
    player = models.player
    print("-----------")
    print(player)
    
    name = input("hey, whats your name? ")
    print(f"WELCOME TO THE ADVENTURE GAME {name.upper()}!")
    time.sleep(0)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("Lets get weird")
    
    print("you wake up...")
    
    print(Area.build_area())
    
    if int(player['level']) < 2:
        scene1(player)
        

# battle module
def scene1(player):
    
    # does player have this room built already
    
    # if yes load the room 
    # else build a new room and save it for the user
    
    print("""Lily wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
        Now she has two choices she can either stay in the room or check what the sound might be about.
 
        Type your choice: Stay or Evaluate?
    """)
    
    if int(player['level']) < 2:
        print('does this work')
 
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="STAY"):
            print("\nLily decides to stay in the room and ends up staying inside forever as noone seems to come to help her.")
            ans = 'correct'
        elif(c1.upper()=="EVALUATE"):
            print("Lily exits the room silently and reaches the main hall.")
            ans='correct'
            main_hall()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Evaluate?")
            c1 = input()


def main_hall():
    
    print("""
            In the main hall, she finds a strange but cute teddy bear on the floor. 
            She wanted to pick the teddy up. 
            But should she? It doesn't belong to her. (•˳̂•̆)
 
            Type your choice: Pick or Ignore?
 
            """)
    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="PICK"):
            print("""\nThe moment Lily picked up the the teddy bear. The Teddy bear starts TALKING!The bear tells Lily that she is in grave danger as there is a monster in the house.And the monster has captured her PARENTS as well!But he hugged her and told her not to get scared as he knows how to beat the moster!""")
            time.sleep(2)
            print("""\nThe bear handed lily a magical potion which can weaken the moster and make him run away!He handed her the potion and then DISAPPEARED!Lily moved forward.""")
            ans = 'correct'
            pick="True"
        elif(c1.upper()=='IGNORE'):
            print("""\nLily decided not to pick up the bear and walked forward.""")
            ans='correct'
            pick="False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            c1=input()
    time.sleep(2)
    scene3(pick)


def scene3(pick_value):
    
    print("""\n\nAfter walking for a while, Lily saw the MONSTOR in front of her!
    It had red eyes and evil looks. She got very scared! """)
    time.sleep(2)
    if(pick_value=="True"):
        time.sleep(2)
        print("""But then she remembered! She had the magic portion and she threw it on the moster!
              Well she had nothing to lose!""")
        time.sleep(2)
        print("\n The monster SCREAMED in pain but he managed to make a portal and pushed Lily to a new world!")
    elif(pick_value=="False"):
        print("The monster attacked Lily and hurt her! She was then thrown to the new world by the monster!")

main()
print("\n\n")
print("=================================END OF CHAPTER 1=================================")

