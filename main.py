import gspread 
import time

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
        
def apiexaust(obj, questionnumber, booleo): # a quick function for API fallbacks for google
    print("Experiencing API exaustion! - Waiting for 25 seconds")
    time.sleep(25)
    obj.changecheckbox(questionnumber, booleo)
    print("We're back!")

def changeRResponses(boolinstances, sessionnumber, instcolorlists, questionnum, boolchoice): # neatly change large reqs
    for instance in boolinstances:
        if instance.replace(" ","") == "None": # skip looping if no instances
            break
        theobj = change131worksheet(eyepod_spreadsheet.worksheet(f"Session {sessionnumber} - {instcolorlists[int(instance)]}"))
        try:
            theobj.changecheckbox(questionnum, boolchoice)
        except:
            apiexaust(theobj, questionnum, boolchoice)

# create multiple sheets for every 131 instance 
sessionNumber = input("What session number is this? - ")
colorOfInstances = input("Provide the base + iris color of the instances seperated in commas - ").split(", ")
reference = list(enumerate(colorOfInstances))


for entity in colorOfInstances:
    initialize131Worksheet(sessionNumber, entity).createsheet()
    print(f"Successfully created a worksheet for {entity} under Session {sessionNumber}.")

print(f"For reference, please utilize integers to refer to specific 131 instances as given by the enumerated sheet. \n {reference}")

# 16 questions
for x in range(1, 17):
    print(f"Question {x} - {formatWorksheet.cell(x+1, 1).value} \n {reference}")
    yesinstances = input("Provide the instances that said yes - ").split(", ")
    noinstances = input("Provide the instances that said no - ").split(", ")
    idkinstances = input("Provide the instances that said idk - ").split(", ")

    changeRResponses(yesinstances, sessionNumber, colorOfInstances, x, "Yes") # for yes responses
    changeRResponses(noinstances, sessionNumber, colorOfInstances, x, "No") # for no responses
    changeRResponses(idkinstances, sessionNumber, colorOfInstances, x, "idk") # for idk responses


print("Program has concluded without any errors.")