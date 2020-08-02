import math

class special_math:


    def fun(p1:tuple, p2:tuple) -> float:
        return math.sqrt((p1[0]  -  p2[0])**2  +  (p1[1]  -  p2[1])**2  +  (p1[2]  -  p2[2])**2);
    
	
	
	#Ta funkcja zwraca liczbę zespoloną na podstawie dwóch liczb zespolonych i reguły opisanej w zadaniu TASK-999
    def fun_add_two_comple_number_with_rule_1(number1:complex, number2:complex):
        if(abs(number1) > 0.5 or abs(number2) > 0.5):
                return 0.5*(number1 + number2)
				
        elif(abs(number1 + number2) > 0.5):
            return 0.5*number1 + number2

        else return 0.5*number2;