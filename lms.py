class Lms:
    def __init__(self,id=0, name="",author="",status=1):
        self.id=id
        self.name=name
        self.author=author
        self.status=status
        
    def __str__(self):
        data=str(self.id)+ " ," + self.name +" ,"+ self.author+" ,"+str(self.status)
        return data

