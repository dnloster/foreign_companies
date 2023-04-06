import pandas as pd
df = pd.read_excel('companies.xlsx')

def add_zero(x):
    if len(str(x)) == 9:
        return '0' + str(x)
    else:
        return str(x)
    
# print(df["Mã số thuế"])
df["Mã số thuế"] = df["Mã số thuế"].apply(add_zero)
df.to_excel('companies.xlsx', index=False)