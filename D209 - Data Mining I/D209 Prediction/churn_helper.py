#import libraries, settings, dataset and autocleaning from helper file

# Import statements
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from time import time
from sklearn.metrics import confusion_matrix


binary_dict = {'Yes': 1,
               'No': 0,
               np.NaN: 0}

def churnauotclean(df):
    
    to_string = ['Zip', 'Lat', 'Lng']
    df[to_string] = df[to_string].astype(str)

    
    df.rename(columns = {'Item1':'Timeliness',
                     'Item2':'Fixes',
                     'Item3':'Replacements',
                     'Item4':'Reliability',
                     'Item5':'Options',
                     'Item6':'Respectfulness',
                     'Item7':'Courteous',
                     'Item8':'Listening'},
          inplace=True)
    
    useless_cols = ['CaseOrder','Customer_id','Interaction', 'UID', 'City', 'County', 'Zip', 'Lat', 'Lng','TimeZone', 'Job']
    
    df.drop(useless_cols, axis=1, inplace=True)

    df.replace({'Yes':1, 'No':0}, inplace=True)

