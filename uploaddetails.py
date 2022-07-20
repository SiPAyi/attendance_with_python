import openpyxl as xl



def addDetails(sheet, last_col_number):
    import getattendence
    student_state = getattendence.takeAttendence()
    for rollNo in student_state:
        sheet.cell(rollNo+1, last_col_number+1).value = student_state[rollNo]

def overWrite(sheet, last_col_number):
    import getattendence
    student_state = getattendence.takeAttendence()
    for rollNo in student_state:
        sheet.cell(rollNo+1, last_col_number).value = student_state[rollNo]    


def uploadDetails(sheet, last_col_number):
    from time import ctime, time
    date = ctime(time())[8:10] + '-' + ctime(time())[4:7] + '-' +ctime(time())[20:25] # 20-Jul-2020
    todays_col_first_row = sheet.cell(1, last_col_number+1)

    if sheet.cell(1, last_col_number).value != date:
        todays_col_first_row.value = date
        addDetails(sheet, last_col_number)
        print('Successfully added ')
    elif sheet.cell(1, last_col_number).value == 'ID':
        addDetails(sheet, last_col_number)
        print('Successfully added ')
    else:
        print('already entered today\'s attendence. do you want to overwrite them ?')    
        overwrite = input('Enter your opinion (y/n) : ')
        if overwrite == 'y':
            overWrite(sheet, last_col_number)
            print('succesfully overwrited')
        else:
            print('thanks :) ')

