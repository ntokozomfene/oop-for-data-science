import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from src.Plotter import Plotter

class ScatterPlotter(Plotter):
    def __init__(self, y, y_pred):
        super().__init__(y, y_pred)
    def plot(self): 
        plt.scatter(self.y_pred, self.residuals)
        plt.title('Predictions vs actual values')
        plt.ylabel('Residuals')
        plt.xlabel('Predictions')
