from os import environ
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI

load_dotenv()

api = TodoistAPI(environ.get("TODO_API"))

tasks = api.filter_tasks(query="today")
    
for list in tasks:
    for task in list:
        print(f"TSK: {task.content}\nTID: {task.id}\nDES: {task.description}\nPRI: {task.priority}\nLAB: {task.labels}\nPAR: {task.parent_id}\n\n")

#comments_iter = api.get_comments(task_id=task.id)
#for comments in comments_iter:
#    for comment in comments:
#        print(f"Comment: {comment.content}")
#project_id="6fqqv4CQvFxXqJCJ")