import random
import models




class Area:
    
    
    def build_area():
        
        area = models.area
        
        # randomize shape of area
        shape = random.choice(models.shapes)
        area['shape'] = shape[0]
        
        # num of exits based on num of walls
        area['exits'].append(Area.get_exits(shape[1]))
        area['items'].append(Area.get_items())
        area['magic'].append(Area.get_magic())
        
        # add monsters
        has_monsters = random.randint(0,4)
        num_monsters = random.randint(0,4)
        
        if has_monsters == 1:
            for i in range(num_monsters):
                area['monsters'].append(Area.get_monster())
        
        return area
        
    
    def get_exits(top):
	    return random.randint(0,top)
        
        
    def get_items():
        return 1
        
        
    def get_others():
        return 1
    

    def check_user_data():
        return False
        
    
    def get_magic():
        return models.magic
        
        
    def get_monster():
        return models.monster
        
        
class Items:
    
    def get_item():
        return 1