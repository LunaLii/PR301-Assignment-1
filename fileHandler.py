import re

file = open('classDiagram.txt', 'r').readlines()
output = open("outputClassDiagram.txt", "w")

def class_handler(file):
    classList = [[]]
    for i, m in enumerate(file[1:-1]): #file[1:-1] removes the first and last elements of the file
        if m == "\n":
            if i != len(file[1:-1]) - 1:
                classList.append([])
        else:
            classList[-1].append(m)
    return classList

flight = ['class Flight {\n', '   flightNumber : 10\n', '   departureTime : 2\n', '}\n']

def getClassName(classArray):
    for listItem in classArray: #for each list item in each class array,
        if "class" in listItem:
            return listItem

def get_attributes(classArray):
    attributes = []
    for listItem in classArray:
        if ":" in listItem:
            attributes.append(listItem.split(' ')[3])
    return attributes

print(getClassName(flight))
print(get_attributes(flight))

#for listItem in rawcode:
   #if "class" in listItem:
       #classList.append(listItem.split(' ')[0:2])
   # if ":" in listItem:
       # output.write()
        # print(listItem.split(' ')[3] + ',')
#DO NOT USE .write, USE "with" 
