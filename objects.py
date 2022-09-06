import random
import models




class Area:
    
    
    def build_area(name):
        
        area = models.area
        
        # randomize shape of area
        shape = random.choice(models.shapes)
        area['shape'] = shape[0]
        
        # num of exits based on num of walls
        area['exits'] = (Area.get_exits(shape[1]))
        
        # add magic
        #area['magic'].append(Area.get_magic())
        
        # add npc
        #area['others'].append(Area.get_others())
        
        # add monsters
        # has_monsters = random.randint(0,4)
        # num_monsters = random.randint(0,4)
        
        # if has_monsters == 1:
            #for i in range(num_monsters):
                #area['monsters'].append(Area.get_monster())
                
        # add items
        #num_items = random.randint(0,shape[1])
        #for i in range(num_items):
            #area['items'].append(Area.get_items())
            
        # add description
        area['descroption'] = Area.get_room_descrption(name, shape[0], area['exits'])
        
        return area
        
    
    def get_room_descrption(name, shape, exits):
        return f"Hey {name}, you are in a {shape} room. There are {len(exits)} exits."
    
    
    
    def get_exits(top):
        
        num_exits = random.randint(0,top)
        exits = []
        
        for i in range(num_exits):
            exit = models.exit
            e = random.randint(0,3)
            exit['id'] = i
            
            if e < 1:
                exit['type'] = "door"
            else:
                exit['type'] = "window"
			
            exits.append(exit.copy())
            
        return exits
			 
			 
	    
	    # 75% chance of door
	    
        
        
    def get_others():
        return models.other
    

    def check_user_data():
        return False
        
    
    def get_magic():
        return models.magic
        
        
    def get_monster():
        return models.monster
        
        
class Items:
    
    def get_items():
        
        return models.item