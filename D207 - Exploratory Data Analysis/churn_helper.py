import numpy as np
import pandas as pd

def churn_add_clean(df):
    
    to_string = ['Zip', 'Lat', 'Lng']
    df[to_string] = df[to_string].astype(str)
    
    df.rename(columns = {'Item1':'Response',
                     'Item2':'Fixes',
                     'Item3':'Replacements',
                     'Item4':'Reliability',
                     'Item5':'Options',
                     'Item6':'Respectfulness',
                     'Item7':'Courteous',
                     'Item8':'Listening'},
          inplace=True)
    
    df = df.astype({'Population':int, 
                'Area':'category',
                'Children':int, 
                'Age':int,
                'Income':float, 
                'Marital':'category', 
                'Gender':'category', 
                'Churn':'category',
                'Outage_sec_perweek':float, 
                'Email':int, 
                'Contacts':int, 
                'Yearly_equip_failure':int,
                'Techie':'category', 
                'Contract':'category', 
                'Port_modem':'category', 
                'Tablet':'category', 
                'InternetService':'category',
                'Phone':'category', 
                'Multiple':'category', 
                'OnlineSecurity':'category', 
                'OnlineBackup':'category',
                'DeviceProtection':'category', 
                'TechSupport':'category', 
                'StreamingTV':'category', 
                'StreamingMovies':'category',
                'PaperlessBilling':'category', 
                'PaymentMethod':'category', 
                'Tenure':float, 
                'MonthlyCharge':float,
                'Bandwidth_GB_Year':float, 
                'Response':int, 
                'Fixes':int, 
                'Replacements':int, 
                'Reliability':int, 
                'Options':int,
                'Respectful':int, 
                'Courteous':int, 
                'Listening':int}, copy=False)