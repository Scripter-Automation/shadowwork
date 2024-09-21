from abc import ABC, abstractmethod
import pandas as pd

class Step(ABC):
    """
    A step of a larger Model. A model is a series of steps which allow a user to generate
    way to reason a manner of creating buy or sell signals. Which allow the user to automatically make
    investment decisions. 

    """
    name:str

    def __init__(self, name):
        self.name = name

    
    
    @abstractmethod
    def method(self,data:pd.DataFrame,*args,**kwargs)->pd.DataFrame:
        """
        This is the final tested method which will be applied as the steps contribution to the model,
        no default implementation of the method is created. It's expected that the user will define his method
        in the class which inherits from this class.

        !!!All method functions must return the transformed data!!!
        """



    def test_method(data:pd.DataFrame,i:int,*args:tuple):
        """
        A special case to test your method before implementing it into the whole dataset
        Here you define a step by step implementation of your method, which will allow the user
        to verify that the result of the method will be as expected. 

        This will not be used when applying the method to the strategy but instead will be used with the
        test_generator. For example purposes the default method is an aplication to a dataframe the equation
        for the area of a square. The same is the default representation of the __repr__. To avoid using the defaults
        dont include super.test_method() nor super.__repr__() in your implementation of this abstract class
        """
        data.at[i,"Area"] = data.at[i,args[0]]*data.at[i,args[1]]

    def test_generator(self,data:pd.DataFrame, start_index:int, end_index:int,*args:tuple):
        """
        A function that returns a generator which can be used directly through a receiving variable using 
        python's core function next()
        """
        for i in range(start_index, end_index):
            print(self.__repr__())
            yield self.test_method(data,i,*args)


    def __repr__(*args)->str:
        """
        A string representation of the method. This is used in the test_generator
        to provide the user a visual representation of the values used in the calculation of such method
        Use your arguments to write an f string (formated string) enabaling to see the parameters.
        """

        return f"""
            Example:
            base x height = {args[0]} x {args[1]} = {args[0]*args[1]} 
        """
    