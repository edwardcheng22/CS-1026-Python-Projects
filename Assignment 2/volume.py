# Python 1026
# Assignment 2
# Edward Cheng
# 251024979
# Volume Calculator: volume.py

# Python 1026
# Edward Cheng
# Assignment 2
# 251024979
# Volume Calculator: volume.py

# Math module is required for calculations involving pi

import math

# Calculating volume functions for each shape

def cubeVol():
    sideLength = int(input("Enter a side length: "))
    initial_vol= 0
    initial_vol = float(sideLength**3)
    print()
    print("This cube has a side legnth of", sideLength, "and an area of", float(initial_vol))
    print()

    return float(initial_vol)

def pyramidVol():
    baseLength = int(input("Enter a base length: "))
    heightLength = int(input("Enter a height length: "))
    initial_vol= 0
    initial_vol = (1/3) *((baseLength **2)*heightLength)
    initial_vol = round(initial_vol, 2)
    print("")
    print("This Pyramid has a base of", baseLength, "and a height of", heightLength, "and an area of ",initial_vol)
    print("")

    return initial_vol


def ellipsoidVol():
    initial_vol= 0
    radius_one= int(input("Enter the first radius: "))
    radius_two = int(input("Enter the second radius: "))
    radius_three = int(input("Enter the third radius: "))
    initial_vol = ((4/3)*math.pi) * (radius_one) * (radius_two) * (radius_three)
    initial_vol = round(initial_vol, 2)
    print()
    print("This Ellipsoid has a radii of " + str(radius_one) + ", " + str(radius_two)+ ", " + str(radius_three)+ ", " "and has a volume of " + str(initial_vol))
    print()

    return initial_vol
