import requests

d = {}
arr = []

for i in range(10000):
    response = requests.get("http://127.0.0.1:5000/is_Even?number=" + str(i))
    print(i, "response is ", response.content)

    d[i] = response.content
    arr.append(response.content)
