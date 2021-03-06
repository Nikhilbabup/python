#
# Program   : Program Birthday count down
# Laguage   : Python
# Author    : Nikhil Babu P

import datetime

def print_header():
    print('-----------------------------')
    print('         BIRTHDAY APP')
    print('-----------------------------')

def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]:'))
    month = int(input('Month [MM]:'))
    day = int(input('Day [DD]:'))

    birthday = datetime.datetime(year,month,day)
    return birthday


def compute_days_between_details(date1,date2):
    dt = date1 - date2
    days = dt.total_seconds() /60 / 60 / 24 

def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_details(bday,now)
    print(number_of_days)
    #print_birthday_information()

main()