# Import libraries
import pandas as pd

# Read Excel File 
data = pd.read_excel("H:/compnies task/inventam solution pvt ltd/Orders-With Nulls.xlsx")

# If you are provide csv file so read in this type
# data = pd.read_csv("H:/compnies task/inventam solution pvt ltd/Orders-With Nulls.xlsx")

# Apply sorting and get Order Date and Sales column Order Dates (latest on top)
task = data[['Order Date','Sales']].sort_values(by="Order Date" , ascending=False)

# create CSV file for result and save in this file
task.to_csv("H:/compnies task/inventam solution pvt ltd/Task_Output.csv")
print("File Save")
