import requests

arr = []

for i in range(10000):
    response = requests.get("http://127.0.0.1:5000/isPrime?number=" + str(i))
    print(i, "response is ", response.text)

    arr.append(response.content)
