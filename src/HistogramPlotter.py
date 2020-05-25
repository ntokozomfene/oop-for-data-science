import numpy as np
import math
import matplotlib.pyplot as plt
from Plotter import Plotter

class HistogramPlotter(Plotter):
    #same thing as its parent, so no need to do anything.
    #use initialization of parent Plotter too
    def __init__(self, y, y_pred):
        super().__init__(y, y_pred)

