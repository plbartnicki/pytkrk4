class Helpful:
    
    @staticmethod
    def sum(list):
        sum = 0
        for x in list:
            sum += x
        
        return sum;
		
    @staticmethod
    def multipl(a, b, c):
        return a*b*c;
    
h = Helpful()
print(h.sum([1,2]))