import pandas as pd

data=pd.read_csv("output.csv")

data['Price']=data['Price'].replace('£','',regex=True).astype(float)

data['Price_Caterogy']=data['Price'].apply(lambda x: 'Cheap' if x<40 else 'Expensive')
print(data[['Price','Price_Caterogy']].head())

data.to_csv('cleaned_output1.csv',index=False)