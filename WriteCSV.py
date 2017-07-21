import csv
import ast
with open("write_In_File.csv",'wb') as var:
    data = csv.writer(var)
    data.writerow(["Class","Marks"])
    for i in range(2):
        my_row = ast.literal_eval(raw_input("Enter your row:"))
        data.writerow(my_row)
           