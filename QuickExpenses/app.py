#QuickExpenses - Tyler Nguyen
from datetime import *
import fileinput
# Menu generate
print('Hello, welcome to QuickExpenses!')
print('Please select option to continue')
# option 1 search and update
print('1. Search')
# option 2 enter new data
print('2. Enter')
# display all in file
# print ('3. Statements')

choice = input('Enter your option: ')
# switch case replacements
if choice == '1':
    # user select 1
    # user enter date to search
    date = input('Enter date to search with this format yyyy/m/d :')
    # file open to read
    file = open('track.txt', 'r')
    # find info
    count = 0
    for line in file:
        if date in line:
            count += 1
            print(line)
        # print 'no result' if date doesn't match any
    if count == 0:
        print("no result")
    file.close()

elif choice == '2':
    # user select 2
    print('Is it for today?')
    print('1.yes')
    print('2.no')
    choice = input("Select option: ")
    # if today, app run through file to see if there is data for today
    # => if there is, automatic generate date and let user update the amount only
    if choice == '1':
        count = 0
        # open file to read
        file = open('track.txt', 'r+')
        # generate date
        today = datetime.today()
        for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
            getattr(today, attr)
        date = str(today.month) + '/' + str(today.day) + '/' + str(today.year)
        # save all the lines to new_f
        new_f = file.readlines()
        # seek to the top position
        file.seek(0)
        for line in new_f:
            # delete the date
            if date not in line:
                # if the date is not on the current line
                # then rewrite the line
                file.write(line)
                # pass to the next one
                pass
            else:
                # set count to 1 if found the date on the current line
                count = 1
                # save the old amount to update
                sp_data = line.split()
                old_amt = sp_data[1]
                print(sp_data)
                # ask new data
                new_amt = input('Enter the amount: ')
                # calculate the amount
                cal_amt = int(old_amt) + int(new_amt)
                line = date + '\t' + str(cal_amt)
                file.write(line)
        file.truncate()
        if count == 0:
            date = str(today.month) + '/' + str(today.day) + '/' + str(today.year)
            amount = input('Enter amount2: ')
            file = open('track.txt', 'a')
            # write it to file
            file.write('\n')
            file.write(date + '\t' + amount + '\n')
            # close file
            file.close()

    # => if there is not today, let user add date manually and add amount
    if choice == '2':
        # if there is not, get the date and let user input amount
        # get date from user
        date = input('Enter date to search with this format dd/mm/yyyy :')
        count = 0
        # open file to read
        file = open('track.txt', 'r+')
        # save all the lines to new_f
        new_f = file.readlines()
        # seek to the top position
        file.seek(0)
        for line in new_f:
            # delete the date
            if date not in line:
                # if the date is not on the current line
                # then rewrite the line
                file.write(line)
                # pass to the next one
                pass
            else:
                # set count to 1 if found the date on the current line
                count = 1
                # save the old amount to update
                sp_data = line.split()
                old_amt = sp_data[1]
                print(sp_data)
                # ask new data
                new_amt = input('Enter the amount1: ')
                # calculate the amount
                cal_amt = int(old_amt) + int(new_amt)
                line = date + '\t' + str(cal_amt)
                file.write(line)
        file.truncate()
        if count == 0:
            amount = input('Enter amount2: ')
            file = open('track.txt', 'a')
            # write it to file
            file.write('\n')
            file.write(date + '\t' + amount + '\n')
            # close file
            file.close()
else:
    print('try again')
