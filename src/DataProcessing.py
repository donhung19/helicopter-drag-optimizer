import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

class ProcessData:
    def __init__(self, path_data):
        self.path = path_data

    def loadData(self):
        df = pd.read_csv(self.path)
        if df is None:
            return None
        return df
        
    def ValidateData(self, df):
        # convert to number, str
        cols_Tonumber = ['rho','f_factor','weight','k_factor','rotor_radius']
        for col in cols_Tonumber:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df['name'] = df['name'].astype(str)

        # delete rows have empty value
        df = df.dropna()

        # mask
        df = df[(df['f_factor'] > 0) & (df['rotor_radius'] > 0)]

        data_list = df.to_dict(orient='records')
        return data_list
    
    def ExportReport(self, model_lists, v_range, path_output):
        report_list = [obj.GetResult(v_range) for obj in model_lists]
        df_report = pd.DataFrame(report_list)
        df_report.to_csv(path_output, index=False)
    