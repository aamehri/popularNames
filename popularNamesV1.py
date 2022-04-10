# GirlNames.txt file contains a list of the 200 most popular names given to
# girls born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the files into a list
# The user should be able to enter a girls name and the program will display
# a message indicating whether the name is among the most popular or not.
def openNamesFile():
    names = []
    with open("GirlNames.txt", "r") as f:
        for name in f:
            name = name.strip()
            names.append(name.lower())
        f.close()
    return names

def linearSearch(name):
    popNames = openNamesFile()
    for count in range(len(popNames)):
        if name.lower() == popNames[count]:
            return True
    return False

def main():
    name = input("Enter a first name: ")
    if linearSearch(name):
        print(name, " was found to be most popular")
    else:
        print(name, " is not in this database")
main()