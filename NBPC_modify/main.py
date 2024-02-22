import pandas as pd 
from results import isn_max_total_cost, max_min_average

datapath = "D:/Project/NBPC_modify/data/"
NB = pd.read_csv(datapath+'NB.csv')
PC = pd.read_csv(datapath+'PC.csv')

# result 1
ans1_NB = isn_max_total_cost(NB)
ans1_PC = isn_max_total_cost(PC)
ans1 = pd.concat([ans1_NB, ans1_PC], ignore_index=True)
print(ans1)

# result 2
ans2_NB = max_min_average(NB,"Total Cost","NB")
ans2_PC = max_min_average(PC,"Total Cost","PC")
ans2 = ans2_NB.merge(ans2_PC, on='Total Cost')
print(ans2)

# result 3 
ans3 = max_min_average(NB,"Battery Cost","NB")
print(ans3)


# Output all of results into result.xlsx
excel_file_path = 'D:/Project/NBPC_modify/result.xlsx'

with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    # Write each DataFrame to a different sheet
    ans1.to_excel(writer, sheet_name='Result1', index=False)
    ans2.to_excel(writer, sheet_name='Result2', index=False)
    ans3.to_excel(writer, sheet_name='Result3', index=False)