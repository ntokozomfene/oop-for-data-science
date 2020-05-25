import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from src.Plotter import Plotter

class ScatterPlotter(Plotter):
    def __init__(self, y, y_pred):
        super().__init__(y, y_pred)
    def plot(self): 
        data = pd.DataFrame({'y':self.y, 'y_pred':self.y_pred})
        data.plot.scatter(x='y', y='y_pred')
        plt.title('Predictions vs actual values')
        plt.ylabel('Residuals')
        plt.xlabel('Predictions')
