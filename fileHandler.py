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
print(class_handler(file))
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

def output_class(classItem):
    #Add all into a string called result, then open the file and write the result into the output file.
    result = get_class_name(classItem) + ":\n  def __init__(self"

    for listItem in get_attributes(classItem):
        result += ', ' + listItem
    result += '):\n'
    for listItem in get_attributes(classItem):
        result += '    self.' + listItem + ' = ' + listItem + '\n'
    result += '\n'
    for listItem in get_methods(classItem):
        result += 'def ' + listItem + '(self):\n'
    result += '\n'
    return result

files = ['outputClassDiagram.py', 'outputClassDiagram2.py']
for classItem, file in zip(class_handler(file), files):
    result = output_class(classItem)
    with open(file, "w") as output:
        output.write(result)


#print(get_attributes(flight))
#print(get_methods(flight))
#output_class(flight)
