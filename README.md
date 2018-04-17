# Working with JSON Data and Python

## This repository contains an exercise working with Python and JSON.
## Here we will make a request to a JSONPlaceholder for dummy Json data

### Steps
1. Make a call to API
2. Store text/json into variable. Can use response.text or response.json()
3. Step3 - We will create a dictionary of users and the count of todos
4. Return array of tuples in descending order
   * Bc we are sorting a dictionary with key/value we will iterate over value by .items()
   * Reverse=True will order in Descending. Highest to lowest
5. Access the highest count. Ordered by descending order the first user will have the highest count
6. Make a list of all users who have the equal amount
7. # Step7 - Turn into a JSON file
   * Create a keep file that will return each individual completed task
   * Write a json file. Use filter function!


# Encoding Custom Types
1. I offer two solutions to the Python's complex class.
  * I create a custom function and pass into the dumps default parameter.
  * I subclass JSONEncoder

# Decoding Custom Types
1. When creating custom JSON files I offer metadata. In this case, for Python's complex class, I create a key with "__complex__". I search for it inside the dictionary, if True I handle the complex class, otherwise I return the dictionary and let the default decoder deal with . Maintaining lightweight functionality. 
