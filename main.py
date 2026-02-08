import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from src.models import Helicopter
from src.DataProcessing import ProcessData
from src.visualizer import Visualizer

def main():
    v_range = np.linspace(10,80,100)
    path = "data/fleet_data.csv"
    data = ProcessData(path)
    df = data.loadData()
    data_list = data.ValidateData(df)

    model_lists = [Helicopter(model) for model in data_list]

    data.ExportReport(model_lists, v_range, "report/optimal_v_report.csv")

    plot = Visualizer()
    plot.plotData(model_lists, v_range)

if __name__ == "__main__":
    main()