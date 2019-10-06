'''
lamb_martin - Some Data Science helper functions. (Assignment)
'''

import pandas as pd
import numpy as np

def reduce_mem_usage(df,verbose=True):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.  
        
        credit: https://www.kaggle.com/gemartin/load-data-reduce-memory-usage
    """
    
    df = df.copy()
    
    if verbose:
        start_mem = df.memory_usage().sum() / 1024**2
        print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))
    
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    
    return df

def split_datetime(X,col):    
    X = X.copy()
    if (X[col].dtypes == np.dtype('datetime64[ns]')):
        col_yr=col+'_year'
        col_mo=col+'_month'
        col_dy=col+'_day'
        
        X[col_yr]=X[col].dt.year
        X[col_mo]=X[col].dt.month
        X[col_dy]=X[col].dt.day
        
        #X=X.drop(col,axis=1)
        return X
    else:
        print("Column not 'datetime' type")
        return