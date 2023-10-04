#!/usr/bin/python3
import os
import sys
from pathlib import Path
from datetime import date

 
def addWeight(user):
    print('Input date yyyy-mm-dd: ', end='')
    validDate = False
    while(not validDate):
        dateString = input()
        try:
            wtDate = date.fromisoformat(dateString)
            validDate = True
        except:
            print('Invalid date enter a date in yyyy-mm-dd', end='')
    validWeight = False
    print(f'Input a weight for {wtDate}: ', end='')
    while(not validWeight):
        weightStr = input()
        try:
            weight = int(weightStr)
            validWeight = True
        except:
            print('Invalid weight enter a weight for {wtDate}: ', end='')

    with open(f'users/{user}.wt', 'a', encoding='utf-8') as f:
        #f.write()
        pass 
        
    sys.exit()
        

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
                f.write(f'{newUser} {date.today()} c-None\n')
            user = newUser
            break
        else:
            print('Username already in use')
else:
    user = users[userNum -1]

print(f'\nUser: {user.capitalize()}')

with open(f'users/{user}.wt', 'r', encoding='utf-8') as f:
    current = f.readline().split(' ')[2].split('-')[1]
    print(f'current weight: {current}')
while(True):
    print('(1) Add Weight')
    print('(0) Exit')
    print('Input action: ', end='')
    action = input().strip()
    match action:
        case '0':
            sys.exit()
        case '1':
            addWeight(user)



#enter weight
#set goal weight
#average weight loss per day
#weight loss history

def main():


'''
class user:
    def __init__(self):
        pass

    def addWeight(self):
'''


if __name__ == "__main__":
    main() 





