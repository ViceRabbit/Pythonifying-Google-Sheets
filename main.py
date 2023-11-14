import gspread 

serviceAccount = gspread.service_account("/workspace/Pythonifying-Google-Sheets/gspread/service_account.json")

eyepod_spreadsheet = serviceAccount.open("Personality questions for SCP-131 test [VICERABBIT]")

formatWorksheet = eyepod_spreadsheet.worksheet("Format")

def clearrow(sheet, row): # a quick function to clear all checkboxes in altering choices
    sheet.update_cell(row, 2, False)
    sheet.update_cell(row, 3, False)
    sheet.update_cell(row, 4, False)

class initialize131Worksheet():
    def __init__(self, session, colorOfEyepod):
        self.session = session
        self.colorOfEyepod = colorOfEyepod
    def createsheet(self):
        self.thesheet = formatWorksheet.duplicate(len(eyepod_spreadsheet.worksheets()), None, f"Session {str(self.session)} - {self.colorOfEyepod}")

class change131worksheet():
    def __init__(self, thesheet):
        self.thesheet = thesheet
    def changecheckbox(self, questionInt, boolofchoice="idk", triggerbox=True):
        self.rowOfQuestion = questionInt + 1
        clearrow(self.thesheet, self.rowOfQuestion)
        self.choiceOfCol = 4 # idk column; already set
        if boolofchoice == "Yes":
            self.choiceOfCol = 2 # yes column
        if boolofchoice == "No":
            self.choiceOfCol = 3 # no column
        self.triggerbox = triggerbox
        
        self.thesheet.update_cell(self.rowOfQuestion, self.choiceOfCol, self.triggerbox)
        

ss = change131worksheet(eyepod_spreadsheet.worksheet("Session 3 - Blue + Orange"))
ss.changecheckbox(1, "Yes")
        
print("tada!!!")