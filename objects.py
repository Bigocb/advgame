








class Area:
    
    # what goes into the area
    # - items
    # - exits
    # - others
    
    def build_area():
        
        exits = Area.get_exits()
        
        items = Area.get_items()
        
        area = items+exits
        
        return area
        
    
    def get_exits():
        return 1
        
        
    def get_items():
        return 1
        
        
    def get_others():
        return 1
    

    def check_user_data():
        return False
        
        
class Items:
    
    def get_item():
        return 1