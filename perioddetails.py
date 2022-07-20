from time import ctime, time

# arranging the details to get the period name 
periods = {"sun":['holyday','holyday','holyday','holyday','holyday','holyday','holyday','holyday','holyday'],
 "mon":['mathematics','chemistry','physics lab','physics lab','lunch','english','leisure','telugu','break', 'no class'],
 "tue":['english','chemistry','physics','maths','lunch','IT-lab','IT-lab','physics','break', 'no class'],
 "wed":['chemistry lab','chemistry lab','maths','chemistry','luch','telugu','english','maths','break', 'no class'],
 "thu":['physics','english','maths','chemistry','lunch','physics','english','leisure','break', 'no class'],
 "fri":['IT','chemistry','maths','physics','lunch','leisure','leisure','leisure','break', 'no class'],
 "sat":['leisure','chemistry','maths','physics','lunch','IT','telugu','leisure','break', 'no class']
}

day = ctime(time())[0:3].lower()


# converting the above details into period name 
def periodNumber():
    # today = ctime(time())  
    # Tue Jul 19 16:45:15 2022
    hour = int(ctime(time())[11:13])
    minutes = int(ctime(time())[14:16])

    if hour == 9 or hour == 8:
        if minutes >= 30 :
            period_number = hour - 7

        else:
            period_number = hour - 8

    elif 10 <= hour and hour <= 15 : 
        if minutes >= 40:
            period_number = hour - 7
        
        elif hour == 10 and minutes>=30 and minutes<= 40:
            period_number = 8
        
        else:
            period_number = hour - 8
        
    elif hour == 16 and minutes <= 40:
        period_number = hour -8
    
    else:
        period_number = 9
    
    return period_number-1

def periodName():
    print('Can I take period details automatically or would you like to give them sir ')
    manual_or_auto = input('Share your opinion (a or m) : ')
    while True:
        if manual_or_auto.lower() in ['m', 'manually']:
            period_name = input('Enter the period name : ')
            break
        elif manual_or_auto.lower() in ['a', 'automatically']:
            period_name = periods[day][periodNumber()]
            break
        else:
            print(period_name)
            period_name = input('Please choose "a" or "m" : ')
    
    return period_name


periodNumber()
