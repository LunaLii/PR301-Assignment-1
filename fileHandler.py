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

#for listItem in class_handler(file):
    #print(listItem)

flight = ['class Flight {\n', '   flightNumber : 10\n', '   departureTime : 2\n', '   date : size()\n', '}\n']

def getClassName(classArray):
    for listItem in classArray: #for each list item in each class array,
        if "class" in listItem:
            return listItem

def get_attributes(classArray):
    attributes = []
    for listItem in classArray:
        if ":" in listItem and "(" not in listItem: #if an open bracket is detected, the listItem contains a method and will thus be ignored since we are trying to single out attributes, not methods. This will be again be used later for the get_methods method.
            attributes.append(listItem.split(' ')[3])
    return attributes

print(getClassName(file))
print(get_attributes(flight))

#for listItem in rawcode:
   #if "class" in listItem:
       #classList.append(listItem.split(' ')[0:2])
   # if ":" in listItem:
       # output.write()
        # print(listItem.split(' ')[3] + ',')
#DO NOT USE .write, USE "with"
