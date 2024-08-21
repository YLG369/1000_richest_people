# FINAL USER INTERFACE

# security
password = 'skibidiohiogyatt'
userInputPassword = input("Enter the password: ")
while userInputPassword != password: 
    userInputPassword = input("PASSWORD INCORRECT. Please try again: ")
print("PASSWORD CORRECT")
print()

# import modules
import pandas as pd
import matplotlib.pyplot as plt

# global variables
quit = False

# importing and cleaning datasets
# import dataset into pandas dataframe
dataframe = pd.read_csv("data/1000_richest_people_in_the_world.csv")

# dataframe cleaning
cleaned_dataframe = pd.read_csv("data/1000_richest_people_in_the_world.csv", usecols = ('Industry           ', 'Net Worth (in billions) '))

# dataframe - most frequent industries
MostOccurencesIndustry = cleaned_dataframe.value_counts('Industry           ')

# dataframe - largest industries
dataframeTopMoney = cleaned_dataframe.nlargest(200, 'Net Worth (in billions) ')
dataframeTopMoneyNoDuplicate = dataframeTopMoney.drop_duplicates(subset = ['Industry           '])
#----------------------------------------------------------------------------------------------------------------------------------------------------------


# setting up functions for user interface
# original dataframe
def showOriginalDataframe():
    print(dataframe)
    print()

# cleaned dataframe
def showCleanedDataframe():
    print(cleaned_dataframe)
    print()

# most frequent industries dataframe
def showMostOccurencesIndustry():
    print(MostOccurencesIndustry)
    print()

# largest industries dataframe
def showTopMoney():
    print(dataframeTopMoneyNoDuplicate)
    print()

# most frequent industries chart
def showChart1():
    MostOccurencesIndustry.plot(
                    kind = 'bar',
                    x = 'Industry           ',
                    y = 'Net Worth (in billions) ',
                    color = 'midnightblue',
                    alpha = 0.3,
                    title = 'Top Ten Most Frequent Industries in the World')
    plt.show()
    print()
    
# largest industries chart
def showChart2():
    dataframeTopMoneyNoDuplicate.plot(
                    kind = 'bar',
                    x = 'Industry           ',
                    y = 'Net Worth (in billions) ',
                    color = 'midnightblue',
                    alpha = 0.3,
                    title = 'Top Ten Biggest Industries in the World')
    plt.show()
    print()
#----------------------------------------------------------------------------------------------------------------------------------------------------------


# user interface
def userOptions():
    global quit
    print("""Welcome to the Industry Data Extraordinaire!
    Please select an option:
    1. Show the original dataset
    2. Show the cleaned dataframe
    3. Show the most frequent industries dataframe
    4. Show the largest industries dataframe
    5. Visualise most frequent industries
    6. Visualise the largest industries
    7. Quit Program
    """)
    print()
    try:
        inputOption = int(input("Select an option: "))
        print()

        if inputOption == 1: 
            showOriginalDataframe()
        elif inputOption == 2:
            showCleanedDataframe()
        elif inputOption == 3:
            showMostOccurencesIndustry()
        elif inputOption == 4:
            showTopMoney()
        elif inputOption == 5:
            showChart1()
        elif inputOption == 6:
            showChart2()
        elif inputOption == 7:
            print("Thanks for using this program.")
            print("This data was sourced from https://www.kaggle.com/datasets/waqi786/1000-richest-people-in-the-world.")
            quit = True
        else:
            print("Pick a number between 1 and 7. It's not that deep!")
    except:
        print('Enter a number. Come on!')

# run program
userOptions()

# main program
while not quit:
    userOptions()