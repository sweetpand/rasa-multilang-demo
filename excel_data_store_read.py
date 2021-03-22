import pandas as pd
import os

def DataStore(name, number, email, occupation):
    if os.path.isfile('user_data.xslx'):
        df=pd.read_excel('user_data.xslx')
        df.append([[name, number, email, occupation]])
        df.to_excel('user_data.xlsx', index=False)
    else:
        df=pd.DataFrame([[name, number, email, occupation]],
                        columns=['name', 'number', 'email', 'occupation'])
        df.to_excel('user_data.xlsx', index=False)