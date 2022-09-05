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
        
        return area
        
    
    def get_exits():
	    return random.randint(0,4)
        
        
    def get_items():
        return 1
        
        
    def get_others():
        return 1
    

    def check_user_data():
        return False
        
        
class Items:
    
    def get_item():
        return 1