import matplotlib.pyplot as plt
import helpers
import os 
import numpy as np

# Check to analyze one graph or all graphs in directory
method = input("Do you want to analyze 1 graph or all? (0 for all)\n")

# For one file
if method == '1':

    # Get path and check if is file
    path = helpers.getPath("What's the .tData file path?\n", True)
    title = os.path.basename(path).split('.')
    fileData = helpers.grabData(path)
    if(len(fileData) == 0):
        exit(0)

    # Store the data 
    groups = len(fileData)       
    tempLabels = []
    tempSearches = []
    tempTotals = []
    for data in fileData:
        tempSearches.append(data[1][0])
        tempTotals.append(data[1][1])
        tempLabels.append(data[0])

    # Plot data
    fig, ax = plt.subplots()
    index = np.arange(groups)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, tempSearches, bar_width,
    alpha=opacity,
    color='b',
    label='# Reference')

    rects2 = plt.bar(index + bar_width, tempTotals, bar_width,
    alpha=opacity,
    color='g',
    label='# Search')

    plt.xlabel('Search vs references')
    plt.ylabel('Tweets')
    plt.title('{} Statistics'.format(title[0]))
    plt.xticks(index + (bar_width/2), tempLabels, rotation=45)
    plt.legend()  

    plt.tight_layout()
    plt.show()

# Grab and store data from the tData directory
elif method == '0':
    dirLabels = []
    dirTotals = []
    
    # Grab data from tData directory
    path = helpers.getPath("What's the directory's filepath?\n", False)
    
    # Grab data
    for dataPath in os.listdir(path):
        print(dataPath)

        # Add label
        label = os.path.basename(dataPath).split('.')
        dirLabels.append(label[0])

        # Grabs data from file
        fileData = helpers.grabData(path + '/' + dataPath)
        if fileData == []:
            pass

        # Add data to totals
        tempTotal = 0
        for data in fileData:
            tempTotal += data[1][0]
        dirTotals.append(tempTotal)

    # Print pie chart
    plt.pie(dirTotals, labels=dirLabels, autopct='%1.1f%%')
    plt.title('tData Reference Comparisons')
    plt.axis('equal')
    plt.show()

# Else a valid option was not given and exits
else:
    print("Not a valid option")
    exit(0)