class DynamicArray:
    def __init__(self, capacity : int=10):
        self.__capacity=capacity
        self.__size=0
        self.__array=[None]*capacity

    def __len__(self):
        return self.__size

    def resize(self,new_capacity):
        new_array=[None]*new_capacity
        for i in range (self.__size):
            new_array[i]=self.__array[i]
        self.__array=new_array
        self.__capacity=new_capacity


    def append(self,value):
        if (self.__size==self.__capacity)        :
            self.resize(2 *self.__capacity)
        self.__array[self.__size]=value
        self.__size+=1


    def __getitem__(self,index):
        if (index<0 or index>=self.__size):
            raise IndexError("Index out of range")
        return self.__array[index]
    

    def __setitem__(self, index, value):
        if ( index<0 or index>=self.__size):
            raise IndexError("Index out of range")
        self.__array[index]=value

    def __str__(self):
        return f"({[self.__array[i] for i in range(self.__size)]})"

    def __repr__(self):
        return f"DynamicArray({[self.__array[i] for i in range(self.__size)]})"
    

    def __add__(self,other: "DynamicArray"):
        if not isinstance(other,DynamicArray):
            raise ValueError
        new__array=DynamicArray(self.__size+other.__size)
        for i in range(self.__size):
            new__array.append(self.__array[i])
        for i in  range(other.__size):
            new__array.append(other.__array[i])
        return new__array

    def __iadd__(self,other: "DynamicArray"):
        if not isinstance(other,DynamicArray):
            raise ValueError
        for i in range(other.__size):
            self.append(other.__array[i]) 
        return self
    
    def __eq__(self, other: "DynamicArray"):
        if not isinstance(other,DynamicArray):
            raise ValueError
        if self.__size!=other.__size:
            return False
        for i in range(self.__size):
            if self.__array[i]!=other.__array[i]:
                return False
        return True
    
    def __ne__(self,other : "DynamicArray"):
        return not self.__eq__(other)
    
    def __lt__(self,other : "DynamicArray"):
        for i in range(min(self.__size,other.__size)):
            if self.__array[i]!=other.__array[i]:
                return self.__array[i]<other.__array[i]
        return self.__size<other.__size
        

    def __le__(self,other : "DynamicArray"):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other : "DynamicArray"):
        for i in range(min(self.__size,other.__size)):
            if self.__array[i]!=other.__array[i]:
                return self.__array[i]>other.__array[i]
        return self.__size>other.__size
    
    def __ge__(self, other : "DynamicArray"):
        return self.__gt__(other) or self.__eq__(other)


    def __iter__(self):
        for i in range(self.__size):
            yield self.__array[i]


    def __hash__(self) -> int:
        return hash(tuple(self.__array[:self.__size]))
