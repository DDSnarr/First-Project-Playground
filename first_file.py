# print("hello world")
# your_input = input('input a word: ')

# list_of_stuff = ["some", "random", "words"]

# # add your input to the list
# list_of_stuff.append(your_input)

# print(list_of_stuff)

def double_number(num):
    double = num* 2
    return double

# num = 10
# print(double_number(num))

def triple_number(num):
    triple = num * 3
    return triple

# num = 10
# print(triple_number(num))

def average(x, y):
    average = ((x + y) / 2)
    return average

# x = 10
# y = 12
# print(average(x, y))

list_nums = [1,2,3,4,5,6,7]

def average_of_list(list_nums):
    total_sum = sum(list_nums)
    length = len(list_nums)
    return total_sum / length

# print(average_of_list(list_nums))
# print(list_nums.reverse())

def test(x):
    # return x
    x += 1

# print(test(2))
