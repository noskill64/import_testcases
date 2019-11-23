import pandas as pd
#
#
my_path = '/home/noskill/Desktop/import_testcases/'
my_sheet = my_path + 'Reviewed_Test_cases_DCD_Updated_19062018.xlsx'
df = pd.read_excel(my_sheet, sheet_name='Settings')
print(df)
