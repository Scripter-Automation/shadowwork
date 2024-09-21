from pandas import Timestamp, DateOffset
import pandas as pd

"""
Janitor is a helper class designed to facilitate the cleaning of data
In the case of having empty columns or 
"""
class Janitor:
    def __init__(self):
        ""
    def __match_periods_intervals(self,i:Timestamp,period:str,interval:int,add_or_sub:bool):
        exp = 1 if add_or_sub==False else 2
        match period:
            case "d":
                period_j = i+(-1)**exp*DateOffset(days=interval)
            case "h":
                period_j = i+(-1)**exp*DateOffset(hours=interval)
            case "m":
                period_j = i+(-1)**exp*DateOffset(minutes=interval)
            case  _:
                raise ValueError("Invalid time unit")
        return period_j

    @staticmethod
    def match_date_until_found(self,data:pd.DataFrame,i:Timestamp,period:str,interval:int,add_or_sub:bool)->Timestamp:
            i=self.__match_periods_intervals(i,period,interval,add_or_sub)

            while i not in data.index:
                i=self.__match_periods_intervals(i,period,interval,add_or_sub)
            return i
    
    @staticmethod
    def clean_unfinished_row(self, data:pd.DataFrame):
        data.dropna(0,"any", inplace=True)

    @staticmethod
    def clean_unfinished_columns(self, data:pd.DataFrame):
        data.dropna(1,"any", inplace=True)

    @staticmethod
    def clean_empty_row(self, data:pd.DataFrame):
        data.dropna(0,"all", inplace=True)

    @staticmethod
    def clean_empty_column(self, data:pd.DataFrame):
        data.dropna(1,"all", inplace=True)
    
    @staticmethod
    def swap_to_integer_indexing(self, data:pd.DataFrame):
        