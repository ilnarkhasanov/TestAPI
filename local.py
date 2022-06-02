import requests

res = requests.post("http://localhost:3000/api/courses/3", {"name": "C++", "videos": 36})
res = requests.post("http://localhost:3000/api/courses/4", {"name": "PHP", "videos": 44})
print(res.json())
