class oggetto:

    attributes = None
    def __init__(self):
        self.attributes = dict()
        

    def add(self,nameAttr,value):
        self.attributes[nameAttr]=value 
           
    
class libro(oggetto):
    def __str__(self):
        st = "libro id=' " + self.attributes["id"] + " '\r\n"
        for value in self.attributes.items():
            if value[0]=="id":
                continue
            st+=value[0] + " " + value[1] + "\r\n"
        
        return st
    
class cd(oggetto):
    def __str__(self):
        st = "cd id=' " + self.attributes["id"] + " '\r\n"
        for value in self.attributes.items():
            if value[0]=="id":
                continue
            st+=value[0] + " " + value[1] + "\r\n"
        
        return st