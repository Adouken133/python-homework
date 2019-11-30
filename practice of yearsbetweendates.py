def normalyear(year1):
    n = 0
    if year1%4 != 0:
        n += 1
    elif year1%100 == 0 and year1%400 != 0:
        n += 1
    
    return n

def leapyear(year1):
    m = 0
    if year1%100 == 0 and year1%400 == 0:
        m += 1
    elif year1%4 == 0:
        m += 1
    return m
    
    
    
def days_in_months(year1,month1):
    n = normalyear(year1)
    m = leapyear(year1)
    if n == 1:
        return normalyear_list[month1 - 1]
    if m == 1:
        return leapyear_list[month1 - 1]
    
    

def next_day(year1,month1,day1):
    # assume all month have 30 days
    if day1 < days_in_months(year1,month1):
        return year1,month1,day1+1
    else:
        if month1 < 12:
            return year1,month1+1,day1
        else:
            return year1+1,1,1

def dates_of_stop(year1,month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
            
    return False

def daysbetweendate(year1,month1,day1,year2,month2,day2):
    days = 0
    while dates_of_stop(year1,month1,day1,year2,month2,day2):
        year1,month1,day1 = next_day(year1,month1,day1)
        days += 1
    return days

if __name__ == '__main__':
    normalyear_list = ['31','28','31','30','31','30','31','31','30','31','30','31']
    leapyear_list = ['31','29','31','30','31','30','31','31','30','31','30','31']
    print(daysbetweendate(1900,1,1,1999,12,31))
