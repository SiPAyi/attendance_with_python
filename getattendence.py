import getdetails

def takeAttendence():

    students = getdetails.getDetails("attendence.xlsx")
    student_state = {}

    for i in range(1, 73):
        print('roll number ', i, students[i]['name'], 'present or not(y/n) : ',end=' ')
        state = input(' ')
        if state.lower() == 'y':
            student_state[i] = 'present'
        else:
            student_state[i] = 'absent'
    return student_state
