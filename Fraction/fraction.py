import math


class Fraction:
    def __init__(self,numerator : int,denominator : int):
        self.setNumerator(numerator)
        self.setDenominator(denominator)
        self.simplify()

    def setNumerator(self,numerator):
        if (isinstance(numerator,int)):
            self.__numerator=numerator
        else:
            print("Please enter valid numerator")

    def getNumerator(self):
        return self.__numerator



    def setDenominator(self,denominator):
        if (denominator==0):
            raise ZeroDivisionError
        if (isinstance(denominator,int)):
            self.__denominator=denominator
        else:
            print("Please enter valid Denominator")


    def getDenominator(self):
        return self.__denominator
    

    def simplify(self)->None:
        def GreatestCommonDivisior(a : int ,b : int):
            while b:
                a,b=b,a%b
            return a

        value=GreatestCommonDivisior(abs(self.__numerator),abs(self.__denominator))
        self.__numerator=self.__numerator//value
        self.__denominator=self.__denominator//value

        if self.__denominator<0:
            self.__denominator=-self.__denominator
            self.__numerator=-self.__numerator






    def __str__(self)->str:
        if (self.__denominator==1):
            return f"{self.__numerator}"
        return f"{self.__numerator}/{self.__denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.__numerator},{self.__denominator})"
    





    def __add__(self,other):
        if (isinstance(other,Fraction)):
            numerator=(self.__numerator * other.__denominator)+(other.__numerator*self.__denominator)
            denominator=self.__denominator*other.__denominator
        elif (isinstance(other,int)):
            numerator=self.__numerator+self.__numerator*other
            denominator=self.__denominator
        else:
            raise ValueError("Can't implement + operation")
        return Fraction(numerator,denominator)
    

    def __sub__(self,other):
        if (isinstance(other,Fraction)):
            numerator=(self.__numerator * other.__denominator)-(other.__numerator*self.__denominator)
            denominator=self.__denominator*other.__denominator
        elif (isinstance(other,int)):
            numerator=self.__numerator-self.__numerator*other
            denominator=self.__denominator
        else:
            raise ValueError("Can't implement - operation")
        return Fraction(numerator,denominator)
    

    def __mul__(self,other):
        if (isinstance(other,Fraction)):
            numerator=self.__numerator * other.__numerator
            denominator=self.__denominator * other.__denominator
        elif (isinstance(other,int)):
            numerator=self.__numerator * other
            denominator=self.__denominator
        else:
            raise ValueError("Can't implement * operation")
        return Fraction(numerator,denominator)


    def __truediv__(self,other):
        if (isinstance(other,Fraction)):
            if (other.__numerator==0):
                raise ZeroDivisionError
            numerator=self.__numerator*other.__denominator
            denominator=self.__denominator*other.__numerator
        elif (isinstance(other,int)):
            if (other==0):
                raise ZeroDivisionError
            numerator=self.__numerator
            denominator=self.__denominator*other
        else:
            raise ValueError("Can't implement / operation")

        return Fraction(numerator,denominator)





    def __eq__(self,other)->bool:
        if (isinstance(other , Fraction)):
            return (self.__numerator==other.__numerator) and (self.__denominator==other.__denominator)
        elif (isinstance(other,int)):
            return (self.__numerator==other*self.__denominator)
        else:
            return False
        

    def __lt__(self,other)->bool:
        if (isinstance(other,Fraction)):
            return self.__numerator*other.__numerator < other.__numerator*self.__denominator   
        elif (isinstance(other,int)):
            return self.__numerator < other*self.__denominator
        else:
            raise ValueError("Can't implement < operation") 
        


    def  __le__(self,other)->bool:
        return self==other or self<other

    def __gt__(self,other)->bool:
        return not self<other

    def __ge__(self,other)->bool:
        return self>other or self==other 

    def __ne__(self,other)->bool:
        return not self==other



    def __hash__(self) -> int:
        return hash((self.__numerator,self.__denominator))
    
    def __float__(self):
        return self.__numerator / self.__denominator
    
    def __int__(self):
        return self.__numerator // self.__denominator
    
    def __neg__(self):
        return Fraction(-self.__numerator,self.__denominator)
    

    def mixed_number(self):
        whole_number=self.__numerator // self.__denominator
        remainder=self.__numerator %  self.__denominator
        if remainder == 0:
            return f"{whole_number}"
        return f"{whole_number} {remainder}/{self.__denominator}"
    

    def __iadd__(self,other):
         return self + other
    
    def __isub__(self,other):
         return self - other
    
    def __imul__(self,other):
         return self * other

    def __itruediv__(self,other):
        return self / other
