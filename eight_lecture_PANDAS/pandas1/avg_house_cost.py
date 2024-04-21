import pandas as pd

file_1 = 'sample_data/california_housing_train.csv'

df = pd.read_csv(file_1)
#DataFrame.head(n=5)
print(df)