list1 = [n for n in range(1900, 2001)]
list2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
list3 = [d for d in range(1, 32)]


for year in list1:
    for month in list2:
        for day in list3:
            if month == "Feb" and day == 29:
                break
            if month == "Apr" and day == 31:
                break
            if month == "Jun" and day == 31:
                break    
            print(day, month, year)
