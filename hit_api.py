import requests

d = {}
arr = []

for i in range(100):
    response = requests.get("http://localhost:5000/is_Even?number=" + str(i))
    print(i, "response is ", response.content)

    d[i] = response.content
    arr.append(response.content)
