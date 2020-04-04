# CS 1026 Python Assignment 4
# Edward Cheng
# 251024979
# Due Date: December 5
# processUpdates.py

from catalogue import CountryCatalogue 

# Try exception implemented to see if text file opens
try:
    a = CountryCatalogue('data.txt')
except:
    "Error!"

# processUpdate function accepts two parameters defined below
def processUpdates(cntryFileName, updateFileName) -> bool:

    done = False

    # Executes loop
    while not done:
        try:
            fhandle = open(cntryFileName, "r")
        except IOError:
            # Asks user for input
            user = input("Would you like to quit? Press Y (yes) or N (no): ")
            if user.upper() == "N":
                cntryFileName = input("Please enter the name of another file: ")
            # Outputs message to "output.txt"
            else:
                c = open("output.txt", "w")
                c.write("Update Unsuccessful\n")
                c.close()
                return False
        f = CountryCatalogue(cntryFileName)
        # Another try and except test 
        try:
            uhandle = open(updateFileName, "r")
        except IOError:
            user = input("Would you like to quit? Press Y (yes) or N (no): ")
            if user.upper() == "N":
                updateFileName = input("Please enter the name of another file: ")
            else:
                c = open("output.txt", "w")
                c.write("Update Unsuccessful\n")
                c.close()
                return False
        u = open(updateFileName, "r")
        lu = u.readlines()
        for line in lu:
            line = line[:len(line)-1]
            line = line.replace(" ", "")
            l = line.split(";")
            country = l[0]
            if f.findCountry(country) == None: # Checks to see if country exists
                population = ""
                area = ""
                continent = ""
                for i in range(1,len(l)):
                    status = l[i][0]
                    if status == "P":
                        population=l[i][2:]
                    elif status == "A":
                        area=l[i][2:]
                    else:
                        continent=l[i][2:]
                # Implement addCountry method from CountryCatalogue class
                f.addCountry(country,population,area,continent)
            else:
                for i in range(1,len(l)):
                    status = l[i][0]
                    if status == "P":
                        f.setPopulationOfCountry(country,l[i][2:])
                    elif status == "A":
                        f.setAreaOfCountry(country, l[i][2:])
                    else:
                        f.setContinentOfCountry(country, l[i][2:])
        f.saveCountryCatalogue("output.txt")
        return True



