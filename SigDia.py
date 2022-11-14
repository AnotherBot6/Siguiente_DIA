def comprobar_fecha(day, month, year):
    if day>=1 and day<=31 and month>=1 and month<=12 :
        return "OK"
    else:
        return "NO"

def N_day(day, month, year):
    day=day+1
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day>=31:
            month=month+1
            day=1
            if month>12:
                year=year+1
                month=1
                day=1
                return(day, month, year)
    
    elif month==4 or month==6 or month==9 or month==11:
        if day>30:
            month=month+1
            day=1
            return(day, month, year)
    elif month==2:
        date=year_B(day, month, year)
        return date
    return(day, month, year)

def year_B(day, month, year):
    if year%4==0:
        if day>29:
            month=month+1
            day=1
            return(day, month, year)
    elif year%4!=0:
        if day>28:
            month=month+1
            day=1
            return(day, month, year)
        

def main():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    if comprobar_fecha(day, month, year) == "OK":
        n_day, n_month, n_year = N_day(day, month, year)
        print(f"Next day: {n_day}/{n_month}/{n_year}")  
    elif comprobar_fecha(day, month, year) == "NO":
        print('Fecha invalida')
   


if __name__ == '__main__':
    main()
