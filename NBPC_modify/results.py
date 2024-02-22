import pandas as pd 

def isn_max_total_cost(csv_file):
    str_sql = csv_file[csv_file["Defective "] == True]
    filter = str_sql["Total Cost"].max() 
    filtered_df = str_sql[str_sql['Total Cost'] == filter]
    return filtered_df["ISN"].to_frame() 

def max_min_average(csv_file,column,data_name):
    str_sql = csv_file[csv_file["Defective "] == True]
    filter_max = str_sql[column].max()
    filter_min = str_sql[column].min()
    filter_average = str_sql[column].mean().round(2)
    result_df = pd.DataFrame({
    column: ['Max', 'Min', 'Average'],
    data_name: ["{:.2f}".format(filter_max), "{:.2f}".format(filter_min), "{:.2f}".format(filter_average)]
    })
    return result_df
    