#!/usr/bin/python3
import os
import sys
from pathlib import Path
from datetime import date

#weight log loop
def main():
    print('Welcome to your personal weight loss tracker')
    print('Select a Username:')
    print('(0) New User')

    currentUsers = get_users()
    for id, userName in enumerate(currentUsers, 1):
        print(f'({id}) {userName.capitalize()}')

    activeUser = set_user(currentUsers)

    end = False 
    while(not end):
        end = user_action(activeUser)
    sys.exit

#get list of current available users
def get_users():
    userPath = Path('./users')
    return [str(path).split('/')[1].split('.')[0] for path in list(userPath.glob('*.wt'))]

#get user id and return user
def set_user(currentUsers):
    validUser = False
    print('\nSelect your username\n(input username number or 0 for a new user): ', end='')
    while(not validUser):
        userNum = input()
        try:
            if int(userNum) in range(len(currentUsers)+1):
                validUser = True
            else:
                print(f'Invalid user number. Enter a number betwen 0-{len(currentUsers)}: ', end='')
        except:
            print(f'Invalid Input. Enter a number betwen 0-{len(currentUsers)}: ', end='')
    if userNum == '0':
        return new_user(currentUsers)
    else:
        return user(currentUsers[int(userNum) -1])


#Get new username and create user and return
def new_user(currentUsers):
    validName = False
    print('Input new username: ', end ='')
    while(not validName):
        newUser = input().lower().strip()
        if newUser not in currentUsers:
            with open(f'users/{newUser}.wt', 'x', encoding='utf-8') as f:
                f.write(f'{newUser} {date.today()} c-None\n')
            return user(newUser)
        else:
            print('Username already in use. Input new username: ', end='')


#Display current user info and actions
def user_action(user):
    print(f'\nUser: {user.name.capitalize()}')
    print(f'Current weight:{user.currentWeight}')
    print(f'----------')
    print(f'(1) Add weight')
    print(f'(2) Weight Log')
    print(f'(3) Remove Weight')
    print(f'(0) Exit')
    print(f'(#) Delete User')

    print(f'Input action: ', end = '')
    validAction = False
    while(not validAction):
        userAction = input().lower().strip()
        match userAction:
            case '1':
                user.add_weight()
                validAction = True
                pass
            case '2':
                user.list_weight()
                validAction = True
                pass
            case '3':
                user.remove_weight()
                validAction = True
                pass
            case '0':
                return True
            case '#':
                return user.delete_account()
            case _:
                print('Invalid action. Input action: ', end = '')

#
#   CLASS IN WORK READ THE FILE AND THEN STORE THE INFO
#
class user:
    def __init__(self, name):
        self.name = name
        self.path = f'users/{name}.wt'
        with open(self.path, 'r', encoding='utf-8') as f:
            current = f.readline().strip().split(' ')
        self.creationDate = current[1]
        self.currentWeight = current[2]

    #add weight to log
    def add_weight(self):
        print('Input date yyyy-mm-dd: ', end='')
        validDate = False
        while(not validDate):
            dateString = input()
            try:
                wtDate = date.fromisoformat(dateString)
                validDate = True
            except:
                print('Invalid date enter a date in yyyy-mm-dd format: ', end='')
        validWeight = False
        print(f'Input a weight (lbs) for {wtDate}: ', end='')
        while(not validWeight):
            weightStr = input()
            try:
                weight = int(weightStr)
                validWeight = True
            except:
                print('Invalid weight enter a weight for {wtDate}: ', end='')
        #write log
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(f'{wtDate}|{weightStr}')


    def remove_weight(self):
        for count, weight in enumerate(self.weightLog, 1):
            print(f'({count}) {weight}')

    def list_weight(self):
        print('\nWeight Log:')
        for weight in self.weightLog:
            print(weight)

    def delete_account(self):
        print('Delete user account {self.name}?')
        print('Type YES to delete: ', end='')
        delete = input()
        if delete == 'YES':
            os.remove(self.path)
            return True
        return False

    def set_current(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            line = f.readline().strip().split(' ')
        self.creationDate = line[1]
        self.currentWeight = line[2]

    def update_current_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            f.readline()
            weight = 0
            date = None
            for line in f:
                if date.fromisoformat(line.split('|')[1]) < date.fromisoformat(current):
                    print(f'{date.fromisoformat(line.split("|")[1])} < {date.fromisoformat(current)}')

if __name__ == "__main__":
    main() 
