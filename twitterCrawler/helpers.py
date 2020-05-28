from datetime import datetime
from datetime import timedelta
import os

# Check if the tweet's date is within given timeFrame
def checkDate(tweetDate, timeFrame):
    #print(tweetDate.strftime("%Y-%m-%d"))

    limit = datetime.today() - timedelta(days=timeFrame)

    # If legal value return true, else false
    if tweetDate >= limit:
        return True
    return False

# Grabs data from a given file
def grabData(fileName):
    fileData = []

    # Checks extension
    check = fileName.split('.')
    if check[1] != 'tData':
        print("Skipping {} as it is not a .tData file".format(fileName))

    # Grabs and returns data
    else:
        with open(fileName) as file:
            for data in file.read().splitlines():
                temp = data.split('||')
                temp[1] = eval(temp[1])
                fileData.append(temp)

    return fileData

# Get path and check if it's a valid path
def getPath(output, fileBool):   
    path = input(output)

    # Check for valid path
    if not os.path.exists(path):
        print("Sorry can't seem to find that file\n")
        exit(0)    

    # If file flag set, check if it's a file
    if fileBool == True:
        if not os.path.isfile(path):
            print("Sorry can't seem to find that file\n")
            exit(0)  

    # If not set, check for directory
    else:
        if not os.path.isdir(path):
            print("Sorry can't seem to find that directory\n")
            exit(0)  
    
    return path
