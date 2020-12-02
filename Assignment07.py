# ------------------------------------------------- #
# Title: Assignment07
# Description: Assignment submission to demonstrate how pickling and structured error handling work
# ChangeLog: (Who, When, What)
# PBeresnev,<12.1.2020>,Created Script
# ------------------------------------------------- #
# Custom Error Class

import pickle  # This imports code from another code file!


class NumError(Exception):
    """custom error docstring"""

    def __str__(self):
        return 'Do not use letters!'


print("Time to open the to-do list. Let us see if it exists")
try:
    file = open("ToDoList.txt", "r")
except FileNotFoundError as e:
    print("no file exists yet or check file name (should be ToDoList.txt)", e)
else:
    print('It exists.  Here are the contents:')
    print(file.read())

# Raising custom errors
try:
    num = input('Enter a number: ')
    if num.isalpha():
        raise Exception('Do not enter letters!')
except Exception as e:
    print(e)

# Raising custom exception class
try:
    num = input('Enter a number: ')
    if num.isalpha():
        raise NumError()
except Exception as e:
    print(e)

# Pickling

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, objFile)
    objFile.close()


def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    objFileData = pickle.load(objFile)  # load() only loads one row of data.
    objFile.close()
    print(objFileData)


# Presentation ------------------------------------ #
# Get ID and NAME From user, then store it in a list object
intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
# store the list object into a binary file
lstCustomer = [intId, strName]
save_data_to_file(strFileName, lstCustomer)
# Read the data from the file into a new list object and display the contents
read_data_from_file(strFileName)
