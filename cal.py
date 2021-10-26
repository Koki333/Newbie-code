years = [y for y in range(1900, 2001)]
months = "jan feb mar apr may jun jul aug sep oct nov dec"
days = "mon tue wed thu fri sat sun"
days_n = [d for d in range(1, 32)]


def cal():
    for year in years:
        for month in months.split():
            for day in days.split():
                    print(day, month, year)




cal()
