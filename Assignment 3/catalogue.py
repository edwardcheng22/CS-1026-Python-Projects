# CS 1026 Python Assignment 4
# Edward Cheng
# 251024979
# Due Date: December 5
# catalogue.py


from country import Country 

class CountryCatalogue:

# Initialize constructor, which takes in a parameter
    def __init__(self, countryFile):

        self._countryCat = dict()
        self.data = open(countryFile, "r", encoding="utf-8")
        self.data.readline()
        line = self.data.readline()
        while len(line) > 0:
            tmpList = line.rstrip('\n').split('|')
            self._countryCat[tmpList[0]] = Country(tmpList[0], tmpList[2], tmpList[3], tmpList[1])
            line = self.data.readline() 

# Function accepts country name and newPop as parameters
    def setPopulationOfCountry(self, name, newPop):
        if name in self._countryCat: # Checks to see if country exists in the catalogue
            self._countryCat[name].setPopulation(newPop) # new value is associated with population 
            return True
        else:
            return False
        print(countryCat.getPopulation)
        
# Same process as outlined above
    def setAreaOfCountry(self, name, newArea):
        if name in self._countryCat:
            self._countryCat[name].setArea(newArea)
            return True
        else:
            return False

    def setContinentOfCountry(self, name, newCont):
        if name in self._countryCat:
            self._countryCat[name].setContinent(newCont)
            return True
        else:
            return False

    def findCountry(self,country):
        return country
        return None    

    def addCountry(self,countryName,pop,area,cont):
        if countryName not in self._countryCat:
            self._countryCat[countryName] = Country(countryName, pop, area, cont)
            return True
        else:
            return False

# Print catalogue 
    def printCountryCatalogue(self):
        for key, value in sorted(self._countryCat.items()):
            outstring = Country(key.title(), value.getPopulation(), value.getArea(), value.getContinent())
            print(outstring.__repr__())
        return
            
# Saves file name after accepting the parameter value
    def saveCountryCatalogue(self,fname):
        writeFile = open(fname, "w")
        newList = sorted(self._countryCat)
        writeFile.write('Country|Continent|Population|Area\n')
        count = 0
        for name in newList:
            
            output = ""
            
            continent = self._countryCat[name].getContinent()
            
            population = self._countryCat[name].getPopulation()
    
            area = self._countryCat[name].getArea()
            
            output = name+"|"+continent+"|"+str(population)+"|"+str(area)
            
            writeFile.write(output+"\n")
            
            count += 1

        # Closes file    
        writeFile.close()
        if count == len(self._countryCat):
            return count
        else:
            return -1
        

