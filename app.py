# from first_file import average_of_list

# variable_list = [1,2,3]
# print(average_of_list(variable_list))

from flask import Flask, request
from random import randint

app = Flask(__name__)


@app.get("/hello")
def hello_world():
    return "Hello, World!"


@app.get("/clyde")
def dog():
    return "Snaggle tooth"


@app.get("/random")
def random():
    return str(randint(0, 10))


@app.get("/test")
def test():
    return str([3, 6, 2, 9])


@app.get("/is_Even")
def is_Even():
    num = request.args.get("number")
    if num is None:
        print("The user forgot to send a number.")
        return "Error! Please send a number by putting ?number=(input) after url."

    num = int(num)

    if num % 2 == 0:
        return "Is even!"
    else:
        return "Is odd!"


app.run(debug=True, port=5000)
