class User:
    def __init__(self,first_name,last_name):
        self.fname=first_name
        self.lname=last_name

    def printfname (self):
        print (self.fname)

    def printlname (self):
        print (self.lname)

    def printfullname (self):
        print (self.fname,self.lname)
