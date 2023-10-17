import pandas as pd

metadata_df = pd.DataFrame()
metadata_df["nulls"] = df.isnull().sum()
metadata_df["dtype_things"] = df.dtypes
metadata_df["memory"] = df.memory_usage()
metadata_df
        
