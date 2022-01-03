dates = [
    {'day': 24, 'month': 11, 'year': 1998},
    {'day': 17, 'month': 7, 'year': 1994},
    {'day': 11, 'month': 5, 'year': 2005},
    {'day': 5, 'month': 3, 'year': 2011},
    {'day': 16, 'month': 5, 'year': 2005},
    {'day': 31, 'month': 12, 'year': 1991},
    {'day': 24, 'month': 8, 'year': 1998}
]


def sort_list(date_list):
    for i in range(len(date_list) - 1):
        for j in range(len(date_list) - 1 - i):
            if (date_list[j]['year'] > date_list[j + 1]['year']) \
                    or (date_list[j]['year'] == date_list[j + 1]['year'] and date_list[j]['month'] > date_list[j + 1]['month']) \
                    or (date_list[j]['year'] == date_list[j + 1]['year'] and date_list[j]['month'] == date_list[j + 1]['month'] and date_list[j]['day'] > date_list[j + 1]['day']):
                date_list[j], date_list[j + 1] = date_list[j + 1], date_list[j]


sort_list(dates)
for data in dates:
    print(str(data['year']) + '-' + str(data['month']) + '-' + str(data['day']))
