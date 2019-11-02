import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


data = pd.read_csv("./scripts/grid_weather_data.csv", delimiter=',')
data.fillna(np.inf, inplace=True)


def get_id(name_farm: str) -> int:
    pass

def get_datas_by_id(data: pd.DataFrame, name_farm: str, column: str) ->tuple:
    pass

def plotp(data: pd.DataFrame, column: str):
    pass
