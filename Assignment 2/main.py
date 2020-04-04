# Python 1026
# Assignment 2
# Edward Cheng
# 251024979
# Volume Calculator: main.py

# Allows main.py file to use functions defined in volume.py
from volume import *
from summarize import *

user = ""

    
# This ensures that the inputted shapes will display a summary of all the volumes.
def main():
    cubeIndex = []
    pyramidIndex = []
    ellipsoidIndex = []
    done = False

    testCase = int(input("What is the test case number?: "))


    # This is a loop that lets the user to keep inputting values until the user types "q" or quit.
    while done == False:
        user = input("Enter Cube/c, Pyramid/p, Ellipsoid/e, Quit/q: ")

        # This ensures that once the user types "quit" or "q", no more inputs can be accepted.
        if user.lower() == "q" or user.lower() == "quit":
            done = True

        # This ensures that once the user types "Cube" or "c", the cube volume obtained from the function in the volume.py will have its value added to the list
        elif user.lower() == "cube" or user.lower() == "c":
            cubeIndex.append(cubeVol())

        elif user.lower() == "pyramid" or user.lower() == "p":
            pyramidIndex.append(pyramidVol())

        elif user.lower() == "ellipsoid" or user.lower() == "e":
            ellipsoidIndex.append(ellipsoidVol())

        # If the user doesn't type in any of the shapes or quit, it will display this message
        else:
            print("Invalid input")

    # If none of the shapes are inputted, display the following message

    if len(cubeIndex) == 0 and len(pyramidIndex) == 0 and len(ellipsoidIndex) == 0:
        print("You have reached the end of your session. You did not perform any volume calculations. ")

    else:
        cubeOutput = ""
        pyramidOutput = ""
        ellipsoidOutput = ""

    # This ensures that the data will be sorted in increasing order

    cubeIndex = sorted(cubeIndex)
    pyramidIndex = sorted(pyramidIndex)
    ellipsoidIndex = sorted(ellipsoidIndex)


    # If the user does not enter any shapes, it will display this message for that particular shape

    if len(cubeIndex) == 0:
        cubeOutput = "You did not enter a shape."

    if len(pyramidIndex) == 0:
        pyramidOutput = "You did not enter a shape."

    if len(ellipsoidIndex) == 0:
        ellipsoidOutput = "You did not enter a shape."


    # If the user does enter a shape, output the following instructions 

    if len(cubeIndex) > 0: 
        for x in range(len(cubeIndex)):
            if x != (len(cubeIndex)-1):
                cubeOutput += (" " + str(cubeIndex[x]) + ",")
            else:
                cubeOutput += (" " + str(cubeIndex[x]))

    # Same process as above
    
    if len(pyramidIndex) > 0: 
        for x in range(len(pyramidIndex)):
            if x != (len(pyramidIndex)-1):
                pyramidOutput += (" " + str(pyramidIndex[x]) + ",")
            else:
                pyramidOutput += (" " + str(pyramidIndex[x]))
            

    if len(ellipsoidIndex) > 0: 
        for x in range(len(ellipsoidIndex)):
            if x != (len(ellipsoidIndex)-1):
                ellipsoidOutput += (" " + str(ellipsoidIndex[x]) + ",")
            else:
                ellipsoidOutput += (" " + str(ellipsoidIndex[x]))
                

    # This will display a message if no shapes are present in the assigned list for a particular shape
    if len(cubeIndex) == 0: 
        cubeOutput = "No Shapes Entered."

    if len(pyramidIndex) == 0:
        pyramidOutput = "No Shapes Entered."

    if len(ellipsoidIndex) == 0:
        ellipsoidOutput = "No Shapes Entered."


    # Print functions that displays a summary of the calculations of the shapes inputted
    print("You have reached the end of your session. The volumes calculated for each shape are: ")
    print("Cube:", cubeOutput) 
    print("Pyramid:", pyramidOutput)
    print("Ellipsoid:", ellipsoidOutput)

    summarize(cubeIndex, pyramidIndex, ellipsoidIndex, testCase)
    
    return


main()
