# CS 1026 Python Assignment 4
# Edward Cheng
# 251024979
# Due Date: December 5
# country.py


class Country:

#Initialize variables in constructor
    
    def __init__(self, name, pop, area, continent):
        self._name = str(name) 
        self._pop = str(pop)
        self._area = str(area)
        self._continent = str(continent)

# Returns country name       
    def getName(self):
        return self._name


    def getPopulation(self):
        return self._pop


    def getArea(self):
        return self._area


    def getContinent(self):
        return self._continent 

# Sets new population value

    def setPopulation(self, pop):
        self._pop = str(pop)
        

    def setArea(self, area):
        self._area = str(area)
        


    def setContinent(self, cont):
        self._continent = str(cont)
        
# Generates a string representation for class objects
    def __repr__(self):
        reprString = ""
        reprString += self.getName() + " (pop: " + str(self.getPopulation()) + ", " + "size: " + str(self.getArea())+ ") in " + self.getContinent()
        return reprString
