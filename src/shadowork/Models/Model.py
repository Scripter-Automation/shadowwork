from abc import ABC
from src.shadowork.Models.Step import Step
import pandas as pd

class Model(ABC):

    steps:dict[str:Step]
    order:list[str]=[]

    def __init__(self, steps:list[Step]):
        """
            A Model must come with it's series of steps 
            and the steps must be organized in the first in first executed fashion.
            The default implementation only creates a dict of steps with each step's
            name as the key. 

            The order of the steps may be changed later with the set_order function of this abstract class
        """
        
        for step in steps:
            self.order.append(step.name)
            self.steps[step.name] = step
    
    def check_order(self):
        """
            A function which will print into the console the order of the steps in this model
        """
        print("Step order:")
        for i,step in enumerate(self.order):
            print(f"{i}: Step Name = {step}")

    def set_order(self, order:list[str]):
        """
            A function which allows the user to redifine the order on which his steps will be executed
            The order must be a list of strings where each string is the name of a step in this model.
            If a name in the new order list is not contained in the previous order, then a ValueError
            will be raised.
        """
        for name in order:
            if not (name in self.order):
                raise ValueError(f"Step {name} does not exist in this model")
            
        self.order = order

    def run_model_step(self, step_name:str, data, *args, **kwargs)->pd.DataFrame:
        """
        A function which will run a single step of this model with the given data and arguments
        The step must be a part of this model. If not, a ValueError will be raised.

        The purpose of this function is to be used by the framework to apply every step of the model in the
        master provider. 
        """
        if not (step_name in self.steps):
            raise ValueError(f"Step {step_name} does not exist in this model")
        
        return self.steps[step_name].method(data, *args, **kwargs)

    @staticmethod
    def apply_step(step:Step, data:pd.DataFrame, *args, **kwargs)->pd.DataFrame:
        """
            A function which applies a step to the data. The step must be a step object.
            The data must be a pandas DataFrame.

            The purpose of this function is to allow a user to transform data outside of the master provider
            and only wants to apply a single step. Giving data independence from the master provider if that
            funcitonality is desired
        """
        return step.method(data,*args,**kwargs)