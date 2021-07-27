
def IdentifyNulls(df):
    totalLen = df.shape[0]
    nulls = df.isnull().sum()
    nulls = nulls.reset_index()
    nulls.columns = ['Name', 'Nulls']
    nulls['Percentage'] = nulls['Nulls']*100 / totalLen  # Calc percentage of null values in each column
    nulls.sort_values('Percentage', ascending=False, inplace=True)
    print(nulls.head(200))

