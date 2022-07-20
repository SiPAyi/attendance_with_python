import openpyxl as xl
import perioddetails
from uploaddetails import uploadDetails

period_name = perioddetails.periodName()
# period_name = 'chemistry'


if period_name not in ['break', 'no class']:
    wb = xl.load_workbook('attendence.xlsx')
    sheet = wb[period_name]
    last_col_number = sheet.max_column
    
    uploadDetails(sheet, last_col_number)

    wb.save("attendence.xlsx")






# get details of students from excel sheet
# assign period name and class details manually or automatically
# take attendence in class
# upload the attendence to the excel sheet
# get attendence details of students 