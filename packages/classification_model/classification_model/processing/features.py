import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class AspectBinning():
    def __init__(self, variables=None):

        self.aspect = ['N', 'E', 'S', 'W']

        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def get_aspect(self, x):
        if(x < 45):
            direction = self.aspect[0]
        elif(x > 45 and x < 135):
            direction = self.aspect[1]
        elif(x > 135 and x < 225):    
            direction = self.aspect[2]
        elif(x > 225 and x < 315):    
            direction = self.aspect[3]
        else:
            direction = self.aspect[0]
        
        return direction

    def transform(self, X):
        X = X.copy()
        X['Aspect_Dir'] = X.Aspect.apply(lambda x: self.get_aspect(float(x))) 
        dummies = pd.get_dummies(X['Aspect_Dir'])
        for row_name in self.aspect:
            X[row_name] = dummies[row_name]
            
        return X

class HydrologyFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables    

    def fit(self, X, y=None):
    	return self


    def transform(self, X):
    	X = X.copy()
    	X['Euclidean_Distance_To_Hydrology'] = np.sqrt(X['Horizontal_Distance_To_Hydrology']**2 + X['Vertical_Distance_To_Hydrology']**2)
    	X['Slope_to_hydrology'] = [0 if dist<0 else 1 for dist in X['Vertical_Distance_To_Hydrology']]
    	return X


class KernelFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables


    def fit(self, X, y=None):
    	return self


    def transform(self, X):
    	X = X.copy()
    	X['Elevation2'] = X['Elevation']**2
    	X['ElevationLog'] = np.log1p(X['Elevation'])
    	return X
