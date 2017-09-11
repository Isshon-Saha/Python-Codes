class start:
    def __init__(self,**kwargs):
        self.Data=kwargs
    def getType(self):
        return self.Data["Type"]
    def getAge(self):
        return self.Data["Age"]

