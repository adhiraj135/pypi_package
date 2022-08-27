import pandas as pd
import os

class linear_dsa:
    def fillna:
        filename=input("enter the csv file name:")
        os.chdir('C:\\Users\\DELL\\Downloads')
        df=pd.read_csv(filename)
        for i in df.columns:
            df[i]=df[i].fillna(df[i].mean())
            print(df[i])

    def replace_zeros:
        for i in df.columns:
            df[i]=df[i].replace(0,df[i].mean())
            print(df[i])

