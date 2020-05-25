import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, y, y_pred, residuals=None):
        self.residuals= residuals
        self.y= y
        self.y_pred = y_pred

    def run_calculations(self):
        resids= np.array(self.y)- np.array(self.y_pred)
        return resids

    def plot(self):
        if self.residuals is None:
            self.residuals= self.run_calculations()
        plt.hist(self.residuals)
        plt.title('Residual distributions')
        plt.xlabel('residuals')
        plt.ylabel('count')



