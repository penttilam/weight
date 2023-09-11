#!/usr/bin/python3
import os
from pathlib import Path
from datetime import date

'''
os.remove('test.txt')

with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('Newline\n')

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read(), end='')
'''

'''
WeightTracker.py
This is an application that tracks a users weight loss
'''

print('Welcome to your personal weight loss tracker')
print('Usernames:')

#get list of current users
userPath = Path('./users')
users = [str(path).split('/')[1].split('.')[0] for path in list(userPath.glob('*.wt'))]
# print(users)

#have user select a user
print('(0) New User')
count = 1
for user in users:
    print(f"({count}) {user.capitalize()}")
    count += 1

while(True):
    print('\nSelect your username\n(input username number or 0 for a new user):', end='')
    userNum = input()
    try:
        userNum = int(userNum)
    except:
        continue
    if int(userNum) in range(count):
        break

#create a new user
if userNum == 0:
    while(True):
        print('Input new user name: ', end ='')
        newUser = input().lower().strip()
        if newUser not in users:
            with open(f'users/{newUser}.wt', 'x', encoding='utf-8') as f:
                #write creation date
                f.write(f'{newUser} {date.today()}\n')
                continue
            break
        else:
            print('Username already in use')





