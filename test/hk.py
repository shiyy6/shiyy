import pandas as pd
import os

path = 'D:\文档\data\底层\barra\hkbarra.xlsx'

pwd = os.getcwd()
os.chdir(os.path.dirname(path))
df = pd.read_excel(os.path.basename(path))
tmp = pd.pivot_table(df,index=['ENDDATE'],columns=['FACTORNAME'],values=['RETURN'])
os.chdir(pwd)



         
            

