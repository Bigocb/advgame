import random
import models




class Area:
    
    # what goes into the area
    # - items
    # - exits
    # - others
    
    def build_area():
        
        area = models.area
        
        area['shape'] = "square"
        
        area['exits'].append(Area.get_exits())
        
        area['items'].append(Area.get_items())
        
        area['magic'].append(Area.get_magic())
        
        # add monsters
        has_monsters = random.randint(0,4)
        num_monsters = random.randint(0,4)
        
        
        if has_monsters == 1:
            for i in range(num_monsters):
                area['monsters'].append(Area.get_monster())
        
        return area
        
    
    def get_exits():
	    return random.randint(0,4)
        
        
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