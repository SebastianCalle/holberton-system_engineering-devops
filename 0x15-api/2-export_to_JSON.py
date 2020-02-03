#!/usr/bin/python3
"""
Api REST JSONPlaceholder
"""
import json
import requests
import sys

if __name__ == '__main__':
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    list_emp = res2.json()
    employee_id = 0
    i = 1
    dict_emp = {}
    while (i <= 1):
        res = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(i))
        username = res.json().get('username')
        list_users = []
        new_dict = {}
        for emp in list_emp:
            if i == emp.get('userId'):
                new_dict[emp['id']] = {
                    "completed": emp['completed'],
                    "task": emp['title'],
                    "username": username
                }
                list_users.append(new_dict.values())
        dict_emp[i] = list_users
        i += 1

    print(dict_emp)

#    with open('todo_all_employes.csv', mode='w') as employee_file:
#        employee_writer = csv.writer(employee_file, delimiter=',',
#                                     quoting=csv.QUOTE_ALL)
#        for em in list_task:
#            employee_writer.writerow([em['userId'], username, em['completed'],
#                                      em['title']])
