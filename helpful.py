class Helpful:
    
    @staticmethod
    def sum(list):
        sum = 0
        for x in list:
            sum += x
        
        return sum
    
h = Helpful()
print(h.sum([1,2]))