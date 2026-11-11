class User:
    
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
        self.user = {}
        
    
    def create_user(self, email_id, name):
        if not self.user.get(self.mobile_number, None):
            self.user[self.mobile_number] = {"name":name, "email":email_id}            
        else:
            raise Exception("User already exist")
            
    
    