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
    while (i <= 10):
        res = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(i))
        username = res.json().get('username')
        list_users = []
        new_dict = {}
        for emp in list_emp:
            if i == emp.get('userId'):
                new_dict[emp['id']] = {
                    "username": username,
                    "task": emp['title'],
                    "completed": emp['completed'],
                }
                list_users.append(new_dict.get(emp['id']))
        dict_emp[str(i)] = list_users
        i += 1

    with open('todo_all_employees.csv', mode='w') as employee_file:
        json.dump(dict_emp, employee_file)
