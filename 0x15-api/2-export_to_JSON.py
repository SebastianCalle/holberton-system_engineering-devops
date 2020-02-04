#!/usr/bin/python3
"""
Api REST JSONPlaceholder
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos'.format(employee_id))
    username = res.json().get('username')
    list_emp = res2.json()
    list_task = []
    new_dict = {}
    emp_dict = {}
    for emp in list_emp:
        if emp.get('userId') == int(employee_id):
            new_dict[emp['id']] = {
                "task": emp['title'],
                "completed": emp['completed'],
                "username": username,
            }
            list_task.append(new_dict[emp['id']])
    emp_dict[str(employee_id)] = list_task

    with open("{}.json".format(employee_id), "w") as employ_f:
        json.dump(emp_dict, employ_f)
