## Working with JSON data and Python
# Here we will make a request to a JSONPlaceholder for dummy Json data

import json
import requests # requests will utilized to make a call to API

# Step1 - Make a call to API
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# Step2 - Store text/json into variable. Can use response.text or response.json()
todos = response.json()

# Step3 - We will create a dictionary of users and the count of todos
todos_by_users = {}
for todo in todos:
    if todo["completed"]: # if True
        try:
            todos_by_users[todo["userId"]] += 1
        except KeyError:
            todos_by_users[todo["userId"]] = 1


# Step4 - Return array of tuples in descending order
    # Bc we are sorting a dictionary with key/value we will iterate over value by .items()
    # Reverse=True will order in Descending. Highest to lowest

todos_by_users_ordered = sorted(todos_by_users.items(), key=lambda x: x[1], reverse=True)

# Step5 - Access the highest count. Ordered by descending order the first user will have the highest count
max_count = todos_by_users_ordered[0][1]

# Step6 - Make a list of all users who have the equal amount
max_users = []
for user, num_complete in todos_by_users_ordered:
    if num_complete < max_count:
        break
    max_users.append(str(user))

#
users = ' and '.join(max_users) # join index with and

s = 's' if len(max_users) > 1 else ''
users_sentence = f"user{s} {users} have completed all {max_count} tasks"


# Step7 - Turn into a JSON file
# Step7a - Create a keep file that will return each individual completed task
def keep(todo):
    is_complete = todo["completed"] # True or False
    user_complete = str(todo["userId"]) in max_users # if user is in users who completed all tasks
    return is_complete and user_complete

# Step7b- Write a json file. Use filter function!
with open("filtered_data_file.json", "w") as data_file:
    users_json = list(filter(keep, todos))
    json.dump(users_json, data_file, indent=2)
