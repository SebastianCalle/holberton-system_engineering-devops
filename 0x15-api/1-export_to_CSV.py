#!/usr/bin/python3
"""
Api REST JSONPlaceholder
"""
import requests
import sys
import csv

if __name__ == '__main__':
    employee_id = sys.argv[1]
    res = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos'.format(employee_id))
    username = res.json().get('username')
    list_emp = res2.json()
    list_task = []
    total_task = 0
    for emp in list_emp:
        if emp.get('userId') == int(employee_id):
            list_task.append(emp)
    with open('{}.csv'.format(employee_id), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quoting=csv.QUOTE_ALL)
        for em in list_task:
            employee_writer.writerow([em['userId'], username, em['completed'],
                                      em['title']])
