

class Factorial:
    def __init__(self, num):
        self.__result = num
        
        
    def get_result(self):
        self.compute_factorial(self.__result)
        return self.__result
        
        
    def set_result(self, result):
        self.__result = result
        
        
    def compute_factorial(self, result):
        """This is a recursive function
        to find the factorial of an integer"""

        if result == 0 or result == 1:
            self.__result = 1
        else:
            self.__result = result * self.compute_factorial(result-1)
            
        return self.__result
            
        
    
    
if __name__ == '__main__':
    num = int(input("\nPlease enter a number: "))
    
    result = Factorial(num)
    
    print("\nThe factorial of {} is {}\n".format(num, result.get_result()))
    