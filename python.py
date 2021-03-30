import os.path
from os import path
import csv

def add():
    add_selection = input("Tell us the class code:\n")
    if path.exists('./classes/'+add_selection+'.csv'):
        print("exists")
    else:
        add_class = input("File doesn't exist, you either typed it wrong[1], or should we create this class[2]:\n")
        if add_class =="2":
            new_class(add_selection)
        else:
            add()
    

def new_class(class_add):
    weight = {}
    add_option = input("Tell us the grading categories separated by commas(ex: exams, tests, homework):\n")
    x = add_option.split(",")
    weight_check = input("Are their weights on different categories? [Y] [N]")
    if weight_check == "Y" or "y":
        for item in x:
            weight[item] = input('Weight for '+item+':')
        print(weight)
    #f = open('./classes/'+class_add+'.csv', "w")

#def add_categories(list)

selection= input("Please Select:\nAdd new grade[1] \nCreate new class [2]\n")
if selection =="1":
    add()
if selection =="2":
    class_add = input("What is the class code:\n")
    new_class(class_add)

