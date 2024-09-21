import yfinance as yf
from src.shadowork.Data.DataProvider import DataProvider

import pandas as pd

class YFinanceProvider(DataProvider):

    data:pd.DataFrame
    
    def name(self):
        return self.name

    def __init__(self, name:str, tickers: list[str], period: str = "1y", interval:str = "1d"):
        self.name = name
        self.ticker = tickers
        self.period = period
        self.interval = interval
    
    def get_ohlc(self, ticker:str="", )->pd.DataFrame:
        ticker = yf.Ticker(self.ticker)
        return ticker.history(period = self.period, interval = self.interval)
    

    def showData(self):
        return super().showData()
    def get_data(self) -> pd.DataFrame:
        return super().get_data()
    