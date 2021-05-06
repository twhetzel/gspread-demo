#!/usr/bin/env python3
import gspread

gc = gspread.service_account()

# Open Spreadsheet
sh = gc.open("gspread Demo file")
print(sh.sheet1.get('A1'))

# Get a list of all Worksheets
worksheet_list = sh.worksheets()
print(f"All Worksheets: {worksheet_list}")

# Get first worksheet by Index
worksheet = sh.get_worksheet(0)

# Get worksheet by Name
worksheet_name = sh.worksheet("Sheet1")
print(f"Worksheet name: {worksheet_name}")

# Get all data from worksheet
list_of_dicts = worksheet.get_all_records()
print(f"All data: {list_of_dicts}")


