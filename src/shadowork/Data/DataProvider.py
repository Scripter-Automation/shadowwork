from enum import Enum
import pandas as pd
from pandas import Timestamp, DateOffset
from abc import ABC, abstractmethod
from typing import Callable, Iterator
from datetime import datetime
from shadowork.Models.Model import Model





class DataProvider(ABC):

    """
        Short Description: A class which defines the interface for all data providers

        (Need to update this documentation given to heavy changes in the architecture)

    """
    data:pd.DataFrame

    @property
    @abstractmethod
    def name(self)->str:
        pass


    @abstractmethod
    def get_data(self)->pd.DataFrame:
        """
            A method designed to retrive data from a specific provider. 
            It should return a pandas DataFrame object.
        """
        return self.data
    
    @staticmethod
    def set_data(data:pd.DataFrame, provider:'DataProvider'):
        """
            A method designed to modify the data of a provider
            The purpose of this function is to be used inside of the master provider, 
            Which will allow the master provider to set the data for a specific provider once a
            transformation is ready to be made.
        """
        if isinstance(data, pd.DataFrame):
            provider.data = data
        else:
            raise ValueError("Data must be a pandas DataFrame")





"""
    A class designed to manage all your data providers
"""
class MasterProvider:
    
    providers:dict[str:DataProvider]
    methods: dict[str:Model]
    preliminary_graphs:list[str]
    preliminary_tables:list[str]
    final_graphs:list[str]
    final_tables:list[str]

    def __init__(self, providers: list[DataProvider], models:list[Model]):
        self.stored_configurations = providers
        self.providers = {}
        self.methods = {}
        for provider in providers:
            self.providers[provider.name] = provider
        for model in models:
            self.methods[model.name] = model

    def get_provider(self,provider_name:str):
        if provider_name in self.providers.keys():
            return self.providers[provider_name]
        else:
            raise Exception({
                "error": "Provider not found",
                "provider": provider_name
            })
        
    def get_all_providers(self):
        return self.providers

    def add_provider(self, provider:DataProvider):
        self.stored_configurations.append(provider)
        self.providers[provider.name]=provider.provider

    def apply_model(self, provider_name:str, method_name:str, *args, **kwargs):
        """
            This function is meant to be ran when the model is already tested and complete.
            When executed it will take the selected DataProvider and modify it's data so
            that the provider will store the result of the model, having it ready to pass into backtesting.
            After this point the data of the provider should not be modified outside of the MasterProvider.
        """
        for step in self.methods[method_name]:
            DataProvider.set_data(
                Model.apply_step(
                    step,
                    self.providers[provider_name].get_data(),
                    *args,
                    **kwargs
                    ),
                self.providers[provider_name]
                )
    def add_graph_to_preliminary_report():
        """"""
    def add_table_to_preliminary_report():
        """"""
    def generate_preliminary_report():
        """"""
    
    def generate_final_report():
        """"""
    
    def add_graph_to_final_report():
        """"""

    def add_table_to_final_report():
        """"""

