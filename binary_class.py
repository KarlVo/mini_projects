#klassen används till att genomföra letandet med given input (lista och tal som ska hittas)
class Binary:
    
    def __init__(self, list, number):
        self.list = list
        self.number = number
    
    def iterate(self, list, number):
        self.upper_bound = len(self.list)   
        self.lower_bound = 0
        print(self.list)
        
        while True:
            self.middle = int((self.upper_bound+self.lower_bound)/2)

            print("new round", self.middle)
            if self.list[int(self.middle)] < self.number:
                self.list = self.list[int(self.middle): int(self.upper_bound)]
               
                self.lower_bound = self.middle
                self.upper_bound = self.upper_bound 
                
                if self.lower_bound or self.upper_bound == self.number:
                    print("Your number was found")
                    break
                
            elif self.list[int(self.middle)] > self.number:
                self.list = self.list[int(self.lower_bound): int(self.middle)]
                self.lower_bound = self.lower_bound
                self.upper_bound = self.middle
                if self.lower_bound or self.upper_bound == self.number:
                    print("Your number was found")
                    break
    
            elif self.middle == int(self.number):
                print("Your number is in the given list")
                break
            else:
                print("Your number was not found")
                break
        

    

    

    