def create_dict(keys,values):
    return dict(zip(keys,values))
def exists(item,collection):
    return item in collection
def add_item(key,value,d):
    
      if isinstance(d,dict):
        d[key]=value
        
def delete_item(key,d):
    if isinstance(d,dict):
        if exists(key,d):
            del d[key]
            
        else:
            pass
    else:
        pass
       