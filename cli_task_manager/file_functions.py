import json

to_do_list = []
completed_tasks = []


def open_task_lists():
    """
    Open txt files to load To-Do List tasks and 
    Completed Tasks from previous session(s)
    """
    open_tasks()
    open_completed_tasks()


def open_tasks():
    task_list = open('tasks.txt', 'r')
    tasks = task_list.readlines()
    for task in tasks:
        to_do_list.append(json.loads(task))
    task_list.close()


def open_completed_tasks():
    task_list = open('completed_tasks.txt', 'r')
    tasks = task_list.readlines()
    for task in tasks:
        completed_tasks.append(json.loads(task))
    task_list.close()


def save_task_lists():
    """
    Write to txt files to save To-Do List tasks and 
    Completed Tasks for next session
    """
    save_tasks()
    save_completed_tasks()


def save_tasks():
    task_list = open('tasks.txt', 'w')
    for task in to_do_list:
        task_list.writelines([json.dumps(task), '\n'])
    task_list.close()


def save_completed_tasks():
    task_list = open('completed_tasks.txt', 'w')
    for task in completed_tasks:
        task_list.writelines([json.dumps(task), '\n'])
    task_list.close()