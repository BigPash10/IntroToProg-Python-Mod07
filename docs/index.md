# How to use structured error handling and pickling in Python
**Dev:** *PBeresnev*  
**Date:** *12/1/20*  
## Introduction:  
In this module we will discuss how to use structured error handling in Python, along with Pickling.  I will demonstrate these concepts in a script and go over several error handling scenarios.  Finally, I’ll show how this script runs in the command line as well as PyCharm.
## Structured Error Handling using Existing Exceptions:  
Python has several ways to handle errors that can be controlled by the coder rather than using the default error messages.  A way to do this is using a try/except block.  The way this works is we write the statement that we think could draw an error using “try”, followed by the statement.  Then “except” is used to write the code that runs if the “try” block generates an error.  We can then write an “else” block that has code which will execute if there is no error, as shown in Listing 1:
```
print("Time to open the to-do list. Let us see if it exists")
try:
    file = open("ToDoList.txt", "r")
except FileNotFoundError as e:
    print("no file exists yet or check file name (should be ToDoList.txt)", e)
else:
    print('It exists.  Here are the contents:')
    print(file.read())
```  
#### Listing 1
In this case I print to the user that we will try to open a to-do list, as shown in the “try” block.  Since I am not sure if the file exists, I write the “except” block to catch that error using the variable “e”.  Note, here I specifically call out the error type that will be caught, though I could just write “Exception” to catch any error.  Then if the called-out error happens, I print out that no file exists along with the Python default error message stored in the variable.  If there is no error, I simply print that it exists and the contents of the file in the “else” block using the “read” method.  
## Raising Custom Errors:  
Another option in Python is to raise custom error messages rather than using Python’s default messages. To demonstrate this, I prompt the user to enter a number using “input” in a “try” block.  If that input contains a letter, I raise a custom exception to not enter letters.  Because this is raised, the “except” block will run, where I catch the error as a variable, “e”, and print it out as shown in Listing 2:
```
## Raising custom errors
try:
    num = input('Enter a number: ')
    if num.isalpha():
        raise Exception('Do not enter letters!')
except Exception as e:
    print(e)
```
#### Listing 2
## Raising custom Exception class:
Finally, Python allows the developer to also create a custom exception class rather than using the default ones.  I demonstrate this again using a try/except block, but this time I also create a custom class.  Once again, I use the example of asking the user for a number with “input” in the “try” block.  I check if that entry has letters and if so, I raise an error.  This time, however, I created a custom Exception class called “NumError”.  When the error is raised the “except” block once again will run where I capture the Exception as “e”.  In this case I also print “e” where the custom error is shown, as demonstrated in Listings 3-4:
```
class NumError(Exception):
    """custom error docstring"""

    def __str__(self):
        return 'Do not use letters!'
```
#### Listing 3
```
# Raising custom exception class
try:
    num = input('Enter a number: ')
    if num.isalpha():
        raise NumError()
except Exception as e:
    print(e)
```
#### Listing 4
## Pickling
The next topic is pickling.  This is a way to store data in Python using various objects, such as dictionaries, lists, or tuples, rather than first converting those to a string and then writing the string to a text file, like we’ve seen before.  To do this, first we import the “pickle” module at the start of the script as shown in Listing 5:
```
import pickle  # This imports code from another code file!
```
#### Listing 5
To demonstrate this, I’ll first use a file name, “AppData.dat” and create a blank list called “lstCustomer” in the Data section of the code.  Then in the processing section I create two functions, one to save data to the file and another to read data from the file.  The save data function takes a file name and a list of data.  Then I create an “objFile” variable that stores the created/opened binary file in “append” mode, indicated by “ab” in the “open” method.  Then I use the “dump” method within “pickle” to add the list of data to the file.  Then I close the file.  
To read data from the file my function takes a file name.  Then I create a variable again to open the file, this time in “rb” mode, allowing reading of a binary file.  Then I assign a variable to the data that is loaded from the file, using the pickle.load() method.  Finally, I close the file and print the data, as shown in Listing 6:
```
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
```
#### Listing 6
In the presentation code I create two variables to get an integer ID and Name string using “input.  I then replace the blank list from before with these two inputs.  Then I call the “save_data_to_file” function to save the list to the binary file we made.  After this I read data from the file using the second function created, as shown in Listing 7:
```
# Presentation ------------------------------------ #
# Get ID and NAME From user, then store it in a list object
intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
# store the list object into a binary file
lstCustomer = [intId, strName]
save_data_to_file(strFileName, lstCustomer)
# Read the data from the file into a new list object and display the contents
read_data_from_file(strFileName)
```
#### Listing 7
## Output:
Fig 1 demonstrates the code running in PyCharm.  First I run it where no text file exists in the folder, hence I get the error messages described.  I then demonstrate that entering a letter on both prompts generates the custom errors described.  Finally, I create the binary file as described, shown in Fig 2:  
![Fig1](https://github.com/BigPash10/IntroToProg-Python-Mod07/blob/main/docs/Fig1.png?raw=true "Fig 1")
#### Figure 1: PyCharm Run with No Existing Text File
![Fig2](https://github.com/BigPash10/IntroToProg-Python-Mod07/blob/main/docs/Fig2.png?raw=true "Fig2")
#### Figure 2: Binary File from PyCharm Script
Next I demonstrate what this looks like in PyCharm if there is an existing Text file, which runs as described.  See Fig 3:  
![Fig3](https://raw.githubusercontent.com/BigPash10/IntroToProg-Python-Mod07/main/docs/FIg3.png "Fig3")
#### Figure 3: PyCharm Run with Existing Text File
Fig 4 shows a similar run to the first run but in the Command Prompt:  
![Fig4](https://github.com/BigPash10/IntroToProg-Python-Mod07/blob/main/docs/Fig4.png?raw=true "Fig4")
#### Figure 4: Command Prompt Run with no Existing Text File
Fig 5 shows what the resulting binary file looks like:  
![Fig5](https://github.com/BigPash10/IntroToProg-Python-Mod07/blob/main/docs/Fig5.png?raw=true "Fig5")
#### Figure 5: Resulting Binary File from Command Prompt Run
Finally, Fig 6 demonstrates the Command Prompt run but with an existing text file:  
![Fig6](https://github.com/BigPash10/IntroToProg-Python-Mod07/blob/main/docs/Fig6.png?raw=true "Fig6")
#### Figure 6: Command Line Run with Existing Text File
## Conclusion:
In this module we learned how to perform structured error handling using try/except and raising existing errors, custom errors or custom Exceptions.  This allows a developer to handle different scenarios when running a script.  Finally, we also looked at how to use pickling to save data from Python in the existing format, whether it’s a list, dictionary, tuple, etc. and then read it back in that format rather than having to convert the data to a string and write it as a text file.
