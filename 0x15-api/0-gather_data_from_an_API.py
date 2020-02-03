#!/usr/bin/python3
"""
Api REST JSONPlaceholder
"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos'.format(employee_id))
    employee_name = res.json().get('name')
    list_emp = res2.json()
    list_true_task = []
    total_task = 0
    for emp in list_emp:
        if emp.get('userId') == int(employee_id):
            total_task += 1
            if emp.get('completed') is True:
                list_true_task.append(emp['title'])

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                         len(list_true_task),
                                                         total_task))
    for emp in list_true_task:
        print('\t {}'.format(emp))
