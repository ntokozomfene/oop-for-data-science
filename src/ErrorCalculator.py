import numpy as np
import math
import matplotlib.pyplot as plt

class ErrorCalculator:
    
    def __init__(self, y, y_pred):
        import numpy as np
        self.y= np.array(y)
        self.y_pred= np.array(y_pred)
        self.size= len(y)
        self.check_size(y, y_pred)
        
    def check_size(self, y, y_pred):
        if len(self.y)== len(self.y_pred):
            return True
        else:
            raise ValueError(f'damn bro. size {self.y} and {self.y_pred}')
            
    def get_residuals(self):
        #for each in self.y:
        #    total_res= self.y_pred- self.y
        #return total_res
        return self.y_pred- self.y
    
    
    def get_standardised_residuals(self):
        resids= self.get_residuals()
        self.std_resids= self.standard_scaler(resids)
        #self.std_y_pred=  self.standard_scaler(self.y_pred)
        #return self.std_y, self.std_y_pred
        return self.std_resids
        
    
    def standard_scaler(self, a):
        standard_dev= np.std(a)
        average= a.mean()
        a_std= (a- average)/ standard_dev
        return a_std  
        
    
    def get_mse(self):
        my_mse= sum((self.y_pred -self.y)**2/ self.size)
        return my_mse
    
    def get_rmse(self):
        rmse= math.sqrt(self.get_mse())
        return rmse
    
    def error_summary(self):
        resids= self.get_standardised_residuals()
        print('error summary:')
        print(f'average standard residuals: {resids.mean()}')
        print(f'minimum standard residuals: {min(resids)}')
        print(f'maximum standard residuals: {max(resids)}')
        print(f'MSE: {self.get_mse()}')
        print(f'RMSE: {self.get_rmse()}')