## Working with JSON data and Python

import json, requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos1 = json.loads(response.text)
## OR
todos2 = response.json()

todos1 == todos2 ## True

# Let us create a Dictionary of all users who completed All Tasks
todos_by_users = {}

for todo in todos1:
    if todo["completed"]: # if True
        try:
            todos_by_users[todo["userId"]] += 1
        except KeyError:  # user does not exist yet
            todos_by_users[todo["userId"]] = 1

# Sort List by users who completed All Tasks
# SOrt by Descending. Default is Ascending
# To sort a dictionary - use .items()
users_who_complete = sorted(todos_by_users.items(), key=lambda x: x[1], reverse=True)

max_number = users_who_complete[0][1] ## 12

# Return a list of only users who completed all
max_users = []

# to iterate we have
for user, num_complete in users_who_complete:
    if num_complete < max_number:
        break # break bc we sorted list in Descending ORder Highest number to Lowest Number
    max_users.append(str(user))


def keep(todo): # filter function to be used later on
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in max_users
    return is_complete and has_max_count

# Write filtered function to JSON
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos1))
    json.dump(filtered_todos, data_file, indent=2)
