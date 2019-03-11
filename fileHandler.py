import re

file = open('classDiagram.txt', 'r').readlines()
print(file)

def fileReader():
    for listItem in file:
        if "class" in listItem:
            replaceList = [" ","class","{","\n"]
            for x in replaceList:
                listItem = listItem.replace(x, "")

            print(listItem + ".py")









file = fileReader()