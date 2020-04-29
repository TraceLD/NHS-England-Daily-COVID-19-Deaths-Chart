from dateutil import parser
import requests
import matplotlib.dates as plt_dates
import matplotlib.pyplot as plt

def get_json():
    r = requests.get('https://covid-nhse.develer.co.uk/data/latest.json')

    return r.json()['totals']

def get_dates(days):
    list = []

    for day in days:
        list.append(parser.parse(day['date']))        

    del list[-1]

    return list

def get_values(days):
    list = []

    for day in days:
        list.append(day['value'])

    del list[-1]
   
    return list

print("Showing daily COVID-19 deaths in England.\nAll deaths are recorded against the date of death rather than the date the deaths were announced.\n")
print("Source: https://covid-nhse.develer.co.uk/")

days_data = get_json()
dates = get_dates(days_data)
values = get_values(days_data)

plot_dates = plt_dates.date2num(dates)

plt.plot_date(plot_dates, values, 'b-')
plt.title("NHS England Daily COVID-19 Deaths")
plt.xlabel("Time")
plt.ylabel("Daily deaths")
plt.show()