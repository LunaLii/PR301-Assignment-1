import re

file = open('classDiagram.txt', 'r').readlines()
output = open("outputClassDiagram.txt", "w")

def classHandler():
    classList = [[]]
    for i, m in enumerate(file[1:-1]):
        if m == "\n":
            if i != len(file[1:-1]) - 1:
                classList.append([])
        else:
            classList[-1].append(m)
    return classList
def fileReader():
    #for classItem in classHandler(): #for each class array in the array of classes,
        classList = []
        for listItem in classItem: #for each list item in each class array,
            if "class" in listItem:
                output.write(listItem + "   def __init__(") #append each class name to the array of classes
                print(classList)



fileReader()

#for listItem in rawcode:
   #if "class" in listItem:
       #classList.append(listItem.split(' ')[0:2])
   # if ":" in listItem:
       # output.write()
        # print(listItem.split(' ')[3] + ',')
file.close()
