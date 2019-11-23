import pandas as pd
#
#
starting = {'Col_1': [10, 11, 12, 13, 14, 15],
            'Col_2': [20, 21, 22, 23, 24, 25],
            'Col_3': [30, 31, 32, 33, 34, 35],
            'Name': ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL'],
            'Col_4': [40, 41, 42, 43, 44, 45],
            'Col_5': [50, 51, 52, 53, 54, 55]}

df = pd.DataFrame(starting)
print(df)
df.set_index('Name')
print(df.index)
df2 = df.set_index('Name')
print(df2)
print(df2.index)
