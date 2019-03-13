import re

file = open('classDiagram.txt', 'r').readlines()

def class_handler(file):
    classList = [[]]
    for i, m in enumerate(file[1:-1]): #file[1:-1] removes the first and last elements of the file
        if m == "\n":
            if i != len(file[1:-1]) - 1:
                classList.append([])
        else:
            classList[-1].append(m)
    return classList

#Following two lines are tests to un-comment and display the classList. Please don't delete these.
#for listItem in class_handler(file):
    #print(listItem)

#flight = ['class Flight {\n', '   flightNumber : int\n', '   departureTime : date\n', '   size()\n', '   add()\n', '}\n']

def get_class_name(classArray):
    for listItem in classArray: #for each list item in each class array,
        if "class" in listItem:
            return listItem[:listItem.index(" {")]

def get_attributes(classArray):
    attributes = []
    for listItem in classArray:
        if ":" in listItem and "(" not in listItem: #if an open bracket is detected, the listItem contains a method and will thus be ignored since we are trying to single out attributes, not methods. This will be again be used later for the get_methods method.
            attributes.append(listItem.split(' ')[3])
    return attributes

def get_methods(classArray):
    methods = []
    for listItem in classArray:
        if "(" in listItem:
            methods.append(listItem[:listItem.index("\n")-2].strip()) #for listItem, find the value between ": " and "(" (which is the method name) and then append it to the array of methods.
    return methods #result: ['size', 'add']

def output_class(classArray):
    with open("outputClassDiagram.txt", "w")  as output:
        output.write(get_class_name(classArray) + ":\n  def __init__(self, ")
        result = ''
        for listItem in get_attributes(classArray):
            result += listItem + ', '
        output.write(result[:-2] + ')\n')
        for listItem in get_attributes(classArray):
            output.write('    self.' + listItem + ' = ' + listItem + '\n')
        output.write('\n')
        for listItem in get_methods(classArray):
            output.write('def ' + listItem + '(self):\n')
        output.write('\n')

for classItem in class_handler(file):
    output_class(classItem)


#print(get_attributes(flight))
#print(get_methods(flight))
#output_class(flight)
