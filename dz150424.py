import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
todos_by_user = {} #{1: 10, 2:8, 3:11, ...}
for i in todos:
    if i["completed"]:
        try:
            todos_by_user[i['userId']] += 1
        except KeyError:
            todos_by_user[i['userId']] = 1
print(todos_by_user)
top_users = sorted(todos_by_user.items(), key=lambda x:x[1], reverse=True)
print(top_users)
max_complete = top_users[0][1]
print(max_complete)

users = []
for user, num in top_users:
    if num<max_complete:
        break
    users.append(str(user))
print(users)

print(f'Users {users} complete {max_complete }')
data_for_json = list()
for i in todos:
    if str(i['userId']) in users:
        if i['completed']:
            data_for_json.append(i)
with open("DZ1504.json", 'w') as f:
    json.dump(data_for_json,f,indent=2)



