import re

file = open('classDiagram.txt', 'r').readlines()
output = open("outputClassDiagram.txt", "w")
print(file)

def fileReader():
    for listItem in file:
        if "class" in listItem:
            output.write(listItem + "   def __init__(")
        if ":" in listItem:
            output.write(listItem.strip()) #Upon finding the first whitespace, remove everything after in listItem

file = fileReader()


