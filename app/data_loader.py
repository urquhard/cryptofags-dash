import pandas as pd
from flask import current_app
from .config import Config

def load_data(envs: Config):
    # Load CSV or other formats. Adjust as needed.
    data_file_1 = envs['DATA_FILE_1']
    data_file_2 = envs['DATA_FILE_2']
    
    df1 = pd.read_csv(data_file_1)
    df2 = pd.read_csv(data_file_2)
    return df1, df2
