import gspread 

serviceAccount = gspread.service_account("/workspace/Pythonifying-Google-Sheets/gspread/service_account.json")

eyepod_spreadsheet = serviceAccount.open("Personality questions for SCP-131 test [VICERABBIT]")

formatWorksheet = eyepod_spreadsheet.worksheet("Format")

#print(f"amount of rows: {worksheet.row_count}")
#print (f"amount of columns: {worksheet.col_count}")
#print(worksheet.acell('a4').value)
#print(worksheet.get('a2:d17'))

#worksheet.update('b2:d3', [[True, True, True], [True, False, True]])

#print(worksheet.get_all_values())

newthing = formatWorksheet.duplicate(len(eyepod_spreadsheet.worksheets()), None, "goofy gooberonis!") #duplicates from format; indexes at end

print("tada!!!")